import os
from collections import OrderedDict
import pathlib
import pofah.path_constants.sample_dict as sd
import pofah.jet_sample as jesa
import pofah.util.event_sample as evsa
import pofah.util.utility_fun as utfu


class SamplePathDirFactory():

    def __init__(self, path_dict):
        self.base_dir = path_dict['base_dir']
        self.sample_dir = path_dict['sample_dir']
        self.sample_file = path_dict['file_names']

    def update_base_path(self, repl_dict):
        self.base_dir = utfu.multi_replace(self.base_dir, repl_dict)
        return self

    def sample_dir_path(self, id):
        s_path = os.path.join(self.base_dir, self.sample_dir[id])
        pathlib.Path(s_path).mkdir(parents=True, exist_ok=True) # have to create directory for each sample here when writing results, not optimal, TODO: fix
        return s_path

    def sample_file_path(self, id):
        return os.path.join(self.base_dir, self.sample_dir[id], self.sample_file[id]+'.h5')


##### utility functions

def read_inputs_to_sample_dict_from_file(sample_ids, paths):
    data = OrderedDict()
    for sample_id in sample_ids:
        data[sample_id] = js.JetSample.from_input_file(sample_id, read_fun(sample_id))
    return data

def read_inputs_to_sample_dict_from_dir(sample_ids, paths, cls, read_n=None, apply_mjj_cut=True):
    data = OrderedDict()
    for sample_id in sample_ids:
        print('reading ', paths.sample_dir_path(sample_id))
        data[sample_id] = cls.from_input_dir(sample_id, paths.sample_dir_path(sample_id), read_n=read_n, apply_mjj_cut=apply_mjj_cut)
    return data

def read_inputs_to_jet_sample_dict_from_dir(sample_ids, paths, apply_mjj_cut=True):
    ''' read dictionary of JetSamples '''
    return read_inputs_to_sample_dict_from_dir(sample_ids, paths, jesa.JetSample, apply_mjj_cut)

def read_inputs_to_event_sample_dict_from_dir(sample_ids, paths, read_n=None, apply_mjj_cut=True):
    ''' read dictionary of EventSamples '''
    return read_inputs_to_sample_dict_from_dir(sample_ids, paths, evsa.EventSample, read_n=read_n, apply_mjj_cut=apply_mjj_cut)
