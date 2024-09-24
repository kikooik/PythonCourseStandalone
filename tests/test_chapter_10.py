import pytest
import ast
from ast import Assign

class TestChapter10ex01:
    @pytest.mark.solution_runner("1 2 2 3 4 4 5 1", 0.1)
    def test_solution_1_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "5 4 3 2 1\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner("9 8 7 6 5 9 7 8", 0.1)
    def test_solution_1_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "9 8 7 6 5\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter10ex02:
    @pytest.mark.solution_runner(("1 2 3 4\n3 4 5 6"), 0.1)
    def test_solution_2_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "3 4\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner(("10 20 30\n20 30 40"), 0.1)
    def test_solution_2_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "20 30\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter10ex03:
    @pytest.mark.solution_runner("hello world", 0.1)
    def test_solution_3_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Уникальные символы: d e h l o r w\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner("programming", 0.1)
    def test_solution_3_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Уникальные символы: a g i m n o p r\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter10ex04:
    @pytest.mark.solution_runner(("1 2 3 4\n3 4 5 6"), 0.1)
    def test_solution_4_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "1 2 5 6\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner(("10 20 30\n20 30 40"), 0.1)
    def test_solution_4_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "10 40\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter10ex05:
    @pytest.mark.solution_runner("Программирование это круто и это интересно", 0.1)
    def test_solution_5_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Программирование и интересно круто это\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner("Python это круто и интересно", 0.1)
    def test_solution_5_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Python и интересно круто это\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter10ex06:
    @pytest.mark.solution_runner(("abcde\ncdefg"), 0.1)
    def test_solution_6_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "c d e\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner(("12345\n34567"), 0.1)
    def test_solution_6_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "3 4 5\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter10ex07:
    @pytest.mark.solution_runner("1 2 2 3 4 4 5", 0.1)
    def test_solution_7_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Количество уникальных элементов: 5\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner("10 10 20 20 30", 0.1)
    def test_solution_7_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "Количество уникальных элементов: 3\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter10ex08:
    @pytest.mark.solution_runner(("1 2 3\n2 3 4\n1 3 5"), 0.1)
    def test_solution_8_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "3\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner(("10 20 30\n20 30 40\n20 30 50"), 0.1)
    def test_solution_8_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "20 30\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"


class TestChapter10ex09:
    @pytest.mark.solution_runner(("1 2 3\n2 3 4\n3 4 5"), 0.1)
    def test_solution_9_output_1(self, solution_runner):
        solution_out = solution_runner
        expected_output = "1\n\n5\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"

    @pytest.mark.solution_runner(("10 20 30\n20 30 40\n30 40 50"), 0.1)
    def test_solution_9_output_2(self, solution_runner):
        solution_out = solution_runner
        expected_output = "10\n\n50\n"
        assert expected_output == solution_out, f"expected output is `{expected_output}` \n Your program gives `{solution_out}`"
