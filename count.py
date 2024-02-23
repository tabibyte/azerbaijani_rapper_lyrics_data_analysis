import os
import re

def process_text(text):
    # Remove non-alphanumeric characters and convert to lowercase
    processed_text = re.sub(r'[^a-zA-Z0-9\səğöüçşı]', ' ', text.lower())

    # Tokenize the text manually
    tokens = re.split(r'\s+', processed_text)

    return tokens

def process_folder(input_folder):
    # Dictionary to store unique tokens for each file
    unique_tokens_per_file = {}

    # Loop through each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            file_path = os.path.join(input_folder, filename)

            # Read the content of the input file
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()

            # Process the text to get tokens
            tokens = process_text(text)

            # Count unique tokens
            unique_tokens = set(tokens)
            unique_tokens_per_file[filename] = len(unique_tokens)

    return unique_tokens_per_file

# Define input folder
input_folder = r'D:\repo\genius_lyrics_v2\azerbaijani_rapper_lyrics_data_analysis\data\main_tokenized_unique'

# Get unique token count for each file
unique_tokens_per_file = process_folder(input_folder)

# Sort the dictionary by values (unique token counts)
sorted_unique_tokens_per_file = {k: v for k, v in sorted(unique_tokens_per_file.items(), key=lambda item: item[1], reverse=True)}

# Print the results
for filename, count in sorted_unique_tokens_per_file.items():
    print(f"File: {filename}, Unique Token Count: {count}")