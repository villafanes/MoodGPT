import requests
import spacy.cli
spacy.cli.download("en_core_web_lg")
spacy.cli.download("en_core_web_sm")
import spacy
import random


def create_sentence(list_of_adjectives):
    # Add other words to form a complete sentence
    # sentence = "The" You can modify this part based on your specific sentence structure
    sentence = ""
    if list_of_adjectives:
        sentence += " " + ' '.join(list_of_adjectives)

    return sentence


def generate_title(lyrics_arrays):
    nlp = spacy.load("en_core_web_sm")

    titles = []

    # Process each lyric array with spaCy and extract entities and adjectives
    for lyric_array in lyrics_arrays:
        # Extract the string from the array
        lyric_text = lyric_array[0]

        # Process the lyrics with spaCy
        doc = nlp(lyric_text)

        # Extract entities and adjectives
        entities = [ent.text for ent in doc.ents if ent.label_ in ["PERSON", "ORG", "GPE"]]
        adjectiveslist = [token.text for token in doc if token.pos_ == "ADJ"]
        nouns = [token.text for token in doc if token.pos_ == "NOUN"]

        # Example: Combine the first entity and an adjective
        titles.extend(adjectiveslist)
        titles.extend(entities)
        titles.extend(nouns)

    return titles


def print_image(input_words):
    r = requests.post(
        "https://api.deepai.org/api/text2img",
        data={
            'text': input_words,
        },
        headers={'api-key': '3ac6a775-0374-4070-8683-d3e5fbbc8850'}
    )
    data = r.json()
    print(data)


def execute(song_lyrics_arrays):
    adjectives = generate_title(song_lyrics_arrays)
    sentences = create_sentence(adjectives) + " 3x3 square grid moodboard"
    print_image(sentences)
    
"""
Example on how to run, parse the lines into execute command to generate image

song_lyrics_arrays2 = [
    ["I hear the wind call my name"],
    ["The stars are dancing in the night"],
    ["A journey through lovely and space"],
    ["In the embrace of endless light"]
]

execute(song_lyrics_arrays2)
"""

