
import math
import numpy as np

def size_window_curve(size_array):
    return np.exp(-0.5 * ((np.log10(size_array) - np.log10(50)) / 0.25) ** 2)

def compute_probability_only_size(size_nm):
    score = size_window_curve(np.array([size_nm]))[0]
    Z = 3 * score - 2
    return 1 / (1 + math.exp(-Z))

def corona_tiny_curve(size_array):
    return 0.1 * np.exp(-((size_array - 5)/8)**2)

def corona_mid_curve(size_array):
    return np.exp(-0.5 * ((np.log10(size_array) - np.log10(100)) / 0.15) ** 2)

def corona_large_curve(size_array):
    peak = 0.35
    return peak * np.exp(-((size_array - 230)/120)**2)
