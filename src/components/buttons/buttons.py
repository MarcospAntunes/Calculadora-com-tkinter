from tkinter import *
from ...utils import adicionaValores

def buttons(window:Tk):
    buttonsProps = [
    { "text": "%", "column": 0, "row": 2 },
    { "text": "CE", "column": 1, "row": 2 },
    { "text": "C", "column": 2, "row": 2 },
    { "text": "⊲", "column": 3, "row": 2 },
    { "text": "1/x", "column": 0, "row": 3 },
    { "text": "x^2", "column": 1, "row": 3 },
    { "text": "√x", "column": 2, "row": 3 },
    { "text": "÷", "column": 3, "row": 3 },
    { "text": "7", "column": 0, "row": 4 },
    { "text": "8", "column": 1, "row": 4 },
    { "text": "9", "column": 2, "row": 4 },
    { "text": "x", "column": 3, "row": 4 },
    { "text": "4", "column": 0, "row": 5 },
    { "text": "5", "column": 1, "row": 5 },
    { "text": "6", "column": 2, "row": 5 },
    { "text": "-", "column": 3, "row": 5 },
    { "text": "1", "column": 0, "row": 6 },
    { "text": "2", "column": 1, "row": 6 },
    { "text": "3", "column": 2, "row": 6 },
    { "text": "+", "column": 3, "row": 6 },
    { "text": "+/-", "column": 0, "row": 7 },
    { "text": "0", "column": 1, "row": 7 },
    { "text": ",", "column": 2, "row": 7 },
    { "text": "=", "column": 3, "row": 7 },
]
    buttons = Frame(window)
    buttons.grid(column=0, row=1,sticky=NSEW)

    for buttonProp in buttonsProps:
        currentButton = Button(
            buttons,
            text=buttonProp["text"],
            justify="center",
            width=1,
            height=1,
            command=lambda text=buttonProp["text"]: adicionaValores(window, text)
        )
        currentButton.grid(
            column=buttonProp["column"], 
            row=buttonProp["row"],
            padx=2,
            pady=2,
            sticky=NSEW
        )
    
    for i in range(4):
        buttons.grid_columnconfigure(i, weight=1)
    for i in range(2, 5):
        buttons.grid_rowconfigure(i, weight=1)