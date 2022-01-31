import pandas as pd
import random
import numpy as np
import h5py

import sarewt.data_reader as dr
import pofah.util.result_writer as rw

""" module containing wrapper for a dijet sample (with 2 jets having M features in phase space) 
    ['mJJ', 'j1Pt', 'j1Eta', 'j1Phi', 'j1M', 'j1E', 'j2Pt', 'j2M', 'j2E', 'DeltaEtaJJ', 'DeltaPhiJJ', 'j1TotalLoss', 'j1RecoLoss', 'j1KlLoss', 'j2TotalLoss', 'j2RecoLoss', 'j2KlLoss']
"""

class JetSample():

    FEAT_NAMES = ['mJJ', 'j1Pt', 'j1Eta', 'j1Phi', 'j1M', 'j1E', 'j2Pt', 'j2M', 'j2E', 'DeltaEtaJJ', 'DeltaPhiJJ']
    FEAT_IDX = dict(zip(FEAT_NAMES, range(len(FEAT_NAMES))))
    
    def __init__(self, name, features, title=None):
        '''
            name = sample id (used in path dicts)
            data = jet features as pandas dataframe
            title = string used for plot titles
        '''
        self.name = name
        self.data = features # assuming data passed as dataframe
        self.title = title or name

    @classmethod
    def from_feature_array(cls, name, features, feature_names):
        df = pd.DataFrame(features, columns=feature_names)
        return cls(name, df)

    @classmethod
    def from_input_file(cls, name, path, **cuts):
        df = dr.DataReader(path).read_jet_features_from_file(features_to_df=True, **cuts)
        # convert any QR-selection colums from 0/1 to bool
        sel_cols = [c for c in df if c.startswith('sel')]
        for sel in sel_cols:  # convert selection column to bool
            df[sel] = df[sel].astype(bool)
        return cls(name, df)

    @classmethod
    def from_input_dir(cls, name, path, read_n=None, **cuts):
        df, _ = dr.DataReader(path).read_jet_features_from_dir(read_n=read_n, features_to_df=True, **cuts)
        # convert any QR-selection colums from 0/1 to bool
        sel_cols = [c for c in df if c.startswith('sel')]
        for sel in sel_cols:  # convert selection column to bool
            df[sel] = df[sel].astype(bool)
        return cls(name, df)

    @classmethod
    def from_event_sample(cls, event_sample):
        jet_features = event_sample.get_event_features()
        return cls(event_sample.name, jet_features)

    @classmethod
    def from_latent_jet_sample(cls, latent_jet_sample):
        return cls(latent_jet_sample.name, latent_jet_sample.data, latent_jet_sample.title)
        
    def __getitem__(self, key):
        ''' slice by column
            return numpy array of values if single key is passed, else whole dataframe subslice with column names if list of strings is passed: 
            sample['key'] returns numpy array holding values(!) of column 'key'
            sample[['key']] returns dataframe with single column 'key'
        '''
        if isinstance(key, str):
            return self.data[key].values 
        [k] = key # extract elements from list
        return self.data[k]
    
    def __len__( self ):
        return len(self.data)
    

    def cut(self, idx):
        ''' slice by row
            return filtered jet sample with events of index idx
            idx ... numpy array, slice or pandas series of booleans
        '''
        cls = type(self)
        if type(idx) is np.ndarray:
            new_dat = self.data.iloc[idx]
        else:
            new_dat = self.data[idx]
        return cls(name=self.name, data=new_dat, title=' '.join([self.title,'filtered']))

    def sample(self, n):
        ''' sample n events from sample at random '''
        cls = type(self)
        new_dat = self.data.sample(n=n)
        return cls(name=self.name+'_sampled', data=new_dat, title=' '.join([self.title,'sampled']) )

    def merge(self, other, shuffle=True):
        ''' merge this and other jet sample and return new union JetSample object '''
        cls = type(self)
        features_merged = pd.concat([self.data, other.data], ignore_index=True)
        if shuffle:
            features_merged = features_merged.sample(frac=1.).reset_index(drop=True)
        names_merged = self.name + '_and_' + other.name
        return cls(name=names_merged, data=features_merged)

    def features(self):
        return list(self.data.columns)
        
    def add_feature(self, label, value):
        self.data[ label ] = value
        
    def accepted(self, quantile, feature=None):
        q_key = 'sel_q{:02}'.format(int(quantile*100)) 
        if q_key not in self.data:
            print('selection for quantile {} not available for this data sample'.format(quantile))
            return
        return self.data[self.data[q_key]][feature].values if feature else self.data[self.data[q_key]]
        
    def rejected(self, quantile, feature=None):
        q_key = 'sel_q{:02}'.format(int(quantile*100)) 
        if q_key not in self.data:
            print('selection for quantile {} not available for this data sample'.format(quantile))
            return
        return self.data[~self.data[q_key]][feature].values if feature else self.data[~self.data[q_key]]
    
    def describe(self, feature):
        print('mean = {0:.2f}, min = {1:.2f}, max = {2:.2f}'.format(self.data[feature].mean(),self.data[feature].min(), self.data[feature].max()))

    def equals(self, other, drop_col=None, print_some=False):
        dat_self = self.data.drop(drop_col, axis=1) if drop_col else self.data
        dat_other = other.data.drop(drop_col, axis=1) if drop_col else other.data

        if print_some:
            idx = random.choices(range(len(self)-1), k=4) # compare 4 entries at random
            with np.printoptions(precision=3, suppress=True):
                print('-- this: ', dat_self.iloc[idx].values)
                print('-- other: ', dat_other.iloc[idx].values)
                print('examples all equal: ', (dat_self.iloc[idx].values == dat_other.iloc[idx].values).all())

        return dat_self.equals(dat_other)

    def _convert_data_for_dump(self):
        dump_data = self.data
        sel_cols = [c for c in self.data if c.startswith('sel')]
        if sel_cols: # convert selection column to int for writing
            dump_data = self.data.copy()
            for sel in sel_cols:
                dump_data[sel] = dump_data[sel].astype(int)
        return dump_data


    def dump(self, path):
        dump_data = self._convert_data_for_dump()        
        rw.write_jet_sample_to_file(dump_data.values, list(dump_data.columns), path)
        print('written data sample to {}'.format(path))
        
    def __repr__(self):
        return self.name
    
    def plot_name(self):
        return self.name.replace(' ', '_')
        


