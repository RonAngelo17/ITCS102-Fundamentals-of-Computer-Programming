import time, sys, random
import os
import json


#function to clear
def clear():
    os.system("cls")

#WELCOME SCREEN
def welcome_screen():
    clear()
    print("+" + "-" * 68 + "+")
    print("|" + "Welcome to PyMenu!".center(68) + "|")
    print("|" + "A Python Menu Program".center(68) + "|")
    print("+" + "-" * 68 + "+")
    time.sleep(1)

    boot = [
        "Loading Modules...",
        "Preparing Interface...",
        "Initializing Menus...",
        "Checking System Status...",
        "Finalizing Setup...",
    ]
   
    print("\n")
    for booting in boot:
        print("   > " + booting)
        time.sleep(0.5)

    print("\nSystem Status: Ready")
    time.sleep(0.5)

    #SMALL LOADING BAR
    print("\nStarting Program:")
    for i in range(21):
        bar = "█" * i + "-" * (20 - i)
        sys.stdout.write(f"\r[{bar}] {int((i/20)*100)}%")
        sys.stdout.flush()
        time.sleep(0.08)
        
    clear()
    print("\nSystem Startup Complete.\n")
    time.sleep(0.8)
    
    # GETTING THE USER'S NAME
    print("\n")
    name = input("Please enter your name: ").strip().title()
    clear()
    return name

#PRINT STATEMENT SUBMENUS FUNCTIONS
def simple_printing():
    print("\n\t──────────────────────────────────────────────────────")
    print("\t▶ Simple Printing")
    print("\t──────────────────────────────────────────────────────")
    print("\tInput:")
    print("\t\tprint('Hello, World!')")
    print("\t\tprint('Python')")
    print("\t\tprint('Merry Christmas')")
    print("\t──────────────────────────────────────────────────────")
    print("\tOutput:")
    print("\t\tHello, World!")
    print("\t\tPython")
    print("\t\tMerry Christmas")
    print("\t──────────────────────────────────────────────────────")

def printing_variables():
    print("\n\t──────────────────────────────────────────────────────")
    print("\t▶ Printing Variables")
    print("\t──────────────────────────────────────────────────────")
    print("\tInput:")
    print("\t\tname = 'Ron Angelo'")
    print("\t\tage = 18")
    print("\t\tcourse = 'BSIT'")
    print("\t\tprint(name)")
    print("\t\tprint('Age:', age)")
    print("\t\tprint('Course:', course)")
    print("\t──────────────────────────────────────────────────────")
    print("\tOutput:")
    print("\t\tRon Angelo")
    print("\t\tAge: 18")
    print("\t\tCourse: BSIT")
    print("\t──────────────────────────────────────────────────────")

def formatted_string():
    print("\n\t──────────────────────────────────────────────────────")
    print("\t▶ Printing Formatted String")
    print("\t──────────────────────────────────────────────────────")
    print("\n\tF-string allows you to format selected parts of a")
    print("\tstring. To specify a string as an f-string, simply ")
    print("\tput an 'f' in front of the string literal, like this:")
    print("\n\t──────────────────────────────────────────────────────")
    print("\tExample:")
    print("\t\tname = 'Ron Angelo'")
    print('\t\ttext =(f"My name is {name}"')
    print("\t\tprint(text)")
    print("\t──────────────────────────────────────────────────────")
    print("\tOutput:")
    print("\t\tMy name is Ron Angelo")
    print("\t──────────────────────────────────────────────────────")

def escape_characters():
    print("\n\t──────────────────────────────────────────────────────")
    print("\t▶ Python Escape Characters")
    print("\t──────────────────────────────────────────────────────")
    print("\n\tEscape characters are used when we need to include")
    print("\tspecial characters in a string that are otherwise ")
    print("\thard (or illegal) to type directly.")
    print("\n\t──────────────────────────────────────────────────────")
    print("\tCommon escape sequences:")
    print("\t\t\\n  - New line")
    print("\t\t\\t  - Tab")
    print("\t\t\\\"  - Double quote")
    print("\t\t\\\\  - Backslash")
    print("\t──────────────────────────────────────────────────────")
    print("\tInput:")
    print("\t\t\\nHello World")
    print("\t\t\\tHello World")
    print("\t\t\\\"Hello World ")
    print("\t\t\\\\Hello World")
    print("\t──────────────────────────────────────────────────────")
    print("\tOutput:")
    print("\n\t\tHello World")
    print("\t\t\tHello World")
    print("\t\t\"Hello World")
    print("\t\t\\Hello World")
    print("\t──────────────────────────────────────────────────────")

    # SAMPLE PROGRAM
    print("\t▶ Escape Character Diamond Sample Program")
    print("\t──────────────────────────────────────────────────────")
    name = input("\tType your name for diamond ---> ")
    print("\n")
    print("\t\t\t\t\t* \n\n\t\t\t\t* \t\t* \n\n\t\t\t* \t\t\t\t* "
          "\n\n\t\t* \t\t\tHi! \t\t\t* "
          f"\n\n\t* \t\t\t\t\t{name}\t\t\t* "
          "\n\n\t\t* \t\t\t\t\t\t* "
          "\n\n\t\t\t* \t\t\t\t* "
          "\n\n\t\t\t\t* \t\t* "
          "\n\n\t\t\t\t\t*")

    print("\t──────────────────────────────────────────────────────")


#PRINT STATEMENTS MENU
def menu_print_statements(name):
    while True:
        clear()
        print("\t+" + "-" * 68 + "+")
        print("\t|" + f"  Hello, {name}!".center(68) + "|")
        print("\t|" + "  Welcome to Print Statements".center(68) + "|")
        print("\t+" + "-" * 68 + "+")
        print("\n\t\tPrinting in Python is the process of displaying text,")
        print("\t\tvariables, or results on the screen using the print()")
        print("\t\tfunction.")
        print("\n\t\t──────────────────────────────────────────────────────")
        print("\t\t▶ PRINT STATEMENTS MENU")
        print("\t\t──────────────────────────────────────────────────────")
        print("\t\t[1] Simple Printing")
        print("\t\t[2] Printing Variables")
        print("\t\t[3] Printing Formatted String")
        print("\t\t[4] Python Escape Characters")
        print("\t\t[0] Back to Main Menu")
        print("\t\t──────────────────────────────────────────────────────")

        choice = input("\n\t\tEnter your choice: ").strip()
        
        if choice == "1":
            clear() 
            simple_printing()
            input("\n\tPress Enter to continue...") 
        elif choice == "2":
            clear()
            printing_variables()
            input("\n\tPress Enter to continue...")
        elif choice == "3":
            clear()
            formatted_string()
            input("\n\tPress Enter to continue...")
        elif choice == "4":
            clear()
            escape_characters()
            input("\n\tPress Enter to continue...")
        elif choice == "0":
            break 
        else:
            print("\n Invalid choice.")
            time.sleep(1)

