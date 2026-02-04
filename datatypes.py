#Data Types
#There are four of them

age = 17     #Integer
weight = 50.57   #Float
greeting = "Hello there"    #String
isMammal = True   #Boolean



#Data structures - Multiple elements in one variable

fruits = ["apple", "cherry", "banana"]  #List-- Elements in a list are ordered, changeable - Different DataTypes
courses = ["MIT", "Data Science" "Cybersecurity" ]      #Array - Similar Datatypes
cars = ("Mercedes ", "Toyota", "VolksWagen","BMW" )  #Tuple -Elements in A List are Ordered and Unchangeable
countries ={"Brazil", "Japan", "Australia", "Spain"}  #Set  - Is an Unordered and Unchangeable
student = {
    "firstname" : "Victor",
    "course" : "MIT",
    "age" : 17 ,
    "nationality" : "British",
                }   #Dictionary -Key value pair





print("Student is" , age, "years old")
print(weight)
print("Is animal a mammal ? : "  , isMammal)
print(fruits)
print(countries)



#Typecasting -Converting one datatype to another
print(float(age))
print(int(50.57))