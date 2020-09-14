import sarewt.data_reader as dare
import pofah.util.jet_sample as jesa
import pofah.path_constants.sample_dict_file_parts_input as sdfi
import os
import glob

base_dir = '/eos/project/d/dshep/TOPCLASS/DijetAnomaly/VAE_results/run_101/sample_results/minl1l2_loss'
sample_dirs =  glob.glob(base_dir+'/q*')

quantiles = ['q1', 'q5', 'q10', 'q90']
sample_ids = ['qcdSigAll', 'GtoWW15naReco', 'GtoWW25naReco', 'GtoWW35naReco', 'GtoWW45naReco']

for sample_dir1, sample_dir2 in zip(sample_dirs[:-1],sample_dirs[1:]):
	for sample_id in sample_ids:
		print('*'*10+'\ncomparing {} samples in {} and {}\n'.format(sample_id, sample_dir1, sample_dir2)+'*'*10)
		sample1 = jesa.JetSample.from_input_dir(os.path.join(sample_dir1, sdfi.path_dict['sample_dir'][sample_id])
		sample2 = jesa.JetSample.from_input_dir(os.path.join(sample_dir2, sdfi.path_dict['sample_dir'][sample_id])
		print('{} == {}: '.format(sample_dir1, sample_dir2, sample1.equals(sample2, drop_col='sel', print_some=True))
