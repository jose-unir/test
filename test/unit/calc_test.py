import pytest
import unittest
from app.calc import Calculator

@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_ok(self):
        cases = [
            (2, 2, 4),
            (2, -2, 0),
            (-2, 2, 0),
            (1, 0, 1),
            (0, 0, 0),
            (-1, -1, -2),
            (1_000_000, 2_000_000, 3_000_000),
        ]
        for a, b, expected in cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.add(a, b), expected)

    def test_add_type_error(self):
        bad = [("2", 2), (2, "2"), ("2", "2"), (None, 2), (2, None), (object(), 2), (2, object())]
        for a, b in bad:
            with self.subTest(a=a, b=b):
                self.assertRaises(TypeError, self.calc.add, a, b)

    def test_substract_ok(self):
        cases = [(10, 6, 4), (256, 258, -2), (-1, 0, -1), (0, 0, 0), (5, 5, 0)]
        for a, b, expected in cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.substract(a, b), expected)

    def test_substract_type_error(self):
        for a, b in [("0", 0), (0, "0")]:
            with self.subTest(a=a, b=b):
                self.assertRaises(TypeError, self.calc.substract, a, b)

    def test_multiply_ok(self):
        cases = [(2, 2, 4), (1, 0, 0), (-1, 0, 0), (-1, 2, -2), (3, -3, -9), (-2, -3, 6)]
        for a, b, expected in cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.multiply(a, b), expected)

    def test_multiply_type_error(self):
        for a, b in [("0", 0), (0, "0")]:
            with self.subTest(a=a, b=b):
                self.assertRaises(TypeError, self.calc.multiply, a, b)

    def test_divide_ok(self):
        cases = [(2, 2, 1), (3, 2, 1.5), (-6, 3, -2), (5.0, 2.0, 2.5)]
        for a, b, expected in cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.divide(a, b), expected)

    def test_divide_type_error(self):
        for a, b in [("2", 2), (2, "2"), ("2", "2")]:
            with self.subTest(a=a, b=b):
                self.assertRaises(TypeError, self.calc.divide, a, b)

    def test_divide_by_zero_raises(self):
        self.assertRaises(ZeroDivisionError, self.calc.divide, 10, 0)

    def test_power_ok(self):
        cases = [(2, 2, 4), (1, 0, 1), (-1, 0, 1), (-3, 3, -27), (0, 3, 0)]
        for base, exp, expected in cases:
            with self.subTest(base=base, exp=exp):
                self.assertEqual(self.calc.power(base, exp), expected)

    def test_power_type_error(self):
        for base, exp in [("0", 0), (0, "0"), (None, 1)]:
            with self.subTest(base=base, exp=exp):
                self.assertRaises(TypeError, self.calc.power, base, exp)

if __name__ == "__main__":  # pragma: no cover
    unittest.main()
