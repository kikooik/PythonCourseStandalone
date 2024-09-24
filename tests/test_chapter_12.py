import pytest

class TestChapter12ex01:
    def test_greet(self):
        from course.chapter_12.solutions.solution_1 import greet
        assert greet("Анна") == "Привет, Анна!"
        assert greet("Иван") == "Привет, Иван!"
        assert greet("Мария") == "Привет, Мария!"

class TestChapter12ex02:
    def test_add(self):
        from course.chapter_12.solutions.solution_2 import add
        assert add(3, 5) == 8
        assert add(-1, 1) == 0
        assert add(10, -3) == 7

class TestChapter12ex03:
    def test_multiply(self):
        from course.chapter_12.solutions.solution_3 import multiply
        assert multiply(3, 5) == 15
        assert multiply(2, -2) == -4
        assert multiply(0, 5) == 0

class TestChapter12ex04:
    def test_square(self):
        from course.chapter_12.solutions.solution_4 import square
        assert square(4) == 16
        assert square(-3) == 9
        assert square(0) == 0

class TestChapter12ex05:
    def test_max_of_two(self):
        from course.chapter_12.solutions.solution_5 import max_of_two
        assert max_of_two(3, 7) == 7
        assert max_of_two(10, 5) == 10
        assert max_of_two(-1, -10) == -1

class TestChapter12ex06:
    def test_length_of_string(self):
        from course.chapter_12.solutions.solution_6 import length_of_string
        assert length_of_string("Python") == 6
        assert length_of_string("") == 0
        assert length_of_string("Программирование") == 16

class TestChapter12ex07:
    def test_count_unique_elements(self):
        from course.chapter_12.solutions.solution_7 import count_unique_elements
        assert count_unique_elements([1, 2, 2, 3, 3, 3]) == {1: 1, 2: 2, 3: 3}
        assert count_unique_elements(["a", "b", "a"]) == {"a": 2, "b": 1}
        assert count_unique_elements([5, 5, 5, 5]) == {5: 4}

class TestChapter12ex08:
    def test_swap_keys_values(self):
        from course.chapter_12.solutions.solution_8 import swap_keys_values
        assert swap_keys_values({'a': 1, 'b': 2}) == {1: 'a', 2: 'b'}
        assert swap_keys_values({1: 'x', 2: 'y'}) == {'x': 1, 'y': 2}
        assert swap_keys_values({'key1': 'val1', 'key2': 'val2'}) == {'val1': 'key1', 'val2': 'key2'}

class TestChapter12ex09:
    def test_sort_by_length(self):
        from course.chapter_12.solutions.solution_9 import sort_by_length
        assert sort_by_length(["apple", "banana", "kiwi"]) == ["kiwi", "apple", "banana"]
        assert sort_by_length(["abc", "a", "abcd"]) == ["a", "abc", "abcd"]
        assert sort_by_length(["Python", "C", "Java"]) == ["C", "Java", "Python"]

class TestChapter12ex10:
    def test_merge_dicts(self):
        from course.chapter_12.solutions.solution_10 import merge_dicts
        dict1 = {'a': {1, 2}, 'b': {3, 4}}
        dict2 = {'b': {5}, 'c': {6, 7}}
        assert merge_dicts(dict1, dict2) == {'a': {1, 2}, 'b': {3, 4, 5}, 'c': {6, 7}}
        dict3 = {'x': {9}, 'y': {10}}
        dict4 = {'y': {11}, 'z': {12}}
        assert merge_dicts(dict3, dict4) == {'x': {9}, 'y': {10, 11}, 'z': {12}}

class TestChapter12ex11:
    def test_intersect_lists(self):
        from course.chapter_12.solutions.solution_11 import intersect_lists
        assert intersect_lists([1, 2, 3, 4], [2, 4, 6]) == [2, 4]
        assert intersect_lists(["a", "b", "c"], ["b", "d"]) == ["b"]
        assert intersect_lists([1, 3, 5], [2, 4, 6]) == []

class TestChapter12ex12:
    def test_uniqueness(self):
        from course.chapter_12.solutions.solution_12 import uniqueness
        assert uniqueness([{1, 2}, {2, 3}, {4, 5}]) == {1, 3, 4, 5}
        assert uniqueness([{1}, {1, 2}, {2, 3}]) == {3}
        assert uniqueness([{10, 20}, {30}, {10, 40}]) == {20, 30, 40}

