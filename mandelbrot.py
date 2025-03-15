import numpy as np

def get_escape_time(c: complex, max_iterations: int) -> int | None:
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
    z = np.array(c)
    if np.abs(z) > 2:
        return 0
    for i in range(max_iterations):
        z = z**2 + c
        if np.abs(z) > 2:
            return i + 1
    return None


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


def get_escape_time_color_arr(c_arr: np.ndarray,max_iterations: int):
    """
        Assigns a color value to each item in the array of complex numbers for the Mandelbrot Set.

        Parameters:
            c_arr: array of complex numbers
            max_iterations: int

        Returns:
            np.ndarray of color values
    """
    escape_times = np.zeros(c_arr.shape) # int array
    z = np.zeros_like(c_arr) # complex array
    for iteration in range(max_iterations):
        no_escape_yet = np.abs(z) <= 2 # avoids overflow
        z[no_escape_yet] = z[no_escape_yet]**2 + c_arr[no_escape_yet]
        escaped = (np.abs(z) > 2) & (escape_times == 0) #escape checking
        escape_times[escaped] = iteration # when it escapes

    escape_times[escape_times == 0] = max_iterations + 1 # non escaping
    color_arr = (max_iterations - escape_times + 1)/(max_iterations + 1)

    return color_arr


def get_julia_color_arr(c_arr: np.ndarray, c: complex, max_iterations: int) -> np.ndarray:
    """
        Assigns a color value to each item in the array of complex numbers of the Julia Set.

        Parameters:
            c_arr: array of complex numbers
            c: complex number
            max_iterations: int

        Returns:
            np.ndarray of color values
    """
    escape_times = np.zeros(c_arr.shape)  # int array
    z = c_arr # complex array

    for iteration in range(max_iterations):
        no_escape_yet = np.abs(z) <= 2
        z[no_escape_yet] = z[no_escape_yet] ** 2 + c
        escaped = (np.abs(z) > 2) & (escape_times == 0) # escape checking
        escape_times[escaped] = iteration # when it escapes

    escape_times[escape_times == 0] = max_iterations + 1 # non escaping
    color_arr = (max_iterations - escape_times + 1) / (max_iterations + 1)

    return color_arr