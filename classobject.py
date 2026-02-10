#Class is a blueprint of an object.
#Object is an instance of a class.
# Object-oriented programming
# A class has two characteristics:
# An Attribute and
# A Behaviour


class Student :
    # Attributes
    name = "Victor"
    age = 17
    gender = "Male"
    course = "MIT"

    #Behaviour  / Functions
    def study(self):
        print("Student is studying")

student1 = Student() # Creating an Object.
student1.study()
print(student1.name)


print()
student2 = Student()
student2.study()


student3  = Student()
print(student3.course)



