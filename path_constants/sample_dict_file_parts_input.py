import copy
import pofah.path_constants.sample_dict as sd

path_dict = copy.deepcopy(sd.path_dict)

update_dict = {
	'base_dir' : '/eos/user/k/kiwoznia/data/VAE_data/events',

	'sample_dir' : {
		'qcdSide': 'qcd_sqrtshatTeV_13TeV_PU40_NEW_sideband_parts',
		'qcdSideExt' : 'qcd_sqrtshatTeV_13TeV_PU40_NEW_EXT_sideband_parts',
		'qcdSig': 'qcd_sqrtshatTeV_13TeV_PU40_NEW_signalregion_parts',
		'qcdSigExt': 'qcd_sqrtshatTeV_13TeV_PU40_NEW_EXT_signalregion_parts',
		'GtoWW15na': 'RSGraviton_WW_NARROW_13TeV_PU40_1.5TeV_NEW_parts',
		'GtoWW15br': 'RSGraviton_WW_BROAD_13TeV_PU40_1.5TeV_NEW_parts',
		'GtoWW25na': 'RSGraviton_WW_NARROW_13TeV_PU40_2.5TeV_NEW_parts',
		'GtoWW25br': 'RSGraviton_WW_BROAD_13TeV_PU40_2.5TeV_NEW_parts',
		'GtoWW35na': 'RSGraviton_WW_NARROW_13TeV_PU40_3.5TeV_NEW_parts',
		'GtoWW35br': 'RSGraviton_WW_BROAD_13TeV_PU40_3.5TeV_NEW_parts',
		'GtoWW45na': 'RSGraviton_WW_NARROW_13TeV_PU40_4.5TeV_NEW_parts',
		'GtoWW45br': 'RSGraviton_WW_BROAD_13TeV_PU40_4.5TeV_NEW_parts',
		'AtoHZ15': 'AtoHZ_to_ZZZ_13TeV_PU40_1.5TeV_NEW_parts',
		'AtoHZ25': 'AtoHZ_to_ZZZ_13TeV_PU40_2.5TeV_NEW_parts',
		'AtoHZ35': 'AtoHZ_to_ZZZ_13TeV_PU40_3.5TeV_NEW_parts',
		'AtoHZ45': 'AtoHZ_to_ZZZ_13TeV_PU40_4.5TeV_NEW_parts',
	},
}

path_dict.update(update_dict)
