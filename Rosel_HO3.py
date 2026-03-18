import tkinter as ron

window = ron.Tk()
window.title("Simple Calculator")
window.geometry("250x300")
window.configure(bg="#3E8EDE")

frame = ron.Frame(window, bg="#3E8EDE")
frame.grid(row=0)

result_label = ron.Label(frame,
                        text="Simple Calculator",
                        font=("Helvetica", 12, "bold"),
                        bg="white",
                        height=2,
                        bd=1,
                        relief="solid",
                        anchor="center")
result_label.grid(row=0, column=0, columnspan=2, sticky="we")

def add():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    sum = num1 + num2
    result_label.config(text=f"The sum of {num1} + {num2} is {sum}.")

def minus():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    difference = num1 - num2
    result_label.config(text=f"The difference of {num1} - {num2} is {difference}.")

def multiply():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    product = num1 * num2
    result_label.config(text=f"The product of {num1} x {num2} is {product}.")

def divide():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    quotient = num1 / num2
    result_label.config(text=f"The quotient of {num1} ÷ {num2} is {quotient}.")

number1_label = ron.Label(frame,
                        text="Enter 1st Number:",
                        font=("Helvetica", 10, "bold"),
                        bg="white",
                        fg="black")
number1_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

number1_entry = ron.Entry(frame, width=15, bd=2, relief="sunken")
number1_entry.grid(row=1, column=1, padx=5)

number2_label = ron.Label(frame,
                        text="Enter 2nd Number:",
                        font=("Helvetica", 10, "bold"),
                        bg="white",
                        fg="black")
number2_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")

number2_entry = ron.Entry(frame, width=15, bd=2, relief="sunken")
number2_entry.grid(row=2, column=1, padx=5)

add_button = ron.Button(frame,
                        text="Add",
                        font=("Helvetica", 10, "bold"),
                        bg="white",
                        fg="black",
                        command=add,
                        relief="raised")
add_button.grid(row=3, column=0, pady=10)

subtract_button = ron.Button(frame,
                            text="Subtract",
                            font=("Helvetica", 10, "bold"),
                            bg="white",
                            fg="black",
                            command=minus,
                            relief="raised")
subtract_button.grid(row=3, column=1, pady=10)

multiply_button = ron.Button(frame,
                            text="Multiply",
                            font=("Helvetica", 10, "bold"),
                            bg="white",
                            fg="black",
                            command=multiply,
                            relief="raised")
multiply_button.grid(row=4, column=0, pady=10)

division_button = ron.Button(frame,
                            text="Division",
                            font=("Helvetica", 10, "bold"),
                            bg="white",
                            fg="black",
                            command=divide,
                            relief="raised")
division_button.grid(row=4, column=1, pady=10)

window.mainloop()