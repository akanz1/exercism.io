import numpy as np
def add(moment):
    return np.datetime64(moment) + np.timedelta64(int(1e9), "s")
