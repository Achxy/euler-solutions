from benchmark import Benchmarked


def _is_palindromic_number(n) -> bool:
    _str_n = str(n)
    return _str_n == _str_n[::-1]


def _is_lychrel(k, _level=1, *, max_depth=50) -> bool:
    if _is_palindromic_number(k) and _level > 1:
        return False
    if _level > max_depth:
        return True
    lvl = _level + 1
    num = k + int(str(k)[::-1])
    return _is_lychrel(num, _level=lvl)


@Benchmarked
def problem_55(num=10_000):
    return sum(1 for n in range(num) if _is_lychrel(n))


if __name__ == "__main__":
    problem_55()
