class Boolean:
    def __init__(self, value):
        self.value = value

    def __and__(self, other):
        return Boolean(self.value and other.value)

    def __or__(self, other):
        return Boolean(self.value or other.value)


# Creating two boolean objects
b1 = Boolean(True)
b2 = Boolean(False)

# Logical AND
result = b1 and b2
print(result.value)

# Logical OR
result = b1 or b2
print(result.value)