#VARIABLE SUBMENUS FUNCTIONS
def input_with_variables():
    print("\n\t──────────────────────────────────────────────────────")
    print("\t▶ Using Input with Variables")
    print("\t──────────────────────────────────────────────────────")
    print("\n\tThe input() function is used to get data from a user")
    print("\tduring program execution.")
    print("\n\t──────────────────────────────────────────────────────")
    print("\tInput:")
    print("\t\tname = input('What is your name?') Ron Angelo")
    print("\t\tprint('Hi!', name, 'Welcome to the matrix')")
    print("\t──────────────────────────────────────────────────────")
    print("\tOutput:")
    print("\t\tHi!, Ron Angelo, Welcome to the matrix")
    print("\t──────────────────────────────────────────────────────")
    
    #SAMPLE PROGRAM
    print("\t▶ Input Sample Program")
    print("\t──────────────────────────────────────────────────────")
    name = input("\tEnter your name:")
    print(f"\tHello {name}")
    age = input("\tHow old are you? ")
    course = input("\tWhat is your course? ")
    print(f"\n\tName:{name} \n\tAge:{age} \n\tCourse:{course}")
    print("\n\t──────────────────────────────────────────────────────")

def data_types_length():
    while True:
        clear()   
        print("\n\t──────────────────────────────────────────────────────")
        print("\t▶ Data Types and String Length")
        print("\t──────────────────────────────────────────────────────")
        print("\n\tVariables can store data of different types.")
        print("\tCommon data types include:")
        print("\n\t──────────────────────────────────────────────────────")
        print("\t- int: Any Positive or Negative Integer numbers")
        print("\t- float: Real numbers with a Decimal point")
        print("\t- str: Textual Data")
        print("\t- bool: Boolean values (True or False)")
        print("\t──────────────────────────────────────────────────────")
        print("\n\tString length can be determined using the len() function.")
        print("\n\t──────────────────────────────────────────────────────")
        print("\tInput:")
        print("\t\ttext = 'Hello, World!'")
        print("\t\tlength = len(text)")
        print("\t\tprint(length)")
        print("\t──────────────────────────────────────────────────────")
        print("\tOutput:")
        print("\t\t13")
        print("\t──────────────────────────────────────────────────────")

        print("\t▶ Data Types and Length Sample Program")
        print("\t──────────────────────────────────────────────────────")
        print("\t[1] Get The Length of Your Name")
        print("\t[2] Get The Data Types of An Input")
        print("\t[0] Back")
        print("\t──────────────────────────────────────────────────────")

        choice = input("\n\tEnter your choice: ")
        if choice == "1":
            clear()
            print("\t──────────────────────────────────────────────────────")
            print("\t▶ Get The Length of Your Name")
            print("\t──────────────────────────────────────────────────────")
            name = input("\tEnter your name: ")
            print(f"\tLength of your name is: {len(name)}")
            print("\n\t──────────────────────────────────────────────────────")
            input("\n\tPress Enter to continue...")
        elif choice == "2":
            clear()
            print("\t──────────────────────────────────────────────────────")
            print("\t▶ Get The Data Types of An Input")
            print("\t──────────────────────────────────────────────────────")
            value = eval(input("\tEnter any value: "))
            print(f"\tData type is: {type(value)}")
            print("\n\t──────────────────────────────────────────────────────")
            input("\n\tPress Enter to continue...")
        elif choice == "0":
            break
        else:
            print("\n\tInvalid choice!")

def string_concatenation():
    print("\n\t──────────────────────────────────────────────────────")
    print("\t▶ String Concatenation")
    print("\t──────────────────────────────────────────────────────")
    print("\n\tString concatenation means add strings together. Use")
    print("\tthe + character to add a variable to another variable: ")
    print("\n\t──────────────────────────────────────────────────────")
    print("\tInput:")
    print("\t\ta = 'Hello'")
    print("\t\tb = 'World'")
    print("\t\tx = 5")
    print("\t\ty = 10")
    print("\t\tc = a + b")
    print("\t\tprint(x + y)")
    print("\t\tprint(c)")
    print("\t──────────────────────────────────────────────────────")
    print("\tOutput:")
    print("\t\tHello World")
    print("\t\t15")
    print("\t──────────────────────────────────────────────────────")

#VARIABLES MENU
def menu_variables(name):
    while True:
        clear()
        print("\t+" + "-" * 68 + "+")
        print("\t|" + f"  Hello, {name}!".center(68) + "|")
        print("\t|" + "  Welcome to Variables".center(68) + "|")
        print("\t+" + "-" * 68 + "+")

        print("\n\t\tVariables are used to store data that can be referenced")
        print("\t\tand manipulated during program execution. A variable is")
        print("\t\tessentially a name that is assigned to a value.")
        print("\n\t\t──────────────────────────────────────────────────────")
        print("\t\t▶ VARIABLES MENU")
        print("\t\t──────────────────────────────────────────────────────")
        print("\t\t[1] Using Input with Variables")
        print("\t\t[2] Data Types and String Length")
        print("\t\t[3] String Concatenation")
        print("\t\t[0] Back to Main Menu")
        print("\t\t──────────────────────────────────────────────────────")
        
        choice = input("\n\t\tEnter your choice: ").strip()

        if choice == "1":
            clear()
            input_with_variables()
            input("\n\tPress Enter to continue...")
        elif choice == "2":
            clear()
            data_types_length()
            input("\n\tPress Enter to continue...")
        elif choice == "3":
            clear()
            string_concatenation()
            input("\n\tPress Enter to continue...")
        elif choice == "0":
            break
        else:
            print("\n\t Invalid choice.")
            time.sleep(1)

