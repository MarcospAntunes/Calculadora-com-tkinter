from tkinter import *
from ..components import displayNumbers
from .calculate import calculate

def adicionaValores(window: Tk, text: str):
    if text == 'CE':
            displayNumbers.displayNumbers(window, 0, replaced=True)
            return
    elif text == '⊲':
        currentOperation = displayNumbers.displayNumbers.label.cget("text")
        currentOperation = currentOperation[:-1]
        displayNumbers.displayNumbers(window, currentOperation, replaced=True)

        if len(displayNumbers.displayNumbers.label.cget("text")) < 1:
            displayNumbers.displayNumbers(window, 0, replaced=True)
        
        return
    
    if (not displayNumbers.displayNumbers.label.cget("text")[-1].isnumeric()) and (not text.isnumeric()):
        currentText = displayNumbers.displayNumbers.label.cget("text")
        currentText = currentText.replace(displayNumbers.displayNumbers.label.cget("text")[-1], text)
        displayNumbers.displayNumbers(window, currentText, replaced=True)
        return

    if(text.isnumeric()):
        number = int(text)
        displayNumbers.displayNumbers(window, number)
        return
    else:
        if text in ['=', '+/-']:
            currentOperation = displayNumbers.displayNumbers.label.cget("text")
            print(currentOperation)
            result = calculate(operator=text, value=currentOperation)
            displayNumbers.displayNumbers(window, result, replaced=True)
            return
        elif text not in ['x**2', '1/x', '√x']:
            displayNumbers.displayNumbers(window, text)
            return
        else:
            format = text.replace('x', '{}'.format(displayNumbers.displayNumbers.label.cget("text")))
            displayNumbers.displayNumbers(window, format, replaced=True)
            return

            