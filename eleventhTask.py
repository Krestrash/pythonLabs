from typing import Any


def zodiac(d, m) -> Any | None:
    signs = [
        ((21, 3), "Овен"), ((20, 4), "Телец"), ((21, 5), "Близнецы"),
        ((21, 6), "Рак"), ((23, 7), "Лев"), ((23, 8), "Дева"),
        ((23, 9), "Весы"), ((23, 10), "Скорпион"), ((22, 11), "Стрелец"),
        ((22, 12), "Козерог"), ((20, 1), "Водолей"), ((19, 2), "Рыбы")
    ]
    for (d, m), sign in signs:
        if (m == m and d >= d) or (m == (m % 12 + 1) and d < signs[(signs.index(((d, m), sign)) - 1)][0][0]):
            return sign
    return None


day, month = map(int, input("Введите день и месяц рождения (дд мм): ").split())
print("Ваш знак зодиака:", zodiac(day, month))