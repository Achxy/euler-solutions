from benchmark import Benchmarked


def collatz(j, _collatz_cache={0: 0, 1: 1}):
    find = _collatz_cache.get(j)
    if find is None:
        ret = collatz((3 * j) + 1 if j & 1 else j // 2) + 1
        _collatz_cache[j] = ret
        return ret
    return find


@Benchmarked
def problem_14(limit=1_000_000):
    return max(range(1, limit), key=collatz)


if __name__ == "__main__":
    problem_14()
