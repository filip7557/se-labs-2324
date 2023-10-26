a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newList = []

num = int(input("Unesi broj: "))

for el in a:
    if el < num:
        newList.append(el)

print(newList)