grade= eval(input("What is your grade? "))

if grade >=95 and grade <= 100:
    print("You got an A+")
elif grade >=90 and grade <=94:
    print("You got an A")
elif grade >=85 and grade <=89:
    print("You got a B")
elif grade >=75 and grade <=84:
    print("You got a C")
else:
    print("You did not pass")