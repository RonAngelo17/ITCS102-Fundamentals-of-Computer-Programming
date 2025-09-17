print("MULTIPLICATION TABLE MAKER")

number = eval(input("Enter a number: "))

print("Multiplication table for", number,":")

for x in range(1, 11):
    product= number*x
    print(number, "x", x, "=", product)