class JetSampleLatent(JetSample):
    """
        jet sample class with latent space features
    """

    def __init__(self, name, features, latent_key=None, latent_data=None):
        super(JetSampleLatent, self).__init__(name=name, features=features)
        self.latent_reps = {}
        if latent_key is not None:
            self.latent_reps[latent_key] = latent_data


    @classmethod
    def from_input_file(cls, name, path, latent_key='latent_ae', read_n=None, **cuts):
        df = dr.DataReader(path).read_jet_features_from_file(features_to_df=True, **cuts)[:read_n]
        # convert any QR-selection colums from 0/1 to bool
        sel_cols = [c for c in df if c.startswith('sel')]
        for sel in sel_cols:  # convert selection column to bool
            df[sel] = df[sel].astype(bool)
        # read latent representation data-structure
        ff = h5py.File(path,'r')
        return cls(name=name, features=df, latent_key=latent_key, latent_data=np.array(ff.get(latent_key))[:read_n])


    def add_latent_representation(self, latent_rep, latent_key='latent_ae'):

        '''
            add latent represenation to jet sample (from autoencoding, pca, etc)
            :param latent_rep: numpy ndarray with latent space representation of size [N_sample x 2 jets x k latent features]
        '''

        self.latent_reps[latent_key] = latent_rep

        return self

    def get_latent_representation(self, latent_key='latent_ae', per_jet=True):

        try:
            if per_jet:
                return self.latent_reps[latent_key][:,0,:], self.latent_reps[latent_key][:,1,:] 
            return self.latent_reps[latent_key]
        except KeyError as e:
            print('Error: no latent representation for ' + latent_key + ' stored in sample')
            return np.empty()


    def dump(self, path):
        dump_data = self._convert_data_for_dump()
        rw.write_jet_sample_latent_to_file(dump_data.values, list(dump_data.columns), self.latent_reps, path)
        print('written data sample to {}'.format(path))
        


def split_jet_sample_train_test(jet_sample, frac, new_names=None):
    
    """ shuffles and splits dataset into training-set and testing-set accorinding to fraction frac """
    cls = type(jet_sample)
    new_names = new_names or (jet_sample.name+'Train', jet_sample.name+'Test')
    df_copy = jet_sample.data.copy()

    N = df_copy.shape[0]
    shuffled = df_copy.sample(frac=1.).reset_index(drop=True) # shuffle original data
    first = shuffled[:int(N*frac)].reset_index(drop=True)
    second = shuffled[int(N*frac):].reset_index(drop=True)
    
    return [cls(new_names[0], first), cls(new_names[1], second)]
