sales = [
    {"name": "Хлеб", "price": 50, "quantity": 100},
    {"name": "Молоко", "price": 80, "quantity": 60},
    {"name": "Сыр", "price": 500, "quantity": 20},
    {"name": "Авокадо", "price": 50, "quantity": 40},
    {"name": "Кола", "price": 200, "quantity": 30},
]

revenue = {}
for item in sales:
    name = item["name"]
    total = item["price"] * item["quantity"]
    if name in revenue:
        revenue[name] += total
    else:
        revenue[name] = total

print("Выручка по каждому товару:")
for name, total in revenue.items():
    print(f"  {name}: {total} ")

best_name = None
best_sum = 0
for name, total in revenue.items():
    if total > best_sum:
        best_sum = total
        best_name = name

print(f"\nСамый прибыльный товар: {best_name} {best_sum} ")

unique_count = 0
for _ in revenue:
    unique_count += 1
print(f"Количество уникальных наименований: {unique_count}")
