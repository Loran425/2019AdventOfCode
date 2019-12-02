import unittest
from Day_1.main import basic_fuel_cost, complex_fuel_cost


class TestBasicFuelCost(unittest.TestCase):
    def test_small_1(self):
        self.assertEqual(basic_fuel_cost(12), 2)

    def test_small_2(self):
        self.assertEqual(basic_fuel_cost(14), 2)

    def test_med(self):
        self.assertEqual(basic_fuel_cost(1969), 654)

    def test_large(self):
        self.assertEqual(basic_fuel_cost(100756), 33583)


class TestComplexFuelCost(unittest.TestCase):
    def test_small(self):
        self.assertEqual(complex_fuel_cost(14), 2)

    def test_med(self):
        self.assertEqual(complex_fuel_cost(1969), 966)

    def test_large(self):
        self.assertEqual(complex_fuel_cost(100756), 50346)
