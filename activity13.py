a=0
numbers= " "

for i in range (1, 6, 1):
    print(i)
    num= eval(input("Enter any number: "))
    a+=num
    numbers+=str(num)+" "

print("The sum of all the numbers is:", a)
print("The numbers are:", numbers)