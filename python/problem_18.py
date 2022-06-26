from tools import Benchmarked, form_path


def _parse_triangle(data: str) -> list[list[int]]:
    return [[int(x) for x in line.split()] for line in data.splitlines()]


def get_triangle_data(path=form_path("p018_triangle.txt")) -> list[list[int]]:
    with open(path, "r") as f:
        return _parse_triangle(f.read())


def _reform(triangle: list):
    second_last_row, last_row, new_last_row = triangle[-2], triangle[-1], []
    for index, item in enumerate(second_last_row):
        new_last_row.append(max(last_row[index], last_row[index + 1]) + item)
    del triangle[-2:]
    triangle.append(new_last_row)


@Benchmarked
def problem_18(data=get_triangle_data()):
    while len(data) != 1:
        _reform(data)
    return data[0][0]


if __name__ == "__main__":
    problem_18()
