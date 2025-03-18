# Function to add two numbers
def add_numbers(a, b):
    return a + b

# Main program
if __name__ == "__main__":
    # Take input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Call the function and store the result
    result = add_numbers(num1, num2)

    # Display the result
    print(f"The sum of {num1} and {num2} is: {result}")