from Tkinter import *
import Tkinter as tk
import random
import webbrowser

colour_array = ['PaleVioletRed1', 'aquamarine2', 'peach puff', 'DarkOliveGreen2', 'SlateBlue2', 'orange']
seq = ['white', 'white', 'white', 'white']
theme = 0       #colour theme
diff = 2        #difficulty [beginner, easy, standard, hard]
destroy = False #flag to close popup & restart game
kill = False    #flag to close all windows & exit

##########################
# Selection Button Class #
##########################
class CustomButton(tk.Canvas):
    def __init__(self, parent): #constructor
        self.state = 0
        self.colour = colour_array[0]
        tk.Canvas.__init__(self, parent, borderwidth=0,
            relief="raised", highlightthickness=0)
        id = self.create_oval((4,4,50,50), outline='black', fill=self.colour)
        self.configure(width=54, height=54)
        self.bind("<ButtonPress-1>", self.set_colour)

    def set_colour(self, event): #iterate through colours
        self.state += 1
        self.state %= len(colour_array)
        self.colour = colour_array[self.state]
        id = self.create_oval((4,4,50,50), outline='black', fill=self.colour)

######################
# Enter Button Class #
######################
class EnterButton(tk.Canvas):
    def __init__(self, parent): #constructor
        colour = 'light slate gray'
        self.press = 'false'
        tk.Canvas.__init__(self, parent, borderwidth=0,
            relief="raised", highlightthickness=0)
        id = self.create_oval((4,4,50,50), outline=colour, fill=colour)
        tk.Canvas.create_text(self, 28, 26, text="Enter", justify=tk.CENTER)
        self.configure(width=54, height=54)
        self.bind("<ButtonPress-1>", self.set_press)

    def set_press(self, event): #change press state
        self.press = 'true'

#######################
# Circles for Guesses #
#######################
class CustomCircle(tk.Canvas):
    def __init__(self, parent, colour): #constructor
        tk.Canvas.__init__(self, parent, borderwidth=0,
            relief="raised", highlightthickness=0)
        id = self.create_oval((4,4,50,50), outline=colour, fill=colour)
        self.configure(width=54, height=54)

###########################
# Canvas to Hold 0-4 Pegs #
###########################
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

########################
# White and Black Pegs #
########################
class Peg(tk.Canvas):
    def __init__(self, parent, colour):
        tk.Canvas.__init__(self, parent)
        id = self.create_oval((5,5,10,10), outline='black', fill=colour)
        self.configure(width=10, height=10)

# Menu for Selecting Colours
def colour_menu():
    global theme
    pop = tk.Toplevel()
    pop.wm_title("Colours")
    pop.protocol("WM_DELETE_WINDOW", set_destroy)
    v = tk.IntVar()
    v.set(theme)

    tk.Label(pop, text="Select Colour Theme:").pack()
    tk.Radiobutton(pop, text="Default", padx = 10, variable=v, value=0).pack(anchor=tk.W)
    tk.Radiobutton(pop, text="Greyscale", padx = 10, variable=v, value=1).pack(anchor=tk.W)
    tk.Radiobutton(pop, text="Blue-green", padx = 10, variable=v, value=2).pack(anchor=tk.W)
    tk.Radiobutton(pop, text="Halloween", padx = 10, variable=v, value=3).pack(anchor=tk.W)
    pop.resizable(0, 0)

    global destroy
    destroy = False
    while(not destroy):
        pop.update()
        theme = v.get()
        set_colour(v.get())
    pop.destroy()

# Menu for Selecting Difficulty
def difficulty_menu():
    global diff
    pop = tk.Toplevel()
    pop.wm_title("Difficulty")
    pop.protocol("WM_DELETE_WINDOW", set_destroy)
    v = tk.IntVar()
    v.set(diff)

    tk.Label(pop, text="Select Colour Theme:").pack()
    tk.Radiobutton(pop, text="Beginner", padx = 10, variable=v, value=0).pack(anchor=tk.W)
    tk.Radiobutton(pop, text="Easy", padx = 10, variable=v, value=1).pack(anchor=tk.W)
    tk.Radiobutton(pop, text="Standard", padx = 10, variable=v, value=2).pack(anchor=tk.W)
    tk.Radiobutton(pop, text="Hard", padx = 10, variable=v, value=3).pack(anchor=tk.W)
    pop.resizable(0, 0)

    global destroy
    destroy = False
    while(not destroy):
        pop.update()
        theme = v.get()
        set_diff(v.get())
    pop.destroy()

# Instructions Menu
def instructions():
    pop = tk.Toplevel()
    pop.wm_title("Instructions")
    pop.resizable(0, 0)
    T = Text(pop, height=9, width=50, bd=0, wrap=tk.WORD)
    T.pack(side=LEFT, fill=Y)
    s = "How To Play\n"
    s += "A random code of 4 colours is generated. You have twelve tries to "
    s += "crack the code. Each turn, use the buttons to choose the colour "
    s += "combination you want to guess. For each colour in the right spot, "
    s += "you will receive a black peg (left side). For any other colour "
    s += "you guessed in the wrong spot, you will receive one white peg "
    s += "(right). If you find the code before 12 tries, you win!"
    T.insert(END, s)
    T.config(state=DISABLED)

# About Menu Options
def about_menu():
    webbrowser.open('https://github.com/zakwht/mastermind')

# Set the Destroy Flag
def set_destroy(self=None):
    global destroy
    destroy = True

# Set the Kill Flag
def set_kill(self=None):
    global kill
    kill = True

