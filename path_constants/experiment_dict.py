
path_dict = {

    # VAE directory patterns (TODO: fix run str)
	
	'model_dir' : '/eos/home-k/kiwoznia/data/VAE_models/$run$',
	'analysis_base_dir_fig' : '/eos/home-k/kiwoznia/data/VAE_results/bump_hunt_results/$run$/fig/$strategy$',
	'analysis_base_dir_bin_count' : '/eos/home-k/kiwoznia/data/VAE_results/bump_hunt_results/$run$/bin_count/$strategy$/$quantile$',
	'model_analysis_base_dir': '/eos/home-k/kiwoznia/data/VAE_results/model_analysis/$run$',
	'model_comparison_dir': '/eos/home-k/kiwoznia/data/VAE_results/model_analysis/$run1$_vs_$run2$',

    # QR directory pattern: run_x/sig_y/xsec_z

    'model_dir_qr': '/eos/home-k/kiwoznia/data/QR_models/run_$run$',
    'analysis_base_dir_qr': '/eos/user/k/kiwoznia/data/QR_results/analysis/run_$run$/sig_$sig_name$/xsec_$sig_xsec$',
}