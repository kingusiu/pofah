import pathlib
import os
import pofah.util.config as co

class Experiment():

    def __init__(self, run_n=0):
        self.run_n = run_n
        self.run_dir = 'run_' + str(self.run_n)
        self.model_dir = os.path.join(co.config['model_dir'], self.run_dir)
        self.fig_dir = os.path.join(co.config['fig_dir'], self.run_dir)
        self.fig_dir_event = os.path.join(self.fig_dir,'analysis_event')
        self.analysis_dir = os.path.join(co.config['analysis_base_dir'], self.run_dir)
        self.model_analysis_dir = os.path.join(co.config['model_analysis_base_dir'], self.run_dir)


    def setup(self, fig_dir=False, result_dir=False, tensorboard_dir=False, model_dir=False, analysis_dir=False, model_analysis_dir=False):

        if fig_dir:
            pathlib.Path(self.fig_dir).mkdir(parents=True, exist_ok=True)
            self.fig_dir_img = os.path.join(self.fig_dir,'analysis_image')
            pathlib.Path(self.fig_dir_img).mkdir(parents=True, exist_ok=True)
            pathlib.Path(self.fig_dir_event).mkdir(parents=True, exist_ok=True)

        if tensorboard_dir:
            self.tensorboard_dir = os.path.join(co.config['tensorboard_dir'], self.run_dir)
            pathlib.Path(self.tensorboard_dir).mkdir(parents=True, exist_ok=True)

        if model_dir:
            pathlib.Path(self.model_dir).mkdir(parents=True, exist_ok=True)

        if analysis_dir:
            self.analysis_dir_fig = os.path.join(self.analysis_dir, 'fig')
            self.analysis_dir_bin_count = os.path.join(self.analysis_dir, 'bin_count')
            pathlib.Path(self.analysis_dir_fig).mkdir(parents=True, exist_ok=True)
            pathlib.Path(self.analysis_dir_bin_count).mkdir(parents=True, exist_ok=True)

        if model_analysis_dir:
            self.model_analysis_dir_roc = os.path.join(self.model_analysis_dir, 'roc')
            self.model_analysis_dir_loss = os.path.join(self.model_analysis_dir, 'loss')
            pathlib.Path(self.model_analysis_dir_roc).mkdir(parents=True, exist_ok=True)
            pathlib.Path(self.model_analysis_dir_loss).mkdir(parents=True, exist_ok=True)
        
        return self

    def setup_model_comparison_dir(self, model1, model2):
        self.model_comparison_dir = os.path.join(co.config['model_analysis_base_dir'], 'run_'+str(model1)+'_vs_run_'+str(model2)) 
        self.model_analysis_dir_roc = os.path.join(self.model_comparison_dir, 'roc')
        self.model_analysis_dir_loss = os.path.join(self.model_comparison_dir, 'loss')
        pathlib.Path(self.model_comparison_dir_roc).mkdir(parents=True, exist_ok=True)
        pathlib.Path(self.model_comparison_dir_loss).mkdir(parents=True, exist_ok=True)