# Helper Method for Changing Colours
def set_colour(colour):
    global colour_array
    halloween = ['gray4', 'DarkOrange1', 'yellow', 'orange4', 'gainsboro', 'OrangeRed3']
    default = ['PaleVioletRed1', 'aquamarine2', 'peach puff', 'DarkOliveGreen2', 'SlateBlue2', 'orange']
    bluegreen = ['lime green', 'dodger blue', 'spring green', 'aquamarine', 'steel blue', 'dark green']
    grey = ['gray90', 'gray75', 'gray44', 'gray30', 'gray20', 'gray5']
    themes = [default, grey, bluegreen, halloween]
    colour_array = themes[colour]

# Helper Method for Changing Difficulty
def set_diff(d):
    global diff
    diff = d

# Create Random Colour Code
def generate_sequence():
    global colour_array
    global seq
    set_colour(theme)
    if diff == 0:
        colour_array = colour_array[:-2]
    if diff == 1:
        colour_array = colour_array[:-1]
    for i in range(4):
        seq[i] = random.choice(colour_array)

# Logic Marathon
def check_pegs(colours):
    black = 0
    white = 0
    bool1 = ['f', 'f', 'f', 'f']
    bool2 = ['f', 'f', 'f', 'f']
    for i in range(4): #get black pegs
        if colours[i] == seq[i]:
            black += 1
            bool1[i] = 't'
            bool2[i] = 't'
    for i in range(4): #get white pegs
        if bool1[i] == 't':
            continue
        for j in range(4):
            if i == j or bool2[j] == 't' or seq[i]!=colours[j]:
                continue
            white += 1
            bool2[j] = 't'
            break
    return [black, white]

# Popup for Victory
def vic_pop(tries):
    pop = tk.Toplevel()
    pop.wm_title("Congratulations!")
    pop.protocol("WM_DELETE_WINDOW", set_destroy)

    mv = " move!" if tries==1 else " moves."
    s = "You cracked the code in " + str(tries) + mv
    tk.Label(pop, text=s).pack()
    tk.Button(pop, text="Play Again", padx = 10, command=set_destroy).pack()
    tk.Button(pop, text="Exit", padx = 10, command=set_kill).pack()
    pop.resizable(0, 0)

    while(not destroy and not kill):
        pop.update()

# Popup for loss
def loss_pop():
    pop = tk.Toplevel()
    pop.wm_title("Sorry!")
    pop.protocol("WM_DELETE_WINDOW", set_destroy)

    s = "You ran out of tries.\nThe correct sequence was:"
    tk.Label(pop, text=s).pack()
    for i in range(4):
        CustomCircle(pop, seq[i]).pack(side=LEFT)
    tk.Button(pop, text="Try Again", padx = 10, command=set_destroy).pack()
    tk.Button(pop, text="Exit", padx = 10, command=set_kill).pack()
    pop.resizable(0, 0)

    while(not destroy and not kill):
        pop.update()

# Code Marathon
def play():
    #########################
    # Set Up Colour Buttons #
    #########################
    mm = tk.Tk()
    mm.title("MasterMind")
    mm.geometry("334x718")
    mm.resizable(0, 0)
    mm.protocol("WM_DELETE_WINDOW", set_kill)
    b0 = PegBoard(mm, 'black', 0)
    b0.grid(row=0,column=0)
    b1 = CustomButton(mm)
    b1.grid(row=0,column=1)
    b2 = CustomButton(mm)
    b2.grid(row=0,column=2)
    b3 = CustomButton(mm)
    b3.grid(row=0,column=3)
    b4 = CustomButton(mm)
    b4.grid(row=0,column=4)
    enter = EnterButton(mm)
    enter.grid(row=0,column=5)
    mm.update()

    ###############
    # Set Up Menu #
    ###############
    menubar = Menu(mm)
    menu = Menu(menubar, tearoff=0)
    menu.add_command(label="Colours", command=colour_menu)
    menu.add_command(label="Difficulty", command=difficulty_menu)
    menu.add_command(label="Restart", command=set_destroy, underline=1, accelerator="Ctrl+R")
    menu.add_separator()
    menu.add_command(label="Instructions", command=instructions)
    menu.add_command(label="About", command=about_menu)
    menu.add_separator()
    menu.add_command(label="Exit", command=set_kill, accelerator="Ctrl+Q")
    menubar.add_cascade(label="MasterMind", menu=menu)
    mm.config(menu=menubar)
    mm.bind_all("<Control-q>", set_kill)
    mm.bind_all("<Control-r>", set_destroy)

    ##########################
    # Begin Playing The Game #
    ##########################
    generate_sequence()
    global diff
    tries = 8 if diff==3 else 12
    while tries>0:
        global destroy
        destroy = False
        mm.update()
        if destroy:
            mm.destroy()
            play()
        if kill:
            mm.destroy()
            exit()
        if(enter.press=='true'):
            colours = [b1.colour, b2.colour, b3.colour, b4.colour]
            for i in range(4):
                bx = CustomCircle(mm, colours[i])
                bx.grid(row=13-tries, column=i+1)
            enter.press = 'false'
            bw = check_pegs(colours)
            if bw[0] == 4:
                vic_pop(13-tries)
                break;
            pbw = PegBoard(mm, 'white', bw[1])
            pbb = PegBoard(mm, 'black', bw[0])
            pbw.grid(row=13-tries, column=5)
            pbb.grid(row=13-tries, column=0)
            tries -= 1
            if tries == 0:
                loss_pop()
    if destroy:
        mm.destroy()
        play()
    if kill:
        mm.destroy()
        exit()
#Consider adding a StopWatch
play()
