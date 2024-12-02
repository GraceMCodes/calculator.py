# Basic Calculator Program

# Function to perform the arithmetic operations
def calculate(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Invalid operator"

# Taking user input
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter an operator (+, -, *, /): ")

    # Perform calculation
    result = calculate(num1, num2, operator)

    # Display the result
    print(f"{num1} {operator} {num2} = {result}")

except ValueError:
    print("Invalid input! Please enter numeric values for the numbers.")
