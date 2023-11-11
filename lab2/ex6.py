import json

class Employee:

    def __init__(self, name, title, age, office):
        self.name = name
        self.title = title
        self.age = age
        self.office = office
    
    def as_dict(self):
        # Returns the attributes as a dictionary
        dic = dict([('employee', self.name), ('title', self.title), ('age', self.age), ('office', self.age)])
        return dic

    def __str__(self):
        return f"{self.name} ({self.age}), {self.title} @ {self.office}"


class Company:

    def __init__(self, name):
        self.name = name
        self.employees = []

    def __str__(self):
        return f"{self.name} ({len(self.employees)} employees)"

    def employ(self, name, title, age, office):
        new_employee = Employee(name, title, age, office)
        self.employees.append(new_employee)

    def fire(self, name):
        for e in self.employees:
            if e.name == name:
                self.employees.remove(e)

    def load_from_json(self, path_to_json):
        with open(path_to_json, "r", encoding="utf-8") as f:
            employees = json.load(f)
        for employee in employees:
            self.employees.append(Employee(employee['employee'], employee['title'], employee['age'], employee['office']))

    def save_to_json(self, path_to_json):
        # Convert every Employee from self.employees into a dictionary
        # (use method as_dict() which you have to implement in the Employee class)
        # Build a list of employees where every employee is a dict
        # json.dump the whole list
        employees = []
        for employee in self.employees:
            employees.append(employee.as_dict())
            
        with open(path_to_json, 'w', encoding='utf-8') as f:
            json.dump(employees, f)

    def print_employees(self):
        """Print all employees to stdout in format:
        Company name
        ----------------
        1. Employee name (age), job_title @ office
        2. Employee name (age), job_title @ office
        ..."""
        print(self.name)
        print("----------------")
        for employee in self.employees:
            print(f'{employee.name} ({employee.age}), {employee.title} @ {employee.office}')


def main():
    nike = Company("Nike")
    print(nike)

    nike.employ("Homer Simpson", "CEO", 44, "Lobby")
    nike.employ("Marge Simpson", "CTO", 33, "Lobby")
    print(nike)

    nike.fire("Homer Simpson")
    print(nike)

    # Implement load_from_json, save_to_json and print_employees methods
    # Then uncomment the implemented methods
    adidas = Company("Adidas")
    adidas.load_from_json("C:\\Users\\student\\Desktop\\fc-si-lv\\se-labs-2324-prp\\lab2\\ex4-employees.json")
    # After loading from json, adidas should have all the employees from
    # json file
    #print(adidas)
    # Print employees should now print all the employees
    adidas.print_employees()

    adidas.employ("Homer Simpson", "CEO", 44, "Lobby")
    adidas.employ("Marge Simpson", "CTO", 33, "Lobby")
    adidas.employ("Bart Simpson", "CEO", 44, "Lobby")
    adidas.employ("Lisa Simpson", "CTO", 33, "Lobby")
    #print(adidas)
    adidas.print_employees()

    adidas.fire("Homer Simpson")
    adidas.fire("Marge Simpson")
    #print(adidas)
    adidas.print_employees()

    # Saving employees db to a new file, the file should now have 2 more
    # employees (Bart and Lisa, since Homer and Marge were fired)
    adidas.save_to_json("C:\\Users\\student\\Desktop\\fc-si-lv\\se-labs-2324-prp\\lab2\\ex6-employees.json")

if __name__ == "__main__":
    main()