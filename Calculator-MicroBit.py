"""

Initial variables

"""
"""

0: Operation selection, 1: First number, 2: Second number, 3: Result

"""
"""

0: +, 1: -, 2: *, 3: /

"""
# Function that resets the system and returns to the beginning
def reset_calculator():
    global status, operation_index, num1, num2
    status = 0
    operation_index = 0
    num1 = 0
    num2 = 0
    update_display()

# When Button A is pressed (Navigate between options)
def on_button_pressed_a():
    global operation_index, num1, num2
    if status == 0:
        # Change operations (0 to 3, when 4 returns to 0)
        operation_index = (operation_index + 1) % 4
    elif status == 1:
        # Increment first number (0-9 range)
        num1 = (num1 + 1) % 10
    elif status == 2:
        # Increment second number (0-9 range)
        num2 = (num2 + 1) % 10
    elif status == 3:
        # When on result screen and A is pressed, go back to start
        reset_calculator()
        return
    update_display()

input.on_button_pressed(Button.A, on_button_pressed_a)

# Function to display current status on screen
def update_display():
    if status == 0:
        basic.show_string("" + (operations[operation_index]))
    elif status == 1:
        basic.show_number(num1)
    elif status == 2:
        basic.show_number(num2)

# When Button B is pressed (Confirm / Move forward)
def on_button_pressed_b():
    global status
    if status == 0:
        status = 1
        # Move to first number selection
        update_display()
    elif status == 1:
        status = 2
        # Move to second number selection
        update_display()
    elif status == 2:
        status = 3
        # Calculate and show result
        calculate_and_show()
    elif status == 3:
        # When on result screen and B is pressed, go back to start
        reset_calculator()

input.on_button_pressed(Button.B, on_button_pressed_b)

# Function that performs mathematical operation and displays on LED
def calculate_and_show():
    global result
    basic.clear_screen()
    basic.pause(200)
    # Brief pause to give the impression of calculating
    if operation_index == 0:
        result = num1 + num2
    elif operation_index == 1:
        result = num1 - num2
    elif operation_index == 2:
        result = num1 * num2
    elif operation_index == 3:
        # Prevent division by zero error
        if num2 == 0:
            basic.show_string("ERROR")
            return
        else:
            result = num1 / num2
    basic.show_number(result)

result = 0
num2 = 0
num1 = 0
operation_index = 0
status = 0
operations: List[str] = []
operations = ["+", "-", "*", "/"]

# Show initial screen when

