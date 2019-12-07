import unittest
from .main import OrbitalMap, Body


class MyTestCase(unittest.TestCase):
    def test_example(self):
        test_input = [
            "COM)B",
            "B)C",
            "C)D",
            "D)E",
            "E)F",
            "B)G",
            "G)H",
            "D)I",
            "E)J",
            "J)K",
            "K)L",
        ]
        system = OrbitalMap()
        for item in test_input:
            system.analyze(item)
        system.check()
        self.assertEqual(system.check_sum, 42)

    def test_pathing(self):
        test_input = [
            "COM)B",
            "B)C",
            "C)D",
            "D)E",
            "E)F",
            "B)G",
            "G)H",
            "D)I",
            "E)J",
            "J)K",
            "K)L",
        ]
        system = OrbitalMap()
        for item in test_input:
            system.analyze(item)
        system.check()
        self.assertEqual(
            system.path("D"),
            [system.bodies["COM"], system.bodies["B"], system.bodies["C"]],
        )


if __name__ == "__main__":
    unittest.main()
