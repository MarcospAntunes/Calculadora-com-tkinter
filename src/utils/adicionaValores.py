from tkinter import *
from ..components import displayNumbers

def adicionaValores(window: Tk, text: str):
    try:
        number = int(text)
        displayNumbers.displayNumbers(window, number)
    except ValueError:
        print(text)