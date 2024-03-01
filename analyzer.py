import os


def tokenize_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        tokens = set(text.split())
    return tokens


def main(directory):
    files = os.listdir(directory)
    files = [file for file in files if file.endswith('.txt')]
    results = []

    # Iterate over each file
    for file_name in files:
        file_path = os.path.join(directory, file_name)
        unique_tokens_this_file = tokenize_file(file_path)

        combined_tokens_other_files = set()
        for other_file_name in files:
            if other_file_name != file_name:
                other_file_path = os.path.join(directory, other_file_name)
                combined_tokens_other_files.update(tokenize_file(other_file_path))

        unique_to_this_file = unique_tokens_this_file - combined_tokens_other_files
        percentage_unique = (len(unique_to_this_file) / len(unique_tokens_this_file)) * 100 if len(
            unique_tokens_this_file) > 0 else 0

        results.append((file_name, percentage_unique))

    # Sort results by percentage
    results.sort(key=lambda x: x[1], reverse=True)

    # Print sorted results
    for file_name, percentage_unique in results:
        print(f"Percentage of tokens unique to {file_name}: {percentage_unique:.2f}%")


if __name__ == "__main__":
    directory = r"D:\repo\genius_lyrics_v2\azerbaijani_rapper_lyrics_data_analysis\data\main_tokenized_unique"
    main(directory)
