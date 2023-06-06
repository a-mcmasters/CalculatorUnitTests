import math


class Calculator:
    def add(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be numbers")
        return a + b

    def subtract(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be numbers")
        return a - b

    def multiply(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be numbers")
        return a * b

    def divide(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be numbers")
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be numbers")
        return a ** b

    def sqrt(self, a):
        if not isinstance(a, (int, float)):
            raise TypeError("Argument must be a number")
        if a < 0:
            raise ValueError("Cannot take the square root of a negative number")
        return math.sqrt(a)

    def factorial(self, a):
        if not isinstance(a, (int, float)):
            raise TypeError("Argument must be a number")
        if not isinstance(a, int) or a < 0:
            raise ValueError("Factorial is only defined for non-negative integers")
        return math.factorial(a)

    def sin(self, a):
        if not isinstance(a, (int, float)):
            raise TypeError("Argument must be a number")
        return math.sin(a)

    def cos(self, a):
        if not isinstance(a, (int, float)):
            raise TypeError("Argument must be a number")
        return math.cos(a)

    def tan(self, a):
        if not isinstance(a, (int, float)):
            raise TypeError("Argument must be a number")
        return math.tan(a)

    def asin(self, a):
        if not isinstance(a, (int, float)):
            raise TypeError("Argument must be a number")
        if not -1 <= a <= 1:
            raise ValueError("Invalid input to asin: input must be in the range [-1, 1]")
        return math.asin(a)

    def acos(self, a):
        if not isinstance(a, (int, float)):
            raise TypeError("Argument must be a number")
        if not -1 <= a <= 1:
            raise ValueError("Invalid input to acos: input must be in the range [-1, 1]")
        return math.acos(a)

    def atan(self, a):
        if not isinstance(a, (int, float)):
            raise TypeError("Argument must be a number")
        return math.atan(a)

    def log(self, a):
        if not isinstance(a, (int, float)):
            raise TypeError("Argument must be a number")
        if a <= 0:
            raise ValueError("Cannot take the logarithm of a non-positive number")
        return math.log(a)

    def log10(self, a):
        if not isinstance(a, (int, float)):
            raise TypeError("Argument must be a number")
        if a <= 0:
            raise ValueError("Cannot take the logarithm of a non-positive number")
        return math.log10(a)

    def exp(self, a):
        if not isinstance(a, (int, float)):
            raise TypeError("Argument must be a number")
        return math.exp(a)
