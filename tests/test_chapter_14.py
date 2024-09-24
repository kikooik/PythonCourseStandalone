import ast
import pytest

class TestChapter14ex01:
    def test_squares(self):
        from course.chapter_14.solutions.solution_1 import squares
        
        assert squares(5) == [0, 1, 4, 9, 16]
        assert squares(3) == [0, 1, 4]
        assert squares(0) == []

        # Проверка на использование list comprehension
        file_path = "course/chapter_14/solutions/solution_1.py"
        with open(file_path, "r") as f:
            tree = ast.parse(f.read())
            assert any(isinstance(node, ast.ListComp) for node in ast.walk(tree)), "List comprehension not used"

class TestChapter14ex02:
    def test_even_numbers(self):
        from course.chapter_14.solutions.solution_2 import even_numbers
        
        assert even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
        assert even_numbers([10, 15, 20, 25]) == [10, 20]
        assert even_numbers([1, 3, 5]) == []

        # Проверка на использование list comprehension
        file_path = "course/chapter_14/solutions/solution_2.py"
        with open(file_path, "r") as f:
            tree = ast.parse(f.read())
            assert any(isinstance(node, ast.ListComp) for node in ast.walk(tree)), "List comprehension not used"

class TestChapter14ex03:
    def test_sum_of_even_squares(self):
        from course.chapter_14.solutions.solution_3 import sum_of_even_squares
        
        assert sum_of_even_squares([1, 2, 3, 4, 5, 6]) == 56
        assert sum_of_even_squares([10, 20, 30]) == 1400
        assert sum_of_even_squares([1, 3, 5]) == 0

        # Проверка на использование list comprehension
        file_path = "course/chapter_14/solutions/solution_3.py"
        with open(file_path, "r") as f:
            tree = ast.parse(f.read())
            assert any(isinstance(node, ast.ListComp) for node in ast.walk(tree)), "List comprehension not used"

class TestChapter14ex04:
    def test_reverse_strings(self):
        from course.chapter_14.solutions.solution_4 import reverse_strings
        
        assert reverse_strings(["hello", "world"]) == ["olleh", "dlrow"]
        assert reverse_strings(["abc", "123"]) == ["cba", "321"]
        assert reverse_strings([""]) == [""]

        # Проверка на использование list comprehension
        file_path = "course/chapter_14/solutions/solution_4.py"
        with open(file_path, "r") as f:
            tree = ast.parse(f.read())
            assert any(isinstance(node, ast.ListComp) for node in ast.walk(tree)), "List comprehension not used"

class TestChapter14ex05:
    def test_string_lengths(self):
        from course.chapter_14.solutions.solution_5 import string_lengths
        
        assert string_lengths(["apple", "banana", "pear"]) == [5, 6, 4]
        assert string_lengths(["a", "ab", "abc"]) == [1, 2, 3]
        assert string_lengths([""]) == [0]

        # Проверка на использование list comprehension
        file_path = "course/chapter_14/solutions/solution_5.py"
        with open(file_path, "r") as f:
            tree = ast.parse(f.read())
            assert any(isinstance(node, ast.ListComp) for node in ast.walk(tree)), "List comprehension not used"

class TestChapter14ex06:
    def test_multiples_of_3_and_5(self):
        from course.chapter_14.solutions.solution_6 import multiples_of_3_and_5
        
        assert multiples_of_3_and_5(50) == [0, 15, 30, 45]
        assert multiples_of_3_and_5(20) == [0, 15]
        assert multiples_of_3_and_5(5) == [0]

        # Проверка на использование list comprehension
        file_path = "course/chapter_14/solutions/solution_6.py"
        with open(file_path, "r") as f:
            tree = ast.parse(f.read())
            assert any(isinstance(node, ast.ListComp) for node in ast.walk(tree)), "List comprehension not used"

class TestChapter14ex07:
    def test_fibonacci(self):
        from course.chapter_14.solutions.solution_7 import fibonacci
        
        assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        assert fibonacci(5) == [0, 1, 1, 2, 3]
        assert fibonacci(0) == []

        # Проверка на использование list comprehension
        file_path = "course/chapter_14/solutions/solution_7.py"
        with open(file_path, "r") as f:
            tree = ast.parse(f.read())
            assert any(isinstance(node, ast.ListComp) for node in ast.walk(tree)), "List comprehension not used"

class TestChapter14ex08:
    def test_flatten(self):
        from course.chapter_14.solutions.solution_8 import flatten
        
        matrix = [[1, 2], [3, 4], [5, 6]]
        assert flatten(matrix) == [1, 2, 3, 4, 5, 6]
        
        matrix2 = [[0], [1, 2, 3], [4, 5]]
        assert flatten(matrix2) == [0, 1, 2, 3, 4, 5]
        
        assert flatten([[]]) == []

        # Проверка на использование list comprehension
        file_path = "course/chapter_14/solutions/solution_8.py"
        with open(file_path, "r") as f:
            tree = ast.parse(f.read())
            assert any(isinstance(node, ast.ListComp) for node in ast.walk(tree)), "List comprehension not used"


import pytest

class TestChapter14ex09:
    def test_count_up_to(self):
        from course.chapter_14.solutions.solution_9 import count_up_to

        assert list(count_up_to(5)) == [1, 2, 3, 4, 5]
        assert list(count_up_to(3)) == [1, 2, 3]
        assert list(count_up_to(0)) == []

class TestChapter14ex10:
    def test_square_numbers(self):
        from course.chapter_14.solutions.solution_10 import square_numbers

        assert list(square_numbers(4)) == [1, 4, 9, 16]
        assert list(square_numbers(3)) == [1, 4, 9]
        assert list(square_numbers(0)) == []

class TestChapter14ex11:
    def test_even_numbers(self):
        from course.chapter_14.solutions.solution_11 import even_numbers

        assert list(even_numbers(10)) == [2, 4, 6, 8, 10]
        assert list(even_numbers(5)) == [2, 4]
        assert list(even_numbers(1)) == []

class TestChapter14ex12:
    def test_my_range(self):
        from course.chapter_14.solutions.solution_12 import my_range

        assert list(my_range(4, 8)) == [4, 5, 6, 7]
        assert list(my_range(0, 3)) == [0, 1, 2]
        assert list(my_range(10, 10)) == []

class TestChapter14ex13:
    def test_factorials(self):
        from course.chapter_14.solutions.solution_13 import factorials

        assert list(factorials(5)) == [1, 2, 6, 24, 120]
        assert list(factorials(3)) == [1, 2, 6]
        assert list(factorials(1)) == [1]

class TestChapter14ex14:
    def test_fibonacci(self):
        from course.chapter_14.solutions.solution_14 import fibonacci

        assert list(fibonacci(7)) == [1, 1, 2, 3, 5, 8, 13]
        assert list(fibonacci(5)) == [1, 1, 2, 3, 5]
        assert list(fibonacci(1)) == [1]

class TestChapter14ex15:
    def test_multiples_of_3_or_5(self):
        from course.chapter_14.solutions.solution_15 import multiples_of_3_or_5

        assert list(multiples_of_3_or_5(15)) == [3, 5, 6, 9, 10, 12, 15]
        assert list(multiples_of_3_or_5(10)) == [3, 5, 6, 9, 10]
        assert list(multiples_of_3_or_5(5)) == [3, 5]

class TestChapter14ex16:
    def test_infinite_sequence(self):
        from course.chapter_14.solutions.solution_16 import infinite_sequence

        gen = infinite_sequence()
        result = [next(gen) for _ in range(5)]
        assert result == [1, 2, 3, 4, 5]
