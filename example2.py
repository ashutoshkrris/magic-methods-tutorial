class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle: width={self.width}, height={self.height}"


# Creating object from the Rectangle class
rect = Rectangle(4, 5)

# Accessing attributes
print(rect.width)

# Printing the rectangle object
print(rect)