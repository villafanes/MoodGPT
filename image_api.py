# uncomment line below to download package, dont run but hover over it alt+enter
# import spacy.cli
# spacy.cli.download("en_core_web_lg") run both
# spacy.cli.download("en_core_web_sm") 
# after running both you should be able to import spacey
# same thing for openAI uncomment next line 
# import open ai
from openai import OpenAI
import spacy
import random


client = OpenAI(
    api_key='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',
)


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
    response = client.images.generate(
        model="dall-e-2",
        prompt=input_words,
        size="512x512",
        quality="standard",
        n=1,
    )
    print(response)


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