#OPERATORS SUBMENUS FUNCTIONS
def arithmetic_operators():
    while True:
        clear()  
        print("\n\t──────────────────────────────────────────────────────")
        print("\t▶ Arithmetic Operators")
        print("\t──────────────────────────────────────────────────────")
        print("\n\tArithmetic operators are used to perform mathematical")
        print("\toperations such as addition, subtraction,")
        print("\tmultiplication, and division.")
        print("\n\t──────────────────────────────────────────────────────")
        print("\tCommon arithmetic operators include:")
        print("\t\t+ : Addition")
        print("\t\t- : Subtraction")
        print("\t\t* : Multiplication")
        print("\t\t/ : Division")
        print("\t\t% : Modulus (Remainder)")
        print("\t\t** : Exponentiation")
        print("\t\t// : Floor Division")
        print("\t──────────────────────────────────────────────────────")
        print("\tInput:")
        print("\t\ta = 10")
        print("\t\tb = 3")
        print("\t\tprint('Addition:', a + b)")
        print("\t\tprint('Subtraction:', a - b)")
        print("\t\tprint('Multiplication:', a * b)")
        print("\t\tprint('Division:', a / b)")
        print("\t\tprint('Modulus:', a % b)")
        print("\t\tprint('Exponentiation:', a ** b)")
        print("\t\tprint('Floor Division:', a // b)")
        print("\t──────────────────────────────────────────────────────")
        print("\tOutput:")
        print("\t\tAddition: 13")
        print("\t\tSubtraction: 7")
        print("\t\tMultiplication: 30")
        print("\t\tDivision: 3.3333333333333335")
        print("\t\tModulus: 1")
        print("\t\tExponentiation: 1000")
        print("\t\tFloor Division: 3")
        print("\t──────────────────────────────────────────────────────")

        print("\t▶ Arithmetic Operators Sample Program")
        print("\t──────────────────────────────────────────────────────")
        print("\t[1] Simple Calculator")
        print("\t[2] Cash Breakdown System")
        print("\t[0] Back")
        print("\t──────────────────────────────────────────────────────")

        choice = input("\n\tEnter your choice: ")

        if choice == "1":
            clear()
            print("\t──────────────────────────────────────────────────────")
            print("\t▶ Simple Calculator")
            print("\t──────────────────────────────────────────────────────")
            number = eval(input("\tEnter first number: "))
            number_1 = eval(input("\tEnter second number: "))

            print("\n\tThe sum of the two numbers is", number + number_1)
            print("\tThe difference of the two numbers is", number - number_1)
            print("\tThe product of the two numbers is", number * number_1)
            print("\tThe quotient of the two numbers is", number / number_1)
            print("\tThe floor division of the two numbers is", number // number_1)
            print("\tThe modulus of the two numbers is", number % number_1)
            print("\n\t──────────────────────────────────────────────────────")
            input("\n\tPress Enter to continue...")

        elif choice == "2":
            clear()
            print("\t──────────────────────────────────────────────────────")
            print("\t▶ Cash Breakdown System")
            print("\t──────────────────────────────────────────────────────")
            money = int(input("\tEnter amount to deposit: "))

            blue = money // 1000
            money %= 1000
            yellow = money // 500
            money %= 500
            green = money // 200
            money %= 200
            violet = money // 100
            money %= 100
            red = money // 50
            money %= 50
            twenty = money // 20
            money %= 20
            ten = money // 10
            money %= 10
            five = money // 5
            money %= 5
            one = money

            print("\n\tHere is the breakdown of the amount you deposited:")
            print("\t1000:", blue)
            print("\t500:", yellow)
            print("\t200:", green)
            print("\t100:", violet)
            print("\t50:", red)
            print("\t20:", twenty)
            print("\t10:", ten)
            print("\t5:", five)
            print("\t1:", one)
            print("\n\t──────────────────────────────────────────────────────")
            input("\n\tPress Enter to continue...")

        elif choice == "0":
            break
        else:
            print("\n\tInvalid choice!")
            input("\n\tPress Enter to continue...")


def assignment_operators():
    clear()
    print("\n\t──────────────────────────────────────────────────────")
    print("\t▶ Assignment Operators")       
    print("\t──────────────────────────────────────────────────────")
    print("\n\tAssignment operators are used to assign values to")
    print("\tvariables. The most common assignment operator is the")
    print("\t= operator, which assigns the value on the right to")
    print("\tthe variable on the left.")
    print("\n\t──────────────────────────────────────────────────────")
    print("\tCommon assignment operators include:")
    print("\t= : Assigns a value to a variable")
    print("\t+= : Adds a value to a variable and assigns the result")
    print("\t-= : Subtracts a value from a variable and assigns the result")
    print("\t*= : Multiplies a variable by a value and assigns the result")
    print("\t/= : Divides a variable by a value and assigns the result")
    print("\t──────────────────────────────────────────────────────")
    print("\tInput:")
    print("\t\ta = 5")
    print("\t\tprint('The value of a is', a)")
    print("\t\ta += 5")
    print("\t\tprint('The value of a is', a)")
    print("\t\ta += 3")
    print("\t\ta += 13")
    print("\t\ta -= 4")
    print("\t\ta *= 2")
    print("\t\ta = a + 6")
    print("\t\tprint('The value of a is', a)")
    print("\t──────────────────────────────────────────────────────")
    print("\tOutput:")
    print("\t\tThe value of a is 5")
    print("\t\tThe value of a is 10")
    print("\t\tThe value of a is 38")
    print("\t──────────────────────────────────────────────────────")

def comparison_operators():
    clear()
    print("\n\t──────────────────────────────────────────────────────")
    print("\t▶ Comparison Operators")
    print("\t──────────────────────────────────────────────────────")
    print("\n\tComparison operators are used to compare two values")
    print("\tand return a boolean result (True or False).")
    print("\n\t──────────────────────────────────────────────────────")
    print("\tCommon comparison operators include:")
    print("\t\t== : Equal to")
    print("\t\t!= : Not equal to")
    print("\t\t> : Greater than")
    print("\t\t< : Less than")
    print("\t\t>= : Greater than or equal to")
    print("\t\t<= : Less than or equal to")
    print("\t──────────────────────────────────────────────────────")
    print("\tInput:")
    print("\t\ta = 10")
    print("\t\tb = 5")
    print("\t\tprint('a == b:', a == b)")
    print("\t\tprint('a != b:', a != b)")
    print("\t\tprint('a > b:', a > b)")
    print("\t\tprint('a < b:', a < b)")
    print("\t\tprint('a >= b:', a >= b)")
    print("\t\tprint('a <= b:', a <= b)")
    print("\t──────────────────────────────────────────────────────")
    print("\tOutput:")
    print("\t\ta == b: False")
    print("\t\ta != b: True")
    print("\t\ta > b: True")
    print("\t\ta < b: False")
    print("\t\ta >= b: True")
    print("\t\ta <= b: False")
    print("\t──────────────────────────────────────────────────────")

#OPERATORS MENU
def menu_operators(name):
    while True:
        clear()
        print("\t+" + "-" * 68 + "+")
        print("\t|" + f"  Hello, {name}!".center(68) + "|")
        print("\t|" + "  Welcome to Operators".center(68) + "|")
        print("\t+" + "-" * 68 + "+")

        print("\n\t\tOperators are special symbols or keywords used to ")
        print("\t\tperform computations on variables and values.")
        print("\t\tSpecial symbols like:-, + , * , /, etc. ")
        print("\n\t\t──────────────────────────────────────────────────────")
        print("\t\t▶ OPEARATORS MENU")
        print("\t\t──────────────────────────────────────────────────────")
        print("\t\t[1] Arithmetic Operators")
        print("\t\t[2] Assignment Operators")
        print("\t\t[3] Comparison Operators")
        print("\t\t[0] Back to Main Menu")
        print("\t\t──────────────────────────────────────────────────────")
        
        choice = input("\n\t\tEnter your choice: ").strip()

        if choice == "1":
            clear()
            arithmetic_operators()
            input("\n\tPress Enter to continue...")
        elif choice == "2":
            clear()
            assignment_operators()
            input("\n\tPress Enter to continue...")
        elif choice == "3":
            clear()
            comparison_operators()
            input("\n\tPress Enter to continue...")
        elif choice == "0":
            break
        else:
            print("\n Invalid choice.")
            time.sleep(1)

#Conditionals SUBMENUS FUNCTIONS
def if_else_statements():
    while True:
        clear()
        print("\n\t──────────────────────────────────────────────────────")
        print("\t▶ If-Else Statements")
        print("\t──────────────────────────────────────────────────────")
        print("\n\tIf-Else statements are used to execute a block of code")
        print("\tif a specified condition is True. If the condition is")
        print("\tFalse, the code block under else is executed.")
        print("\n\t──────────────────────────────────────────────────────")
        print("\tInput:")
        print("\t\ta = 10")
        print("\t\tb = 5")
        print("\t\tif a > b:")
        print("\t\t\tprint('a is greater than b')")
        print("\t\telse:")
        print("\t\t\tprint('a is not greater than b')")
        print("\t──────────────────────────────────────────────────────")
        print("\tOutput:")
        print("\t\ta is greater than b")
        print("\t──────────────────────────────────────────────────────")

        print("\t▶ If-Else Sample Program")
        print("\t──────────────────────────────────────────────────────")
        print("\t[1] Voting Eligibility Program")
        print("\t[2] Student Fare Discount Calculator")
        print("\t[0] Back")
        print("\t──────────────────────────────────────────────────────")

        choice = input("\n\tEnter your choice: ")
        if choice == "1":
            clear()
            print("\t──────────────────────────────────────────────────────")
            print("\t▶ Voting Eligibility Program")
            print("\t──────────────────────────────────────────────────────")
            age = int(input("\tEnter your age: "))
            if age >= 18:
                print("\n\tResult: You are eligible to vote.")
            else:
                print("\n\tResult: You are NOT eligible to vote.")
            print("\n\t──────────────────────────────────────────────────────")
            input("\n\tPress Enter to continue...")

        elif choice == "2":
            clear()
            print("\t──────────────────────────────────────────────────────")
            print("\t▶ Student Fare Discount Calculator")
            print("\t──────────────────────────────────────────────────────")
            name = input("\tEnter your name: ")
            fee = eval(input("\tHow much is your fare fee? "))
            status = input("\tAre you a student or not? ")

            if status.lower() == "student":
                discount = fee * 0.2
                discountedfare = fee - discount
                print(f"\n\tHello {name}, You have a discount of {discount}. Your new fare is {discountedfare}.")
            else:
                print("\n\tSorry, you don't get a discount, your fare fee is the same.")

            print("\n\t──────────────────────────────────────────────────────")
            input("\n\tPress Enter to continue...")

        elif choice == "0":
            break
        else:
            print("\n\tInvalid choice!")
            input("\n\tPress Enter to continue...")


def if_elif_else_statements():
    while True:
        clear()
        print("\n\t──────────────────────────────────────────────────────")
        print("\t▶ If-Elif-Else Statements")
        print("\t──────────────────────────────────────────────────────")
        print("\n\tIf-Elif-Else statements are used to check multiple")
        print("\tconditions. The first condition that evaluates to True")
        print("\texecutes its corresponding code block.")
        print("\n\t──────────────────────────────────────────────────────")
        print("\tInput:")
        print("\t\tscore = 85")
        print("\t\tif score >= 90:")
        print("\t\t\tprint('Grade: A')")
        print("\t\telif score >= 80:")
        print("\t\t\tprint('Grade: B')")
        print("\t\telse:")
        print("\t\t\tprint('Grade: C or below')")
        print("\t──────────────────────────────────────────────────────")
        print("\tOutput:")
        print("\t\tGrade: B")
        print("\t──────────────────────────────────────────────────────")

        print("\t▶ If-Elif-Else Sample Program")
        print("\t──────────────────────────────────────────────────────")
        print("\t[1] BMI Category Checker")
        print("\t[0] Back")
        print("\t──────────────────────────────────────────────────────")

        choice = input("\n\tEnter your choice: ")

        if choice == "1":
            clear()
            print("\t──────────────────────────────────────────────────────")
            print("\t▶ BMI Category Checker")
            print("\t──────────────────────────────────────────────────────")
            weight = float(input("\tEnter your weight (kg): "))
            height = float(input("\tEnter your height (meters): "))
            bmi = weight / (height ** 2)

            print(f"\n\tYour BMI is: {bmi:.2f}")

            if bmi < 18.5:
                print("\tCategory: Underweight")
            elif bmi < 25:
                print("\tCategory: Normal weight")
            elif bmi < 30:
                print("\tCategory: Overweight")
            else:
                print("\tCategory: Obese")

            print("\n\t────────────────────────────────────────────────")
            input("\n\tPress Enter to continue...")

        elif choice == "0":
            break
        else:
            print("\n\tInvalid choice!")
            input("\n\tPress Enter to continue...")


def nested_conditions():
    while True:
        clear()
        print("\n\t──────────────────────────────────────────────────────")
        print("\t▶ Nested Conditions")
        print("\t──────────────────────────────────────────────────────")
        print("\n\tNested conditions are if, elif, or else blocks placed")
        print("\tinside other conditional statements. They allow you to ")
        print("\tcheck secondary conditions only after an initial")
        print("\tcondition has been met. ")
        print("\n\t──────────────────────────────────────────────────────")
        print("\tInput:")
        print("\t\tnumber = 15")
        print("\t\tif number > 0:")
        print("\t\t\tif number % 2 == 0:")
        print("\t\t\t\tprint('Positive Even Number')")
        print("\t\t\telse:")
        print("\t\t\t\tprint('Positive Odd Number')")
        print("\t\telse:")
        print("\t\t\tprint('Negative Number')")
        print("\t──────────────────────────────────────────────────────")
        print("\tOutput:")
        print("\t\tPositive Odd Number")
        print("\t──────────────────────────────────────────────────────")

        print("\t▶ Nested Conditions Sample Program")
        print("\t──────────────────────────────────────────────────────")
        print("\t[1] Manga Recommender Program")
        print("\t[0] Back")
        print("\t──────────────────────────────────────────────────────")

        choice = input("\n\tEnter your choice: ")

        if choice == "1":
            clear()
            print("\t──────────────────────────────────────────────────────")
            print("\t▶ Manga Recommender Program")
            print("\t──────────────────────────────────────────────────────")

            print("\tWelcome to the Manga Reader Recommender!")
            print("\tAnswer a few questions to find your next read.")
            genre = input("\tWhat genre do you prefer? (Action, Romance, Sports) ")
            length = input("\tHow should the manga be? (short, medium, long) ")
            year = input("\tWhich decade? (2000s or 2010s)")

            if genre.lower() == "action":
                if length.lower() == "short":
                    if year == "2000s":
                        print("\tYou should read:\n\tBlack Cat \n\tPsyren")
                    else:
                        print("\tYou should read:\n\tAkame ga Kill! \n\tSeraph of the End")
                elif length.lower() == "medium":
                    if year == "2000s":
                        print("\tYou should read: \n\tClaymore \n\tHunter x Hunter")
                    else:
                        print("\tYou should read: \n\tDemon Slayer \n\tAttack on Titan \n\tJujutsu Kaisen")
                elif length.lower() == "long":
                    if year == "2000s":
                        print("\tYou should read: \n\tNaruto \n\tBleach \n\tOne Piece")
                else:
                    print("\tYou should read: \n\tMy Hero Academia")

            elif genre.lower() == "romance":
                if length.lower() == "short":
                    if year == "2000s":
                        print("\tYou should read: \n\tI Want to Eat your Pancreas")
                    else:
                        print("\tYou should read: \n\tYour Lie in April")
                elif length.lower() == "medium":
                    if year == "2000s":
                        print("\tYou should read: \n\tKimi ni Todoke")
                    else:
                        print("\tYou should read: \n\tHorimiya")
                elif length.lower() == "long":
                    if year == "2000s":
                        print("\tYou should read: \n\tNana")
                else:
                    print("\tYou should read: \n\tLove is War")

            elif genre.lower() == "sports":
                if length.lower() == "short":
                    if year == "2000s":
                        print("\tYou should read: \n\tAll Rounder Meguru")
                    else:
                        print("\tYou should read: \n\tTeppu")
                elif length.lower() == "medium":
                    if year == "2000s":
                        print("\tYou should read: \n\tSwitch")
                    else:
                        print("\n\tDays")
                elif length.lower() == "long":
                    if year == "2000s":
                        print("\tYou should read: \n\tDiamond no Ace")
                    else:
                        print("\tYou should read: \n\tBlue Lock")
                else:
                    print("\tGenre not recognized. Please try again.")

            print("\n\t────────────────────────────────────────────────")
            input("\n\tPress Enter to continue...")

        elif choice == "0":
            break
        else:
            print("\n\tInvalid choice!")
            input("\n\tPress Enter to continue...")

#CONDITIONALS MENU
def menu_conditionals(name):
    while True:
        clear()
        print("\t+" + "-" * 68 + "+")
        print("\t|" + f"  Hello, {name}!".center(68) + "|")
        print("\t|" + "  Welcome to Conditional Statements".center(68) + "|")
        print("\t+" + "-" * 68 + "+")

        print("\n\t\tConditional statements are used to execute certain")
        print("\t\tblocks of code based on whether a specified condition")
        print("\t\tis True or False.")
        print("\n\t\t──────────────────────────────────────────────────────")
        print("\t\t▶ CONDITIONAL STATEMENTS MENU")
        print("\t\t──────────────────────────────────────────────────────")
        print("\t\t[1] If-Else Statements")
        print("\t\t[2] If-Elif-Else Statements")
        print("\t\t[3] Nested Conditions")
        print("\t\t[0] Back to Main Menu")
        print("\t\t──────────────────────────────────────────────────────")
        
        choice = input("\n\t\tEnter your choice: ").strip()

        if choice == "1":
            clear()
            if_else_statements()
            input("\n\tPress Enter to continue...")
        elif choice == "2":
            clear()
            if_elif_else_statements()
            input("\n\tPress Enter to continue...")
        elif choice == "3":
            clear()
            nested_conditions()
            input("\n\tPress Enter to continue...")
        elif choice == "0":
            break
        else:
            print("\n Invalid choice.")
            time.sleep(1)

#LOOPS SUBMENUS FUNCTIONS
def for_loops():
    while True:    
        clear()
        print("\n\t──────────────────────────────────────────────────────")
        print("\t▶ For Loops")
        print("\t──────────────────────────────────────────────────────")
        print("\n\tA for loop is used for iterating over a sequence (like")
        print("\ta list, tuple, or string) or other iterable objects.")
        print("\n\t──────────────────────────────────────────────────────")
        print("\tInput:")
        print("\t\tfruits = ['apple', 'banana', 'cherry']")
        print("\t\tfor fruit in fruits:")
        print("\t\t\tprint(fruit)")
        print("\t──────────────────────────────────────────────────────")
        print("\tOutput:")
        print("\t\tapple")
        print("\t\tbanana")
        print("\t\tcherry")
        print("\t──────────────────────────────────────────────────────")
    
        print("\t▶ For Loops Sample Program")
        print("\t──────────────────────────────────────────────────────")
        print("\t[1] Factorial Calculator")
        print("\t[2] Multiplication Table Generator")
        print("\t[0] Back")
        print("\t──────────────────────────────────────────────────────")

        choice = input("\n\tEnter your choice: ")
        if choice == "1":
            clear()
            print("\t──────────────────────────────────────────────────────")
            print("\t▶ Factorial Calculator")
            print("\t──────────────────────────────────────────────────────")
            number = int(input("\tEnter a number to calculate its factorial: "))
            factorial = 1
            for i in range(1, number + 1):
                factorial *= i
            print(f"\n\tThe factorial of {number} is {factorial}.")
            print("\n\t──────────────────────────────────────────────────────")
            input("\n\tPress Enter to continue...")
        elif choice == "2":
            clear()
            print("\t──────────────────────────────────────────────────────")
            print("\t▶ Multiplication Table Generator")
            print("\t──────────────────────────────────────────────────────")
            number = int(input("\tEnter a number to generate its multiplication table: "))
            print(f"\n\tMultiplication Table for {number}:")
            for i in range(1, 11):
                print(f"\t{number} x {i} = {number * i}")
            print("\n\t──────────────────────────────────────────────────────")
            input("\n\tPress Enter to continue...")
        elif choice == "0":
            break
        else:
            print("\n\tInvalid choice!")
            input("\n\tPress Enter to continue...")

def nested_loops():
    while True:
        clear()
        print("\n\t──────────────────────────────────────────────────────")
        print("\t▶ Nested For Loops")
        print("\t──────────────────────────────────────────────────────")
        print("\n\tNested loops are loops within loops. The inner loop")
        print("\tis executed for each iteration of the outer loop.")
        print("\n\t──────────────────────────────────────────────────────")
        print("\tInput:")
        print("\t\tadj = ['red', 'big', 'tasty']")
        print("\t\tfruits = ['apple', 'banana', 'cherry']") 
        print("\t\tfor x in adj:")
        print("\t\t\tfor y in fruits:")
        print("\t\t\t\tprint(x, y)")
        print("\t──────────────────────────────────────────────────────")
        print("\tOutput:")
        print("\t\tred apple")
        print("\t\tred banana")
        print("\t\tred cherry")
        print("\t\tbig apple")
        print("\t\tbig banana")
        print("\t\tbig cherry")
        print("\t\ttasty apple")
        print("\t\ttasty banana")
        print("\t\ttasty cherry")
        print("\t──────────────────────────────────────────────────────")
        print("\t▶ Nested For Loops Sample Program")
        print("\t──────────────────────────────────────────────────────")
        print("\t[1] Make a Triangle")
        print("\t[2] Make a Simple Christmas Tree")
        print("\t[0] Back")
        print("\t──────────────────────────────────────────────────────")

        choice = input("\n\tEnter your choice: ")
        if choice == "1":
            clear()
            print("\t──────────────────────────────────────────────────────")
            print("\t▶ Make a Triangle")
            print("\t──────────────────────────────────────────────────────")
            print("\tHere is a Triangle made using For Loops:\n")
            print("\t\t\t\t *", end="")
            for i in range(1, 11, 1):
                print("\t\t", end="")  
                for x in range(10, i, -1):
                    print(" ", end=" ")
                for y in range(1, i, 1):
                    print("*", end=" ")
                for z in range(1, i, 1):
                    print("*", end=" ")
                print()
            print("\n\t──────────────────────────────────────────────────────")
            input("\n\tPress Enter to continue...")
        elif choice == "2":
            clear()
            print("\t──────────────────────────────────────────────────────")
            print("\t▶ Make a Simple Christmas Tree")
            print("\t──────────────────────────────────────────────────────")
            print("\tHere is a Simple Christmas Tree made using nested For Loops:\n")
            layers = 3        
            rows_per_layer = 5  

            for layer in range(layers):
                for i in range(1, rows_per_layer + layer + 1):  
                    print("\t\t", end="") 

                    for x in range(rows_per_layer + layers - i):
                        print(" ", end=" ")
                    for y in range(1, i):
                        print("*", end=" ")
                    for z in range(1, i + 1):
                        print("*", end=" ")
                    print()

            trunk_height = 5
            trunk_width = 5
            for i in range(trunk_height):
                print("\t\t", end="")  
                for j in range(rows_per_layer + layers - 2):
                    print(" ", end=" ")
                print("|" * trunk_width)

            print("\n\t──────────────────────────────────────────────────────")
            input("\n\tPress Enter to continue...")
        elif choice == "0":
            break
        else:
            print("\n\tInvalid choice!")
            input("\n\tPress Enter to continue...") 

def while_loops():
    while True:
        clear()
        print("\n\t──────────────────────────────────────────────────────")
        print("\t▶ While Loops")
        print("\t──────────────────────────────────────────────────────")
        print("\n\tA while loop repeatedly executes a block of code as")
        print("\tlong as a specified condition is True.")
        print("\n\t──────────────────────────────────────────────────────")
        print("\tInput:")
        print("\t\ti = 1")
        print("\t\twhile i <= 5:")
        print("\t\t\tprint(i)")
        print("\t\t\ti += 1")
        print("\t──────────────────────────────────────────────────────")
        print("\tOutput:")
        print("\t\t1")
        print("\t\t2")
        print("\t\t3")
        print("\t\t4")
        print("\t\t5")
        print("\t──────────────────────────────────────────────────────")

        print("\t▶ While Loops Sample Program")
        print("\t──────────────────────────────────────────────────────")
        print("\t[1] Number Guessing Game")
        print("\t[0] Back")
        print("\t──────────────────────────────────────────────────────")

        choice = input("\n\tEnter your choice: ")
        if choice == "1":
            clear()
            print("\t──────────────────────────────────────────────────────")
            print("\t▶ Number Guessing Game")
            print("\t──────────────────────────────────────────────────────")
            print("\tRandom Guessing Game")
            print("\t+++++++++++++++++++++++++++++++++++++++++++++++++++++++")

            random_value= random.randint(1,5)
            tries = 0
            Tuloy=True

            name= input("\tInput your name: ")

            while Tuloy == True:
                num= eval(input("\tGuess a number from 1 to 5:"))
                tries +=1
                if num == random_value:
                    print("\tJackpot!!!")
                    break
                else:
                    print("\tSad, try again")
                    continue

            print(f"\tHi {name}, Your Guess is Correct, Number of Tries: {tries}")
            print("\n\t──────────────────────────────────────────────────────")
            input("\n\tPress Enter to continue...")
        elif choice == "0":
            break
        else:
            print("\n\tInvalid choice!")
            input("\n\tPress Enter to continue...")

#LOOPS MENU
def menu_loops(name):
    while True:
        clear()
        print("\t+" + "-" * 68 + "+")
        print("\t|" + f"  Hello, {name}!".center(68) + "|")
        print("\t|" + "  Welcome to Loops".center(68) + "|")
        print("\t+" + "-" * 68 + "+")

        print("\n\t\tLoops are used to execute a block of code repeatedly")
        print("\t\tuntil a certain condition is met.") 
        print("\n\t\t──────────────────────────────────────────────────────")
        print("\t\t▶ LOOPS MENU")   
        print("\t\t──────────────────────────────────────────────────────")
        print("\t\t[1] For Loops")
        print("\t\t[2] Nested For Loops")
        print("\t\t[3] While Loops")
        print("\t\t[0] Back to Main Menu") 
        print("\t\t──────────────────────────────────────────────────────")
        
        choice = input("\n\t\tEnter your choice: ").strip()

        if choice == "1":
            clear()
            for_loops()
            input("\n\tPress Enter to continue...")
        elif choice == "2":
            clear()
            nested_loops()
            input("\n\tPress Enter to continue...")
        elif choice == "3":
            clear()
            while_loops()
            input("\n\tPress Enter to continue...")
        elif choice == "0":
            break
        else:
            print("\n Invalid choice.")
            time.sleep(1)

#LISTS SUBMENUS FUNCTIONS
def access_list_items():
    while True:
        clear()
        print("\n\t──────────────────────────────────────────────────────")
        print("\t▶ Accessing List Items")
        print("\t──────────────────────────────────────────────────────")
        print("\n\tElements in a list are accessed using indexing. Python")
        print("\tindexes start at 0, so a[0] gives the first element. ")
        print("\tNegative indexes allow access from the end (e.g., -1 ")
        print("\tgives the last element).")
        print("\n\t──────────────────────────────────────────────────────")
        print("\tInput:")
        print("\t\tprog_lang = ['Python', 'Perl', 'C++', 'Java']")
        print("\t\tprint(prog_lang[0])  # Accessing the first item")
        print("\t\tprint(prog_lang[2])  # Accessing the third item")
        print("\t\tprint(prog_lang[-1]) # Accessing the last item")
        print("\t──────────────────────────────────────────────────────")
        print("\tOutput:")
        print("\t\tPython")
        print("\t\tC++")
        print("\t\tJava")
        print("\t──────────────────────────────────────────────────────")

        print("\t▶ Accessing List Items Sample Program")
        print("\t──────────────────────────────────────────────────────")
        print("\t[1] Favorite Desserts List Accessor")
        print("\t[0] Back")
        print("\t──────────────────────────────────────────────────────")

        choice = input("\n\tEnter your choice: ")
        if choice == "1":
            clear()
            print("\t──────────────────────────────────────────────────────")
            print("\t▶ Favorite Desserts List Accessor")
            print("\t──────────────────────────────────────────────────────")
            desserts = ['ice cream', 'mango graham', 'halo-halo', 'buko-salad']
            print("\t['ice cream', 'mango graham', 'halo-halo', 'buko-salad']")
            index = int(input("\tEnter the index of the dessert you want to access (0-4):"))
            if 0 <= index < len(desserts):
                print(f"\n\tThe dessert at index {index} is {desserts[index]}.")
            else:
                print("\n\tInvalid index! Please enter a number between 0 and 4.")
            print("\n\t──────────────────────────────────────────────────────")
            input("\n\tPress Enter to continue...")
        elif choice == "0":
            break
        else:
            print("\n\tInvalid choice!")
            input("\n\tPress Enter to continue...")

def slicing_list():
        clear()
        print("\n\t──────────────────────────────────────────────────────")
        print("\t▶ Slicing of a List in Python")
        print("\t──────────────────────────────────────────────────────")
        print("\n\tSlicing allows you to create a new list by extracting")
        print("\ta specific portion of an existing list using index")
        print("\tranges. The syntax is list [start:end], where start is")
        print("\tinclusive and end is exclusive.")
        print("\n\t──────────────────────────────────────────────────────")
        print("\tInput:")
        print("\t  prog_lang = ['Python', 'Perl', 'C++', 'Java', 'Ruby']")
        print("\t  print(prog_lang[1:4])  # Slicing from index 1 to 3")
        print("\t  print(prog_lang[:3])   # Slicing from start to index 2")
        print("\t  print(prog_lang[2:])   # Slicing from index 2 to end")
        print("\t──────────────────────────────────────────────────────")
        print("\tOutput:")
        print("\t\t['Perl', 'C++', 'Java']")
        print("\t\t['Python', 'Perl', 'C++']")
        print("\t\t['C++', 'Java', 'Ruby']")
        print("\t──────────────────────────────────────────────────────")

def adding_items_list():
    while True:
        clear()
        print("\n\t──────────────────────────────────────────────────────")
        print("\t▶ Adding Items to a List")
        print("\t──────────────────────────────────────────────────────")
        print("\n\tYou can add items to a list using methods like append(),")
        print("\textend(), and insert(). append() adds an item to the end,")
        print("\textend() adds multiple items, and insert() adds an item at")
        print("\ta specified index.")
        print("\n\t──────────────────────────────────────────────────────")
        print("\tInput:")
        print("\t\tprog_lang = ['Python', 'Perl']")
        print("\t\tprog_lang.append('C++') # Adding single item")
        print("\t\tprint(prog_lang)")
        print("\t\tprog_lang.extend(['Java', 'Ruby']) # Adding multiple items")
        print("\t\tprint(prog_lang)")
        print("\t\tprog_lang.insert(1, 'JavaScript') # Inserting at index 1")
        print("\t\tprint(prog_lang)")
        print("\t──────────────────────────────────────────────────────")
        print("\tOutput:")
        print("\t\t['Python', 'Perl', 'C++']")
        print("\t\t['Python', 'Perl', 'C++', 'Java', 'Ruby']")
        print("\t\t['Python', 'JavaScript', 'Perl', 'C++', 'Java', 'Ruby']")    
        print("\t──────────────────────────────────────────────────────")

        print("\t▶ Adding Items to a List Sample Program")
        print("\t──────────────────────────────────────────────────────")
        print("\t[1] My Anime Watchlist Program")
        print("\t[0] Back")
        print("\t──────────────────────────────────────────────────────")

        choice = input("\n\tEnter your choice: ")
        if choice == "1":
            clear()
            print("\t──────────────────────────────────────────────────────")
            print("\t▶ My Anime Watchlist Program")
            print("\t──────────────────────────────────────────────────────")

            anime_list = []
            while True:
                anime = input("\tEnter the title of an anime (or type 'exit' to finish): ")

                if anime.lower() == 'exit':
                    break

                anime_list.append(anime)
                print(f"'\t{anime}' has been added to your anime list.")

            print("\tYou have exited the anime entry program.")
            print("\tYour anime list includes:")
            for alist in anime_list:
                print("\t-", alist)
            print("\n\t──────────────────────────────────────────────────────")
            input("\n\tPress Enter to continue...")
        elif choice == "0":
            break
        else:
            print("\n\tInvalid choice!")
            input("\n\tPress Enter to continue...")

def remove_items_list():
        clear()
        print("\n\t──────────────────────────────────────────────────────")
        print("\t▶ Remove Items from a List")
        print("\t──────────────────────────────────────────────────────")
        print("\n\tYou can remove items from a list using methods like ")
        print("\tremove(), pop(), and del. remove() deletes the first ")
        print("\tmatching value, pop() removes an item at a specified ")
        print("\tindex (or the last item if no index is specified), and")
        print("\tdel deletes an item at a specific index or the entire list.")
        print("\n\t──────────────────────────────────────────────────────")
        print("\tInput:")
        print("\t\tprog_lang = ['Python', 'Perl', 'C++', 'Java']")
        print("\t\tprog_lang.remove('Perl') # Removing by value")
        print("\t\tprint(prog_lang)")
        print("\t\tprog_lang.pop(1) # Removing by index")
        print("\t\tprint(prog_lang)")
        print("\t\tdel prog_lang[0] # Deleting by index")
        print("\t\tprint(prog_lang)")
        print("\t──────────────────────────────────────────────────────")
        print("\tOutput:")
        print("\t\t['Python', 'C++', 'Java']")
        print("\t\t['Python', 'Java']")
        print("\t\t['Java']")
        print("\t──────────────────────────────────────────────────────")
        input("\n\tPress Enter to continue...")
      

#LISTS MENU
def menu_list(name):
    while True:
        clear()
        print("\t+" + "-" * 68 + "+")
        print("\t|" + f"  Hello, {name}!".center(68) + "|")
        print("\t|" + "  Welcome to Lists".center(68) + "|")
        print("\t+" + "-" * 68 + "+")

        print("\n\t\tLists are used to store multiple items in a single")
        print("\t\tvariable. Lists are ordered, changeable, and allow") 
        print("\t\tduplicate values. Lists are created using square ")
        print("\t\tbrackets [].")
        print("\n\t\t──────────────────────────────────────────────────────")
        print("\t\tInput:")
        print("\t\t\tprog_lang = ['Python', 'Perl', 'C++', 'Java']")
        print("\t\t\tprint(prog_lang)")   
        print("\t\t──────────────────────────────────────────────────────")
        print("\t\tOutput:")
        print("\t\t\t['Python', 'Perl', 'C++', 'Java']")
        print("\t\t──────────────────────────────────────────────────────")                                                          
        print("\t\t▶ LISTS MENU")   
        print("\t\t──────────────────────────────────────────────────────")
        print("\t\t[1] Accessing List Items")
        print("\t\t[2] Slicing of a List in Python")
        print("\t\t[3] Adding Items from a List")
        print("\t\t[4] Remove Items from a List")
        print("\t\t[0] Back to Main Menu")
        print("\t\t──────────────────────────────────────────────────────")

        
        choice = input("\n\t\tEnter your choice: ").strip()

        if choice == "1":
            clear()
            access_list_items()
            input("\n\tPress Enter to continue...")
        elif choice == "2":
            clear()
            slicing_list()
            input("\n\tPress Enter to continue...")
        elif choice == "3":
            clear()
            adding_items_list()
            input("\n\tPress Enter to continue...")
        elif choice == "4":
            clear()
            remove_items_list()
            input("\n\tPress Enter to continue...")
        elif choice == "0":
            break
        else:
            print("\n Invalid choice.")
            time.sleep(1)


#FUNCTIONS SUBMENUS FUNCTIONS

#FUNCTIONS MENU
def menu_functions(name):
        clear()
        print("\t+" + "-" * 68 + "+")
        print("\t|" + f"  Hello, {name}!".center(68) + "|")
        print("\t|" + "  Welcome to Functions".center(68) + "|")
        print("\t+" + "-" * 68 + "+")

        print("\n\t\tFunctions are of code which only runs when it is ")
        print("\t\tcalled. A function is defined using the def keyword, ")
        print("\t\tfollowed by the function name and parentheses ().")
        print("\n\t\t──────────────────────────────────────────────────────")
        print("\t\tInput:")
        print("\t\t\tdef greet(name):")
        print("\t\t\t\tprint('Hello, ' + name + '!')")          
        print("\t\tgreet('Ron') # Calling the function")
        print("\t\t──────────────────────────────────────────────────────")
        print("\t\tOutput:")
        print("\t\t\tHello, Ron!")
        print("\t\t──────────────────────────────────────────────────────")
        print("\t\t▶ Return Values")
        print("\t\t──────────────────────────────────────────────────────")
        print("\n\t\tFunctions can send data back to the code that called ")
        print("\t\tthem using the return statement. When a function reaches")
        print("\t\ta return statement, it stops executing and sends the  ")
        print("\t\tresult back: ")
        print("\n\t\t──────────────────────────────────────────────────────")
        print("\t\tInput:")
        print("\t\t\tdef add(a, b):")
        print("\t\t\t\treturn a + b")   
        print("\n\t\tresult = add(3, 5) # Calling the function and storing the return value")
        print("\t\t──────────────────────────────────────────────────────")
        print("\t\tOutput:")
        print("\t\t\t8")
        print("\t\t──────────────────────────────────────────────────────")
        input("\n\t\tPress Enter to continue...")
 


#DICTIONARIES SUBMENUS FUNCTIONS
def dictionary_sample_program():
    while True:
        clear()
        print("\n\t──────────────────────────────────────────────────────")
        print("\t▶ Dictionary Sample Program")
        print("\t──────────────────────────────────────────────────────")
        print("\tDLL Student Information System")
        print("\t================================")
        stud_record = {}

        while True:
            print("\tSELECT FROM THE FOLLOWING OPTIONS")
            print("\tA - ADDING STUDENT RECORD")
            print("\tB - PRINT ALL RECORD")
            print("\tC - SEARCH STUDENT")
            print("\tD - DELETE STUDENT RECORD")
            print("\tE - EDIT STUDENT RECORD")
            print("\tF - EXPORT DATA")
            print("\tG - IMPORT SYSTEM")
            print("\tX - EXIT SYSTEM")
            choice = input("\tInput your choice: ").lower().strip()

            if choice == 'a':
                os.system('cls')
                print("\tADD STUDENT RECORD")

                student_id = input("\tInput Student ID number:")
                first_name = input("\tInput student First Name:").upper()
                last_name = input("\tInput student Last Name:").upper()
                course = input("\tInput student Course:").upper()
                section = input("\tInput student Section:").upper()
                email = input("\tInput student Email:")

                stud_record[student_id] = [first_name, last_name, course, section, email]
                print("\tDATA SAVED SUCCESFULLY")
                continue

            elif choice == 'b':
                os.system('cls')
                print("\tPRINTING STUDENT RECORD")
                print("\t============================================")

                for id, info in stud_record.items():
                    print(f"\tSTUDENT ID {id} - RECORD {info}")
                continue

            elif choice == 'c':
                os.system('cls')
                print("\tSEARCH STUDENT RECORD")

                search_id = input("\tINPUT STUDENT ID:")

                for each_student in stud_record.keys():
                    if search_id in stud_record.keys():
                        print("\n\n\tRECORD FOUND")
                        print("\t===============================================")
                        for id in stud_record[search_id]:
                            print(f"\t-- {id} ")
                        print("\t===============================================")
                    else:
                        print("\tNO RECORD FOUND")
                    break
                continue

            elif choice == 'd':
                os.system('cls')
                print("\tDELETE STUDENT RECORD")

                search_id = input("\tINPUT STUDENT ID:")

                for each_student in stud_record.keys():
                    if search_id in stud_record.keys():
                        print(f"\n\n\tRECORD FOUND for {search_id}")
                        print("\t===============================================")
                        for id in stud_record[search_id]:
                            print(f"\t-- {id} ")
                        print("\t===============================================")
                        stud_record.pop(search_id)
                        print("\tRECORD DELETED")
                    else:
                        print("\tNO RECORD FOUND")
                    break
                continue

            elif choice == 'e':
                os.system('cls')
                print("\tEDIT/MODIFY STUDENT RECORD")

                search_id = input("\tINPUT STUDENT ID:")

                for each_student in stud_record.keys():
                    if search_id in stud_record.keys():
                        print("\n\n\tRECORD FOUND")
                        print("\t===============================================")
                        for id in stud_record[search_id]:
                            print(f"\t-- {id} ")
                        print("\t===============================================")

                        first_name = input("\tInput NEW student First Name:").upper()
                        last_name = input("\tInput NEW student Last Name:").upper()
                        course = input("\tInput NEW student Course:").upper()
                        section = input("\tInput NEW student Section:").upper()
                        email = input("\tInput NEW student Email:")

                        stud_record[search_id][0] = first_name
                        stud_record[search_id][1] = last_name
                        stud_record[search_id][2] = course
                        stud_record[search_id][3] = section
                        stud_record[search_id][4] = email
                        print("\tDATA UPDATED SUCCESFULLY")
                    else:
                        print("\tNO RECORD FOUND")
                    break
                continue

            elif choice == 'f':
                print("\tEXPORT DATA")
                with open('student_record.json', 'w') as new_file:
                    json.dump(stud_record, new_file, indent=4)
                print("\tDATA EXPORTED SUCCESSFULLY")
                continue

            elif choice == 'g':
                print("\tIMPORT DATA")
                with open('student_record.json', 'r') as new_file:
                    imported_student = json.load(new_file)
                stud_record = imported_student
                print("\tDATA IMPORTED SUCCESSFULLY")
                continue

            elif choice == 'x':
                print("\tSystem Exit")
                break

            else:
                print("Invalid Choice, Re-enter Code")
    input("\n\tPress Enter to continue...")  

#DICTIONARIES MENU
def menu_dictionaries(name):
    while True:
        clear()
        print("\t+" + "-" * 68 + "+")
        print("\t|" + f"  Hello, {name}!".center(68) + "|")
        print("\t|" + "  Welcome to Dictionaries".center(68) + "|")
        print("\t+" + "-" * 68 + "+")

        print("\n\t\tDictionaries are used to store data values in key:value")
        print("\t\tpairs. A dictionary is ordered, changeable, and does not")
        print("\t\tallow duplicate keys. Dictionaries are created using ")
        print("\t\tcurly brackets {}.")
        print("\n\t\t──────────────────────────────────────────────────────")
        print("\t\tInput:")
        print("\t\t\tstudent = {'name': 'Alice', 'age': 21, 'course': 'CS'}")
        print("\t\t\tprint(student)")   
        print("\t\t──────────────────────────────────────────────────────")
        print("\t\tOutput:")
        print("\t\t\t{'name': 'Alice', 'age': 21, 'course': 'CS'}")
        print("\t\t──────────────────────────────────────────────────────")      
        print("\t\t▶ DICTIONARIES MENU")
        print("\t\t──────────────────────────────────────────────────────")
        print("\t\t[1] Dictionary Sample Program")
        print("\t\t[0] Back to Main Menu")
        print("\t\t──────────────────────────────────────────────────────")

        choice = input("\n\t\tEnter your choice: ").strip()
        if choice == "1":
            clear()
            dictionary_sample_program()
            input("\n\tPress Enter to continue...")
        elif choice == "0":
            break
        else:
            print("\n Invalid choice.")
            time.sleep(1)                                                    
    
#MAIN MENU        
def main_menu(name):
    while True:
        clear()
        print("+" + "-" * 68 + "+")
        print("|" + f"Welcome to PyMenu - User: {name}".center(68) + "|")
        print("+" + "-" * 68 + "+")
        print("\n   ▶ MAIN MENU")
        print("   ────────────────────────────────────────────────")
        print("   [1] Print Statements")
        print("   [2] Variables")
        print("   [3] Operators")
        print("   [4] Conditional Statements")
        print("   [5] Loops")
        print("   [6] Lists")
        print("   [7] Functions")
        print("   [8] Dictionaries")
        print("   [0] Exit Program")
        print("   ────────────────────────────────────────────────")

        choice = input("\n   Enter your choice: ").strip()
        
        if choice == "1":
            menu_print_statements(name)        
        elif choice == "2":
            menu_variables(name)
        elif choice == "3":
            menu_operators(name)
        elif choice == "4":
            menu_conditionals(name)
        elif choice == "5":
            menu_loops(name)
        elif choice == "6":
            menu_list(name)
        elif choice == "7":
            menu_functions(name)
        elif choice == "8":
            menu_dictionaries(name)
        elif choice == "0":
            clear()
            print("\n")
            print("=" * 60)
            print(f"  Thank you for using PyMenu, {name}!".center(60))
            print("  Goodbye!".center(60))
            print("=" * 60)
            print("\n")
            break  
        else:
            print("\n  Invalid choice. Please try again.")
            time.sleep(1.5)

#TO START PROGRAM/CALL THE FUNCTION
user = welcome_screen()
main_menu(user)
