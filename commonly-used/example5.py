class Playlist:
    def __init__(self, name, songs=[]):
        self.name = name
        self.songs = songs

    def __str__(self):
        return f"Playlist Name: {self.name}"

    def __repr__(self):
        return f"Playlist(name={self.name})"

    def __len__(self):
        return len(self.songs)

    def __getitem__(self, index):
        return self.songs[index]


playlist = Playlist("My Favorite Songs", ["Song1", "Song2", "Song3"])
print(playlist[1])
print(playlist[4])
