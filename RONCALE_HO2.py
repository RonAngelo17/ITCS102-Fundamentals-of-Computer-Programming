import tkinter as tk

windows = tk.Tk()
windows.title("Windows ni kiroashi")
windows.geometry("600x600")
windows.resizable(False, True)
windows.configure(bg="pink")

title = tk.Label(windows, text="MY PROFILE", font=("Arial", 24, "bold"), bg="pink")
title.pack(pady=30)

name = tk.Label(windows, text="Full Name: Juan Dela Cruz", font=("Arial", 14), bg="pink")
name.pack(pady=5)

age = tk.Label(windows, text="Age: 20", font=("Arial", 14), bg="pink")
age.pack(pady=5)

course = tk.Label(windows, text="Course: BS Computer Science", font=("Arial", 14), bg="pink")
course.pack(pady=5)

bday = tk.Label(windows, text="Birthday: January 1, 2004", font=("Arial", 14), bg="pink")
bday.pack(pady=5)

motto = tk.Label(windows, text='"Code is poetry."', font=("Arial", 14, "italic"), bg="pink")
motto.pack(pady=20)

windows.mainloop()
