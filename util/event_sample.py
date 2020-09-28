import numpy as np
import pandas as pd
import os
import operator
import pofah.util.input_data_reader as idr
import pofah.util.result_writer as rw
import pofah.path_constants.sample_dict as sd
import pofah.util.converter as conv
import pofah.util.utility_fun as utfu
import sarewt.data_reader as dare


class EventSample():

    def __init__(self, name, particles=None, event_features=None, particle_feature_names=None):
        '''
        datastructure that holds set of N events with each having two components: data of particles and data of jet features
        :param name: name of the sample
        :param particles: particle features like eta, phi, pt (numpy array) (todo: extend to preprocessed form like images (implement subclass?))
        :param event_features: N x F_n features (pandas dataframe)
        '''
        self.name = name
        self.particles = np.asarray(particles) # numpy array [ 2 (jets) x N events x 100 particles x 3 features ]
        self.particle_feature_names = particle_feature_names
        self.event_features = pd.DataFrame(event_features) # dataframe: names = columns

    @classmethod
    def from_input_file(cls, name, path):
        reader = idr.InputDataReader(path)
        particles, part_feature_names = reader.read_jet_constituents()
        jet_features = reader.read_dijet_features_to_df()
        return cls(name, np.stack(particles), jet_features, part_feature_names)

    @classmethod
    def from_input_dir(cls, name, path):
        ''' reading data in all files in 'path' to event sample'''
        reader = dare.DataReader(path)
        constituents, constituents_names, features, features_names = reader.read_events_from_dir()
        return cls(name, np.stack([constituents[:,0,:,:], constituents[:,1,:,:]]), pd.DataFrame(features, columns=features_names), constituents_names)

    def get_particles(self):
        return [self.particles[0],self.particles[1]]

    def get_event_features(self):
        return self.event_features

    def add_event_feature(self, label, value):
        self.event_features[label] = value

    def dump(self,path):
        particles = np.stack((self.particles[0],self.particles[1]), axis=1) # particles in input files stored as ( N x 2 jets x 100 particles x 3 features )
        rw.write_event_sample_to_file(particles, self.event_features.values, self.particle_feature_names, list(self.event_features.columns), path)


class CaseEventSample(EventSample):

    @classmethod
    def from_input_dir(cls, path, names=['qcdSig', 'GtoZZ25', 'WtoWZ25', 'WkktoWWW25', 'btotW26'], truth_ids=range(4)):
        reader = dare.CaseDataReader(path)
        constituents, constituents_names, features, features_names, truth_labels = reader.read_events_from_dir()
        samples = []
        for name, label in zip(names, truth_ids):
            # get examples for sample with truth label 'label'
            sample_const, sample_feat = utfu.filter_arrays_on_value(constituents, features, filter_arr=truth_labels.squeeze(), filter_val=label, comp=operator.eq)
            # convert particles from px, py, pz, E to eta, phi, pt (if not converting, drop E column)
            converted_sample_const = conv.xyze_to_eppt(sample_const)
            # delete nan and inf values produced in conversion
            sample_const, sample_feat = conv.delete_nan_and_inf_events(converted_sample_const, sample_feat)
            samples.append(cls(name, [sample_const[:,0,:,:], sample_const[:,1,:,:]], sample_feat, features_names)) # inverting constituents format from [N x 2 x 100 x 3] to [2 x N x 100 x 3] 
        return samples
