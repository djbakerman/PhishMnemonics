# PhishMnemonics

## Description

`PhishMnemonics` is a Python script designed to generate a string of 15 random words pulled from the lyrics of shuffled Phish songs. The generated words adhere to certain criteria, such as having a minimum length of three characters and excluding common words like 'and' and 'the'. This script is perfect for Phish fans looking to generate mnemonic-like strings from their favorite songs.

## Algorithm Overview

1. **Read Lyrics**: The script reads in the lyrics of multiple Phish songs from a text file (`phish.txt`), where each song's lyrics are separated by a newline.
2. **Shuffle Songs**: For better randomness, the list of songs is shuffled multiple times.
3. **Filter Words**: Words from the lyrics are filtered based on the following criteria:
   - Must have a minimum length of three characters.
   - Should not be common words like 'and' and 'the'.
   - All special characters are removed, and words are converted to lowercase.
4. **Random Selection**: 15 words are then randomly selected from this filtered list to create the final mnemonic-like string.

## Usage

### Pre-requisites

- Python 3.x
- A text file (`phish.txt`) containing Phish songs, separated by newlines.

### Steps

1. Clone this repository or download the `PhishMnemonics.py` script.
2. Place your `phish.txt` file in the same directory as the script.
3. Open a terminal and navigate to the directory containing the script.
4. Run the script using the command:
    ```bash
    python3 PhishMnemonics.py
    ```
5. The script will output a string of 15 random words meeting the specified criteria.

## Example Output

To run the script, execute the following command in your terminal:

```bash
python3 genMnemonic.py

Here are 15 random words from Phish songs:
highway hold good bayou jam trying dream art hyhu midnight bird ziggy free blue stardust
```
