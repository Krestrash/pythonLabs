pasw = input("Enter pass")
if len(pasw) <16:
    print("too short")
elif pasw.isdigit() or pasw.isalpha():
    print("weak password")
else:
    print("Strong password")