print("ODD NUMBER ACCUMULATOR")
print("Enter 10 numbers. We'll sum only the odd ones.")
sum=0

for x in range(10):
    number= eval(input("Enter a number (can be positive, negative, or zero) --> "))
    if number % 2 != 0:
        sum += number

print("Sum of all odd numbers are:", sum)

