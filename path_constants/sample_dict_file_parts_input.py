import copy
import pofah.path_constants.sample_dict as sd

path_dict = copy.deepcopy(sd.path_dict)

update_dict = {
	'base_dir' : '/data/t3home000/bmaier/CASE/',

	'sample_dir' : {
		'qcdSig': 'BB_UL_MC_small_sig',
		'qcdSide': 'BB_UL_MC_small_side',
		'qcdSideExt': 'BB_UL_MC_small_side',
	},
}

path_dict.update(update_dict)
