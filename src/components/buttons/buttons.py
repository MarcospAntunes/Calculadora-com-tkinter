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
    { "text": "9", "column": 0, "row": 4 },
]
    buttons = Frame(window, padx=50).grid(column=0, row=1)

    for buttonProp in buttonsProps:
        currentButton = Button(
            buttons,
            text=buttonProp["text"],
            justify="center",
            padx=5,
            pady=5,
            command=lambda: adicionaValores(window, currentButton)
        )
        currentButton.grid(
            column=buttonProp["column"], 
            row=buttonProp["row"]
        )