from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width = 20, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)
#e.insert(0, "")

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    if '.' in first_number:
        f_num = float(first_number)
    else:
        f_num = int(first_number)
    e.delete(0, END)

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    if '.' in first_number:
        f_num = float(first_number)
    else:
        f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication" 
    if '.' in first_number:
        f_num = float(first_number)
    else:
        f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division" 
    if '.' in first_number:
        f_num = float(first_number)
    else:
        f_num = int(first_number)
    e.delete(0, END)

def button_perc():
    first_number = e.get()
    e.delete(0, END)
    e.insert(0, int(first_number)/100.0)

def button_backSpace():
    current = e.get()
    new = current[:-1]
    e.delete(0, END)
    e.insert(0, new)

def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if '.' in second_number:
        s_num = float(second_number)
    else:
        s_num = int(second_number)

    if math == "addition":
        e.insert(0, f_num + s_num)

    elif math == "subtraction":
        e.insert(0, f_num - s_num)

    elif math == "multiplication":
        e.insert(0, f_num * s_num)

    elif math == "division":
        e.insert(0, f_num / s_num)




# Define Buttons

button_1 = Button(root, text = "1", width=1, padx=40, pady=20, command = lambda: button_click(1))
button_2 = Button(root, text = "2", width=1, padx=40, pady=20, command = lambda: button_click(2))
button_3 = Button(root, text = "3", width=1, padx=40, pady=20, command = lambda: button_click(3))
button_4 = Button(root, text = "4", width=1, padx=40, pady=20, command = lambda: button_click(4))
button_5 = Button(root, text = "5", width=1, padx=40, pady=20, command = lambda: button_click(5))
button_6 = Button(root, text = "6", width=1, padx=40, pady=20, command = lambda: button_click(6))
button_7 = Button(root, text = "7", width=1, padx=40, pady=20, command = lambda: button_click(7))
button_8 = Button(root, text = "8", width=1, padx=40, pady=20, command = lambda: button_click(8))
button_9 = Button(root, text = "9", width=1, padx=40, pady=20, command = lambda: button_click(9))
button_0 = Button(root, text = "0", width=1, padx=40, pady=20, command = lambda: button_click(0))
button_backSpace = Button(root, text = "C", width=1, padx=40, pady=20, command = button_backSpace)
button_clear = Button(root, text = "AC", padx=34, pady=20, command = button_clear)

button_add = Button(root, text = "+", width=1, padx=40, pady=20, command = button_add)
button_equal = Button(root, text = "=", width=1, padx=40, pady=20, command = button_equal)
button_perc = Button(root, text = "%", width=1, padx=40, pady=20, command = button_perc)

button_subtract = Button(root, text = "-", width=1, padx=40, pady=20, command = button_subtract)
button_multiply = Button(root, text = "*", width=1, padx=40, pady=20, command = button_multiply)
button_divide = Button(root, text = "/", width=1, padx=40, pady=20, command = button_divide)


# Put the buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_backSpace.grid(row=4, column=2)

button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1)
button_perc.grid(row=5, column=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)


root.mainloop()