money = int(input("Enter amount to deposit: "))

blue = money // 1000
money = money % 1000

yellow = money // 500
money = money % 500

green = money // 200
money = money % 200

violet = money // 100
money = money % 100

red = money // 50
money = money % 50

twenty = money // 20
money = money % 20

ten = money // 10
money = money % 10

five = money // 5
money = money % 5

one = money // 1
money = money % 1

print("Here is the breakdown of the amount you deposited:")
print("1000:", blue)
print("500:", yellow)
print("200:", green)
print("100:", violet)
print("50:", red)
print("20:", twenty)
print("10:", ten)
print("5:", five)
print("1:", one)