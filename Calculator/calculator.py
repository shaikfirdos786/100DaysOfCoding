from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    print(logo)

    num1 = float(input("What's the first number? "))

    for operation in operations:
        print(operation)
    continue_ = True
    while continue_:
        operation_symbol = input(
            "Pick an operation from the above line to perform the calculation. "
        )

        num2 = float(input("What's the next number? "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} ={answer}")

        should_continue = input(
            f"Type 'y' to continue calculation with {answer}, or type 'n' to start new calculation, or type 'stop' to stop calculation. "
        )
        if should_continue.lower() == 'y':
            num1 = answer
        elif should_continue.lower() == 'n':
            continue_ = False
            calculator()
        else:
            continue_ = False


calculator()
