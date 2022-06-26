from tools import Benchmarked, form_path


def _parse_names(data):
    return sorted(data.replace('"', "").split(","))


def _get_data(path=form_path("p022_names.txt")):
    with open(path, "r") as f:
        return _parse_names(f.read())


@Benchmarked
def problem_22(sorted_data=_get_data()):
    return sum(
        sum(map(lambda char: ord(char) - 64, val)) * pos
        for pos, val in enumerate(sorted_data, start=1)
    )


if __name__ == "__main__":
    problem_22()
