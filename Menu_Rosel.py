import time, sys
import os

#function to clear
def clear():
    os.system("cls")

#wELCOME SCREEN
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
        time.sleep(0.7)

    print("\nSystem Status: Ready")
    time.sleep(0.5)

    # Small loading bar 
    print("\nStarting Program:")
    for i in range(21):
        bar = "█" * i + "-" * (20 - i)
        sys.stdout.write(f"\r[{bar}] {int((i/20)*100)}%")
        sys.stdout.flush()
        time.sleep(0.1)
        
    clear()
    print("\nSystem Startup Complete.\n")
    time.sleep(0.8)
    
    # Getting the user's name
    print("\n")
    name = input("Please enter your name: ").strip().title()
    clear()
    return name

#PRINT STATEMENT SUBMENUS FUNCTIONS
def simple_printing():
    print("\n\t────────────────────────────────────────────────")
    print("\t▶ Simple Printing")
    print("\t────────────────────────────────────────────────")
    print("\tInput:")
    print("\t\tprint('Hello, World!')")
    print("\t\tprint('Python')")
    print("\t\tprint('Merry Christmas')")
    print("\t────────────────────────────────────────────────")
    print("\tOutput:")
    print("\t\tHello, World!")
    print("\t\tPython")
    print("\t\tMerry Christmas")
    print("\t────────────────────────────────────────────────")

def printing_variables():
    print("\n\t────────────────────────────────────────────────")
    print("\t▶ Printing Variables")
    print("\t────────────────────────────────────────────────")
    print("\tInput:")
    print("\t\tname = 'Ron Angelo'")
    print("\t\tage = 18")
    print("\t\tcourse = 'BSIT'")
    print("\t\tprint(name)")
    print("\t\tprint('Age:', age)")
    print("\t\tprint('Course:', course)")
    print("\t────────────────────────────────────────────────")
    print("\tOutput:")
    print("\t\tRon Angelo")
    print("\t\tAge: 18")
    print("\t\tCourse: BSIT")
    print("\t────────────────────────────────────────────────")

def formatted_string():
    print("\n\t────────────────────────────────────────────────")
    print("\t▶ Printing Formatted String")
    print("\t────────────────────────────────────────────────")
    print("\n\tF-string allows you to format selected parts of a")
    print("\tstring.To specify a string as an f-string, simply ")
    print("\tput an f in front of the string literal, like this:")
    print("\n\t────────────────────────────────────────────────")
    print("\t────────────────────────────────────────────────")
    print("\tExample:")
    print("\t\tname = 'Ron Angelo'")
    print('\t\ttext =(f"My name is {name}"')
    print("\t\tprint(text)")
    print("\t────────────────────────────────────────────────")
    print("\tOutput:")
    print("\t\tMy name is Ron Angelo")
    print("\t────────────────────────────────────────────────")

def escape_characters():
    print("\n\t────────────────────────────────────────────────")
    print("\t▶ Python Escape Characters")
    print("\t────────────────────────────────────────────────")
    print("\tEscape characters are used when we need to include")
    print("\tspecial characters in a string that are otherwise ")
    print("\thard (or illegal) to type directly.")
    print("\tCommon escape sequences:")
    print("\t────────────────────────────────────────────────")
    print("\t\t\\n  - New line")
    print("\t\t\\t  - Tab")
    print("\t\t\\\"  - Double quote")
    print("\t\t\\\\  - Backslash")
    print("\t────────────────────────────────────────────────")
    print("\tInput:")
    print("\t\t\\nHello World")
    print("\t\t\\tHello World")
    print("\t\t\\\"Hello World ")
    print("\t\t\\\\Hello World")
    print("\t────────────────────────────────────────────────")
    print("\tOuput:")
    print("\n\t\tHello World")
    print("\t\t\tHello World")
    print("\t\t\"Hello World")
    print("\t\t\\\Hello World")
    print("\t────────────────────────────────────────────────")
    print("\n")

    while True:
        print("\n\t────────────────────────────────────────────────")
        print("\t▶ Escape Characters Sample Program")
        print("\t────────────────────────────────────────────────")
        print("\t[1] Creating Diamond")
        print("\t[0] Go Back")
        print("\t────────────────────────────────────────────────")
        
        choice_1= input("\n  Enter your choice: ").strip()
        if choice_1 == "1":
            name = input("\t\tType your name ---> ")
            print("\t\t\t\t\t* \n\n\t\t\t\t* \t\t* \n\n\t\t\t* \t\t\t\t* \n\n\t\t* \t\t\tHi! \t\t\t* \n\n\t* \t\t\t\t\t",name,"\t\t\t* \n\n\t\t* \t\t\t\t\t\t* \n\n\t\t\t* \t\t\t\t* \n\n\t\t\t\t* \t\t* \n\n\t\t\t\t\t*")
        elif choice_1 == "0":
            break       
        else:
            print("\n Invalid choice.")
        

