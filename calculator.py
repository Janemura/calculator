# Function to perform the mathematical operation
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
            return "Error! Division by zero."
    else:
        return "Invalid operator!"

# Main program
def main():
    # Ask the user for input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter the operation (+, -, *, /): ")

    # Call the calculate function and print the result
    result = calculate(num1, num2, operator)
    print(f"{num1} {operator} {num2} = {result}")

# Run the main program
if __name__ == "__main__":
    main()
