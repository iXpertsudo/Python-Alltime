class Employee :

    #Attributes
    def __init__(self, fullname, position, status, age):
        self.fullname = fullname
        self.position = position
        self.status = status
        self.age = age

    def work(self):
        print(self.fullname, " is working")

employee1 = Employee("Victor Smith", "MD", "Married", 24)
print(employee1.fullname, employee1.position, employee1.status, employee1.age)
employee1.work()

employee2 = Employee("Claire Sandra ", "Program Manager", "Single", 34)
employee3 = Employee("Solange Parker", "Project Manager", "Single", 43)


