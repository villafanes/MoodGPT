import requests
from lyricsgenius import Genius

def get_lyrics(artist, title):
    api_key = '4kcHpLNfV65xVafDjTSaTpw45hD-Gu7B2M7LocpNTyUlAkbxg5ooFWd16brLf0mP'
    genius = Genius(api_key)

    # remove extraneous outputs
    genius.remove_section_headers = True
    genius.verbose = False

    try:
        song = genius.search_song(title, artist)
        if song:
            # array of every line of lyrics
            lyrics = song.lyrics
            lyrics = lyrics.split('\n')

            # remove empty elements
            for i in lyrics:
                if i == '':
                    lyrics.remove(i)

            #remove non-lyrics
            lyrics.remove(lyrics[0])
            lyrics.remove(lyrics[-1])

            # record artist and song without typos
            artist_used = song.artist
            song_used = song.title
            
            return lyrics, artist_used, song_used
        else:
            return None, None, None

    except requests.exceptions.Timeout:
        print("Request to Genius_API timed out. Try running the program again.")
        return None, None, None

