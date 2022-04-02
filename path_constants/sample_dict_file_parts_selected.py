import copy
import pofah.path_constants.sample_dict as sd

path_dict = copy.deepcopy(sd.path_dict)

update_dict = {
	
        'base_dir' : '/eos/user/k/kiwoznia/data/QR_results/events/vae_run_$run_n_vae$/qr_run_$run_n_qr$/sig_$sig_name$/xsec_$sig_xsec$/loss_$loss_strat$',

        # no sample directory, as all events of a data sample merged into single file
        'sample_dir' : {
                'qcdSideReco': '',
                'qcdSideExtReco' : '',
                'qcdSigReco': '',
                'qcdSigExtReco': '',
                'GtoWW15naReco': '',
                'GtoWW15brReco': '',
                'GtoWW25naReco': '',
                'GtoWW25brReco': '',
                'GtoWW35naReco': '',
                'GtoWW35brReco': '',
                'GtoWW45naReco': '',
                'GtoWW45brReco': '',
                # prepared train and test split data for QR training
                'qcdSigAllTrainReco': '',
                'qcdSigAllTestReco': '',
    },

}

path_dict.update(update_dict)
