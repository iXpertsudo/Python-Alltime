# A function/ Methods is  block of code that performs a specific task and can be used again and again.
# Instead of using the same code many times you put it inside a function and reuse it.

# STANDARD LIBRARY FUNCTIONS/ IN-BUILT FUNCTIONS
y = max(45, 78, 95, 89, 565895, 89 , 2, 789, 568, 456, 1)
print("The maximum number is", y)



x = min(45, 78, 95, 89, 5655, 89, 2, 789, 56)
print("The minimum number is", x)

print()

# USER-DEFINED FUNCTIONS
def name () :
    print("Victor")

name()  #Calling the function

print()

def add ():
    print(10 + 20)

add()

print()

def dog() :
     name = "Brave"
     breed = "German Shepherd"
     age = 5
     print(name, breed, age)
dog()

print()

# Parameter/Variable
#Arguments/Values

def dog(name, breed, age):
     print(name, breed, age)


dog("Brave", "German Shepherd", 5 )
dog("Fluffy", "Golden Retriever", 6 )
dog("Space", "Rotweiler", 10 )
dog("Sparkles ", "Pitbull", 14 )


print()
# A program to display details of five
# employees at eMobilis.

# Use a user-defined function with the help
#of parameters and arguments.

# Details -Fullname, position, gender, age


def employee (FirstName, LastName, position, gender,age) :
    print(FirstName, LastName, position, gender, age)

employee("Michael", "Johnson", "Software Engineer", "Male", 34)
employee("Emily", "Carter", "Frontend Developer", "Female", 28)
employee("Daniel", "Thompson", "Backend Developer", "Male", 41)
employee("Sarah", "Williams", "Project Manager", "Female", 36)
employee("James", "Anderson", "Data Analyst", "Male", 30)




