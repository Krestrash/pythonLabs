age = int(input("Введите возраст "))
if age < 21 or age > 65:
    print("Кредит не выдается. Возраст должен быть от 21 до 65 лет.")
    exit()

income = int(input("Введите месячный доход "))
credit = int(input("Введите размер кредита "))
term = int(input("Введите срок "))
credit_history = input("Введите кред историю(отличная/хорошая/удовлетворительная/плохая)")
has_guarantor = bool(int(input("Есть ли у вас поручитель(1 - да, 0 - нет)")))
has_coll = bool(int(input("У вас есть залог(1 - да, 0 - нет)")))

ratio = credit / (income * 12)

score = 0

if age < 25 or age > 55:
    score += 2
elif age > 45:
    score += 1

if ratio >= 3:
    score += 3
elif ratio >= 2:
    score += 2
elif ratio >= 1:
    score += 1

if credit_history == "плохая":
    score += 4
elif credit_history == "удовлетворительная":
    score += 2
elif credit_history == "хорошая":
    score += 1

if has_guarantor != "да":
    score += 1

if has_coll != "да":
    score += 1

if term > 60:
    score += 3
elif term > 36:
    score += 2
elif term > 12:
    score += 1

if score <= 3:
    category = "низкий"
    rate = 9
    decision = "одобрено"
    rec = "можно выдавать кредит на обычных условиях"
elif score <= 6:
    category = "средний"
    rate = 13
    decision = "одобрено с условиями"
    rec = "лучше потребовать залог или поручителей"
elif score <= 10:
    category = "высокий"
    rate = 18
    decision = "одобрено с ограничениями"
    rec = "нужен залог и поручители, можно уменьшить сумму"
else:
    category = "критический"
    rate = 24
    decision = "отклонено"
    rec = "кредит выдавать нельзя, слишком большой риск"

m_rate = rate / 100 / 12
payment = credit * (m_rate * (1 + m_rate) ** term) / ((1 + m_rate) ** term - 1)


print("Результаты ")
print("Соотношение кредит к доходу: ", round(ratio, 2))
print("Платеж в месяц: ", round(payment, 2))
print("Балл риска: ", score)
print("Категория риска: ", category)
print("Ставка: ", rate, "%")
print("Решение: ", decision)
print("Рекомендация: ", rec)
