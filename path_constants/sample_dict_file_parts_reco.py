import pofah.path_constants.sample_dict as sd

path_dict = sd.path_dict


update_dict = {
	
        'base_dir' : '/eos/home-k/kiwoznia/dev/autoencoder_for_anomaly/convolutional_VAE/results',

	'sample_dir' : {
		'qcdSigReco': 'qcd_sqrtshatTeV_13TeV_PU40_parts',
                'GtoWW15naReco': 'RSGraviton_WW_NARROW_13TeV_PU40_1.5TeV_parts',
                'GtoWW15brReco': 'RSGraviton_WW_BROAD_13TeV_PU40_1.5TeV_parts',
                'GtoWW25naReco': 'RSGraviton_WW_NARROW_13TeV_PU40_2.5TeV_parts',
                'GtoWW25brReco': 'RSGraviton_WW_BROAD_13TeV_PU40_2.5TeV_parts',
                'GtoWW30naReco': 'RSGraviton_WW_NARROW_13TeV_PU40_3.0TeV_parts',
                'GtoWW30brReco': 'RSGraviton_WW_BROAD_13TeV_PU40_3.0TeV_parts',
                'GtoWW35naReco': 'RSGraviton_WW_NARROW_13TeV_PU40_3.5TeV_parts',
                'GtoWW35brReco': 'RSGraviton_WW_BROAD_13TeV_PU40_3.5TeV_parts',
                'GtoWW45naReco': 'RSGraviton_WW_NARROW_13TeV_PU40_4.5TeV_parts',
                'GtoWW45brReco': 'RSGraviton_WW_BROAD_13TeV_PU40_4.5TeV_parts',
	},
}

path_dict.update(update_dict)
