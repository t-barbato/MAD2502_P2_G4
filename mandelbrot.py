def get_escape_time(c: complex, max_iterations: int) -> int | None:
    z = c
    if abs(z) > 2:
        return 0
    for i in range(max_iterations):
        z = z**2 + c
        if abs(z) > 2:
            return i + 1
    return None