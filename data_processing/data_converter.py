import numpy as np

def xyze_to_eppt(constituents):
	''' converts an array [N x 2 x 100, 4] of constituents
		from px, py, pz, E to eta, phi, pt (mass omitted)
	'''
	PX, PY, PZ, E = range(4)
	pt = np.sqrt(np.float_power(constituents[:,:,:,PX], 2) + np.float_power(constituents[:,:,:,PY], 2), dtype='float16') # numpy.float16 dtype -> float power to avoid overflow
	eta = np.arcsinh(np.divide(constituents[:,:,:,PZ], pt, out=np.zeros_like(pt), where=pt!=0.), dtype='float16')
	phi = np.arctan2(constituents[:,:,:,PY], constituents[:,:,:,PX], dtype='float16')

	return np.stack([eta, phi, pt], axis=3)


def eppt_to_xyz(constituents):
	''' converts an array [N x 2 x 100, 4] of constituents
		from eta, phi, pt to px, py, pz (energy omitted)
	'''
	ETA, PHI, PT = range(3)
	px = constituents[:,:,:,PT] * np.cos(constituents[:,:,:,PHI])
	py = constituents[:,:,:,PT] * np.sin(constituents[:,:,:,PHI])
	pz = constituents[:,:,:,PT] * np.sinh(constituents[:,:,:,ETA])

	return np.stack([px,py,pz], axis=3)


def normalize_features(constituents, feature_names):
    ''' normalize dataset
        cylindrical & cartesian coordinates: gaussian norm
        pt: min-max norm

    '''
    # min-max normalize pt
    idx_pt = feature_names.index('pt')
    constituents[:,:,idx_pt] = min_max_norm(constituents, idx_pt)
    # standard normalize angles and cartesians
    for idx, _ in enumerate([n for n in feature_names if 'pt' not in feature_names]):
        constituents[:,:,idx] = std_norm(constituents, idx)
    return constituents

