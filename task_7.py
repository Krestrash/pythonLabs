input_string = input("Введите строку: ")
compressed_string = ""

if input_string:
    current_char = input_string[0]
    count = 0

    i = 0
    while i < len(input_string):
        char = input_string[i]
        if char == current_char:
            count += 1
        else:
            compressed_string += current_char + str(count)
            current_char = char
            count = 1
        i += 1

    compressed_string += current_char + str(count)

    print(f"\nСжатая строка: {compressed_string}")
