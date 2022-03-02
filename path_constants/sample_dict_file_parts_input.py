import copy
import pofah.path_constants.sample_dict as sd

path_dict = copy.deepcopy(sd.path_dict)

update_dict = {
	'base_dir' : '/eos/cms/store/user/bmaier/cms/case/samples/ul/',

	'sample_dir' : {
		'qcdSig': 'BB_UL_MC_small_sig/train',
		'qcdSigExt': 'BB_UL_MC_small_sig/test',
		'qcdSide': 'BB_UL_MC_small_side/train',
		'qcdSideExt': 'BB_UL_MC_small_side/test',
	},
}

path_dict.update(update_dict)
