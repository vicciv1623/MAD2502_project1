import numpy as np

def left_endpoint(x_vals: np.ndarray, func: np.ufunc) -> float:
    width = np.diff(x_vals)
    height = func(x_vals[:-1])
    return np.sum(width * height)

def trapezoid(x_vals: np.ndarray, func:np.ufunc) -> float:
    widths = np.diff(x_vals)
    heights = (func(x_vals[:-1]) + func(x_vals[1:])) / 2
    return np.sum(widths * heights)

def simpson(x_vals: np.ndarray, func: np.ufunc) -> float:
  a_vals = x_vals[:-1]
  b_vals = x_vals[1:]
  fun_mid = func((a_vals + b_vals)/2)
  return np.sum((b_vals - a_vals)/6 * (func(a_vals) + 4*fun_mid + func(b_vals)))
