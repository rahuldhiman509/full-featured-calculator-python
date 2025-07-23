import math

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    def sqrt(self, a):
        if a < 0:
            raise ValueError("Cannot take square root of negative number.")
        return math.sqrt(a)

    def power(self, a, b):
        return math.pow(a, b)

    def log10(self, a):
        if a <= 0:
            raise ValueError("Logarithm undefined for non-positive values.")
        return math.log10(a)

    def sin(self, a):
        return math.sin(math.radians(a))

    def cos(self, a):
        return math.cos(math.radians(a))

    def tan(self, a):
        return math.tan(math.radians(a))
