import unittest
import pytest
from app import util

@pytest.mark.unit
class TestUtil(unittest.TestCase):
    def test_convert_to_number_ok(self):
        cases = [
            ("4", 4),
            ("0", 0),
            ("-0", 0),
            ("-1", -1),
            ("4.0", 4.0),
            ("0.0", 0.0),
            ("-0.0", 0.0),
            ("-1.0", -1.0),
        ]
        for s, expected in cases:
            with self.subTest(s=s):
                if isinstance(expected, float):
                    self.assertAlmostEqual(expected, util.convert_to_number(s), delta=1e-7)
                else:
                    self.assertEqual(expected, util.convert_to_number(s))

    def test_convert_to_number_invalid_type(self):
        bad = ["", "3.h", "s", None, object()]
        for s in bad:
            with self.subTest(s=s):
                self.assertRaises(TypeError, util.convert_to_number, s)

if __name__ == "__main__":  # pragma: no cover
    unittest.main()
