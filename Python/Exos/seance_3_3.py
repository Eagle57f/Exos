from tkinter import *
var=0

def plus():
    global var
    var+=1
    tex1.config(text=var)


fen1 = Tk()
fen1.title("Nombre de clics")
fen1.geometry('200x75')
tex1 = Label(fen1, text='0')
tex1.pack()
bou1 = Button(fen1, text='ajouter 1', command = plus)
bou1.pack()
fen1.mainloop()