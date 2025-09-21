def rem_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for v in vowels:
        s = s.replace(v, '')
    print(s)

str = input("Введите строку: ")
rem_vowels(str)
