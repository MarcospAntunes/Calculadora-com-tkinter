from tkinter import *

def displayNumbers(window:Tk, number:float = 0):
    if 'label' not in displayNumbers.__dict__:
        displayNumbers.label = Label(window, text=str(number))
        displayNumbers.label.grid(row=0, column=0)
    else:
        current_text = displayNumbers.label.cget("text")
        if current_text == "0":
            displayNumbers.label.config(text=str(number))
        else:
            new_text = current_text + str(number)
            displayNumbers.label.config(text=new_text)