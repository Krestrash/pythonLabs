def exchange(money):
    notes = [100, 50, 10, 5, 2, 1]
    result = {}
    for b in notes:
        result[b], money = divmod(money, b)
    return result


s = int(input("Введите сумму: "))
print(exchange(s))
