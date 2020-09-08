import pandas as pd

import pofah.util.input_data_reader as idr
import sarewt.data_reader as dr
import pofah.util.result_writer as rw

""" module containing wrapper for a dijet sample (with 2 jets having M features in phase space) 
    ['mJJ', 'j1Pt', 'j1Eta', 'j1Phi', 'j1M', 'j1E', 'j2Pt', 'j2M', 'j2E', 'DeltaEtaJJ', 'DeltaPhiJJ', 'j1TotalLoss', 'j1RecoLoss', 'j1KlLoss', 'j2TotalLoss', 'j2RecoLoss', 'j2KlLoss']
"""

class JetSample():
    
    def __init__(self, name, data, title=None):
        '''
            name = sample id (used in path dicts)
            data = jet features as pandas dataframe
            title = string used for plot titles
        '''
        self.name = name
        self.data = data # assuming data passed as dataframe
        self.title = name if title is None else title

    @classmethod
    def from_feature_array(cls, name, features, feature_names):
        df = pd.DataFrame(features,columns=feature_names)
        return cls(name, df)

    @classmethod
    def from_input_file(cls, name, path):
        df = idr.InputDataReader(path).read_dijet_features_to_df()
        if 'sel' in df:  # convert selection column to bool
            df['sel'] = df['sel'].astype(bool)
        return cls(name, df)

    @classmethod
    def from_input_dir(cls, name, path):
        df = dr.DataReader(path).read_jet_features_from_dir_to_df()
        if 'sel' in df:  # convert selection column to bool
            df['sel'] = df['sel'].astype(bool)
        return cls(name, df)

    @classmethod
    def from_event_sample(cls, event_sample):
        jet_features = event_sample.get_event_features()
        return cls(event_sample.name, jet_features)
        
    def __getitem__(self, key):
        ''' return numpy array of values if single key is passed, else whole dataframe subslice with column names if list of strings is passed: 
            sample['key'] returns numpy array holding values(!) of column 'key'
            sample[['key']] returns dataframe with single column 'key'
        '''
        if isinstance(key, str):
            return self.data[key].values 
        [k] = key # extract elements from list
        return self.data[k]
    
    def __len__( self ):
        return len(self.data)
    
    def features( self ):
        return list( self.data.columns )
        
    def add_feature( self, label, value ):
        self.data[ label ] = value
        
    def accepted( self, feature=None ):
        if 'sel' not in self.data:
            print('selection not available for this data sample')
            return
        return self.data[self.data['sel']][feature].values if feature else self.data[self.data['sel']]
        
    def rejected( self, feature=None ):
        if 'sel' not in self.data:
            print('selection not performed for this data sample')
            return
        return self.data[~self.data['sel']][feature].values if feature else self.data[~self.data['sel']]
    
    def describe( self, feature ):
        print('mean = {0:.2f}, min = {1:.2f}, max = {2:.2f}'.format(self.data[feature].mean(),self.data[feature].min(), self.data[feature].max()))
    
    def dump( self, path ):
        dump_data = self.data
        if 'sel' in self.data: # convert selection column to int for writing
            dump_data = self.data.copy()
            dump_data['sel'] = dump_data['sel'].astype(int)
        rw.write_jet_sample_to_file( dump_data.values, list(dump_data.columns), path )
        print('written data sample to {}'.format(path))
        
    def __repr__( self ):
        return self.name
    
    def plot_name( self ):
        return self.name.replace(' ','_')
        

def split_jet_sample_train_test(jet_sample, frac):
    
    """ shuffles and splits dataset into training-set and testing-set accorinding to fraction frac """
    
    df_copy = jet_sample.data.copy()

    N = df_copy.shape[0]
    shuffled = df_copy.sample(frac=1.).reset_index(drop=True) # shuffle original data
    first = shuffled[:int(N*frac)].reset_index(drop=True)
    second = shuffled[int(N*frac):].reset_index(drop=True)
    
    return [JetSample(jet_sample.name+'Train', first), JetSample(jet_sample.name+'Test', second)]
