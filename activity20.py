IfDirty=True

while IfDirty==True:
    wash_again= input("Continue washing the cloethes (yes/no) : ")

    if wash_again.lower() == "yes":
        print("Washing the clothes again...")
        continue
    else:
        print("Washing stops now...")
        break
        IfDirty==False

