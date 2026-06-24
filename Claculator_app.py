from tkinter import *
window=Tk()
window.title("Calculator")
# window.geometry("500x500")
window.minsize(800,600)
"""--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""

entry1 = Entry(window, width=50,borderwidth=10,font=("Arial", 20))
entry1.place(x=1, y=1)
"""--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""


def click(num):
    result=entry1.get()
    entry1.delete(0,END)
    entry1.insert(0,str(result)+str(num))


button1=Button(command=lambda:click(1))
button1.config(width=5,text="1",font=("Arial", 20))
button1.place(x=0,y=100)

button1=Button(command=lambda:click(2))
button1.config(width=5,text="2",font=("Arial", 20))
button1.place(x=100,y=100)

button1=Button(command=lambda:click(3))
button1.config(width=5,text="3",font=("Arial", 20))
button1.place(x=200,y=100)

button1=Button(command=lambda:click(4))
button1.config(width=5,text="4",font=("Arial", 20))
button1.place(x=0,y=165)

button1=Button(command=lambda:click(5))
button1.config(width=5,text="5",font=("Arial", 20))
button1.place(x=100,y=165)

button1=Button(command=lambda:click(6))
button1.config(width=5,text="6",font=("Arial", 20))
button1.place(x=200,y=165)

button1=Button(command=lambda:click(7))
button1.config(width=5,text="7",font=("Arial", 20))
button1.place(x=0,y=230)

button1=Button(command=lambda:click(8))
button1.config(width=5,text="8",font=("Arial", 20))
button1.place(x=100,y=230)

button1=Button(command=lambda:click(9))
button1.config(width=5,text="9",font=("Arial", 20))
button1.place(x=200,y=230)

button1=Button(command=lambda:click(0))
button1.config(width=5,text="0",font=("Arial", 20))
button1.place(x=0,y=295)
"""--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""

i=0
math=0
def add():
    global i
    global math
    math="add"
    n1=entry1.get()
    i=int(n1)
    entry1.delete(0,END)

button1=Button(command=lambda:add())
button1.config(width=5,text="+",font=("Arial", 20))
button1.place(x=300,y=100)
"""--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""

def subtract():
    n1=entry1.get()
    global i
    global math
    math = "subtract"
    i=int(n1)
    entry1.delete(0,END)

button1=Button(command=lambda:subtract())
button1.config(width=5,text="-",font=("Arial", 20))
button1.place(x=300,y=165)
"""--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""

def multiply():
    n1=entry1.get()
    global i
    global math
    math = "multiply"
    i=int(n1)
    entry1.delete(0,END)

button1=Button(command=lambda:multiply())
button1.config(width=5,text="*",font=("Arial", 20))
button1.place(x=300,y=230)
"""--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""

def division():
    n1=entry1.get()
    global i
    global math
    math = "division"
    i=int(n1)
    entry1.delete(0,END)

button1=Button(command=lambda:division())
button1.config(width=5,text="/",font=("Arial", 20))
button1.place(x=300,y=295)
"""--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""

def equal_to():
    n2=entry1.get()
    j=int(n2)
    entry1.delete(0,END)
    if math=="add":
        n3=i+j
        entry1.insert(0,str(n3))
    elif math=="subtract":
        n3=i-j
        entry1.insert(0, str(n3))
    elif math=="multiply":
        n3=i*j
        entry1.insert(0, str(n3))
    elif math=="division":
        n3=i/j
        entry1.insert(0, str(n3))


button1=Button(command=lambda:equal_to())
button1.config(width=5,text="=",font=("Arial", 20))
button1.place(x=200,y=295)
"""--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""


def clear():
    entry1.delete(0,END)


button1=Button(command=lambda:clear())
button1.config(width=5,text="Clear",font=("Arial", 20))
button1.place(x=100,y=295)
"""--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
mainloop()