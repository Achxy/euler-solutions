from benchmark import measure


@measure
def problem_2(lim):
    a, b, c, d = 1, 1, 2, 0
    while lim > c:
        d += c
        a = b + c
        b = a + c
        c = a + b
    return d


if __name__ == "__main__":
    print(problem_2(40_00_000))
