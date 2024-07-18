from tkinter import Tk
from src import *

def main():
    window = Tk()
    window.title("Calculadora")
    window.geometry("200x250")
    window.grid_columnconfigure(0, weight=1)
    window.grid_rowconfigure(1,weight=1)
    calculadora(window)
    window.mainloop()

if __name__ == "__main__":
    main()
