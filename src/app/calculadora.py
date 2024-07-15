from ..components import buttons, displayNumbers
from tkinter import Tk

def calculadora(window: Tk):
    displayNumbers.displayNumbers(window)
    buttons.buttons(window)
    window.update()