from tkinter import *
a=0
x=0
x1,y1=20,50

fen=Tk()


def cun():
    global a
    x1,y1=20,50
    can1.create_oval(x1,y1,x1+60,y1+60,outline=coul[a])
    a+=1

def cdeux():
    global a
    x1,y1=80,50
    can1.create_oval(x1,y1,x1+60,y1+60,outline=coul[a])
    a+=1

def ctrois():
    global a
    x1,y1=140,50
    can1.create_oval(x1,y1,x1+60,y1+60,outline=coul[a])
    a+=1

def cquatre():
    global a
    x1,y1=50,80
    can1.create_oval(x1,y1,x1+60,y1+60,outline=coul[a])
    a+=1

def ccinq():
    global a
    x1,y1=110,80
    can1.create_oval(x1,y1,x1+60,y1+60,outline=coul[a])
    a+=1


Button(fen,text='Quitter',command=fen.destroy).grid(row=1, column=0)

Button(fen,text='c1',command=cun).grid(row=2, column=1)
Button(fen,text='c2',command=cdeux).grid(row=2, column=2)
Button(fen,text='c3',command=ctrois).grid(row=2, column=3)
Button(fen,text='c4',command=cquatre).grid(row=2, column=4)
Button(fen,text='c5',command=ccinq).grid(row=2, column=5)

can1=Canvas(fen,bg='white',height=150,width=220)
can1.grid(row=0)
coul=['red','yellow','blue','green','black']

fen.mainloop()