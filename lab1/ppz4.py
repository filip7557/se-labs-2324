number = int(input("Unesi broj: "))
divisors = []

for i in range(1, number+1):
    if number % i == 0:
        divisors.append(i)

print(f"Djelitelji broja {number}:", divisors)