import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import Label
from PIL import Image, ImageTk
from Turn import Turn

#for index 0
#open
#white
#black

#for index 1
#noMill
#newMill
#oldMill

#when the button is pressed
#need to get the variable name of button
#variable name of the button will be the dictionary key
#need to get player color
#call function with player color and button name
#function should access the key (button name) and change index[0] of list to player

placements = {
    'g1': ['open', 'noMill', 20, 20],
    'g4': ['open', 'noMill', 245, 20],
    'g7': ['open', 'noMill', 480, 20],
    'f2': ['open', 'noMill', 105, 90],
    'f4': ['open', 'noMill', 245, 90],
    'f6': ['open', 'noMill', 385, 90],
    'e3': ['open', 'noMill', 175, 160],
    'e4': ['open', 'noMill', 245, 160],
    'e5': ['open', 'noMill', 315, 160],
    'd1': ['open', 'noMill', 20, 245],
    'd2': ['open', 'noMill', 105, 245],
    'd3': ['open', 'noMill', 175, 245],
    'd5': ['open', 'noMill', 315, 245],
    'd6': ['open', 'noMill', 385, 245],
    'd7': ['open', 'noMill', 480, 245],
    'c3': ['open', 'noMill', 175, 340],
    'c4': ['open', 'noMill', 245, 340],
    'c5': ['open', 'noMill', 315, 340],
    'b2': ['open', 'noMill', 105, 410],
    'b4': ['open', 'noMill', 245, 410],
    'b6': ['open', 'noMill', 385, 410],
    'a1': ['open', 'noMill', 20, 480],
    'a4': ['open', 'noMill', 245, 480],
    'a7': ['open', 'noMill', 480, 480],
}

