# This is a simple calculator program that performs basic arithmetic operations.
# It takes two numbers and an operation as input from the user and prints the result.
# The program handles division by zero and invalid operations gracefully.
# It uses a function to encapsulate the calculation logic and a main function to handle user input and output.
# The calculator supports addition, subtraction, multiplication, and division.

# Function to perform the calculation
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        # Addition of a check to prevent division by zero
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operation."

# Main program
def main():
    # Ask the user for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Ask the user for the operation
    operation = input("Enter the operation (+, -, *, /): ")

    # Perform the calculation and print the result
    result = calculate(num1, num2, operation)
    print(f"{num1} {operation} {num2} = {result}")

# Run the main program
if __name__ == "__main__":
    main()

