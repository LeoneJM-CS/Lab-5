import tkinter
import tkinter as tk
from tkinter import *

top = Tk()

top.geometry("500x550")
answer = Text(width=45, height=2)
answer.place(x=100, y=100)


def show(x):
    try:

        if x == "=":
            final_answer = eval(answer.get(1.0, "end-1c"))
            answer.insert(tk.INSERT, x)
            answer.insert(tk.INSERT, final_answer)
        elif x == "C":
            answer.delete(1.0, END)
        else:
            answer.insert(tk.INSERT, x)
    except:
        answer.delete(1.0, END)


b1 = Button(top, text="1", width=10, height=5, command=lambda: show("1"))
b1.place(x=100, y=250)

b2 = Button(top, text="2", width=10, height=5, command=lambda: show("2"))
b2.place(x=200, y=250)

b3 = Button(top, text="3", width=10, height=5, command=lambda: show("3"))
b3.place(x=300, y=250)

b4 = Button(top, text="4", width=10, height=5, command=lambda: show("4"))
b4.place(x=100, y=350)

b5 = Button(top, text="5", width=10, height=5, command=lambda: show("5"))
b5.place(x=200, y=350)

b6 = Button(top, text="6", width=10, height=5, command=lambda: show("6"))
b6.place(x=300, y=350)

b7 = Button(top, text="7", width=10, height=5, command=lambda: show("7"))
b7.place(x=100, y=450)

b8 = Button(top, text="8", width=10, height=5, command=lambda: show("8"))
b8.place(x=200, y=450)

b9 = Button(top, text="9", width=10, height=5, command=lambda: show("9"))
b9.place(x=300, y=450)

b0 = Button(top, text="0", width=10, height=5, command=lambda: show("0"))
b0.place(x=200, y=550)

divide = Button(top, text="/", width=10, height=5, command=lambda: show("/"))
divide.place(x=400, y=250)

multiply = Button(top, text="X", width=10, height=5, command=lambda: show("*"))
multiply.place(x=400, y=350)

subtraction = Button(top, text="-", width=10, height=5, command=lambda: show("-"))
subtraction.place(x=400, y=450)

addition = Button(top, text="+", width=10, height=5, command=lambda: show("+"))
addition.place(x=400, y=550)

clear = Button(top, text="C", width=10, height=5, command=lambda: show("C"))
clear.place(x=400, y=150)

equals = Button(top, text="=", width=10, height=5, command=lambda: show("="))
equals.place(x=300, y=550)

decimal = Button(top, text=".", width=10, height=5, command=lambda: show("."))
decimal.place(x=100, y=550)


top.mainloop()