class Board(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Nine Men\'s Morris')

        window_width = 900
        window_height= 700
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        center_x = int(screen_width/2 - window_width/2)
        center_y = int(screen_height/2 - window_height/2)

        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    def createBoard(self):
        canvas = tk.Canvas(self, width=500, height=500, bg='#987554')
        canvas.pack(anchor=tk.CENTER, expand=True)

        turn = Turn()

        print(type(placements["g1"]))
        for value in placements.values():
            print(type(value))
            value.append(tk.Button(canvas, text='O'))

        #for placement in placements.values():
        #    print(type(placement[4]))
        #    placement[4].config(command=lambda : Board.onButtonPress(placement[4],turn))
        #    canvas.create_window(placement[2],placement[3],placement[4])

        g1 = tk.Button(canvas, text='O')
        g1.config(command=lambda : Board.onButtonPress(g1,turn))
        canvas.create_window(20, 20, window=g1)
        g4 = tk.Button(canvas, text='O')
        g4.config(command=lambda: Board.onButtonPress(g4,turn))
        canvas.create_window(245, 20, window=g4)
        g7 = tk.Button(canvas, text='O')
        g7.config(command=lambda: Board.onButtonPress(g7,turn))
        canvas.create_window(480, 20, window=g7)

        canvas.create_line((20, 20), (245, 20), fill='black')
        canvas.create_line((245, 20), (480, 20), fill='black')

        f2 = tk.Button(canvas, text='O')
        f2.config(command=lambda: Board.onButtonPress(f2,turn))
        canvas.create_window(105, 90, window=f2)
        f4 = tk.Button(canvas, text='O')
        f4.config(command=lambda: Board.onButtonPress(f4,turn))
        canvas.create_window(245, 90, window=f4)
        f6 = tk.Button(canvas, text='O')
        f6.config(command=lambda: Board.onButtonPress(f6,turn))
        canvas.create_window(385, 90, window=f6)

        canvas.create_line((105, 90), (245, 90), fill='black')
        canvas.create_line((245, 90), (385, 90), fill='black')


        e3 = tk.Button(canvas, text='O')
        e3.config(command=lambda: Board.onButtonPress(e3,turn))
        canvas.create_window(175, 160, window=e3)
        e4 = tk.Button(canvas, text='O')
        e4.config(command=lambda: Board.onButtonPress(e4,turn))
        canvas.create_window(245, 160, window=e4)
        e5 = tk.Button(canvas, text='O')
        e5.config(command=lambda: Board.onButtonPress(e5,turn))
        canvas.create_window(315, 160, window=e5)

        canvas.create_line((175, 160), (245, 160), fill='black')
        canvas.create_line((245, 160), (315, 160), fill='black')

        d1 = tk.Button(canvas, text='O')
        d1.config(command=lambda: Board.onButtonPress(d1,turn))
        canvas.create_window(20, 245, window=d1)
        d2 = tk.Button(canvas, text='O')
        d2.config(command=lambda: Board.onButtonPress(d2,turn))
        canvas.create_window(105, 245, window=d2)
        d3 = tk.Button(canvas, text='O')
        d3.config(command=lambda: Board.onButtonPress(d3,turn))
        canvas.create_window(175, 245, window=d3)
        d5  = tk.Button(canvas, text='O')
        d5.config(command=lambda: Board.onButtonPress(d5,turn))
        canvas.create_window(315, 245, window=d5)
        d6 = tk.Button(canvas, text='O')
        d6.config(command=lambda: Board.onButtonPress(d6,turn))
        canvas.create_window(385, 245, window=d6)
        d7 = tk.Button(canvas, text='O')
        d7.config(command=lambda: Board.onButtonPress(d7,turn))
        canvas.create_window(480, 245, window=d7)

        canvas.create_line((20, 245), (105, 245), fill='black')
        canvas.create_line((105, 245), (175, 245), fill='black')
        canvas.create_line((315, 245), (385, 245), fill='black')
        canvas.create_line((385, 245), (480, 245), fill='black')

        c3 = tk.Button(canvas, text='O')
        c3.config(command=lambda: Board.onButtonPress(c3,turn))
        canvas.create_window(175, 340, window=c3)
        c4 = tk.Button(canvas, text='O')
        c4.config(command=lambda: Board.onButtonPress(c4,turn))
        canvas.create_window(245, 340, window=c4)
        c5 = tk.Button(canvas, text='O')
        c5.config(command=lambda: Board.onButtonPress(c5,turn))
        canvas.create_window(315, 340, window=c5)

        canvas.create_line((175, 340), (245, 340), fill='black')
        canvas.create_line((245, 340), (315, 340), fill='black')

        b2 = tk.Button(canvas, text='O')
        b2.config(command=lambda: Board.onButtonPress(b2,turn))
        canvas.create_window(105, 410, window=b2)
        b4 = tk.Button(canvas, text='O')
        b4.config(command=lambda: Board.onButtonPress(b4,turn))
        canvas.create_window(245, 410, window=b4)
        b6 = tk.Button(canvas, text='O')
        b6.config(command=lambda: Board.onButtonPress(b6,turn))
        canvas.create_window(385, 410, window=b6)

        canvas.create_line((105, 410), (245, 410), fill='black')
        canvas.create_line((245, 410), (385, 410), fill='black')

        a1 = tk.Button(canvas, text='O')
        a1.config(command=lambda: Board.onButtonPress(a1,turn))
        canvas.create_window(20, 480, window=a1)
        a4 = tk.Button(canvas, text='O')
        a4.config(command=lambda: Board.onButtonPress(a4,turn))
        canvas.create_window(245, 480, window=a4)
        a7 = tk.Button(canvas, text='O')
        a7.config(command=lambda: Board.onButtonPress(a7,turn))
        canvas.create_window(480, 480, window=a7)

        canvas.create_line((20, 480), (245, 480), fill='black')
        canvas.create_line((245, 480), (480, 480), fill='black')

        canvas.create_line((20, 20), (20, 245), fill='black')
        canvas.create_line((245, 20), (245, 90), fill='black')
        canvas.create_line((480, 20), (480, 245), fill='black')
        canvas.create_line((105, 90), (105, 245), fill='black')
        canvas.create_line((245, 90), (245, 160), fill='black')
        canvas.create_line((385, 90), (385, 245), fill='black')
        canvas.create_line((175, 160), (175, 245), fill='black')
        canvas.create_line((315, 160), (315, 245), fill='black')
        canvas.create_line((175, 245), (175, 340), fill='black')
        canvas.create_line((315, 245), (315, 340), fill='black')
        canvas.create_line((105, 245), (105, 410), fill='black')
        canvas.create_line((245, 340), (245, 480), fill='black')
        canvas.create_line((385, 245), (385, 410), fill='black')
        canvas.create_line((20, 245), (20, 480), fill='black')
        canvas.create_line((245, 410), (245, 480), fill='black')
        canvas.create_line((480, 245), (480, 480), fill='black')

    def setUp(self):
        self.createBoard()

    def onButtonPress(button, turn):
        if button['text'] == "O" and turn.getTurn() == 'black':
            button.config(text="",height=3,width=5,bg="black")
            turn.changeTurn()
        elif button['text'] == "O" and turn.getTurn() == 'white':
            button.config(text="",height=3,width=5,bg="white")
            turn.changeTurn()

