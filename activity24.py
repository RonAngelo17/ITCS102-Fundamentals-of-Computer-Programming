from activity23_1 import *

print("WELCOME TO MY COMPILER PROGRAM")
name= input("Hi Visitors, what is your name? ")

print(f"Hi {name},select from the options below")
print("A - Greet Name\nB - Factorial\nC - Triangle\nE - Exit")

isCont = True

while isCont == True:
    choice= input("Select from A-E: ").lower()

    if choice == 'a':
        name = input("Please state your name")
        GreetWithName(name)
        continue
    elif choice == 'b':
        number= eval(input("Input any number: "))
        print(f"factorial of {number} is {Factorial(number)}")
        continue
    elif choice == 'c':
        GetTriangle()
        continue
    elif choice == 'e':
        print("program terminated ...")
    else:
        print("Invalid input")