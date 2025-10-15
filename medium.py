columns= eval(input("Enter number of columns: "))

for x in range(1, 11, 1):
    for y in range(1, columns+1, 1):
        print(f"{x}x{y}={x*y}", end="\t\t")
    print()




for i in range(1,6,1):
    for j in range(6, i, -1):
        print(" ", end="")
    for k in range(1, i+1, 1):
        print("* ", end="")
    print()