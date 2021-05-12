import tkinter as tk
from tkinter import *
from tkinter import filedialog

root = Tk()
root.iconphoto(False, tk.PhotoImage(file='calc.png'))
root.title("Calculator")
text_Input = StringVar()
multi = False

# Functions

def buttonNum():
    
    return

def buttonAdd():
    return

# I/O Box

txtDisplay = Entry(root, font=("ariel", 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4, bg="powder blue", justify='right')

# Buttons

button_1 = Button(root, padx = 16, bd = 8, fg = "black", font=("ariel", 20, "bold"), text = "1")
button_2 = Button(root, padx = 16, bd = 8, fg = "black", font=("ariel", 20, "bold"), text = "2")
button_3 = Button(root, padx = 16, bd = 8, fg = "black", font=("ariel", 20, "bold"), text = "3")
button_4 = Button(root, padx = 16, bd = 8, fg = "black", font=("ariel", 20, "bold"), text = "4")
button_5 = Button(root, padx = 16, bd = 8, fg = "black", font=("ariel", 20, "bold"), text = "5")
button_6 = Button(root, padx = 16, bd = 8, fg = "black", font=("ariel", 20, "bold"), text = "6")
button_7 = Button(root, padx = 16, bd = 8, fg = "black", font=("ariel", 20, "bold"), text = "7")
button_8 = Button(root, padx = 16, bd = 8, fg = "black", font=("ariel", 20, "bold"), text = "8")
button_9 = Button(root, padx = 16, bd = 8, fg = "black", font=("ariel", 20, "bold"), text = "9")
button_0 = Button(root, padx = 16, bd = 8, fg = "black", font=("ariel", 20, "bold"), text = "0")
button_Add = Button(root, padx = 16, bd = 8, fg = "black", font=("ariel", 20, "bold"), text = "+")
button_Subtr = Button(root, padx = 16, bd = 8, fg = "black", font=("ariel", 20, "bold"), text = "-")
button_Mult = Button(root, padx = 16, bd = 8, fg = "black", font=("ariel", 20, "bold"), text = "*")
button_Div = Button(root, padx = 16, bd = 8, fg = "black", font=("ariel", 20, "bold"), text = "/")
button_Clear = Button(root, padx = 16, bd = 8, fg = "black", font=("ariel", 20, "bold"), text = "C")
button_Solve = Button(root, padx = 16, bd = 8, fg = "black", font=("ariel", 20, "bold"), text = "=")

# Display 

txtDisplay.grid(columnspan = 4)
button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)
button_3.grid(row = 3, column = 2)
button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)
button_7.grid(row = 1, column = 0)
button_8.grid(row = 1, column = 1)
button_9.grid(row = 1, column = 2)
button_0.grid(row = 4, column = 0)
button_Add.grid(row = 1, column = 3)
button_Subtr.grid(row = 2, column = 3)
button_Mult.grid(row = 3, column = 3)
button_Div.grid(row = 4, column = 3)
button_Clear.grid(row = 4, column = 1)
button_Solve.grid(row = 4, column = 2)

root.mainloop()