from tkinter import *

def display(window:Tk, number:float = 0):
    display = Frame(window, padx= 50, pady=25).grid(column=0, row=0)
    Label(display, text=number, justify="right").grid(column=0, row=0)