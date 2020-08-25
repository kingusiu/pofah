import pofah.path_constants.sample_dict as sd

path_dict = sd.path_dict

update_dict = {
	'base_dir' : '/eos/user/k/kiwoznia/data/VAE_data/events',

	'sample_dir' : {
		'qcdSig': 'qcd_sqrtshatTeV_13TeV_PU40_parts',
		'qcdSigSingle': 'qcd_sqrtshatTeV_13TeV_PU40'
	},
}

path_dict.update(update_dict)
