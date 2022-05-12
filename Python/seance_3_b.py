from tkinter import *


def smiley():
    global c
    win = Tk()
    c = Canvas(win, width = 800, height = 800, bg="black")
    c.pack()

    c.create_oval(100, 100, 350, 350, outline = "white", fill = "black")
    c.create_oval(125, 125, 175, 175, outline = "white",fill = "black")
    c.create_oval(225, 125, 275, 175, outline = "white",fill = "black")
    c.create_line(125, 250, 275, 250, width = 1, fill = "white")

    Button(win, text = "Quit", command = win.destroy).pack()

    win.mainloop()

smiley()