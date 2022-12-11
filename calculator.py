# Define functions for each operation
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # Check for division by zero
    if b == 0:
        print("Error: Cannot divide by zero")
        return

    return a / b

def exponentiate(a, b):
    return a ** b

def modulus(a, b):
    return a % b

# Get input from the user
num1 = int(input("Enter an num1: "))
operator = input("Enter operator: ")
num2 = int(input("Enter an num2: "))

# Perform the requested operation
if operator == "+":
    result = add(num1, num2)
elif operator == "-":
    result = subtract(num1, num2)
elif operator == "*":
    result = multiply(num1, num2)
elif operator == "/":
    result = divide(num1, num2)
elif operator == "**":
    result = exponentiate(num1, num2)
elif operator == "%":
    result = modulus(num1, num2)
else:
    print("Error: Invalid operator")

# Print the result
print(result)