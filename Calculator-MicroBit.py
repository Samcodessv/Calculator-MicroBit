import math

# Initialize the operations list with the new square root operation
operations = ["+", "-", "*", "/", "√"]  # Updated to include square root as the 5th operation

# Calculate function

def calculate_and_show(operation_index, num1, num2=0):
    if operation_index == 0:
        result = num1 + num2
    elif operation_index == 1:
        result = num1 - num2
    elif operation_index == 2:
        result = num1 * num2
    elif operation_index == 3:
        result = num1 / num2
    elif operation_index == 4:
        result = math.sqrt(num1)  # New case for square root
    else:
        result = "Invalid operation"
    # Code to display the result not shown here
    return result

# Modifying modulo operation from % 4 to % 5
operation_index = operation_index % 5  # Updated to cycle through 5 operations
