factorial = 1
number= eval(input("Enter a number: "))

for x in range (number, 0, -1):
    factorial*=x

print("The factorial of", number, "is", factorial)
      
    