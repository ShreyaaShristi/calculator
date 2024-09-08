def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def main():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # Get user input
    choice = input("Enter choice (1/2/3/4): ")

    # Check if the choice is valid
    if choice not in ['1', '2', '3', '4']:
        print("Invalid input! Please enter a number between 1 and 4.")
        return

    try:
        # Get the numbers from the user
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    # Perform the chosen operation
    if choice == '1':
        result = add(num1, num2)
        print(f"The result of {num1} + {num2} is {result}.")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"The result of {num1} - {num2} is {result}.")
    elif choice == '3':
        result = multiply(num1, num2)
        print(f"The result of {num1} * {num2} is {result}.")
    elif choice == '4':
        result = divide(num1, num2)
        print(f"The result of {num1} / {num2} is {result}.")

if __name__ == "__main__":
    main()
