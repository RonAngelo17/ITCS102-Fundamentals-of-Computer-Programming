name= input("Hi, What is your name?")

print("+"*25, "\nODD NUMBER SELECTOR, press 0 to stop the loop" )

print("+"*25)
 
sum=0
odd=""
IfOdd=True

while IfOdd == True:
    number= eval(input("Input a random number: "))
    
    if number%2==1:
        print("Odd Number Detected")
        number+=0
        sum+=number
        odd+=str(number)+" "
        continue
    elif number==0:
        print("Loop Terminated")
        break
    else:
        if number%2==0:
            print("Even Number Detected")
        else:
            print("Invalid number/input")
            continue

print("Hi", name, "the sum of all Odd numbers is", sum)
print("Odd number include the ff:", (odd))
    
        

    
