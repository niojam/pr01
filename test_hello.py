import pytest
import mock
import os


class MockStdin():
    """
    Pytest-console-scripts wants file-like object for stbydin so we wrap input in a class.

    Pytest-console-scripts docs see: https://github.com/kvas-it/pytest-console-scripts
    """

    def __init__(self, input_values: list):
        self.input = input_values

    def read(self):
        return "\n".join(self.input)


def run_hello_script(runner, name, school, mass=1, height=1) -> "tuple[str, str]":
    script_name = "hello.py"
    working_dir = os.path.dirname(os.path.abspath(__file__))
    script = runner.run('python3.7', script_name, stdin=MockStdin([name, school, str(mass), str(height)]),
                        cwd=working_dir)
    return script.stdout, script.stderr


@pytest.mark.timeout(1.0)
@pytest.mark.incgroup("syntax")
@pytest.mark.weight(0)
@mock.patch('builtins.input', side_effect=lambda x="prompt": "1")
def test_no_SyntaxError(capsys):
    import hello

@pytest.mark.timeout(1.0)
@pytest.mark.script_launch_mode('subprocess')
@pytest.mark.incgroupdepend("syntax")
def test_hello_no_name(script_runner):
    output, _ = run_hello_script(script_runner, name="", school="")

    expected_output_text = "Name was not inserted!"
    assert expected_output_text in output


@pytest.mark.timeout(1.0)
@pytest.mark.script_launch_mode('subprocess')
@pytest.mark.incgroupdepend("syntax")
def test_hello_no_school(script_runner):
    output, _ = run_hello_script(script_runner, name="John", school="")

    expected_output = "School was not inserted!"
    assert expected_output in output


@pytest.mark.timeout(1.0)
@pytest.mark.script_launch_mode('subprocess')
@pytest.mark.incgroupdepend("syntax")
def test_hello_name_school(script_runner):
    output, _ = run_hello_script(script_runner, name="John", school="TTÜ")

    expected_output = "John, welcome to TTÜ"
    assert expected_output in output


@pytest.mark.timeout(1.0)
@pytest.mark.script_launch_mode('subprocess')
@pytest.mark.incgroupdepend("syntax")
def test_bmi_low(script_runner):
    output, _ = run_hello_script(script_runner, name="John", school="TTÜ", mass=10 * 4, height=2)

    expected_output = "10.0, alakaaluline"
    assert expected_output in output


@pytest.mark.timeout(1.0)
@pytest.mark.script_launch_mode('subprocess')
@pytest.mark.incgroupdepend("syntax")
def test_bmi_normal(script_runner):
    output, _ = run_hello_script(script_runner, name="John", school="TTÜ", mass=20 * 9, height=3)

    expected_output = "20.0, normaalkaal"
    assert expected_output in output


@pytest.mark.timeout(1.0)
@pytest.mark.script_launch_mode('subprocess')
@pytest.mark.incgroupdepend("syntax")
def test_bmi_high(script_runner):
    output, _ = run_hello_script(script_runner, name="John", school="TTÜ", mass=30 * 16, height=4)

    expected_output = "30.0, ülekaaluline"
    assert expected_output in output
