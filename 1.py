def count_words_and_most_common(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            words = text.split()
            print(f"В текстовом файле {len(words)} слов.")

            word_count = {}
            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

            most_common_word = max(word_count, key=word_count.get)
            print(f"Самое популярное слово это: '{most_common_word}' встречается {word_count[most_common_word]} раз.")
    except FileNotFoundError:
        print("File not found.")

count_words_and_most_common('mer.txt')