from benchmark import Benchmarked


def is_pentagonal(n):
    """
    Pn = n(3n - 1)/2
    Pn - n(3n - 1)/2 = 0
    (-3n^2)/2 - n/2 + Pn = 0

    di = 0.25 - 4 * - 1.5 * Pn
    di = 0.25 + 6Pn

    n = [0.5 +/- sqrt(di)] / -2 * 1.5
    """
    return not (0.5 + (0.25 + 6 * n) ** 0.5) / 3 % 1


@Benchmarked
def problem_44():
    ...
