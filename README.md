## MasterMind
<img src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Mastermind.jpg" width="200" align="right">

__MasterMind__ is a simulation of the classic code-breaking board game, [Mastermind](https://en.wikipedia.org/wiki/Mastermind_(board_game)), programmed in Python. The GUI is built with the components of the [Tkinter](https://docs.python.org/2/library/tkinter.html) package.

### Gameplay

The goal of the game is to guess the randomly-generated code consisting of four random colours. The player can iterate through the six colours using the selection buttons, and enter the guess. For each correct colour at the same index in the code, the player receives one black peg. Of the remaining colours, if any are the right colour at the wrong index, a white peg is awarded. If the player successfully cracks the code in 12 tries, they beat the game.

Instructions are included when the program is run.

### Difficulties

The game has four built-in difficulties:
* Beginner: Make 12 guesses from 4 colours
* Easy: Make 12 guesses from 5 colours
* Standard: Make 12 guesses from 6 colours
* Hard: Make 8 guesses from 6 colours

2018-10-20