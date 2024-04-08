from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multipy(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multipy,
    "/": divide,
}


def calculator():
    print(logo)
    num1 = float(input("What's your first number? "))
    for key in operations:
        print(key)

    game = True

    while game:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's your next number? "))
        calculation_symbol = operations[operation_symbol]
        answer = calculation_symbol(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' if you want to continue calculation with {answer}, or type 'n' to start a new calculation.: ") == "y":
            num1 = answer
        else:
            game = False
            calculator()


calculator()
