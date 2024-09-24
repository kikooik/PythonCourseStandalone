import pytest
import ast
from ast import Assign

class TestChapter11ex01:
    @pytest.mark.solution_runner("Иван Ольга Иван Ольга Ольга Сергей Иван", 0.1)
    def test_solution_1_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Иван: 3\nОльга: 3\nСергей: 1\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner("Иван Иван Иван", 0.1)
    def test_solution_1_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Иван: 3\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter11ex02:
    @pytest.mark.solution_runner("Иван: 5\nОльга: 6\nИван: 6\n", 0.1)
    def test_solution_2_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Класс 5: Иван\nКласс 6: Ольга, Иван\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner("Анна: 7\nСергей: 8\nАнна: 8\n", 0.1)
    def test_solution_2_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Класс 7: Анна\nКласс 8: Сергей, Анна\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter11ex03:
    @pytest.mark.solution_runner(("10 15 3 7\n17"), 0.1)
    def test_solution_3_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "(10, 7)\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner(("1 2 3 4\n5"), 0.1)
    def test_solution_3_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "(2, 3)\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner(("1 2 3\n10"), 0.1)
    def test_solution_3_output_3(self, solution_runner):
        solution_out = solution_runner
        expected_output = "10\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter11ex04:
    @pytest.mark.solution_runner("swiss", 0.1)
    def test_solution_4_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "w\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner("aabbcc", 0.1)
    def test_solution_4_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "None\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter11ex05:
    @pytest.mark.solution_runner(("mgu.edu: andrei_serov alexander_pushkin elena_belova kirill_stepanov\n"
                                  "gmail.com: alena.semyonova ivan.polekhin marina_abrabova\n"), 0.1)
    def test_solution_5_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = (
            "alena.semyonova@gmail.com\n"
            "alexander_pushkin@mgu.edu\n"
            "andrei_serov@mgu.edu\n"
            "elena_belova@mgu.edu\n"
            "ivan.polekhin@gmail.com\n"
            "kirill_stepanov@mgu.edu\n"
            "marina_abrabova@gmail.com\n"
        )
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter11ex06:
    @pytest.mark.solution_runner(("Барсик 4 Иван Петров\nМурзик 2 Ольга Иванова\n"
                                  "Лютик 5 Иван Петров\nСнежок 3 Мария Смирнова\n"
                                  "Рыжик 7 Анна Кузнецова\nБублик 6 Сергей Николаев\n"
                                  "Черныш 1 Анна Кузнецова\n"), 0.1)
    def test_solution_6_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = (
            "Иван Петров: Барсик, 4; Лютик, 5\n"
            "Ольга Иванова: Мурзик, 2\n"
            "Мария Смирнова: Снежок, 3\n"
            "Анна Кузнецова: Рыжик, 7; Черныш, 1\n"
            "Сергей Николаев: Бублик, 6\n"
        )
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter11ex07:
    @pytest.mark.solution_runner("a a a b c a a d c d d", 0.1)
    def test_solution_7_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner("x y z x x z y z", 0.1)
    def test_solution_7_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "x y z x_1 x_2 z_1 y_1 z_2\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter11ex08:
    @pytest.mark.solution_runner(("Толстой Лев: Анна Каренина, Война и Мир\n",
                                  "Лондон Джек: Мартин Иден, Аляска Кид\n",
                                  "Толстой Лев: Воскресение\n"), 0.1)
    def test_solution_8_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = (
            "Толстой Лев: Анна Каренина, Война и Мир, Воскресение\n"
            "Лондон Джек: Мартин Иден, Аляска Кид\n"
        )
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter11ex09:
    @pytest.mark.solution_runner("Это пример текста. Этот текст для проверки биграмм и триграмм.", 0.1)
    def test_solution_9_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = (
            "Слова: это: 1, пример: 1, текста: 1, этот: 1, текст: 1, для: 1, проверки: 1, биграмм: 1, и: 1, триграмм: 1\n"
            "Биграммы: это пример: 1, пример текста: 1, текста этот: 1, этот текст: 1, текст для: 1, для проверки: 1, проверки биграмм: 1, биграмм и: 1, и триграмм: 1\n"
            "Триграммы: это пример текста: 1, пример текста этот: 1, текста этот текст: 1, этот текст для: 1, текст для проверки: 1, для проверки биграмм: 1, проверки биграмм и: 1, биграмм и триграмм: 1\n"
        )
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"
