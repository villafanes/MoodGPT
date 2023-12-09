"""
# MoodGPT Project

## Overview
MoodGPT is a Python-based application that generates mood boards based on song lyrics. It utilizes the Genius API to fetch lyrics and an AI image generator API to create visual representations of the mood conveyed by the lyrics. It also displays the relative frequencies of the top 5 most repeated lyrics so the user can have an idea of which keywords have the largest influence on the image generation.

## Modules
- `moodgpt_gui.py`: The Graphical User Interface (GUI) for interacting with the application.
- `image_api.py`: Handles the processing and generation of mood boards from song lyrics.
- `genius_api.py`: Fetches song lyrics using the Genius API.

## Prerequisites
- Python 3.x
- Tkinter 
- PIL (Python Imaging Library)
- `lyricsgenius` Python package
- `requests` Python package
- 'spacy' Python package

## Installation
1. Ensure Python 3.x is installed on your system.
2. Install required Python packages (pip install Pillow lyricsgenius requests spacy)

## Usage
1. Run the `moodgpt_gui.py` script to start the application (python moodgpt_gui.py)
2. Enter the song title and artist name in the provided fields after deleting the text already in the entry widgets.
3. Click "Enter" to generate and display the mood board. Adjust your entered prompts accordingly if any error messages pop up.
4. Use the "Quit" button in the top right corner to exit the application from the home screen or the usual exit button to quit at any time.

"""
