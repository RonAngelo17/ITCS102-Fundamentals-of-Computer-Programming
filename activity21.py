import random

print("Random Guessing Game")
print("+"*20)

random_value= random.randint(1,10)
tries = 0
Tuloy=True

name= input("Input your name: ")

while Tuloy == True:
    num= eval(input("Guess a number from 1 to 10:"))
    tries +=1
    if num == random_value:
        print("Paldo !!!")
        break
    else:
        print("Bokya, try again")
        continue

print(f"Hi {name}, Your Guess is Correct, Number of Tries: {tries}")
