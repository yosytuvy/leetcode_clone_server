import inspect
from typing import get_type_hints

from special_data_types import build_linked_list, linked_list_to_list
import ast


def validate_code_syntax(code):
    try:
        ast.parse(code)
    except SyntaxError as e:
        # raise HTTPException(status_code=400, detail="Invalid Python syntax")
        print(e)


def inspect_method_types(cls, method_name):
    """
    Inspect the types of a method's parameters and return type

    Args:
        cls: The class containing the method
        method_name: Name of the method to inspect

    Returns:
        Dictionary with parameter and return type information
    """
    # Get the method
    method = getattr(cls, method_name)

    # Get type hints
    type_hints = get_type_hints(method)

    # Get signature
    signature = inspect.signature(method)

    # Prepare results
    param_types = {}
    for name, param in signature.parameters.items():
        if name != "self":  # Exclude self
            param_types[name] = str(type_hints.get(name, "No type hint"))

    return {
        "parameter_types": param_types,
        "return_type": str(type_hints.get("return", "No return type hint")),
    }


def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False


def convert_input(input_type, input):
    return {
        "<class 'ListNode'>": build_linked_list,
        "typing.List[typing.Optional[special_data_types.ListNode]]": build_linked_list,
        "<class 'special_data_types.ListNode'>": build_linked_list,
    }[input_type](input)


def convert_output(output_type, output):
    return {
        "<class 'ListNode'>": linked_list_to_list,
        "<class 'special_data_types.ListNode'>": linked_list_to_list,
    }[output_type](output)
