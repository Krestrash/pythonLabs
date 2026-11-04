incomes = {}
expenses = {}

categories = ["жилье", "питание", "транспорт", "развлечения", "здоровье", "одежда", "прочее"]


def add_income():
    source = input("Источник дохода: ")
    amount = float(input("Сумма: "))
    if source in incomes:
        incomes[source] += amount
    else:
        incomes[source] = amount
    print("Доход добавлен")


def add_expense():
    print("Категории:", ", ".join(categories))
    cat = input("Категория расхода: ").lower()
    amount = float(input("Сумма: "))
    if cat in expenses:
        expenses[cat] += amount
    else:
        expenses[cat] = amount
    print("Расход добавлен")


def total_income():
    s = 0
    for v in incomes.values():
        s += v
    return s


def total_expense():
    s = 0
    for v in expenses.values():
        s += v
    return s


def show_analysis():
    inc = total_income()
    exp = total_expense()
    balance = inc - exp

    print("\n--- Анализ финансов ---")
    print(f"Общий доход: {inc}")
    print(f"Общий расход: {exp}")
    print(f"остаток: {balance}")

    if inc > 0:
        print(f"Доля расходов от дохода: {exp / inc * 100:.1f}%")

    if exp > 0:
        print("\nрасходы по категориям:")
        for cat, amount in expenses.items():
            percent = amount / exp * 100
            print(f"  {cat}: {amount} ({percent:.1f}%)")

    if inc > 0:
        print("\nДоходы по источникам:")
        for src, amount in incomes.items():
            percent = amount / inc * 100
            print(f"  {src}: {amount} ({percent:.1f}%)")

    print()


def show_recommendations():
    inc = total_income()
    exp = total_expense()

    print("\n--- Рекомендации ---")

    if inc == 0:
        print("Добавьте данные о доходах для получения рекомендаций")
        return

    if exp > inc:
        print("Расходы превышают доходы.Нужно срочно сократить траты")
    elif exp > inc * 0.8:
        print("Расходы занимают больше 80% дохода. Старайтесь откладывать хотя бы 10-20%")
    elif exp > inc * 0.5:
        print("Расходы в пределах нормы, но можно попробовать откладывать больше")
    else:
        print("Хорошая ситуация. Расходы меньше половины дохода, можно активно копить")

    if "жилье" in expenses and expenses["жилье"] > inc * 0.4:
        print("На жилье уходит больше 40% дохода.Попробуйте найти более дешевый вариант")

    if "питание" in expenses and expenses["питание"] > inc * 0.25:
        print("на питание уходит больше 25%. Можно попробовать готовить дома чаще")

    if "развлечения" in expenses and expenses["развлечения"] > inc * 0.15:
        print("На развлечения тратится больше 15%. Стоит пересмотреть досуг")

    if "транспорт" in expenses and expenses["транспорт"] > inc * 0.15:
        print("Транспорт занимает больше 15%. подумайте об альтернативных способах передвижения")

    saving = inc - exp
    if saving > 0:
        print(f"Вы можете откладывать {saving} в месяц")
        print(f"За год это будет {saving * 12}.")

    print()


def plan_purchase():
    inc = total_income()
    exp = total_expense()
    saving = inc - exp

    if saving <= 0:
        print("Сейчас нет свободных средств для накопления")
        return

    name = input("На что копим: ")
    goal = float(input("Нужная сумма: "))

    months = goal / saving
    if months < 1:
        months = 1

    print(f"\nЧтобы накопить {goal} на '{name}', откладывая {saving} в месяц,")
    print(f"потребуется примерно {months:.1f} месяцев")

    if months > 24:
        print("Это больше двух лет. можно либо увеличить доход или найти более дешевый вариант")
    elif months > 12:
        print("Это больше года. надо откладывать чуть больше, чтобы ускорить процесс")
    else:
        print("Цель достижима в разумные сроки")

    print()


while True:
    print("1. Добавить доход")
    print("2. Добавить расход")
    print("3. Анализ")
    print("4. Рекомендации")
    print("5. Планирование крупной покупки")
    print("0. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        add_income()
    elif choice == "2":
        add_expense()
    elif choice == "3":
        show_analysis()
    elif choice == "4":
        show_recommendations()
    elif choice == "5":
        plan_purchase()
    elif choice == "0":
        break
    else:
        print("Неверный ввод.")

    
