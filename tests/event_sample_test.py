import unittest
import numpy as np

import pofah.util.sample_factory as sf
import pofah.path_constants.sample_dict_file_parts_input as sdfi
import pofah.util.event_sample as evsa


# *********************************************
#		unit testing event_sample
# *********************************************

class EventSampleTestCase(unittest.TestCase):

	def test_reading_from_dir(self):
		# test reading in event sample from dir
		name = 'qcdSig'
		path = '/eos/user/k/kiwoznia/data/VAE_data/baby_events/qcd_sqrtshatTeV_13TeV_PU40'

		sample = evsa.EventSample.from_input_dir(name, path)
		p1, p2 = sample.get_particles()

		self.assertEqual(p1.shape, p2.shape)
		self.assertEqual(len(p1.shape), 3)


	def test_merging(self):

		# test reading in event sample from dir
		name_sig = 'qcdSig'
		path_sig = '/eos/user/k/kiwoznia/data/VAE_data/baby_events/qcd_sqrtshatTeV_13TeV_PU40'

		sample_sig = evsa.EventSample.from_input_dir(name_sig, path_sig)
		p1_sig, p2_sig = sample_sig.get_particles()
		feat_sig = sample_sig.get_event_features()

		name_side = 'qcdSide'
		path_side = '/eos/user/k/kiwoznia/data/VAE_data/baby_events/qcd_sqrtshatTeV_13TeV_PU40_SIDEBAND'

		sample_side = evsa.EventSample.from_input_dir(name_side, path_side)
		p1_side, p2_side = sample_side.get_particles()
		feat_side = sample_side.get_event_features()

		sample_merged = sample_sig.merge(sample_side)
		p1_merged, p2_merged = sample_merged.get_particles()
		feat_merged = sample_merged.get_event_features()

		self.assertEqual(len(sample_merged), len(sample_side)+len(sample_sig))
		self.assertEqual(len(p1_merged), len(p1_side)+len(p1_sig))
		self.assertEqual(len(p2_merged), len(p2_side)+len(p2_sig))
		self.assertEqual(len(feat_merged), len(feat_side)+len(feat_sig))
		self.assertEqual(np.min(p1_merged), min(np.min(p1_side), np.min(p1_sig)))
		self.assertEqual(np.max(p1_merged), max(np.max(p1_side), np.max(p1_sig)))
		self.assertEqual(np.min(p2_merged), min(np.min(p2_side), np.min(p2_sig)))
		self.assertEqual(np.max(p2_merged), max(np.max(p2_side), np.max(p2_sig)))
		# import ipdb; ipdb.set_trace()
		self.assertEqual(np.min(feat_merged.values), min(np.min(feat_side.values), np.min(feat_sig.values)))
		self.assertEqual(np.max(feat_merged.values), max(np.max(feat_side.values), np.max(feat_sig.values)))



if __name__ == '__main__':
	unittest.main()
