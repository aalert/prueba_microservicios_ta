import unittest

from helpers import parse_absolutime_time


class TestParseAbsolutimeTime(unittest.TestCase):

    def test_parse_absolutime_time_no_units(self):
        with self.assertRaises(ValueError):
            parse_absolutime_time("0")

    def test_parse_absolutime_time_seconds(self):
        with self.assertRaises(ValueError):
            parse_absolutime_time("30s")

    def test_parse_absolutime_time_multiple_units_seconds(self):
        with self.assertRaises(ValueError):
            parse_absolutime_time("15m, 3h, 2d, 30s")

    def test_parse_absolutime_time_invalid_units(self):
        with self.assertRaises(ValueError):
            parse_absolutime_time("15m, 3h, 2d, 1h, 30s")

    def test_parse_absolutime_time_invalid_format_no_units(self):
        with self.assertRaises(ValueError):
            parse_absolutime_time("abc")

    def test_parse_absolutime_time_invalid_format_missing_comma(self):
        result = parse_absolutime_time("15m 3h 2d")
        self.assertEqual(result, ("15m", "3h", "2d"))

    def test_parse_absolutime_time_invalid_format_missing_space(self):
        result = parse_absolutime_time("15m,3h,2d")
        self.assertEqual(result, ("15m", "3h", "2d"))

    def test_parse_absolutime_time_invalid_format_missing_value(self):
        with self.assertRaises(ValueError):
            parse_absolutime_time("m, 3h, 2d")

    def test_parse_absolutime_time_invalid_format_invalid_unit(self):
        with self.assertRaises(ValueError):
            parse_absolutime_time("15x, 3h, 2d")

if __name__ == '__main__':
    unittest.main()