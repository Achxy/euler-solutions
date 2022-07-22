from problem_18 import get_triangle_data, problem_18
from tools import Benchmarked, form_path


@Benchmarked
def problem_67(data=get_triangle_data(form_path("p067_triangle.txt"))):
    return problem_18.function(data)


if __name__ == "__main__":
    problem_67()
