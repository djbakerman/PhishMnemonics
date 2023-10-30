import random
import re

# Read the lyrics from phish.txt
with open('phish.txt', 'r') as file:
    all_songs = file.read().split('\n')

# Shuffle the songs to increase randomness
for _ in range(5):
    random.shuffle(all_songs)

# Initialize an empty list to hold the filtered words
filtered_words = []

# Regex to remove non-letter characters
pattern = re.compile('[^a-zA-Z]')

# Loop through the songs and collect enough words
for song in all_songs:
    # Stop if we've collected enough words
    if len(filtered_words) >= 15:
        break

    # Split the current song into words
    song_words = song.split()

    # Add cleaned and filtered words to the list
    for word in song_words:
        cleaned_word = pattern.sub('', word).lower()
        if len(cleaned_word) >= 3 and cleaned_word not in ['and', 'the']:
            filtered_words.append(cleaned_word)

# Randomly select 15 words from the filtered list
if len(filtered_words) >= 15:
    random_words = random.sample(filtered_words, 15)
    print("Here are 15 random words from Phish songs:")
    print(" ".join(random_words))
else:
    print(f"Only {len(filtered_words)} eligible words were found across all songs. Unable to generate a sample of 15.")
