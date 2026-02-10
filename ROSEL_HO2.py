import tkinter as ron

window = ron.Tk()
window.title("My Profile")
window.geometry("600x600")
window.resizable(False, True)
window.configure(bg="blue")

title_label = ron.Label(window, text="Student Profile", font=("Helvetica", 24, "bold"), bg="blue")
title_label.pack(pady=20)

name_label = ron.Label(window, text="Name : Ron Angelo H. Rosel", font=("Helvetica", 16), bg="blue")
name_label.pack(anchor="w", padx=30)

age_label = ron.Label(window, text="Age : 18 years old", font=("Helvetica", 16), bg="blue")
age_label.pack(anchor="w", padx=30, pady=5)

course_label = ron.Label(window, text="Course and Section : BSIT", font=("Helvetica", 16), bg="blue")
course_label.pack(anchor="w", padx=30, pady=5)

birthday_label = ron.Label(window, text="Birthday : February 17, 2007", font=("Helvetica", 16), bg="blue")
birthday_label.pack(anchor="w", padx=30, pady=5)

motto_label = ron.Label(window, text="Motto :", font=("Helvetica", 16), bg="blue")
motto_label.pack(anchor="w", padx=30, pady=10)

quote_label = ron.Label(window, text="Love the life you live, live the life you love", font=("Helvetica", 16, "italic"), bg="blue")
quote_label.pack(anchor="w", padx=50)

window.mainloop()
