import numpy as np

def get_escape_time(c: np.array(complex), max_iterations: int) -> int | None:
    """
    Takes a complex number and gets the escape time for it. The escape time is the moment when the absolute value of the
    magnitude is greater than 2.

    Parameters:
        c: complex number
        max_iterations: int

    Return:
        int of number of iterations it takes to escape within range of max_iterations. If it does not escape,
        returns None.

    """
    z = c
    if np.abs(z) > 2:
        return 0
    for i in range(max_iterations):
        z = z**2 + c
        if np.abs(z) > 2:
            return i + 1
    return None

def get_escape_time_alt(c: np.array(complex), max_iterations: int) -> int:
    """
    Takes a complex number and gets the escape time for it. The escape time is the moment when the absolute value of the
    magnitude is greater than 2.

    Parameters:
        c: complex number
        max_iterations: int

    Return:
        number of iterations it takes to escape within range of max_iterations. If it does not escape,
        returns max_iterations + 1

        """
    z = c
    if np.abs(z) > 2:
        return 0
    for i in range(max_iterations):
        z = z**2 + c
        if np.abs(z) > 2:
            return i + 1
    return max_iterations + 1


def get_complex_grid(top_left: complex, bottom_right: complex, step: float) -> np.ndarray:
    """
    Creates an array of evenly spaced complex numbers to generate the Mandelbrot Set. Each complex number represents
    one pixel of the image.

    Parameters:
        top_left: complex number that grid is starting at
        bottom_right: complex number that grid goes to, but does not include
        step: float that is the difference between each value in a row

    Return:
        np.ndarray of complex numbers
    """
    reals = np.arange(top_left.real, bottom_right.real, step)
    imags = np.arange(top_left.imag, bottom_right.imag, -1 * step)
    imags = (imags.reshape((len(imags), 1)))
    return reals + (imags * 1j)

def get_escape_time_color_arr(c_arr: np.ndarray, max_iterations: int) -> np.ndarray:
    """
    Assigns a color value to each item in the array of complex numbers for the Mandelbrot Set.

    Parameters:
        c_arr: array of complex numbers
        max_iterations: int

    Returns:
        np.ndarray of color values
    """
    color_arr = np.zeros_like(c_arr).real
    for i in range(len(c_arr)):
        for j in range(len(c_arr)):
            color_arr[i][j] = get_escape_time(c_arr[i][j], max_iterations)
    color_arr = (max_iterations-color_arr+1)/(max_iterations+1)
    return color_arr



# get_escape_time_color_arr with np.vectorize

# def get_escape_time_color_arr(c_arr: np.ndarray, max_iterations: int) -> np.ndarray:
#     vectorized_escape_times = np.vectorize(get_escape_time_alt)
#     color_arr = np.array(vectorized_escape_times(c_arr.real, max_iterations))
#     color_arr = (max_iterations - color_arr + 1)/(max_iterations + 1)
#     return color_arr

def get_julia_color_arr(c_arr: np.ndarray, c: complex, max_iterations: int) -> np.ndarray:
    """
        Assigns a color value to each item in the array of complex numbers of the Julia Set.

        Parameters:
            c_arr: array of complex numbers
            max_iterations: int

        Returns:
            np.ndarray of color values
        """
    color_arr = np.zeros_like(c_arr).real
    for i in range(len(c_arr)):
        for j in range(len(c_arr)):
            color_arr[i][j] = get_escape_time_julia(c_arr[i][j], c, max_iterations)
    color_arr = (max_iterations-color_arr+1)/(max_iterations+1)
    return color_arr

def get_escape_time_julia(start: np.ndarray, c: complex, max_iterations: int) -> int:
    """
    Takes a complex number grid and gets the escape time for it. The escape time is the moment when the absolute value
    of the magnitude is greater than 2.

    Parameters:
        start: complex number grid
        c: complex number
        max_iterations: int

    Return:
        int of number of iterations it takes to escape within range of max_iterations. If it does not escape,
        returns max_iterations + 1:
    """
    z = start
    if np.abs(z) > 2:
        return 0
    for i in range(max_iterations):
        z = z ** 2 + c
        if np.abs(z) > 2:
            return i + 1
    return None