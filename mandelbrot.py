import numpy as np

def get_escape_time(c: np.array(complex), max_iterations: int) -> int | None:
    z = np.array(c)
    if np.abs(z) > 2:
        return 0
    for i in range(max_iterations):
        z = z**2 + c
        if np.abs(z) > 2:
            return i + 1
    return None


def get_complex_grid(top_left: complex, bottom_right: complex, step: float) -> np.ndarray:
    reals = np.arange(top_left.real, bottom_right.real, step)
    imags = np.arange(top_left.imag, bottom_right.imag, -1 * step)
    imags = (imags.reshape((len(imags), 1)))
    return reals + (imags * 1j)


# def get_escape_time_color_arr(c_arr: np.ndarray, max_iterations: int) -> np.ndarray:
#     # color_arr = c_arr.copy()
#     # for ind,value in enumerate(c_arr):
#     #     for ind_col, col in enumerate(value):
#     #
#     #         if get_escape_time(col, max_iterations) is None:
#     #             color_arr[ind][ind_col] = 0
#     #
#     #         elif get_escape_time(col, max_iterations) == 0:
#     #             color_arr[ind][ind_col] = 1
#     #
#     #         else:
#     #             color = (max_iterations - (get_escape_time(col, max_iterations) + 1)) / (max_iterations + 1)
#     #             color_arr[ind][ind_col] = color
#     #
#     #
#     # return color_arr
#
#     escape_time_arr = np.zeros_like(c_arr)
#     for ind, value in enumerate(c_arr):
#         for ind_col, col in enumerate(value):
#             escape_time_arr[ind][ind_col] = get_escape_time(complex(c_arr[ind][ind_col]), max_iterations)
#
#     color_arr = np.zeros_like(c_arr)
#
#     color_arr[escape_time_arr == 0] = 1
#     color_arr[escape_time_arr is None] = 0
#
#     color_arr[escape_time_arr != 0 and escape_time_arr != 1] = (max_iterations - escape_time_arr + 1) / (
#                 max_iterations + 1)
#     return color_arr

# def get_escape_time_color_arr(c_arr: np.ndarray, max_iterations: int) -> np.ndarray:
#     escape_time_arr = np.zeros_like(c_arr)
#     color_arr = np.zeros_like(c_arr)
#     for i in range(len(c_arr)):
#         for j in range(len(c_arr[i])):
#             escape_time_arr[i][j] = get_escape_time(c_arr[i][j], max_iterations)
#     color_arr[escape_time_arr != 0 and escape_time_arr != max_iterations and escape_time_arr is not None] = (max_iterations-escape_time_arr+1)/(max_iterations+1)
#     color_arr[escape_time_arr == max_iterations] = 1/(max_iterations+1)
#     color_arr[escape_time_arr == 0] = 1
#     color_arr[escape_time_arr is None] = 0
#     return color_arr

# def get_escape_time_color_arr(c_arr: np.ndarray, max_iterations: int) -> np.ndarray:
#     color_arr = (np.zeros_like(c_arr)).real
#     inter = 0
#     for i in range(len(c_arr)):
#         for j in range(len(c_arr)):
#             inter = get_escape_time(c_arr[i][j], max_iterations)
#             if inter == 0:
#                 color_arr[i][j] = 1
#             elif inter == max_iterations:
#                 color_arr[i][j] = 1/(max_iterations + 1)
#             elif inter is None:
#                 color_arr[i][j] = 0
#             else:
#                 color_arr[i][j] = (max_iterations-inter+1)/(max_iterations+1)
#     return color_arr

def get_escape_time_color_arr(c_arr: np.ndarray, max_iterations: int) -> np.ndarray:
    color_arr = np.zeros_like(c_arr).real
    for i in range(len(c_arr)):
        for j in range(len(c_arr)):
            color_arr[i][j] = get_escape_time(c_arr[i][j], max_iterations)
    color_arr = (max_iterations-color_arr+1)/(max_iterations+1)
    return color_arr

grid = get_complex_grid(-2+1.25j, 0.5-1.25j, 0.01)
colors = get_escape_time_color_arr(grid, 30)

# get_escape_time_color_arr with np.vectorize

# def get_escape_time_color_arr(c_arr: np.ndarray, max_iterations: int) -> np.ndarray:
#     vectorized_escape_times = np.vectorize(get_escape_time)
#     color_arr = np.array(vectorized_escape_times(c_arr.real, max_iterations))
#     color_arr = color_arr[np.] # something to filter out the None values
#     color_arr = (max_iterations - color_arr + 1)/(max_iterations + 1)
#     return color_arr

