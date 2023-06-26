class Playlist:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Playlist Name: {self.name}"

    def __repr__(self):
        return f"Playlist(name={self.name})"


playlist = Playlist("My Favorite Songs")
print(repr(playlist))