#PRINT STATEMENTS MENU
def menu_print_statements(name):
    clear()
    print("+" + "-" * 68 + "+")
    print("|" + f"  Hello, {name}!".center(68) + "|")
    print("|" + "  Welcome to Print Statements".center(68) + "|")
    print("+" + "-" * 68 + "+")

    print("\n\tPrinting in Python is the process of displaying text,")
    print("\tvariables, or results on the screen using the print()")
    print("\tfunction.")

    while True:
        print("\n\t────────────────────────────────────────────────")
        print("\t▶ PRINT STATEMENTS MENU")
        print("\t────────────────────────────────────────────────")
        print("\t[1] Simple Printing")
        print("\t[2] Printing Variables")
        print("\t[3] Printing Formatted String")
        print("\t[4] Python Escape Characters")
        print("\t[0] Back to Main Menu")
        print("\t────────────────────────────────────────────────")
        
        choice = input("\n  Enter your choice: ").strip()
        
        if choice == "1":
            simple_printing()
        elif choice == "2":
            printing_variables()
        elif choice == "3":
            formatted_string()
        elif choice == "4":
            escape_characters()
        elif choice == "0":
            clear()
            break
        else:
            print("\n Invalid choice.")
            time.sleep(1)

#VARIABLE SUBMENUS FUNCTIONS
def input_with_variables():
    print("\n\t────────────────────────────────────────────────")
    print("\t▶ Using Input with Variables")
    print("\t────────────────────────────────────────────────")
    print("\n\tThe input() function is used to get data from a")
    print("\tuser during program execution. The program pauses")
    print("\tuntil the user types something and presses the")
    print("\tEnter key.")
    print("\n\t────────────────────────────────────────────────")
    print("\tInput:")
    print("\t\ta = 'Hello'")
    print("\t\tb = 'World'")
    print("\t\tc = a + b")
    print("\t\tprint(c)")
    print("\t────────────────────────────────────────────────")
    print("\tOutput:")
    print("\t\tHello World")
    print("\t────────────────────────────────────────────────")

    while True:
        print("\n\t────────────────────────────────────────────────")
        print("\t▶ Using Input With Variable Sample Program")
        print("\t────────────────────────────────────────────────")
        print("\t[1] Get Your Name and Greet You")
        print("\t[0] Go Back")
        print("\t────────────────────────────────────────────────")
        
        choice_1= input("\n  Enter your choice: ").strip()
        if choice_1 == "1":
            name=input("\t\tWhat is your name? ")
            print("\t\tHi!",name, "Welcome to the matrix")
        elif choice_1 == "0":
            break       
        else:
            print("\n Invalid choice.")
    
def data_types_length():
    print("\n\t────────────────────────────────────────────────")
    print("\t▶ Data Types and String Length")
    print("\t────────────────────────────────────────────────")
    print("\tVariables can store data of different types, and")
    print("\tdifferent types can do different things.")
    print("\n\t────────────────────────────────────────────────")
    print("\tCommon data types include:")
    print("\t- int: Any Positive or Negative Integer numbers")
    print("\t- float: Real numbers with a Decimal point")
    print("\t- str: Textual Data")
    print("\t- bool: Boolean values (True or False)")
    print("\t────────────────────────────────────────────────")
    print("\n\tString length can be determined using the len()")
    print("\tfunction, which returns the number of characters")
    print("\tin a string.")
    print("\n\t────────────────────────────────────────────────")
    print("\tInput:")
    print("\t\ttext = 'Hello, World!'")
    print("\t\tlength = len(text)")
    print("\t\tprint(length)")
    print("\t────────────────────────────────────────────────")
    print("\tOutput:")
    print("\t\t13")
    print("\t────────────────────────────────────────────────")

    while True:
        print("\n\t────────────────────────────────────────────────")
        print("\t▶ Data Types and Lengths Sample Program")
        print("\t────────────────────────────────────────────────")
        print("\t[1] Get The Length of Your Name")
        print("\t[2] Get The Data Types of An Input")
        print("\t[0] Go Back")
        print("\t────────────────────────────────────────────────")
        
        choice= input("\n  Enter your choice: ").strip()
        if choice == "1":
            name=input("\t\tType your name ---> ")
            print("\t\tWelcome my friend", name)
            print("\t\tYour name has", len(name), "characters.")    
        elif choice == "2":
            any=eval(input("\t\tInput anything ---> "))
            print("\t\tThe data type of that is", type(any))
        elif choice == "0":
            break       
        else:
            print("\n Invalid choice.")


