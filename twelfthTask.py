minutes = int(input("Минуты: "))
sms = int(input("СМС: "))
data = int(input("МБ трафика: "))

base = 24.99
extra = 0

if minutes > 60:
    extra_m = (minutes - 60) * 0.89
    print(f"Доп. минуты: {extra_m:.2f} руб.")
    extra += extra_m
if sms > 30:
    extra_s = (sms - 30) * 0.59
    print(f"Доп. СМС: {extra_s:.2f} руб.")
    extra += extra_s
if data > 1024:
    extra_d = (data - 1024) * 0.79
    print(f"Доп. интернет: {extra_d:.2f} руб.")
    extra += extra_d

tsum = base + extra
tax = tsum * 0.02
total = tsum + tax

print(f"Базовый тариф: {base:.2f} руб.")
print(f"Дополнительная оплата: {extra:.2f} руб.")
print(f"Налог: {tax:.2f} руб.")
print(f"Итого: {total:.2f} руб.")