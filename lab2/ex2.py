f = open('C:\\Users\\student\\Desktop\\fc-si-lv\\se-labs-2324-prp\\lab2\\ex2-text.csv', 'r', encoding="utf=8")

text = []

for line in f:
    text.append(line)
    
f.close()
    
employees = []
locations = []

for i in range(len(text)-1):
    data = text[i+1].split(',')
    employees.append(f'{data[0]},{data[1]},')
    locations.append(f'{data[0]},{data[3]}')
    
f = open('C:\\Users\\student\\Desktop\\fc-si-lv\\se-labs-2324-prp\\lab2\\ex2-employees.txt', 'w', encoding="utf=8")
f.write('\n'.join(employees))
f.close()

f = open('C:\\Users\\student\\Desktop\\fc-si-lv\\se-labs-2324-prp\\lab2\\ex2-locations.txt', 'w', encoding="utf=8")
f.write(''.join(locations))
f.close()


    
    