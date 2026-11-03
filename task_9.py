
typ = int(input("Enter type: 1.Distance 2.Mass 3.Volume "))



if typ == 1:
    defbase = {"mm":1, "cm":10, "m":1000, "k":1000000 }
elif typ == 2:
    defbase = {"mg":1, "g":1000, "kg":1000000, "t":1000000000 }
elif typ == 3:    
    defbase = {"ml":1, "l":1000, "cube m": 1000000 }

base = input("Enter one of  base units: "+ " ".join(map(str, defbase.keys())) + " ")
res = input("Enter result unit: ")
numb = int(input("Enter number: "))

print(numb*defbase[base]/defbase[res])