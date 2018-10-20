from Tkinter import *
import Tkinter as tk
import random

colour_array = ['PaleVioletRed1', 'aquamarine2', 'peach puff', 'DarkOliveGreen2', 'SlateBlue2']
seq = ['white', 'white', 'white', 'white']

class CustomButton(tk.Canvas):
    def __init__(self, parent): #constructor
        self.colour = 'PaleVioletRed1'
        tk.Canvas.__init__(self, parent, borderwidth=0,
            relief="raised", highlightthickness=0)
        id = self.create_oval((4,4,50,50), outline=self.colour, fill=self.colour)
        self.configure(width=54, height=54)
        self.bind("<ButtonPress-1>", self.set_colour)

    def set_colour(self, event): #iterate through colours
        if self.colour == 'PaleVioletRed1':
            self.colour = 'aquamarine2'
        elif self.colour == 'aquamarine2':
            self.colour = 'peach puff'
        elif self.colour == 'peach puff':
            self.colour = 'DarkOliveGreen2'
        elif self.colour == 'DarkOliveGreen2':
            self.colour = 'SlateBlue2'
        elif self.colour == 'SlateBlue2':
            self.colour = 'PaleVioletRed1'
        id = self.create_oval((4,4,50,50), outline=self.colour, fill=self.colour)

class EnterButton(tk.Canvas):
    def __init__(self, parent):
        colour = 'light slate gray'
        self.press = 'false'
        tk.Canvas.__init__(self, parent, borderwidth=0,
            relief="raised", highlightthickness=0)
        id = self.create_oval((4,4,50,50), outline=colour, fill=colour)
        tk.Canvas.create_text(self, 28, 26, text="Enter", justify=tk.CENTER)
        self.configure(width=54, height=54)
        self.bind("<ButtonPress-1>", self.set_press)

    def set_press(self, event):
        self.press = 'true'

class CustomCircle(tk.Canvas):
    def __init__(self, parent, colour): #constructor
        tk.Canvas.__init__(self, parent, borderwidth=0,
            relief="raised", highlightthickness=0)
        id = self.create_oval((4,4,50,50), outline=colour, fill=colour)
        self.configure(width=54, height=54)

class PegBoard(tk.Canvas):
    def __init__(self, parent, colour, n):
        tk.Canvas.__init__(self, parent)
        if n > 0:
            p1 = Peg(self, colour)
            p1.grid(row=1, column=0)
        if n > 1:
            p2 = Peg(self, colour)
            p2.grid(row=1, column=1)
        if n > 2:
            p3 = Peg(self, colour)
            p3.grid(row=0, column=0)
        if n > 3:
            p4 = Peg(self, colour)
            p4.grid(row=0, column=1)
        self.configure(width=54, height=54)

class Peg(tk.Canvas):
    def __init__(self, parent, colour):
        tk.Canvas.__init__(self, parent)
        id = self.create_oval((5,5,10,10), outline='black', fill=colour)
        self.configure(width=10, height=10)

def generate_sequence():
    global colour_array
    global seq
    for i in range(4):
        seq[i] = random.choice(colour_array)

#set up colour buttons
mm = tk.Tk()
mm.title("Master Mind")
mm.geometry("324x720")
mm.resizable(0, 0)
##### CHANGE THIS TO NOT A circle
#### MAKE IT pegs, for accurate dimensions; black peg side = 0
b0 = EnterButton(mm)
b0.grid(row=13,column=0)
b1 = CustomButton(mm)
b1.grid(row=13,column=1)
b2 = CustomButton(mm)
b2.grid(row=13,column=2)
b3 = CustomButton(mm)
b3.grid(row=13,column=3)
b4 = CustomButton(mm)
b4.grid(row=13,column=4)
enter = EnterButton(mm)
enter.grid(row=13,column=5)
mm.update()

generate_sequence()
tries = 12
while(tries>0):
    mm.update()
    if(enter.press=='true'):
        colours = [b1.colour, b2.colour, b3.colour, b4.colour]
        for i in range(4):
            bx = CustomCircle(mm, colours[i])
            bx.grid(row=tries,column=i+1)
        tries -= 1
        enter.press = 'false'
        pbw = PegBoard(mm, 'white', 2)
        pbb = PegBoard(mm, 'black', 3)
        pbw.grid(row=tries, column=5)
        pbb.grid(row=tries, column=0)



# to implement:
# white and black circles... two more classes [::] <- like
# logic for finding out how many ^ very easy
# instructions!







#personal space
