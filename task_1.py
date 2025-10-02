text = input("Введите текст: ")
text = text.lower()
words = []
current_word = ""
i = 0
while i < len(text):
    char = text[i]
    if char.isspace():
        if current_word:
            words.append(current_word)
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


print(f"1. Словарь: {word_counts}")
print(f"2. Количество уникальных слов: {unique_words_count}")
