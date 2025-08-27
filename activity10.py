from getpass import getpass

username = 'RonTzy'
password = 'password01'

u= input("USERNAME: ")
p= getpass("PASSWORD: ")

if u == username and p == password :
	print("Access Granted")
else:
	print("Access Denied")
	