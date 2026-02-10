# Create a simple calculator program
# Using python.

# four operators.

# Enter a number.

num1= int(input("Enter a number: "))
num2= int(input("Enter another number: "))

# Operator
operators = input("Enter operators: (+, -, *, /):")


#Condiitions

if operators == "+":
    print(num1 + num2)

elif operators == "-":
    print(num1 - num2)

elif operators == "*":
    print(num1 * num2)

elif operators == "/":
    print(num1 / num2)
    if num2 != 0:
        print(num1/ num2)
    else:
        print("Oops! You can't divide by zero!")

else:
 print("This operator is not valid.")
