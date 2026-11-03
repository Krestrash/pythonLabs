text = input("Введите текст: ")
text = text.lower()
def analyze_text(text: str, exclude_short: bool):
    words = []
    max_len = ""
    current_word = ""
    i = 0
    while i < len(text):
        char = text[i]
        if char.isspace():
            if current_word:
                if exclude_short and len(current_word)<2:
                    print("")
                else:    
                    if len(words) == 0:
                        min_len = current_word
                    words.append(current_word)
                    if len(max_len) < len(current_word):
                        max_len = current_word
                    if len(min_len) > len(current_word):
                        min_len = current_word

            current_word = ""
        else:
            current_word += char
        i += 1

    if current_word:
        words.append(current_word)


    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    unique_words_count = 0
    for word in word_counts:
        unique_words_count += 1
    return word_counts, unique_words_count, words, max_len, min_len

word_counts, unique_words_count, words, max_len, min_len = analyze_text(text, False)
print(f"1. Словарь: {word_counts}")
print(f"2. Количество уникальных слов: {unique_words_count}")
print(f"3. {len(words)}")
print(f"4. {max_len}")
print(f"5. {min_len}")
print(f"6. {max(word_counts, key=word_counts.get)}")
word_counts, unique_words_count, words, max_len, min_len = analyze_text(text, True)
print(f"1. Словарь: {word_counts}")
print(f"2. Количество уникальных слов: {unique_words_count}")
print(f"3. {len(words)}")
print(f"4. {max_len}")
print(f"5. {min_len}")
print(f"6. {max(word_counts, key=word_counts.get)}")
