def find_and_replace_word(filename, target_word, replacement_word):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            modified_text = text.replace(target_word, replacement_word)
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(modified_text)
        print(f"The word '{target_word}' has been replaced with '{replacement_word}' in the file.")
    except FileNotFoundError:
        print("File not found.")

find_and_replace_word('input.txt', 'Hello', 'Glad to see you')