print("Welcome to the Manga Reader Recommender!")
print("Answer a few questions to find your next read.")

genre=input("What genre do you prefer? (Action, Romance, Sports) ")
length = input("How should the manga be? (short, medium, long) ")
year = input("Which decade? (2000s or 2010s)")

if genre.lower() == "action":
    if length.lower() == "short":
        if year == "2000s":
            print("You should read:\nBlack Cat \nPsyren")
        else:
            print("You should read:\nAkame ga Kill! \nSeraph of the End")
    elif length.lower() == "medium":
        if year == "2000s":
            print("You should read: \nClaymore \nHunter x Hunter")
        else:
            print("You should read: \nDemon Slayer \nAttack on Titan \nJujutsu Kaisen")
    elif length.lower() == "long":
        if year == "2000s":
            print("You should read: \nNaruto \nBleach \nOne Piece")
        else:
            print("You should read: \nMy Hero Academia")

elif genre.lower() == "romance":
    if length.lower() == "short":
        if year == "2000s":
            print("You should read: \nI Want to Eat your Pancreas")
        else:
            print("You should read: \nYour Lie in April")
    elif length.lower() == "medium":
        if year == "2000s":
            print("You should read: \nKimi ni Todoke")
        else:
            print("You should read: \nHorimiya")
    elif length.lower() == "long":
        if year == "2000s":
            print("You should read: \nNana")
        else:
            print("You should read: \nLove is War") 

elif genre.lower() == "sports":
    if length.lower() == "short":
        if year == "2000s":
            print("You should read: \nAll Rounder Meguru")
        else:
            print("You should read: \nTeppu")
    elif length.lower() == "medium":
        if year == "2000s":
            print("You should read: \nSwitch")
        else:
            print("\nDays")
    elif length.lower() == "long":
        if year == "2000s":
            print("You should read: \nDiamond no Ace")
        else:
            print("You should read: \nBlue Lock")   



