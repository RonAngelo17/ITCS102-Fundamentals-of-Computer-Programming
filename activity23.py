from activity23_1 import GreetWithName, GreetPerson, FunctionWithReturn, Factorial

def MyFirstFunction():
    print("Hi, this is my first function")
    print("What it does is it greet people")
    print("Hi Visitor")

MyFirstFunction()
GreetWithName("Ron")
GreetWithName("Zoro")
GreetPerson("Angelo", "Lucena", "18")

print(f"I want to get the summation of {FunctionWithReturn(5)}")
print(f"I want to get the summation of {FunctionWithReturn(7)+5}")
print(f"The factorial of {Factorial(5)}")