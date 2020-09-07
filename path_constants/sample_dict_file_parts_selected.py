import copy
import pofah.path_constants.sample_dict_file_parts_reco as sd_reco

path_dict = copy.deepcopy(sd_reco.path_dict)


update_dict = {
	
        'base_dir' : '/eos/home-k/kiwoznia/data/VAE_results/bump_hunt_results/$EXTENTION$/selections',

}

path_dict.update(update_dict)
