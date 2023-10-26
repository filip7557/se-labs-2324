name = input("Unesi ime: ")
age = int(input("Unesi godine: "))
repeat = int(input("Unesi broj ponavljanja: "))

age100 = 2023 - age + 100

for _ in range(repeat):
    print(f"Bok {name}, imat ćeš 100 godina {age100} godine.")