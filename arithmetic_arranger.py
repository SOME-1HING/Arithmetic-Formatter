LIMIT = 5
MAX_WIDTH = 4
SUPPORTED_OPERATORS = ["+", "-"]

ERROR = [
    "Error: Too many problems.",
    "Error: Numbers cannot be more than four digits.",
    "Error: Numbers must only contain digits.",
    "Error: Operator must be '+' or '-'.",
]


def calc(num1, num2, operator):  # Defining the calculation function
    num1 = int(num1)
    num2 = int(num2)
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2


# Defining the arithmetic formatter function
def arithmetic_arranger(problems, display=False):

    first_line = ""  # First Line
    second_line = ""  # Second Line
    third_line = ""  # Third Line
    fourth_line = ""  # Fourth Line
    arranged_problems = ""  # Output String
    gap = "    "  # Gap between each problem

    # If there are too many problems supplied to the function.
    if len(problems) > LIMIT:
        return ERROR[0]

    for problem in problems:
        first_number = str(problem.split()[0])
        operator = str(problem.split()[1])
        second_number = str(problem.split()[2])

        # Checks whether each number (operand) only contain digits or not.
        if first_number.isdigit() and second_number.isdigit():
            # Check if each operand has max 4 digits or not.
            if len(first_number) > MAX_WIDTH or len(second_number) > MAX_WIDTH:
                return ERROR[1]
        else:
            return ERROR[2]

        # Arithmetic Operation
        if operator in SUPPORTED_OPERATORS:
            answer = str(calc(first_number, second_number, operator))
        else:
            return ERROR[3]

        separation = max(len(first_number), len(second_number)) + 2

        if problem != problems[-1]:
            first_line = first_line + first_number.rjust(separation) + gap
            second_line = (
                second_line + operator + second_number.rjust(separation - 1) + gap
            )
            third_line = third_line + "-" * separation + gap
            fourth_line = fourth_line + answer.rjust(separation) + gap

        else:
            first_line = first_line + first_number.rjust(separation)
            second_line = second_line + operator + second_number.rjust(separation - 1)
            third_line = third_line + "-" * separation
            fourth_line = fourth_line + answer.rjust(separation)

    arranged_problems = first_line + "\n" + second_line + "\n" + third_line
    if display:
        arranged_problems += "\n" + fourth_line

    return arranged_problems
