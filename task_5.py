word1_raw = input("Введите первое слово: ")
word2_raw = input("Введите второе слово: ")

word1 = word1_raw.lower()
word2 = word2_raw.lower()

sorted_word1 = sorted(word1)
sorted_word2 = sorted(word2)

if sorted_word1 == sorted_word2:
    is_anagram = True
else:
    is_anagram = False



print(f"\nСлова '{word1_raw}' и '{word2_raw}' являются анаграммами: {is_anagram}")
