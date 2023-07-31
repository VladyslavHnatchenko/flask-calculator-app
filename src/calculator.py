# Simple Strategy design pattern

class Calculator:
    def calculate(self, operand1, operand2):
        raise NotImplementedError("Subclasses must implement the 'calculate' method.")


class AddOperator(Calculator):
    def calculate(self, operand1, operand2):
        return operand1 + operand2


class SubtractOperator(Calculator):
    def calculate(self, operand1, operand2):
        return operand1 - operand2


class DivideOperator(Calculator):
    def calculate(self, operand1, operand2):
        if operand2 == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return operand1 / operand2


class MultiplyOperator(Calculator):
    def calculate(self, operand1, operand2):
        return operand1 * operand2
