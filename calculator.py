
from agents import function_tool


@function_tool
def add_numbers(a: float, b: float) -> float:
    """Use only when the user explicitly asks to add two numbers."""

    print(f"[TOOL CALLED] Addition: {a} + {b}")

    return a + b


@function_tool
def multiply_number(a: float, b: float) -> float:
    """Use only when the user explicitly asks to add two numbers."""

    print(f"[TOOL CALLED] Multiplication: {a} * {b}")

    return a * b
