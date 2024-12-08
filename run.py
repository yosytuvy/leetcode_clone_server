import json
from helpers import convert_input, convert_output, inspect_method_types
from run_code import run_code
from special_data_types import build_linked_list, linked_list_to_list

SPECIAL_TYPES = [
    "<class 'ListNode'>",
    "typing.List[typing.Optional[special_data_types.ListNode]]",
    "<class 'special_data_types.ListNode'>",
    "'typing.Optional[special_data_types.ListNode]'"
]


def run_problem_code(problem):
    problem_number = problem["problemNumber"]
    with open(f"./solutions/{problem_number}.py", "r") as file:
        solution_code = file.read()
    try:
        restricted_globals = run_code(solution_code)
    except Exception as e:
        print(e)
        return

    Solution = restricted_globals["Solution"]
    method = problem["functionName"]

    method_types = inspect_method_types(Solution, method)
    test_cases = problem["testCases"]

    results = []
    for test_case in test_cases:
        inputs = [val for val in test_case["input"].values()]

        inputs_tuple = tuple()
        for i, param_type in enumerate(method_types["parameter_types"].values()):
            if 'ListNode' in param_type:
                inputs[i] = build_linked_list(inputs[i])
            inputs_tuple += (inputs[i],)

        expected_output = test_case["output"]

        try:
            solution = Solution()
            output = getattr(solution, method)(*inputs_tuple)

            if  'ListNode' in method_types["return_type"]:
                output = linked_list_to_list(output)

            results.append(
                {
                    "input": inputs_tuple,
                    "expected": expected_output,
                    "output": output,
                    "passed": output == expected_output,
                }
            )
            if not output == expected_output:
                print()

        except Exception as e:
            print(e)
            results.append(
                {
                    "input": test_case["input"],
                    "error": str(e),
                    "passed": False,
                }
            )
    return results


if __name__ == "__main__":
    data = []
    with open("data.json", "r") as file:
        data = json.load(file)

    data = data[19:]
    results = []
    for problem in data:
        results.append(run_problem_code(problem))

    print()
