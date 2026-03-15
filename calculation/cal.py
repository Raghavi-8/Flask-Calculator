def calculate(num1, num2, operation):

    if operation == 1:
        return num1 + num2

    elif operation == 2:
        return num1 - num2

    elif operation == 3:
        return num1 * num2

    elif operation == 4:
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2

    elif operation == 5:
        return num1 % num2

    elif operation == 6:
        return num1 ** num2

    else:
        return "Invalid operation"