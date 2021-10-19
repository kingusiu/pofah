import numpy as np

def std_norm(data, idx):
    return (data[:,:,idx] - np.mean(data[:,:,idx]))/np.std(data[:,:,idx])


def min_max_norm(data, idx):
    return (data[:,:,idx] - np.min(data[:,:,idx]))/(np.max(data[:,:,idx])-np.min(data[:,:,idx]))


def nan_or_inf_idx(array):
    idx = []
    idx.extend(np.argwhere(np.isnan(array))[:,0]) # events that have at least one particle with a nan value
    idx.extend(np.argwhere(np.isinf(array))[:,0]) # events that have at least one particle with an inf value
    return np.unique(np.asarray(idx))


def delete_nan_and_inf_events(constituents, features):
    idx = nan_or_inf_idx(constituents)
    print('[converter.xyze_to_eppt]: {} NaN or inf values found. deleting affected events'.format(len(idx)))
    return np.delete(constituents, idx, axis=0), np.delete(features, idx, axis=0)


def mask_events_outliers(events, indices, values): # -> np.ndarray
    ''' remove outliers from dataset 
        events ... dataset
        indices ... indices of features to be cleaned
        values ... for each features: value at which to cut feature
        returns ... dataset without events with outliers
    '''
    mask = np.ones(len(events), dtype=bool)
    for (idx, val) in zip(indices, values):
        passed = np.abs(events[:,:,idx]) < val
        mask *= passed.all(axis=1)
    return events[mask]


