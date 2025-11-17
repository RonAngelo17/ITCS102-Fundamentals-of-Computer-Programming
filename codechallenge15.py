import os
os.system('cls')
print("DLL Student Information System")
print("================================")

stud_record= {}

while True:
    os.system('cls')
    print("SELECT FROM THE FOLLOWING OPTIONS")
    print("A - ADDING STUDENT RECORD")
    print("B - SEARCH STUDENT")
    print("C - EDIT STUDENT RECORD")
    print("D - DELETE STUDENT RECORD")
    print("E - PRINT ALL RECORD")
    print("F - EXPORT DATA")
    print("G - EXIT SYSTEM")

    choice = input("Input your choice: ").lower().strip()

    if choice == 'a':
        print("ADD STUDENT RECORD")

        student_id= input("Input Student ID number")
        first_name = input("Input student First Nmae")
        last_name = input("Input student Last Name")
    if choice == 'b':
        pass
        continue
    if choice == 'c':
        pass
        continue
    if choice == 'd':
        pass
        continue
    if choice == 'e':
        pass
        continue
    if choice == 'f':
        pass
        continue
    if choice == 'g':
        print("System Exit")
        continue
    else:
        print("Invalid Choice, Re-enter Code")