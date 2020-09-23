import numpy as np

def nan_or_inf_idx(*arrays):
	idx = []
	for arr in arrays:
		idx.extend(np.argwhere(np.isnan(arr))[:,0]) # events that have at least one particle with a nan value
		idx.extend(np.argwhere(np.isinf(arr))[:,0]) # events that have at least one particle with an inf value
	return np.unique(np.asarray(idx))

def xyze_to_eppt(constituents):
	''' converts an array [N x 100, 4] of particles
		from px, py, pz, E to eta, phi, pt (mass omitted)
	'''
	PX, PY, PZ, E = range(4)

	pt = np.sqrt(np.float_power(constituents[:,:,PX], 2) + np.float_power(constituents[:,:,PY], 2)) # numpy.float16 dtype -> float power to avoid overflow
	eta = np.arcsinh(np.divide(constituents[:,:,PZ], pt, out=np.zeros_like(pt), where=pt!=0.))
	phi = np.arctan2(constituents[:,:,PY], constituents[:,:,PX])

	# check for nan values
	del_idx = nan_or_inf_idx(pt, eta, phi)
	if nan_idx.size > 0 or inf_idx:
		print('[converter.xyze_to_eppt]: {} NaN values found'.format(len(nan_idx)))
		np.delete(pt, nan_idx), np.delete(eta, nan_idx), np.delete(phi, nan_idx)
	return np.stack([eta, phi, pt], axis=1)
