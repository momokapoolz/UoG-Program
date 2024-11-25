from tkinter import *
window = Tk()
window.geometry('400x300')
window.title('Website')

def perform(operation):
    a = int(enter_boxA.get())
    b = int(enter_boxB.get())
    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '*':
        result = a * b
    elif operation == '/':
        result = a / b
    text_result.delete(0, END)
    text_result.insert(0, str(result))

def Add_clicked():
    perform('+')

def Sub_clicked():
    perform('-')

def Mul_clicked():
    perform('*')

def Div_clicked():
    perform('/')


    

#label entry for a
labelA = Label(window, text= 'A')
labelA.grid(column=0, row=0)
enter_boxA = Entry(window, width= 12)
enter_boxA.grid(column=1, row=0, columnspan=4)

#label entry for b
labelB = Label(window, text= 'B')
labelB.grid(column=0, row=1)
enter_boxB = Entry(window, width= 12)
enter_boxB.grid(column=1, row=1, columnspan=4)

#mathematics buttons
btnAdd = Button(window, text= '+', command= Add_clicked)
btnAdd.grid(column=1, row=2)
btnSub = Button(window, text= '-', command= Sub_clicked)
btnSub.grid(column=2, row=2)
btnMul = Button(window, text= '*', command= Mul_clicked)
btnMul.grid(column=3, row=2)
btnDiv = Button(window, text= '/', command= Div_clicked)
btnDiv.grid(column=4, row=2)

text_result = Entry(window, width=10, text='operation',state='readonly')
text_result.grid(column=1, row=3, columnspan=4)

window.mainloop()