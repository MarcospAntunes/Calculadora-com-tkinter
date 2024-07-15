from tkinter import *
from ..components import displayNumbers

def adicionaValores(window: Tk, button: Button):
    text = button.cget("text")
    try:
        number = int(text)
        displayNumbers.displayNumbers(window, number)
    except:
        print(text)