# conftest.py
import os
import pytest
from subprocess import Popen, PIPE, STDOUT, TimeoutExpired

@pytest.fixture()
def solution_runner(request):
    marker = request.node.get_closest_marker("solution_runner")
    if marker is None:
        pytest.fail("The 'solution_runner' marker must be provided")
    chapter = int(request.cls.__name__[-6:-4])
    solution = int(request.cls.__name__[-2:])
    chapter = "chapter_0" + str(chapter) if chapter < 10 else "chapter_" + str(chapter)
    solution = "solution_" + str(solution) + ".py"
    file_path = os.path.join("course", chapter, "solutions", solution)
    result = []

    if not os.path.isfile(file_path):
        pytest.fail("Solution not exist")
    try:
        inputed_values, timeout = marker.args
        if isinstance(inputed_values, str):
            vals = inputed_values + "\n"
            p = Popen(
                ["python3", file_path], stdout=PIPE, stdin=PIPE, stderr=PIPE, text=True
            )
            p.stdin.writelines(vals)
            p.stdin.close()
            p.wait(timeout=timeout)
            result = p.stdout.read()
        elif callable(inputed_values):
            vals = inputed_values() + "\n"
            p = Popen(
                ["python3", file_path], stdout=PIPE, stdin=PIPE, stderr=PIPE, text=True
            )
            p.stdin.writelines(vals)
            p.stdin.close()
            p.wait(timeout=timeout)
            result = p.stdout.read()
        elif isinstance(inputed_values, tuple):
            vals = [val() + "\n" if callable(val) else val + "\n" for val in inputed_values]
            p = Popen(
                ["python3", file_path], stdout=PIPE, stdin=PIPE, stderr=PIPE, text=True
            )
            p.stdin.writelines(vals)
            p.stdin.close()
            p.wait(timeout=timeout)
            result = p.stdout.read()
        elif isinstance(inputed_values, list):
            if isinstance(inputed_values[0], tuple):
                for vals in inputed_values:
                    vals = [val() + "\n" if callable(val) else val + "\n" for val in vals]
                    p = Popen(
                        ["python3", file_path],
                        stdout=PIPE,
                        stdin=PIPE,
                        stderr=PIPE,
                        text=True,
                    )
                    p.stdin.writelines(vals)
                    p.stdin.close()
                    p.wait(timeout=timeout)
                    result.append(p.stdout.read())
            elif isinstance(inputed_values[0], str):
                for vals in inputed_values:
                    vals += "\n"
                    p = Popen(
                        ["python3", file_path],
                        stdout=PIPE,
                        stdin=PIPE,
                        stderr=PIPE,
                        text=True,
                    )
                    p.stdin.writelines(vals)
                    p.stdin.close()
                    p.wait(timeout=timeout)
                    result.append(p.stdout.read())
    except TimeoutExpired:
        pytest.fail("Programm not terminate in timeout")

    return result