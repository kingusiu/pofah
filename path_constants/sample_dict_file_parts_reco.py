import copy
import pofah.path_constants.sample_dict as sd

path_dict = copy.deepcopy(sd.path_dict)


update_dict = {
	
        'base_dir' : '/eos/user/k/kiwoznia/data/VAE_results/events/$run$',

	'sample_dir' : {
                'qcdSideReco': 'qcd_sqrtshatTeV_13TeV_PU40_NEW_sideband_parts',
                'qcdSideExtReco' : 'qcd_sqrtshatTeV_13TeV_PU40_NEW_EXT_sideband_parts',
		'qcdSigReco': 'qcd_sqrtshatTeV_13TeV_PU40_NEW_signalregion_parts',
                'qcdSigExtReco': 'qcd_sqrtshatTeV_13TeV_PU40_NEW_EXT_signalregion_parts',
                'GtoWW15naReco': 'RSGraviton_WW_NARROW_13TeV_PU40_1.5TeV_NEW_parts',
                'GtoWW15brReco': 'RSGraviton_WW_BROAD_13TeV_PU40_1.5TeV_NEW_parts',
                'GtoWW25naReco': 'RSGraviton_WW_NARROW_13TeV_PU40_2.5TeV_NEW_parts',
                'GtoWW25brReco': 'RSGraviton_WW_BROAD_13TeV_PU40_2.5TeV_NEW_parts',
                'GtoWW35naReco': 'RSGraviton_WW_NARROW_13TeV_PU40_3.5TeV_NEW_parts',
                'GtoWW35brReco': 'RSGraviton_WW_BROAD_13TeV_PU40_3.5TeV_NEW_parts',
                'GtoWW45naReco': 'RSGraviton_WW_NARROW_13TeV_PU40_4.5TeV_NEW_parts',
                'GtoWW45brReco': 'RSGraviton_WW_BROAD_13TeV_PU40_4.5TeV_NEW_parts',
                # prepared train and test split data for QR training
                'qcdSigAllTrainReco': 'qcd_sqrtshatTeV_13TeV_PU40_NEW_ALL_Train_signalregion_parts',
                'qcdSigAllTestReco': 'qcd_sqrtshatTeV_13TeV_PU40_NEW_ALL_Test_signalregion_parts',
                'qcdSigAllTrain30pct': 'qcd_sqrtshatTeV_13TeV_PU40_NEW_ALL_Train_signalregion_parts',
                'qcdSigAllTrain50pct': 'qcd_sqrtshatTeV_13TeV_PU40_NEW_ALL_Train_signalregion_parts',
                'qcdSigAllTrain70pct': 'qcd_sqrtshatTeV_13TeV_PU40_NEW_ALL_Train_signalregion_parts',
                'qcdSigAllTest30pct': 'qcd_sqrtshatTeV_13TeV_PU40_NEW_ALL_Test_signalregion_parts',
                'qcdSigAllTest50pct': 'qcd_sqrtshatTeV_13TeV_PU40_NEW_ALL_Test_signalregion_parts',
                'qcdSigAllTest70pct': 'qcd_sqrtshatTeV_13TeV_PU40_NEW_ALL_Test_signalregion_parts',
	},
}

path_dict.update(update_dict)
