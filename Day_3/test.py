import unittest
from .main import Map, Segment, Point


class DistTest(unittest.TestCase):
    def test_1(self):
        wire_1 = ["R8", "U5", "L5", "D3"]
        wire_2 = ["U7", "R6", "D4", "L4"]
        dist = 6
        m = Map(wire_1, wire_2)
        self.assertEqual(m.closest(), dist)

    def test_2(self):
        wire_1 = ["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"]
        wire_2 = ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"]
        dist = 159
        m = Map(wire_1, wire_2)
        self.assertEqual(m.closest(), dist)

    def test_3(self):
        wire_1 = ["R98", "U47", "R26", "D63", "R33", "U87", "L62", "D20", "R33", "U53", "R51"]
        wire_2 = ["U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"]
        dist = 135
        m = Map(wire_1, wire_2)
        self.assertEqual(m.closest(), dist)


class SpeedTest(unittest.TestCase):
    def test_1(self):
        wire_1 = ["R8", "U5", "L5", "D3"]
        wire_2 = ["U7", "R6", "D4", "L4"]
        time = 30
        m = Map(wire_1, wire_2)
        self.assertEqual(time, m.fastest())

    def test_2(self):
        wire_1 = ["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"]
        wire_2 = ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"]
        time = 610
        m = Map(wire_1, wire_2)
        self.assertEqual(time, m.fastest())

    def test_3(self):
        wire_1 = ["R98", "U47", "R26", "D63", "R33", "U87", "L62", "D20", "R33", "U53", "R51"]
        wire_2 = ["U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"]
        time = 410
        m = Map(wire_1, wire_2)
        print(m.intersections)
        self.assertEqual(time, m.fastest())


class SegmentTesting(unittest.TestCase):
    def test_contains(self):
        p1 = Point(0, 0)
        p2 = Point(0, 5)
        segment = Segment(p1, p2)
        p3 = Point(0, 3)
        self.assertTrue(p3 in segment)

    def test_x_limits(self):
        p1 = Point(0, 0)
        p2 = Point(0, 5)
        segment = Segment(p1, p2)
        self.assertEqual(range(0, 1), segment.x_limits())

    def test_y_limits(self):
        p1 = Point(0, 0)
        p2 = Point(0, 5)
        segment = Segment(p1, p2)
        self.assertEqual(range(0, 6), segment.y_limits())


if __name__ == "__main__":
    unittest.main()
