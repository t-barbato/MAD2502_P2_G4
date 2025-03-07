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