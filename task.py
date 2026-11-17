# Интернет магазин. Можно добавить в корзину товары через пользовательский ввод ( назавание, колл-во,сумма) можно удалить товар из корзины.Итог покупок в файл.Декоратор скидка 10 процентов если больше 100руб
store = {}

sale = 0


def check_sale(func):
    def wrapper(*args, **kwargs):
        all_sum = 0
        for item in store:
            all_sum = all_sum + store[item][0] * store[item][1]
        if all_sum > 100:
            global sale
            sale = 0.1
        else:
            sale = 0
        return func(*args, **kwargs)

    return wrapper


def add_item(name, quantity, price):
    if name not in store:
        store[name] = (quantity, price)
    else:
        store[name][0] += quantity


def remove_item(name, quantity):
    if name in store:
        if quantity == store[name][0]:
            del store[name]
        elif quantity < store[name][0]:
            store[name] = (store[name][0] - quantity, store[name][1])
        else:
            print("Кол -во удаляемого больше кол-ва в корзине")


@check_sale
def checkout():
    with open("text.txt", "w+") as file:
        all_sum = 0
        for item in store:
            file.write("Название: " + str(item) + "\t" + "Количество: " + str(store[item][0]) + "\t" + "Цена: " + str(
                store[item][1]) + "\n")
            all_sum = all_sum + store[item][0] * store[item][1]
        all_sum = all_sum - all_sum * sale
        if sale != 0:
            file.write(str("Приминена скидка 10% \n"))
        file.write("Сумма покупок: " + str(all_sum))
        file.close()


while True:
    ch = int(input("1. Добавить товар 2.Удалить товар 3.Вывести отчет в файл 4. Выход"))
    if ch == 1:
        name = str(input("Название"))
        quantity = int(input("Кол-во"))
        if quantity < 1:
            print("Кол-во должно быть >=1")
            continue
        price = float(input("Цена"))
        if price <= 0:
            print(" Цена должна быть  > 0")
            continue
        add_item(name, quantity, price)
    elif ch == 2:
        name = str(input("Название"))
        quantity = int(input("Кол-во"))
        if quantity < 1:
            print("Кол-во должно быть >=1")
            continue
        remove_item(name, quantity)
    elif ch == 3:
        checkout()
    elif ch == 4:
        exit()
