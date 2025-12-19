import numpy as np

def exp_rand(rate_param, sample_size = 1):
    rand_uniform = np.random.uniform(size = sample_size) # generates uniform rand number set
    return -rate_param * np.log(rand_uniform) # acts inverse CDF to get exponential distribution

def isotropic_unit_vector(sample_size = 1):
    phi = np.random.uniform(low = -np.pi, high = np.pi, size=sample_size) # produced random uniform values -pi to pi
    theta = np.arccos(1-2*np.random.uniform(size=sample_size)) # uses inverse CDF to produce theta values that won't pole
    # convert to cartesian co ordinates
    sin_theta = np.sin(theta)
    x = sin_theta*np.cos(phi)
    y = sin_theta*np.sin(phi)
    z = np.cos(theta)
    return np.array([x, y, z]) # output as 2D-array

def isotropic_1d_vector(sample_size=1):
    # as it is assumed infinite in y and z, only x needed
    theta = np.arccos(1-2*np.random.uniform(size=sample_size)) # uses inverse CDF to produce theta values that won't pole
    x = np.cos(theta) # use formula for conventional z as reduced random number generation
    return x