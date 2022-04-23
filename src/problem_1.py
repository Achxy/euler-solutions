from benchmark import measure


def _summation_of_progression(leng, num):
    k = leng // num
    return k * ((num + (num * k)) / 2)


@measure
def problem_1(length):
    length -= 1
    return int(
        _summation_of_progression(length, 3)
        + _summation_of_progression(length, 5)
        - _summation_of_progression(length, 15)
    )


if __name__ == "__main__":
    print(problem_1(1000))
