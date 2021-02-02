import copy
import pofah.path_constants.sample_dict_file_parts_reco as sd_reco

path_dict = copy.deepcopy(sd_reco.path_dict)

update_dict = {
	
        'base_dir' : '/eos/user/k/kiwoznia/data/QR_results/run_$run$/sig_$sig_name$/xsec_$sig_xsec$',

}

path_dict.update(update_dict)
