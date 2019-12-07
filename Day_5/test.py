import unittest
from .main import IntCodeMachine


class IntCodeTest(unittest.TestCase):
    def test_example(self):
        test_input = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        computer = IntCodeMachine(test_input)
        processed = computer.execute()
        expected = [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
        self.assertEqual(processed, expected)

    def test_short1(self):
        test_input = [1, 0, 0, 0, 99]
        computer = IntCodeMachine(test_input)
        processed = computer.execute()
        expected = [2, 0, 0, 0, 99]
        self.assertEqual(processed, expected)

    def test_short2(self):
        test_input = [2, 3, 0, 3, 99]
        computer = IntCodeMachine(test_input)
        processed = computer.execute()
        expected = [2, 3, 0, 6, 99]
        self.assertEqual(processed, expected)

    def test_short3(self):
        test_input = [2, 4, 4, 5, 99, 0]
        computer = IntCodeMachine(test_input)
        processed = computer.execute()
        expected = [2, 4, 4, 5, 99, 9801]
        self.assertEqual(processed, expected)

    def test_short4(self):
        test_input = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        computer = IntCodeMachine(test_input)
        processed = computer.execute()
        expected = [30, 1, 1, 4, 2, 5, 6, 0, 99]
        self.assertEqual(processed, expected)

    def test_error(self):
        test_input = [-1, 0, 0, 0, 99]
        computer = IntCodeMachine(test_input)
        self.assertRaises(ValueError, computer.execute)


if __name__ == "__main__":
    unittest.main()
