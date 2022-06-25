from tools import Benchmarked


# TODO: This can be faster
def _palindromic_in_base_10_and_2(n: int):
    base_2 = bin(n)[2:]
    base_10 = str(n)
    if base_10 == base_10[::-1] and base_2 == base_2[::-1]:
        return n
    return 0


@Benchmarked
def problem_36(num=1_000_000):
    return sum(_palindromic_in_base_10_and_2(k) for k in range(num))


if __name__ == "__main__":
    problem_36()