class TestChapter12ex13:
    def test_replace_in_matrix(self):
        from course.chapter_12.solutions.solution_13 import replace_in_matrix
        matrix = [[1, 2], [1, 3]]
        replace_in_matrix(matrix, 1, 9)
        assert matrix == [[9, 2], [9, 3]]
        matrix2 = [[0, 0], [0, 1]]
        replace_in_matrix(matrix2, 0, 5)
        assert matrix2 == [[5, 5], [5, 1]]

class TestChapter12ex14:
    def test_find_anagrams(self):
        from course.chapter_12.solutions.solution_14 import find_anagrams
        word_list = ["listen", "silent", "enlist", "hello", "loleh"]
        result = find_anagrams(word_list)
        expected = {
            'listen': ['silent', 'enlist'], 
            'silent': ['listen', 'enlist'], 
            'enlist': ['listen', 'silent'], 
            'hello': ['loleh'], 
            'loleh': ['hello']
        }
        assert result == expected
        word_list2 = ["rat", "tar", "art", "car"]
        result2 = find_anagrams(word_list2)
        expected2 = {
            'rat': ['tar', 'art'],
            'tar': ['rat', 'art'],
            'art': ['rat', 'tar'],
            'car': []
        }
        assert result2 == expected2

class TestChapter12ex15:
    def test_calculate_salary(self):
        from course.chapter_12.solutions.solution_15 import calculate_salary
        assert calculate_salary(40) == 4000
        assert calculate_salary(40, 150) == 6000
        assert calculate_salary(0, 100) == 0

class TestChapter12ex16:
    def test_greet_users(self):
        from course.chapter_12.solutions.solution_16 import greet_users
        assert greet_users("Анна", "Иван") == "Привет, Анна!\nПривет, Иван!\n"
        assert greet_users("Мария", "Сергей", "Ольга") == "Привет, Мария!\nПривет, Сергей!\nПривет, Ольга!\n"

class TestChapter12ex17:
    def test_join_strings(self):
        from course.chapter_12.solutions.solution_17 import join_strings
        assert join_strings("яблоко", "банан", "апельсин") == ["апельсин", "яблоко"]
        assert join_strings("кушать", "пить") == "кушать"
        assert join_strings("ананас", "лимон", "манго") == "ананас"

class TestChapter12ex18:
    def test_user_info(self):
        from course.chapter_12.solutions.solution_18 import user_info
        assert user_info("Анна", age=25, city="Москва") == "Имя: Анна\nage: 25\ncity: Москва"
        assert user_info("Иван", job="Программист", city="Санкт-Петербург") == "Имя: Иван\njob: Программист\ncity: Санкт-Петербург"

class TestChapter12ex19:
    def test_multiply_all(self):
        from course.chapter_12.solutions.solution_19 import multiply_all
        assert multiply_all(2, 3, 4) == 24
        assert multiply_all(1, 5) == 5
        assert multiply_all(0, 10) == 0

class TestChapter12ex20:
    def test_find_max(self):
        from course.chapter_12.solutions.solution_20 import find_max
        assert find_max(2, 5, 9, 3) == 9
        assert find_max(7, 1) == 7
        assert find_max(0, -1, -10) == 0

class TestChapter12ex21:
    def test_generate_report(self):
        from course.chapter_12.solutions.solution_21 import generate_report
        assert generate_report("Анна", "Задача1", "Задача2", productivity=85) == (
            "Отчёт для Анна\nВыполненные задачи: Задача1, Задача2\nproductivity: 85")
        assert generate_report("Иван", "Проект1", "Проект2", productivity=90, overtime=5) == (
            "Отчёт для Иван\nВыполненные задачи: Проект1, Проект2\nproductivity: 90\novertime: 5")

class TestChapter12ex22:
    def test_check_analysis(self):
        from course.chapter_12.solutions.solution_22 import check_analysis
        assert check_analysis(id123={"яблоко": 100, "банан": 50}, id124={"банан": 50}, id125={"яблоко": 100}) == (
            "id123", "яблоко")
        assert check_analysis(id200={"апельсин": 200}, id201={"груша": 150, "яблоко": 50}) == (
            "id200", "апельсин")
