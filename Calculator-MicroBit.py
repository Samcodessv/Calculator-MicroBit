from microbit import *

class Calculator:
    def __init__(self):
        self.display = display

    def show_result(self, result):
        self.display.scroll(str(result))

    def get_input(self):
        num1 = self.prompt_num("Enter first number:")
        operation = self.prompt_operation()
        num2 = self.prompt_num("Enter second number:")
        return num1, operation, num2

    def prompt_num(self, message):
        self.display.scroll(message)
        num = ''
        while True:
            if button_a.is_pressed():
                if num:
                    return int(num)
            if button_b.is_pressed():
                num += '1'
                self.display.show(num)
            sleep(100)

    def prompt_operation(self):
        operation = ''
        self.display.scroll("Select: A for +, B for -")
        while True:
            if button_a.is_pressed():
                return '+'
            if button_b.is_pressed():
                return '-'
            sleep(100)

    def calculate(self, num1, operation, num2):
        if operation == '+':
            return num1 + num2
        elif operation == '-':
            return num1 - num2

    def run(self):
        while True:
            num1, operation, num2 = self.get_input()
            result = self.calculate(num1, operation, num2)
            self.show_result(result)

if __name__ == '__main__':
    calc = Calculator()
    calc.run()