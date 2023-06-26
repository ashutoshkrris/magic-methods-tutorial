import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __lt__(self, other):
        return self.distance_from_origin() < other.distance_from_origin()

    def __gt__(self, other):
        return self.distance_from_origin() > other.distance_from_origin()

    def __eq__(self, other):
        return self.distance_from_origin() == other.distance_from_origin()

    def __ne__(self, other):
        return self.distance_from_origin() != other.distance_from_origin()


# Creating two point objects
p1 = Point(2, 3)
p2 = Point(4, 5)

# Less than
result = p1 < p2
print(result)

# Greater than
result = p1 > p2
print(result)

# Equal to
result = p1 == p2
print(result)

# Not equal to
result = p1 != p2
print(result)
