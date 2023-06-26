class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Vector(self.x / scalar, self.y / scalar)


# Creating two vector objects
v1 = Vector(2, 3)
v2 = Vector(4, 5)

# Addition
result = v1 + v2
print(result.x, result.y)

# Subtraction
result = v2 - v1
print(result.x, result.y)

# Multiplication
result = v1 * 2
print(result.x, result.y)

# Division
result = v2 / 2
print(result.x, result.y)
