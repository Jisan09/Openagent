import os
import urllib.request

# Create the "data" folder if it doesn't exist
if not os.path.exists("data"):
    os.makedirs("data")

# Read the complete text from the provided URL
text_data = (urllib.request.urlopen("https://www.gutenberg.org/cache/epub/70911/pg70911.txt")).read().decode("utf-8")

# Split the text into chapters based
chapters = text_data.split("\nCHAPTER ")

# Save each chapter into separate .txt files
for i, chapter_text in enumerate(chapters[1:]):
    if not os.path.exists(f"data/chapter{i+1}"):
        os.makedirs(f"data/chapter{i+1}")
    chapter_filename = f"data/chapter{i+1}/chapter_{i+1}.txt"

    with open(chapter_filename, "w", encoding="utf-8") as file:
        file.write(f"### This for testing ###\nJisan says - 'This is chapter {i+1}'\n\nCHAPTER {chapter_text}")