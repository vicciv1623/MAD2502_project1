def simpson(x_vals: np.ndarray, func: np.ufunc) -> float:
  a_vals = x_vals[:-1]
  b_vals = x_vals[1:]
  fun_mid = func((a_vals + b_vals)/2)
  return np.sum((b_vals - a_vals)/6 * (func(a_vals) + 4*fun_mid + func(b_vals)))
