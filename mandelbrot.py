import numpy as np

def get_escape_time(c: complex, max_iterations: int) -> int | None:
    z = c
    if abs(z) > 2:
        return 0
    for i in range(max_iterations):
        z = z**2 + c
        if abs(z) > 2:
            return i + 1
    return None

def get_complex_grid(top_left: complex, bottom_right: complex, step: float) -> np.ndarray:
    # num_rows = len(np.arange(bottom_right.imag, top_left.imag, step))
    # num_cols = len(np.arange(top_left.real, bottom_right.real, step))
    reals = np.arange(top_left.real, bottom_right.real, step)
    imags = np.arange(top_left.imag, bottom_right.imag, -1 * step)
    # imags = np.flip(imags)
    imags = (imags.reshape((len(imags), 1)))
    return reals + (imags * 1j)

def get_escape_time_color_arr(c_arr: np.ndarray, max_iterations: int) -> np.ndarray:
    color_arr = c_arr.copy()
    for ind,value in enumerate(c_arr):
        for ind_col, col in enumerate(value):

            if get_escape_time(col, max_iterations) is None:
                color_arr[ind][ind_col] = 0

            elif get_escape_time(col, max_iterations) == 0:
                color_arr[ind][ind_col] = 1

            else:
                color = (max_iterations - (get_escape_time(col, max_iterations) + 1)) / (max_iterations + 1)
                color_arr[ind][ind_col] = color


    return color_arr
