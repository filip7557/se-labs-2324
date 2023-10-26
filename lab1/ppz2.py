number = int(input("Unesi broj: "))
check = int(input("Unesi drugi broj: "))

if(number % 4 == 0):
    print("Broj je višekratnik 4.")
elif(number % 2 == 0):
    print("Broj je paran.")
else:
    print("Broj je neparan.")

if(number % check == 0):
    print("Brojevi su djeljivi.")
else:
    print("Brojevi nisu djeljivi.")