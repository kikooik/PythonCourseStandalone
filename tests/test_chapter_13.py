import pytest
import ast
from ast import Assign

class TestChapter13ex01:
    def test_apply_to_all(self):
        from course.chapter_13.solutions.solution_1 import apply_to_all

        def sqr(a):
            return a * a

        def increment(a):
            return a + 1

        data = [1, 2, 3, 4, 5]
        assert apply_to_all(data, sqr) == [1, 4, 9, 16, 25]
        assert apply_to_all(data, increment) == [2, 3, 4, 5, 6]

class TestChapter13ex02:
    def test_filter_data(self):
        from course.chapter_13.solutions.solution_2 import filter_data

        def even(a):
            return a % 2 == 0

        def positive(a):
            return a > 0

        data = [1, 2, 3, 4, 5, 6]
        assert filter_data(data, even) == [2, 4, 6]
        assert filter_data([-1, -2, 3, 4, 0], positive) == [3, 4]

class TestChapter13ex03:
    def test_apply_multiple(self):
        from course.chapter_13.solutions.solution_3 import apply_multiple

        def increment(a):
            return a + 1

        def sqr(a):
            return a * a

        data = [1, 2, 3, 4]
        assert apply_multiple(data, increment, sqr) == [4, 9, 16, 25]
        assert apply_multiple([2, 3, 4], sqr, increment) == [5, 10, 17]

class TestChapter13ex04:
    def test_check_all(self):
        from course.chapter_13.solutions.solution_4 import check_all

        def positive(a):
            return a > 0

        def even(a):
            return a % 2 == 0

        data = [1, 2, 3, 4]
        assert check_all(data, positive) == True
        assert check_all([2, 4, 6], even) == True
        assert check_all([1, 3, 5], even) == False

class TestChapter13ex05:
    def test_find_max_by(self):
        from course.chapter_13.solutions.solution_5 import find_max_by

        def abs_value(a):
            return abs(a)

        data = [-10, -20, 5, 3]
        assert find_max_by(data, abs_value) == -20
        assert find_max_by([1, -1, 2, -2], abs_value) == 2

class TestChapter13ex06:
    def test_create_operation(self):
        from course.chapter_13.solutions.solution_6 import create_operation

        add_func = create_operation("add")
        subtract_func = create_operation("subtract")
        multiply_func = create_operation("multiply")
        divide_func = create_operation("divide")

        assert add_func(4, 6) == 10
        assert subtract_func(10, 6) == 4
        assert multiply_func(2, 3) == 6
        assert divide_func(8, 2) == 4

class TestChapter13ex07:
    def test_apply_to_matrix(self):
        from course.chapter_13.solutions.solution_7 import apply_to_matrix

        matrix = [[1, 2], [3, 4]]

        def double(a):
            return a * 2

        assert apply_to_matrix(matrix, double) == [[2, 4], [6, 8]]
        assert apply_to_matrix([[0, 1], [2, 3]], double) == [[0, 2], [4, 6]]

class TestChapter13ex08:
    def test_apply_to_nested_list(self):
        from course.chapter_13.solutions.solution_8 import apply_to_nested_list

        def sqr(a):
            return a * a

        nested_list = [[1, 2, 3], [4, [4, 5]], [6, 7, 8, 9]]
        assert apply_to_nested_list(nested_list, sqr) == [[1, 4, 9], [16, [16, 25]], [36, 49, 64, 81]]

        nested_list2 = [[0, 1], [2, [3, 4]]]
        assert apply_to_nested_list(nested_list2, sqr) == [[0, 1], [4, [9, 16]]]

class TestChapter13ex09:
    def test_transform_list(self):
        from course.chapter_13.solutions.solution_9 import transform_list

        def double(a):
            return a * 2

        def positive(a):
            return a > 0

        data = [10, -5, 0, 20, -7, 15]
        assert transform_list(data, double, positive) == [20, -5, 0, 40, -7, 30]
        assert transform_list([1, -2, 3, -4], double, positive) == [2, -2, 6, -4]

class TestChapter13ex10:
    def test_apply_functions_sequence(self):
        from course.chapter_13.solutions.solution_10 import apply_functions_sequence

        def increment(a):
            return a + 1

        def doubler(a):
            return a * 2

        func_list = [increment, doubler]
        data = [1, 2, 3]
        assert apply_functions_sequence(data, func_list) == [4, 6, 8]

        func_list2 = [doubler, increment]
        assert apply_functions_sequence([2, 3], func_list2) == [5, 7]

class TestChapter13ex11:
    def test_multi_criteria_sort(self):
        from course.chapter_13.solutions.solution_11 import multi_criteria_sort

        data = [(1, 5), (2, 3), (1, 2), (2, 7), (1, 4)]
        assert multi_criteria_sort(data, lambda x: x[0], lambda x: x[1]) == [(1, 2), (1, 4), (1, 5), (2, 3), (2, 7)]

        data2 = [(3, 4), (2, 3), (2, 2), (3, 1)]
        assert multi_criteria_sort(data2, lambda x: x[0], lambda x: x[1]) == [(2, 2), (2, 3), (3, 1), (3, 4)]


