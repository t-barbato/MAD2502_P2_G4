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
    reals = np.arange(top_left.real, bottom_right.real, step)
    imags = np.arange(top_left.imag, bottom_right.imag, -1 * step)
    imags = (imags.reshape((len(imags), 1)))
    return reals + (imags * 1j)


def get_escape_time_color_arr(c_arr: np.ndarray, max_iterations: int) -> np.ndarray:
    # color_arr = c_arr.copy()
    # for ind,value in enumerate(c_arr):
    #     for ind_col, col in enumerate(value):
    #
    #         if get_escape_time(col, max_iterations) is None:
    #             color_arr[ind][ind_col] = 0
    #
    #         elif get_escape_time(col, max_iterations) == 0:
    #             color_arr[ind][ind_col] = 1
    #
    #         else:
    #             color = (max_iterations - (get_escape_time(col, max_iterations) + 1)) / (max_iterations + 1)
    #             color_arr[ind][ind_col] = color
    #
    #
    # return color_arr

    escape_time_arr = np.zeros_like(c_arr)
    for ind, value in enumerate(c_arr):
        for ind_col, col in enumerate(value):
            escape_time_arr[ind][ind_col] = get_escape_time(complex(c_arr[ind][ind_col]), max_iterations)

    color_arr = np.zeros_like(c_arr)

    color_arr[escape_time_arr == 0] = 1
    color_arr[escape_time_arr is None] = 0

    color_arr[escape_time_arr != 0 and escape_time_arr != 1] = (max_iterations - escape_time_arr + 1) / (
                max_iterations + 1)
    return color_arr