def string_concatenation():
    print("\n\t────────────────────────────────────────────────")
    print("\t▶ String Concatenation")
    print("\t────────────────────────────────────────────────")
    print("\n\tString concatenation means add strings together.")
    print("\tUse the + character to add a variable to another ")
    print("\tvariable:")
    print("\n\t────────────────────────────────────────────────")
    print("\tInput:")
    print("\t\ta = 'Hello'")
    print("\t\tb = 'World'")
    print("\t\tx = 5")
    print("\t\ty = 10'")
    print("\t\tc = a + b")
    print("\t\tprint(x + y)")
    print("\t\tprint(c)")
    print("\t────────────────────────────────────────────────")
    print("\tOutput:")
    print("\t\tHello World")
    print("\t\t15")
    print("\t────────────────────────────────────────────────")

        



#VARIABLES MENU
def menu_variables(name):
    clear()
    print("+" + "-" * 68 + "+")
    print("|" + f"  Hello, {name}!".center(68) + "|")
    print("|" + "  Welcome to Variables".center(68) + "|")
    print("+" + "-" * 68 + "+")

    print("\n\tVariables are used to store data that can be referenced")
    print("\tand manipulated during program execution. A variable")
    print("\tis essentially a name that is assigned to a value.")

    while True:
        print("\n\t────────────────────────────────────────────────")
        print("\t▶ VARIABLES MENU")
        print("\t────────────────────────────────────────────────")
        print("\t[1] Using Input with Variables")
        print("\t[2] Data Types and String Length")
        print("\t[3] String Concatenation")
        print("\t[0] Back to Main Menu")
        print("\t────────────────────────────────────────────────")
        
        choice = input("\n  Enter your choice: ").strip()

        if choice == "1":
            input_with_variables()
        elif choice == "2":
            data_types_length()
        elif choice == "3":
            string_concatenation()
        elif choice == "0":
            clear()
            break
        else:
            print("\n Invalid choice.")
            time.sleep(1)

#OPERATORS SUBMENUS FUNCTIONS
def arithmetic_operators():
    print("\n\t────────────────────────────────────────────────")
    print("\t▶ Arithmetic Operators")
    print("\t────────────────────────────────────────────────")
    print("\n\tArithmetic operators are used to perform mathematical")
    print("\toperations such as addition, subtraction, multiplication,")
    print("\tand division.")
    print("\n\t────────────────────────────────────────────────")
    print("\tCommon arithmetic operators include:")
    print("\t- + : Addition")
    print("\t- - : Subtraction")
    print("\t- * : Multiplication")
    print("\t- / : Division")
    print("\t- % : Modulus (Remainder)")
    print("\t- ** : Exponentiation")
    print("\t- // : Floor Division")
    print("\t────────────────────────────────────────────────")
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
    print("\t────────────────────────────────────────────────")
    print("\tOutput:")
    print("\t\tAddition: 13")
    print("\t\tSubtraction: 7")
    print("\t\tMultiplication: 30")
    print("\t\tDivision: 3.3333333333333335")
    print("\t\tModulus: 1")
    print("\t\tExponentiation: 1000")
    print("\t\tFloor Division: 3")
    print("\t────────────────────────────────────────────────")


    

#OPERATORS MENU
def menu_operators(name):
    clear()
    print("+" + "-" * 68 + "+")
    print("|" + f"  Hello, {name}!".center(68) + "|")
    print("|" + "  Welcome to Operators".center(68) + "|")
    print("+" + "-" * 68 + "+")

    print("\n\tOperators in general are used to perform operations on ")
    print("\tvalues and variables. Special symbols like -, + , * , /, etc.")

    while True:
        print("\n\t────────────────────────────────────────────────")
        print("\t▶ OPEARATORS MENU")
        print("\t────────────────────────────────────────────────")
        print("\t[1] Arithmetic Operators")
        print("\t[2] Assignment Operators")
        print("\t[3] Comparison Operators")
        print("\t[0] Back to Main Menu")
        print("\t────────────────────────────────────────────────")
        
        choice = input("\n  Enter your choice: ").strip()

        if choice == "1":
            arithmetic_operators()
        elif choice == "2":
            assignment_operators()
   



        








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
        print("   [4] Conditionals")
        print("   [5] Functions")
        print("   [6] Loops")
        print("   [7] Lists")
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
            clear()
            print("\n Conditionals menu - Coming soon!")
            time.sleep(1.5)
        elif choice == "5":
            clear()
            print("\n Functions menu - Coming soon!")
            time.sleep(1.5)    
        elif choice == "6":
            clear()
            print("\n  Loops menu - Coming soon!")
            time.sleep(1.5) 
        elif choice == "7":
            clear()
            print("\n  Lists menu - Coming soon!")
            time.sleep(1.5)  
        elif choice == "8":
            clear()
            print("\n Dictionaries menu - Coming soon!")
            time.sleep(1.5) 
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
