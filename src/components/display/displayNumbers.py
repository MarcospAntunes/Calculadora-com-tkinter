from tkinter import *

def displayNumbers(window: Tk, number: float = 0, replaced: bool = False):
    if 'label' not in displayNumbers.__dict__:
        displayNumbers.label = Label(window, justify="right", text=str(number))
        displayNumbers.label.grid(row=0, column=1)
    else:
        current_text = displayNumbers.label.cget("text")
        if current_text == "0":
            displayNumbers.label.config(text=str(number))
        else:
            if replaced or displayNumbers.label.cget("text") == 'Error':
                displayNumbers.label.config(text=str(number))
            else:
                new_text = current_text + str(number)
                displayNumbers.label.config(text=new_text)