from tkinter import *

def buttons(window:Tk):
    buttons = Frame(window, padx=50).grid(column=0, row=1)
    Button(buttons, text="%", justify="center").grid(column=0, row=2)
    Button(buttons, text="CE", justify="center").grid(column=1, row=2)
    Button(buttons, text="C", justify="center").grid(column=2, row=2)
    Button(buttons, text="⊲", justify="center").grid(column=3, row=2)

    Button(buttons, text="1/x", justify="center").grid(column=0, row=3)
    Button(buttons, text="x^2", justify="center").grid(column=1, row=3)
    Button(buttons, text="√2", justify="center").grid(column=2, row=3)
    Button(buttons, text="÷", justify="center").grid(column=3, row=3)