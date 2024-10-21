# Function to perform basic arithmetic operations
def calculator():
    # Prompt user for input numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Prompt user for operation choice
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    operation = input("Enter the operation (1/2/3/4): ")

    # Perform the corresponding operation and display the result
    if operation == '1':
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")
    elif operation == '2':
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")
    elif operation == '3':
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation choice. Please select 1, 2, 3, or 4.")

# Call the calculator function
calculator()
