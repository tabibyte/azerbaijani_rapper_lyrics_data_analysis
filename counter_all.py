import os
import re
import random


def process_text(text):
    # Remove non-alphanumeric characters and convert to lowercase
    processed_text = re.sub(r'[^a-zA-Z0-9\səğöüçşı]', ' ', text.lower())

    # Tokenize the text manually
    tokens = re.split(r'\s+', processed_text)

    # Randomly select 5000 tokens
    tokens = random.sample(tokens, min(len(tokens), 5000))

    return tokens


def process_folder(input_folder):
    # Dictionary to store unique tokens and total tokens count for each file
    token_info_per_file = {}

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
            total_tokens_count = len(tokens)
            token_info_per_file[filename] = {"unique_tokens_count": len(unique_tokens),
                                             "total_tokens_count": total_tokens_count}

    return token_info_per_file


# Define input folder
input_folder = r'D:\repo\genius_lyrics_v2\new_statistics\lyrics\main_tokenized'

# Get unique token count and total token count for each file
token_info_per_file = process_folder(input_folder)

# Sort the files by the percentage of unique tokens
sorted_files = sorted(token_info_per_file.items(),
                      key=lambda item: item[1]["unique_tokens_count"] / item[1]["total_tokens_count"], reverse=True)

# Print the results
for filename, info in sorted_files:
    unique_tokens_count = info['unique_tokens_count']
    total_tokens_count = info['total_tokens_count']
    percentage_unique_tokens = (unique_tokens_count / total_tokens_count) * 100
    print(f"{filename}, {unique_tokens_count}")
