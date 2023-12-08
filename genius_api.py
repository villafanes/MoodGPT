import requests
from lyricsgenius import Genius

def get_lyrics(artist, title):
    api_key = '4kcHpLNfV65xVafDjTSaTpw45hD-Gu7B2M7LocpNTyUlAkbxg5ooFWd16brLf0mP'
    genius = Genius(api_key)
    try:
        song = genius.search_song(title, artist)
        if song:
            # array of every line of lyrics
            lyrics = song.lyrics
            # remove empty elements
            lyrics = lyrics.split('\n')

            for i in lyrics:
                if i == '':
                    lyrics.remove(i)

            # remove headings
            for i in lyrics:
                for j in i:
                    if j == '[':
                        lyrics.remove(i)

            return lyrics
        else:
            return None
    except requests.exceptions.Timeout:
        print("Request to Genius_API timed out. Try running the program again.")
        return None
