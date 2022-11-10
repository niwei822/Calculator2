"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, cube, divide, mod, multiply, power, square,
                        subtract)

# Replace this with your code


def calculator():
    while True:
        expression = input("Enter your expression: ")
        expression = expression.split(" ")
        if "q" in expression:
            return
        # num1 = float(expression[1])
        # num2 = float(expression[2])
        if len(expression) == 3:
            num1 = float(expression[1])
            num2 = float(expression[2])
            
            if expression[0] == "+":
                result = add(num1, num2)
            elif expression[0] == "-":
                result = subtract(num1, num2)
            elif expression[0] == "*":
                result = multiply(num1, num2)
            elif expression[0] == "/":
                result = divide(num1, num2)
            elif expression[0] == "mod":
                result = mod(num1, num2)
            elif expression[0] == "pow":
                result = pow(num1, num2)
            else:
                print("Invalid input 2")
                continue
        elif len(expression) == 2:
            num1 = float(expression[1])
            if expression[0] == "square":
                result = square(num1)
            elif expression[0] == "cube":
                result = cube(num1)
            else:
                print("Invalid input!")
                continue
        else:
            print("Please enter valid input!")
            continue
        print(result)
    
calculator()
