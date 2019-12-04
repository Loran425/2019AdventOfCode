import unittest
from .main import double_digit_check, ascending_check, password_check


class ComponentCases(unittest.TestCase):
    def test_double_digit_pass(self):
        password = [1, 1, 2, 3, 4, 5]
        valid = double_digit_check(password)
        self.assertTrue(valid)

    def test_double_digit_fail(self):
        password = [1, 2, 3, 4, 5, 6]
        valid = double_digit_check(password)
        self.assertFalse(valid)

    def test_ascending_pass(self):
        password = [1, 2, 3, 4, 5, 6]
        valid = ascending_check(password)
        self.assertTrue(valid)

    def test_ascending_fail(self):
        password = [1, 5, 3, 4, 5, 6]
        valid = ascending_check(password)
        self.assertFalse(valid)


class PasswordCase(unittest.TestCase):
    def test_double_descending(self):
        password = "122156"
        valid = password_check(password)
        self.assertFalse(valid)

    def test_single_ascending(self):
        password = "123456"
        valid = password_check(password)
        self.assertFalse(valid)

    def test_success(self):
        password = "113456"
        valid = password_check(password)
        self.assertTrue(valid)

    def test_example_1(self):
        password = "111111"
        valid = password_check(password)
        self.assertTrue(valid)

    def test_example_2(self):
        password = "223450"
        valid = password_check(password)
        self.assertFalse(valid)

    def test_example_3(self):
        password = "123789"
        valid = password_check(password)
        self.assertFalse(valid)


class PasswordStrictCase(unittest.TestCase):
    def test_example_1(self):
        password = "112233"
        valid = password_check(password, strict=True)
        self.assertTrue(valid)

    def test_example_2(self):
        password = "123444"
        valid = password_check(password, strict=True)
        self.assertFalse(valid)

    def test_example_3(self):
        password = "111122"
        valid = password_check(password, strict=True)
        self.assertTrue(valid)


if __name__ == "__main__":
    unittest.main()
