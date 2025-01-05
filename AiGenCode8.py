class MusicPlayer:
    def __init__(self):
        self.music_files = {}

    def add_music_file(self, artist, song, genre):
        self.music_files[artist] = {
            'song': song,
            'genre': genre
        }

    def play_music_file(self, artist=None, song=None):
        if artist and song:
            print(f"Playing: {artist} - {song}")
        else:
            for artist in self.music_files:
                print(f"\n{artist}:")
                for music_file in self.music_files[artist]:
                    print(f"- {music_file}: {self.music_files[artist][music_file]}")

    def update_music_file(self, artist, song, genre):
        if artist and song:
            self.music_files[artist]['song'] = song
            self.music_files[artist]['genre'] = genre

class MusicDatabase:
    def __init__(self):
        self.music_players = {}

    def add_music_player(self, name):
        self.music_players[name] = MusicPlayer()

    def view_all_music_players(self):
        for player in self.music_players.values():
            print(f"{player.__class__.__name__}:")
            player.play_music_file()
            print("\n")

# Usage
database = MusicDatabase()
database.add_music_player('Player 1')
database.add_music_player('Player 2')

artist1 = 'The Beatles'
song1 = 'Yesterday'

database.music_players['Player 1'].add_music_file(artist1, song1, 'Rock')
database.music_players['Player 2'].add_music_file('Michael Jackson', 'Billie Jean', 'Pop')

database.view_all_music_players()

# Update a music file
database.music_players['Player 1'].update_music_file(artist1, 'Hey Jude', 'Rock')
