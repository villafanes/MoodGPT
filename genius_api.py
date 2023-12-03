from lyricsgenius import Genius

api_key =  '4kcHpLNfV65xVafDjTSaTpw45hD-Gu7B2M7LocpNTyUlAkbxg5ooFWd16brLf0mP'
genius = Genius(api_key)
artist = input('Enter artist name: ')
title = input('Enter song title: ')
song = genius.search_song(title,artist)

#array of every line of lyrics
lyrics = song.lyrics
lyrics = lyrics.split('\n')

#remove empty elements
for i in lyrics:
    if i == '':
        lyrics.remove(i)

#remove headings
for i in lyrics:
    for j in i:
        if j == '[':
            lyrics.remove(i)
