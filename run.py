import os
import sys
import yaml

import importlib.util

from io import StringIO
from contextlib import redirect_stdout


def load_yaml_test_cases(yaml_file):
    with open(yaml_file, "r") as file:
        return yaml.safe_load(file)


def run_with_input_and_capture_output(solve_function, input_data):
    input_mock = StringIO(input_data)
    output_capture = StringIO()

    with redirect_stdout(output_capture):
        solve_function(input_mock)

    return output_capture.getvalue().strip()


def get_test_cases(competition=None, task=None):
    for root, _, files in os.walk("."):
        for file in files:
            if not file.endswith(".yaml"):
                continue

            yaml_path = os.path.join(root, file)
            task_file = yaml_path.replace(".yaml", ".py")

            if competition and competition not in yaml_path:
                continue
            if task and task not in yaml_path:
                continue

            if os.path.exists(task_file):
                yield yaml_path, task_file


def run_tests(competition=None, task=None):
    for yaml_path, task_file in get_test_cases(competition, task):
        print(f"Running tests for {task_file}")

        spec = importlib.util.spec_from_file_location("module.name", task_file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        solve_function = module.solve

        test_cases = load_yaml_test_cases(yaml_path)

        for i, test_case in enumerate(test_cases):
            result = run_with_input_and_capture_output(
                solve_function, test_case["input"].strip()
            )
            if result == test_case["output"].strip():
                print(f"  Test case {i+1}: PASSED")
            else:
                print(f"  Test case {i+1}: FAILED")
                print(f"    Expected: {test_case['output']}")
                print(f"    Got:      {result}")


if __name__ == "__main__":
    competition = sys.argv[1] if len(sys.argv) > 1 else None
    task = sys.argv[2] if len(sys.argv) > 2 else None
    run_tests(competition, task)
