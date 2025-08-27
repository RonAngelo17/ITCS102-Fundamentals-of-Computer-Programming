name = input("Enter your name: ")
fee = eval(input("How much is your fare fee? "))
status = input("Are you a student or not? ")

if status.lower() == "student":
	discount = fee * 0.2
	discountedfare = fee - discount
	print("Hello", name , "You have a discount of", discount , "Your new fare is", discountedfare)
else:
	print("Sorry, you don't get a discount, your fee fare is the same. ")