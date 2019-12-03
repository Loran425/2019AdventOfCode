#!/usr/bin/env python
# Solution to the AOC2019 Challenge 5/6
# https://adventofcode.com/2019/day/3

from dataclasses import dataclass, field


@dataclass
class Point:
    x: int
    y: int

    def manhattan_dist(self):
        return abs(self.x) + abs(self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


@dataclass
class Segment:
    p1: Point
    p2: Point
    _p2: Point = field(init=False, repr=False)
    orientation: str = field(init=False, repr=False)
    length: int = field(init=False, repr=False)

    def __post_init__(self):
        self.orientation = self.__orientation()
        self.length = self.__length()

    def __contains__(self, item):
        if self.orientation == "slope":
            raise NotImplementedError("Sloped lines membership not implemented")

        if isinstance(item, Point):
            return item.y in self.y_limits() and item.x in self.x_limits()
        else:
            raise TypeError("Only Valid for Points at this time")

    def __orientation(self):
        if self.p1.y == self.p2.y:
            return "H"
        elif self.p1.x == self._p2.x:
            return "V"
        else:
            return "slope"

    def __length(self):
        # All vertical/horizontal lines so only one of these two will be non zero
        dx = abs(self.p1.x - self._p2.x)
        dy = abs(self.p1.y - self._p2.y)
        return dx + dy

    @property
    def p2(self):
        return self._p2

    @p2.setter
    def p2(self, point):
        self._p2 = point
        if self.p1 and self._p2:
            self.orientation = self.__orientation()
            self.length = self.__length()

    def x_limits(self):
        return range(min(self.p1.x, self._p2.x), max(self.p1.x, self._p2.x) + 1)

    def y_limits(self):
        return range(min(self.p1.y, self._p2.y), max(self.p1.y, self._p2.y) + 1)


NULL_POINT = Point(0, 0)


class Map:
    def __init__(self, wire_1, wire_2):
        self.wire_1 = self.parse_points(wire_1)
        self.wire_2 = self.parse_points(wire_2)
        self.wire_1_segments = [Segment(*x) for x in zip(self.wire_1, self.wire_1[1:])]
        self.wire_2_segments = [Segment(*x) for x in zip(self.wire_2, self.wire_2[1:])]
        self.intersections = list()
        self.process()

    @staticmethod
    def parse_points(data):
        points = []
        x = y = 0
        points.append(Point(x, y))
        for instruction in data:
            direction = instruction[0]
            length = int(instruction[1:])
            if direction == "U":
                y += length
            elif direction == "D":
                y -= length
            elif direction == "L":
                x -= length
            elif direction == "R":
                x += length
            else:
                raise ValueError(f"Invalid direction: {direction}")
            points.append(Point(x, y))
        return points

    def process(self):
        changes = []
        for seg_1 in self.wire_1_segments:
            for seg_2 in self.wire_2_segments:
                node = self.intersection_check(seg_1, seg_2)
                if node != NULL_POINT:
                    self.intersections.append(node)
                    changes.append((seg_1, seg_2, node))

    @staticmethod
    def intersection_check(seg_1: Segment, seg_2: Segment) -> Point:
        if seg_1.orientation == "H":
            if seg_2.orientation == "H":
                return NULL_POINT
            else:
                if seg_2.p1.x in seg_1.x_limits() and seg_1.p1.y in seg_2.y_limits():
                    return Point(seg_2.p2.x, seg_1.p1.y)
                else:
                    return NULL_POINT
        else:
            if seg_2.orientation == "V":
                return NULL_POINT
            else:
                if seg_2.p1.y in seg_1.y_limits() and seg_1.p1.x in seg_2.x_limits():
                    return Point(seg_1.p1.x, seg_2.p2.y)
                else:
                    return NULL_POINT

    def closest(self):
        nearest_point = sorted(self.intersections, key=lambda x: x.manhattan_dist())[0]
        return nearest_point.manhattan_dist()

    def fastest(self):
        distances = dict()
        for point in self.intersections:
            distances[repr(point)] = 0

            for segment in self.wire_1_segments:
                if point in segment:
                    distances[repr(point)] += Segment(segment.p1, point).length
                    break
                else:
                    distances[repr(point)] += segment.length

            for segment in self.wire_2_segments:
                if point in segment:
                    distances[repr(point)] += Segment(segment.p1, point).length
                    break
                else:
                    distances[repr(point)] += segment.length

        return min(distances.values())


if __name__ == "__main__":
    f = open("input.txt")
    wire_1 = f.readline().strip().split(",")
    wire_2 = f.readline().strip().split(",")
    m = Map(wire_1, wire_2)
    print(f'Manhattan Distance to closest intersection: {m.closest()}')
    print(f'Sum of time to the fastest intersection: {m.fastest()}')
