import spacy.cli
import spacy
from collections import Counter
import base64
import requests
import os
spacy.cli.download("en_core_web_lg")
spacy.cli.download("en_core_web_sm")


def create_sentence(list_of_adjectives):
    sentence = "3 squares by 3 squares grid moodboard of: "
    if list_of_adjectives:
        sentence += " " + ' '.join(list_of_adjectives)

    return sentence


def generate_title(lyrics_arrays):
    nlp = spacy.load("en_core_web_sm")

    titles = []

    # Process each lyric array with spaCy and extract entities and adjectives
    # chatgpt help
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
    url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"

    body = {
        "steps": 30,
        "width": 1024,
        "height": 1024,
        "seed": 0,
        "cfg_scale": 5,
        "samples": 1,
        "text_prompts": [
            {
                "text": input_words,
                "weight": 1
            }
        ],
    }

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer sk-q01UhLqfaR59h8RqixIWJXIZtMiC36njCDsL9V4iWHu3vIlG",  # Replace with your Stability.ai API key
    }

    response = requests.post(
        url,
        headers=headers,
        json=body,
    )

    data = response.json()

    # Make sure the out directory exists
    # chatgpt help
    if not os.path.exists("./out"):
        os.makedirs("./out")

    # Save the image locally
    # chatgpt help
    image_path = f'./out/generated_image.png'
    with open(image_path, "wb") as f:
        f.write(base64.b64decode(data["artifacts"][0]["base64"]))

    return image_path


def execute(song_lyrics_arrays):
    adjectives = generate_title(song_lyrics_arrays)
    sentences = create_sentence(adjectives)
    try:
        return print_image(sentences)
    except Exception as e:
        return None


def top_5_words_and_counts(words):
    # chatgpt help
    # Step 1: Count word occurrences
    word_counts = Counter(words)

    # Step 2: Sort by occurrence in descending order
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    # Step 3: Extract top 5 words and counts
    top_5_words = [word for word, count in sorted_words[:5]]
    top_5_counts = [count for word, count in sorted_words[:5]]

    return top_5_words, top_5_counts

