import os
from collections import Counter


# Function to read all text files in a folder and join their contents
def read_files_and_join(folder_path):
    all_text = ""
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
                all_text += file.read() + " "  # Adding a space between the contents of each file
    return all_text


# Function to find the top 100 most used words
def top_100_words(text):
    # Tokenize the text and count occurrences of each word
    word_counts = Counter(text.split())
    # Extract the top 100 most common words
    top_100 = word_counts.most_common(100)
    return top_100


# Main function
folder_path = r"data\main_tokenized"  # Specify the path to your folder containing text files
all_text = read_files_and_join(folder_path)
top_100 = top_100_words(all_text)

print("Top 100 most used words:")
for i, (word, count) in enumerate(top_100, 1):
    print(f"{i}. {word} - {count}")