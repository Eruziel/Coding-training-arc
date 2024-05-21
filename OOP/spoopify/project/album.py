from project.song import Song


class Album:
    def __init__(self, name, *song):
        self.name = name
        self.published = False
        self.songs = [*song]

    def add_song(self, song: Song):
        if song in self.songs:
            return f"Song is already in the album."

        if song.single:
            return f"Cannot add {song.name}. It's a single"

        if self.published:
            return "Cannot add songs. Album is published."

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name):

        try:
            removed = next(filter(lambda s: s.name == song_name, self.songs))
        except StopIteration:
            return "Song is not in the album."

        if not self.published:
            self.songs.remove(removed)
            return f"Removed song {removed.name} from album {self.name}."

        return "Cannot remove songs. Album is published."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."
        else:
            return f"Album {self.name} is already published."

    def details(self):
        result = ''
        all_songs = '\n'.join(f"== {s.get_info()}" for s in self.songs)
        result += f"Album {self.name}\n"
        result += all_songs

        return result
