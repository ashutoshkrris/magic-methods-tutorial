class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print("Opening the file...")
        self.file = open(self.filename, "w")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        print("Closed the file...")


# Using the context manager
with FileHandler("example.txt") as file:
    print("Writing to the file...")
    file.write("Earthly is great!")
