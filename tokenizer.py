import os
import re
from nltk.tokenize import word_tokenize

def process_text(text):
    # Remove non-alphanumeric characters, convert to lowercase and tokenize
    processed_text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text.lower())
    tokens = word_tokenize(processed_text)
    return tokens

def process_folder(input_folder, output_folder, unique_tokens_folder):
    # Create the output folders if they don't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    if not os.path.exists(unique_tokens_folder):
        os.makedirs(unique_tokens_folder)

    # Loop through each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            unique_tokens_output_path = os.path.join(unique_tokens_folder, filename)

            # Read the content of the input file
            with open(input_path, 'r') as file:
                text = file.read()

            processed_tokens = process_text(text)

            with open(output_path, 'w') as file:
                file.write(' '.join(processed_tokens))

            # Write unique tokens to the unique tokens output file
            unique_tokens = set(processed_tokens)
            with open(unique_tokens_output_path, 'w') as file:
                file.write(' '.join(unique_tokens))

# Define input and output folders
input_folder = '/path/to/input/folder'
output_folder = '/path/to/output/folder'
unique_tokens_folder = '/path/to/unique_tokens/folder'

process_folder(input_folder, output_folder, unique_tokens_folder)