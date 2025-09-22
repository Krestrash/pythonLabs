def exchange(sum):
    notes = {"100":0, "50":0, "10":0, "5":0, "2":0, "1":0}
    while sum > 0:
        sum = sum // 10


sum = input("Введите сумму: ")
