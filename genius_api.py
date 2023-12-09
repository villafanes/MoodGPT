import requests
from lyricsgenius import Genius

def get_lyrics(artist, title):
    api_key = '4kcHpLNfV65xVafDjTSaTpw45hD-Gu7B2M7LocpNTyUlAkbxg5ooFWd16brLf0mP'
    genius = Genius(api_key)

    #remove extraneous outputs
    genius.remove_section_headers = True
    genius.verbose = False
    
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

            #record artist and title without typos
            artist_used = song.artist
            song_used = song.title

            return lyrics=
        else:
            print("Song cannot be found.")
            return None
    except requests.exceptions.Timeout:
        print("Request to Genius_API timed out. Try running the program again.")
        return None
