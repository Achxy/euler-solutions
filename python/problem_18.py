from tools import Benchmarked, form_path


def _parse_triangle(data):
    return [[int(x) for x in line.split()] for line in data.splitlines()]


def get_triangle_data(path=form_path("p018_triangle.txt")):
    with open(path, "r") as f:
        return _parse_triangle(f.read())


def _reform(triangle):
    lrow = triangle[-1]
    triangle.append([max(lrow[i], lrow[i + 1]) + v for i, v in enumerate(triangle[-2])])
    del triangle[-3:-1]


@Benchmarked
def problem_18(data=get_triangle_data()):
    while len(data) != 1:
        _reform(data)
    return data[0][0]


if __name__ == "__main__":
    problem_18()
