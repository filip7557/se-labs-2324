f = open('C:\\Users\\student\\Desktop\\fc-si-lv\\se-labs-2324-prp\\lab2\\ex2-text.csv', 'r', encoding="utf=8")

text = []

for line in f:
    text.append(line)
    
f.close()

employees = []

for i in range(len(text) - 1):
    data = text[i+1].split(',')
    employees.append(dict([('employee', data[0]), ('title', data[1]), ('age', data[2]), ('office', data[3])]))
    
print(employees)