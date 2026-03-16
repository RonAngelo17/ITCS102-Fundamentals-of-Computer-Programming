import tkinter as tk

window = tk.Tk()
window.geometry("800x300")
window.title("Profile Builder")
window.configure(bg="light green")


profile_builder_label = tk.Label(window, text="Profile Builder", font=("Poppins", 15, "bold"), bg="light green", anchor="center")
profile_builder_label.grid(row=0, column=3)

frame = tk.Frame(window, bg="green", bd=2, relief="groove")
frame.grid(row=1, column=3, padx=20, pady=10, fill="x" )

first_name_entry = tk.Entry(frame, relief="sunken")
first_name_entry.grid(row=0, column=0, columnspan=2,pady=5, padx=5)

middle_name_entry = tk.Entry(frame, relief="sunken")
middle_name_entry.grid(row=0, column=2, columnspan=2,pady=5, padx=5)

last_name_entry = tk.Entry(frame, relief="sunken")
last_name_entry.grid(row=0, column=4, columnspan=2,pady=5, padx=5)

first_name_label= tk.Label(frame, text="First Name", font=("Poppins", 12), bg="green")
first_name_label.grid(row=1, column=0, columnspan=2)

middle_name_label= tk.Label(frame, text="Middle Name", font=("Poppins", 12), bg="green")
middle_name_label.grid(row=1, column=2, columnspan=2)

last_name_label= tk.Label(frame, text="Last Name", font=("Poppins", 12), bg="green")
last_name_label.grid(row=1, column=4, columnspan=2)

birth_year_entry = tk.Entry(frame, relief="sunken")
birth_year_entry.grid(row=2, column=0, padx=5)

birth_year_label = tk.Label(frame, text="Birth Year", font=("Poppins", 12), bg="green")
birth_year_label.grid(row=3, column=0)

gender_label = tk.Label(frame, text="Gender", font=("Poppins", 12), bg="green")
gender_label.grid(row=4, column=0)

submit_button = tk.Button(window, text="Submit", font=("Poppins", 12, "bold"), bg="green")
submit_button.grid(row=3, column=3)


window.mainloop()
