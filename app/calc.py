
class InvalidPermissions(Exception):
    """Custom exception for invalid permissions."""
    pass


class Calculator:
    """A simple calculator class with basic arithmetic operations."""

    def add(self, x, y):
        """Return the sum of x and y."""
        self.check_types(x, y)
        return x + y

    def subtract(self, x, y):
        """Return the difference of x and y."""
        self.check_types(x, y)
        return x - y

    def multiply(self, x, y):
        """Return the product of x and y."""
        self.check_types(x, y)
        return x * y

    def divide(self, x, y):
        """Return the division of x by y. Raises ZeroDivisionError if y is 0."""
        self.check_types(x, y)
        if y == 0:
            raise ZeroDivisionError("Division by zero is not possible")
        return x / y

    def power(self, x, y):
        """Return x raised to the power of y."""
        self.check_types(x, y)
        return x ** y

    def check_types(self, x, y):
        """Validate that x and y are numbers (int or float)."""
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Parameters must be numbers")


if __name__ == "__main__":  # pragma: no cover
    calc = Calculator()
    result = calc.add(2, 2)
    print(result)
