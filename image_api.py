import requests
import spacy.cli

spacy.cli.download("en_core_web_lg")
spacy.cli.download("en_core_web_sm")
import spacy
from collections import Counter

'''
song lyrics have to be taken from genius and set equal as song_lyrics_passed
ex. 
song_lyrics_passed = functiontogetgeniuslyrics()

this has to be declared outside the scope just like the other global variables
execute can stay the same, just again that global variable of song_lyrics_passed has to be from the genius function
'''


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
    for array in lyrics_arrays:
        lyric_lowercase = array.lower()
        # Process the lyrics with spaCy
        doc = nlp(lyric_lowercase)

        # Extract entities and adjectives
        adjectiveslist = [token.text for token in doc if token.pos_ == "ADJ"]
        nouns = [token.text for token in doc if token.pos_ == "NOUN"]

        # Example: Combine the first entity and an adjective
        titles.extend(adjectiveslist)
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
    print("API Output: ", data)

    if 'output_url' in data:
        return data['output_url']
    else:
        print('Song entered contains explicit content. Try entering a new song.')
        return None

def execute(song_lyrics_arrays):
    adjectives = generate_title(song_lyrics_arrays)
    sentences = create_sentence(adjectives) + " 3x3 square grid moodboard"
    return print_image(sentences)


def top_5_words_and_counts(words):
    # Step 1: Count word occurrences
    word_counts = Counter(words)

    # Step 2: Sort by occurrence in descending order
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    # Step 3: Extract top 5 words and counts
    top_5_words = [word for word, count in sorted_words[:5]]
    top_5_counts = [count for word, count in sorted_words[:5]]

    return top_5_words, top_5_counts


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