class TestChapter13ex12:
    @pytest.mark.solution_runner("1 2 3 4 5", 0.1)
    def test_square_lambda(self, solution_runner):
        solution_out = solution_runner
        expected_output = "[1, 4, 9, 16, 25]\n"
        assert solution_out == expected_output, f"Expected {expected_output}, but got {solution_out}"

        # Проверка, что используется lambda функция
        file_path = "course/chapter_13/solutions/solution_12.py"
        with open(file_path, "r") as f:
            tree = ast.parse(f.read())
            assert any(isinstance(node, ast.Lambda) for node in ast.walk(tree)), "Lambda function not used"

class TestChapter13ex13:
    @pytest.mark.solution_runner("1 2 3 4 5 6 7 8", 0.1)
    def test_filter_even_lambda(self, solution_runner):
        solution_out = solution_runner
        expected_output = "[2, 4, 6, 8]\n"
        assert solution_out == expected_output, f"Expected {expected_output}, but got {solution_out}"

        # Проверка на lambda
        file_path = "course/chapter_13/solutions/solution_13.py"
        with open(file_path, "r") as f:
            tree = ast.parse(f.read())
            assert any(isinstance(node, ast.Lambda) for node in ast.walk(tree)), "Lambda function not used"

class TestChapter13ex14:
    @pytest.mark.solution_runner("apple banana pear grape", 0.1)
    def test_sort_strings_by_length_lambda(self, solution_runner):
        solution_out = solution_runner
        expected_output = "['pear', 'apple', 'grape', 'banana']\n"
        assert solution_out == expected_output, f"Expected {expected_output}, but got {solution_out}"

        # Проверка на lambda
        file_path = "course/chapter_13/solutions/solution_14.py"
        with open(file_path, "r") as f:
            tree = ast.parse(f.read())
            assert any(isinstance(node, ast.Lambda) for node in ast.walk(tree)), "Lambda function not used"

class TestChapter13ex15:
    @pytest.mark.solution_runner("1 3 4 1 5 2 2 5", 0.1)
    def test_sort_tuples_by_second_lambda(self, solution_runner):
        solution_out = solution_runner
        expected_output = "[(4, 1), (5, 2), (1, 3), (2, 5)]\n"
        assert solution_out == expected_output, f"Expected {expected_output}, but got {solution_out}"

        # Проверка на lambda
        file_path = "course/chapter_13/solutions/solution_15.py"
        with open(file_path, "r") as f:
            tree = ast.parse(f.read())
            assert any(isinstance(node, ast.Lambda) for node in ast.walk(tree)), "Lambda function not used"

class TestChapter13ex16:
    @pytest.mark.solution_runner("2 3 4\n3 2 1", 0.1)
    def test_exponentiate_lambda(self, solution_runner):
        solution_out = solution_runner
        expected_output = "[8, 9, 4]\n"
        assert solution_out == expected_output, f"Expected {expected_output}, but got {solution_out}"

        # Проверка на lambda
        file_path = "course/chapter_13/solutions/solution_16.py"
        with open(file_path, "r") as f:
            tree = ast.parse(f.read())
            assert any(isinstance(node, ast.Lambda) for node in ast.walk(tree)), "Lambda function not used"

class TestChapter13ex17:
    @pytest.mark.solution_runner("apple banana pear grape", 0.1)
    def test_string_lengths_lambda(self, solution_runner):
        solution_out = solution_runner
        expected_output = "[5, 6, 4, 5]\n"
        assert solution_out == expected_output, f"Expected {expected_output}, but got {solution_out}"

        # Проверка на lambda
        file_path = "course/chapter_13/solutions/solution_17.py"
        with open(file_path, "r") as f:
            tree = ast.parse(f.read())
            assert any(isinstance(node, ast.Lambda) for node in ast.walk(tree)), "Lambda function not used"

class TestChapter13ex18:
    @pytest.mark.solution_runner("1 2 3 4 5", 0.1)
    def test_double_lambda(self, solution_runner):
        solution_out = solution_runner
        expected_output = "[2, 4, 6, 8, 10]\n"
        assert solution_out == expected_output, f"Expected {expected_output}, but got {solution_out}"

        # Проверка на lambda
        file_path = "course/chapter_13/solutions/solution_18.py"
        with open(file_path, "r") as f:
            tree = ast.parse(f.read())
            assert any(isinstance(node, ast.Lambda) for node in ast.walk(tree)), "Lambda function not used"

class TestChapter13ex19:
    @pytest.mark.solution_runner("apple banana avocado cherry apricot", 0.1)
    def test_filter_strings_by_first_letter_lambda(self, solution_runner):
        solution_out = solution_runner
        expected_output = "['apple', 'apricot', 'avocado']\n"
        assert solution_out == expected_output, f"Expected {expected_output}, but got {solution_out}"

        # Проверка на lambda
        file_path = "course/chapter_13/solutions/solution_19.py"
        with open(file_path, "r") as f:
            tree = ast.parse(f.read())
            assert any(isinstance(node, ast.Lambda) for node in ast.walk(tree)), "Lambda function not used"
