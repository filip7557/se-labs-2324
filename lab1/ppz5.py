import random

def generate_random_list(low, high):
    a = []
    num_elements = random.randint(5, 15)
    for _ in range(num_elements):
        a.append(random.randint(low, high))
    return a

a = generate_random_list(1, 10)
b = generate_random_list(3, 13)
commons = []

for el in a:
    if el in b and el not in commons:
        commons.append(el)

print(a)
print(b)
print(commons)