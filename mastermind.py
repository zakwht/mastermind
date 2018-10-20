from Tkinter import *
import Tkinter as tk



#https://stackoverflow.com/questions/42579927/rounded-button-tkinter-python
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

class CustomCircle(tk.Canvas):
    def __init__(self, parent, colour): #constructor
        tk.Canvas.__init__(self, parent, borderwidth=0,
            relief="raised", highlightthickness=0)
        id = self.create_oval((4,4,50,50), outline=colour, fill=colour)
        self.configure(width=54, height=54)

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


#set up colour buttons
mm = tk.Tk()
mm.title("Master Mind")
mm.geometry("324x720")
mm.resizable(0, 0)
b1 = CustomButton(mm)
b1.grid(row=13,column=0)
b2 = CustomButton(mm)
b2.grid(row=13,column=1)
b3 = CustomButton(mm)
b3.grid(row=13,column=2)
b4 = CustomButton(mm)
b4.grid(row=13,column=3)
enter = EnterButton(mm)
enter.grid(row=13,column=4)
mm.update()

tries = 12
while(tries>0):
    mm.update()
    if(enter.press=='true'):
        colours = [b1.colour, b2.colour, b3.colour, b4.colour]
        for i in range(4):
            bx = CustomCircle(mm, colours[i])
            bx.grid(row=tries,column=i)
        tries -= 1
        enter.press = 'false'
