def GreetWithName(name):
    print(f"Hi{name}, Hope your having a splendid day")

def GreetPerson(name, loc, age):
    print(f"Hi {name}, from {loc}, {age} yr\'s old")

def FunctionWithReturn(number):
    print(f"This function calculates the summation from 1 to {number}")
    sum = 0
    for x in range(1, number+1, 1):
        sum += x
    return sum

def Factorial(number):
    print(f"This function calculates the factorial from 1 to {number}")
    factorial=1
    for y in range(number, 0, -1):
        factorial *= y
    return factorial

def GetTriangle():
    for x in range(1, 10,1):
        for y in range(10, 0, -1):
            print(end=" ", x)