import os
os.system('cls')
import json

print("DLL Student Information System")
print("================================")

stud_record= {}

while True:

    print("SELECT FROM THE FOLLOWING OPTIONS")
    print("A - ADDING STUDENT RECORD")
    print("B - PRINT ALL RECORD")
    print("C - SEARCH STUDENT")
    print("D - DELETE STUDENT RECORD")
    print("E - EDIT STUDENT RECORD")
    print("F - EXPORT DATA")
    print("G - IMPORT SYSTEM")
    print("X - EXIT SYSTEM")
    choice = input("Input your choice: ").lower().strip()

    if choice == 'a':
        os.system('cls')
        print("ADD STUDENT RECORD")

        student_id= input("Input Student ID number:")
        first_name = input("Input student First Name:").upper()
        last_name = input("Input student Last Name:").upper()
        course= input("Input student Course:").upper()
        section= input("Input student Section:").upper()
        email= input("Input student Email:")

        stud_record[student_id]= [first_name, last_name, course, section, email]
        print("DATA SAVED SUCCESFULLY")
        
        continue
    elif choice == 'b':
        os.system('cls') 

        print("PRINTING STUDENT RECORD")
        print("============================================")

        for id, info in stud_record.items():
            print(f"STUDENT ID {id} - RECORD {info}")
    
        continue
    elif choice == 'c':
        os.system('cls') 
        print("SEARCH STUDENT RECORD")

        search_id= input("INPUT STUDENT ID:").lower()

        for each_student in stud_record.keys():
            if search_id in stud_record.keys():
                print("\n\nRECORD FOUND")
                print(" ===============================================")
                for id in stud_record[search_id]:
                    print(f"-- {id} ")
                    break
                print(" ===============================================")
            else:
                print("NO RECORD FOUND")
            break
        continue
    elif choice == 'd':
        os.system('cls') 
        print("DELETE STUDENT RECORD")

        search_id= input("INPUT STUDENT ID:").lower()

        for each_student in stud_record.keys():
            if search_id in stud_record.keys():
                print(f"\n\nRECORD FOUND for {search_id}")
                print(" ===============================================")
                for id in stud_record[search_id]:
                    print(f"-- {id} ")

                print(" ===============================================")

                stud_record.pop(search_id)
                print("RECORD DELETED")
            else:
                print("NO RECORD FOUND")
            break
        continue
    elif choice == 'e':
        os.system('cls') 
        print("EDIT/MODIFY STUDENT RECORD")

        search_id= input("INPUT STUDENT ID:").lower()

        for each_student in stud_record.keys():
            if search_id in stud_record.keys():
                print("\n\nRECORD FOUND")
                print(" ===============================================")
                for id in stud_record[search_id]:
                    print(f"-- {id} ")
            
                print(" ===============================================")

               
                first_name = input("Input NEW student First Name:").upper()
                last_name = input("Input NEW student Last Name:").upper()
                course= input("Input NEW student Course:").upper()
                section= input("Input NEW student Section:").upper()
                email= input("Input NEW student Email:")

                stud_record[search_id][0]= first_name
                stud_record[search_id][1]= last_name
                stud_record[search_id][2]= course
                stud_record[search_id][3]= section
                stud_record[search_id][4]= email
                print("DATA UPDATED SUCCESFULLY")

            else:
                print("NO RECORD FOUND")
            break
        continue    
    elif choice == 'f':
        print("EXPORT DATA")

        with open('student_record.json', 'w') as new_file:
            json.dump(stud_record, new_file, indent=4)

        print("DATA EXPORTED SUCCESSFULLY")
        continue
    elif choice == 'g':
        print("IMPORT DATA")
    
        with open('student_record.json','r') as new_file:
            imported_student= json.load(new_file)

        stud_record = imported_student
        print("DATA IMPORTED SUCCESSFULLY")
        continue
    elif choice == 'x':
        print("System Exit")
        break
    else:
        print("Invalid Choice, Re-enter Code")