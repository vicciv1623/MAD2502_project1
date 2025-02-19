import numpy as np

def left_endpoint(x_vals, func):
    width = np.diff(x_vals)
    height = func(x_vals[:-1])
    return np.sum(width * height)

def trapezoid(x_vals, func):
    widths = np.diff(x_vals)
    heights = (func(x_vals[:-1]) + func(x_vals[1:])) / 2
    return np.sum(widths * heights)
