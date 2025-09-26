s = int(input("Введите сумму: "))
oneh, s = divmod(s, 100)
fifty, s = divmod(s, 50)
ten, s = divmod(s, 10)
five, s = divmod(s, 5)
two, s = divmod(s, 2)
one, s = divmod(s, 1)

print(f"Купюры для размена: 100 = {oneh}, 50 = {fifty}, 10 = {ten}, 5 = {five}, 2 = {two}, 1 = {one} ")

