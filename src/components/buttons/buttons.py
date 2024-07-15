from tkinter import *
from ...utils import adicionaValores

def buttons(window:Tk):
    buttons = Frame(window, padx=50).grid(column=0, row=1)
    porcentagemButton = Button(
        buttons, 
        text="%", 
        justify="center", 
        padx=5, 
        pady=5, 
        command=lambda: adicionaValores(window, porcentagemButton)
    )
    porcentagemButton.grid(column=0, row=2)

    deletAllButton = Button(
        buttons, 
        text="CE", 
        justify="center", 
        padx=5, pady=5, 
        command=lambda: adicionaValores(window, deletAllButton)
    )
    deletAllButton.grid(column=1, row=2)

    deletCurrentNumberButton = Button(
        buttons, 
        text="C", 
        justify="center", 
        padx=5, 
        pady=5, 
        command=lambda: adicionaValores(window, deletCurrentNumberButton)
    )
    deletCurrentNumberButton.grid(column=2, row=2)

    deletButton = Button(
        buttons, 
        text="⊲", 
        justify="center", 
        padx=5, pady=5, 
        command=lambda: adicionaValores(window, deletButton)
    )
    deletButton.grid(column=3, row=2)

    fractionButton = Button(
        buttons, 
        text="1/x", 
        justify="center", 
        padx=5, 
        pady=5, 
        command=lambda: adicionaValores(window, fractionButton)
    )
    fractionButton.grid(column=0, row=3)

    numberPowerTwoButton = Button(
        buttons, 
        text="x^2", 
        justify="center", 
        padx=5, pady=5, 
        command=lambda: adicionaValores(window, numberPowerTwoButton)
    )
    numberPowerTwoButton.grid(column=1, row=3)

    squareRootButton = Button(
        buttons, 
        text="√x", 
        justify="center", 
        padx=5, 
        pady=5, 
        command=lambda: adicionaValores(window, squareRootButton)
    )
    squareRootButton.grid(column=2, row=3)

    divideButton = Button(
        buttons, 
        text="÷", 
        justify="center", 
        padx=5, 
        pady=5, 
        command=lambda: adicionaValores(window, divideButton)
    )
    divideButton.grid(column=3, row=3)
    numberNine = Button(
        buttons, 
        text="9", 
        justify="center", 
        padx=5, 
        pady=5, 
        command=lambda: adicionaValores(window, numberNine)
    )
    numberNine.grid(column=0, row=4)