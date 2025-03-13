import numpy as np

def get_escape_time(c: np.array(complex), max_iterations: int) -> int | None:
    z = c
    if np.abs(z) > 2:
        return 0
    for i in range(max_iterations):
        z = z**2 + c
        if np.abs(z) > 2:
            return i + 1
    return None

def get_escape_time_alt(c: np.array(complex), max_iterations: int) -> int | None:
    z = c
    if np.abs(z) > 2:
        return 0
    for i in range(max_iterations):
        z = z**2 + c
        if np.abs(z) > 2:
            return i + 1
    return max_iterations + 1


def get_complex_grid(top_left: complex, bottom_right: complex, step: float) -> np.ndarray:
    reals = np.arange(top_left.real, bottom_right.real, step)
    imags = np.arange(top_left.imag, bottom_right.imag, -1 * step)
    imags = (imags.reshape((len(imags), 1)))
    return reals + (imags * 1j)

# def get_escape_time_color_arr(c_arr: np.ndarray, max_iterations: int) -> np.ndarray:
#     color_arr = np.zeros_like(c_arr).real
#     for i in range(len(c_arr)):
#         for j in range(len(c_arr)):
#             color_arr[i][j] = get_escape_time(c_arr[i][j], max_iterations)
#     color_arr = (max_iterations-color_arr+1)/(max_iterations+1)
#     return color_arr



# get_escape_time_color_arr with np.vectorize

def get_escape_time_color_arr(c_arr: np.ndarray, max_iterations: int) -> np.ndarray:
    vectorized_escape_times = np.vectorize(get_escape_time_alt)
    color_arr = np.array(vectorized_escape_times(c_arr.real, max_iterations))
    color_arr = (max_iterations - color_arr + 1)/(max_iterations + 1)
    return color_arr

