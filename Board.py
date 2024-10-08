import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Label

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
    'g1': ['open', 'noMill'],
    'g4': ['open', 'noMill'],
    'g7': ['open', 'noMill'],
    'f2': ['open', 'noMill'],
    'f4': ['open', 'noMill'],
    'f6': ['open', 'noMill'],
    'e3': ['open', 'noMill'],
    'e4': ['open', 'noMill'],
    'e5': ['open', 'noMill'],
    'd1': ['open', 'noMill'],
    'd2': ['open', 'noMill'],
    'd3': ['open', 'noMill'],
    'd5': ['open', 'noMill'],
    'd6': ['open', 'noMill'],
    'd7': ['open', 'noMill'],
    'c3': ['open', 'noMill'],
    'c4': ['open', 'noMill'],
    'c5': ['open', 'noMill'],
    'b2': ['open', 'noMill'],
    'b4': ['open', 'noMill'],
    'b6': ['open', 'noMill'],
    'a1': ['open', 'noMill'],
    'a4': ['open', 'noMill'],
    'a7': ['open', 'noMill'],
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

        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=2)
        self.rowconfigure(0, weight=2)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=2)

        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    def createPieces(self):
        left = tk.Canvas(self, width=100, height=300, bg='#987554')
        left.grid(column=0, row=1)
        right = tk.Canvas(self, width=100, height=300, bg='#987554')
        right.grid(column=2, row=1)

    def replayOptions(self):
        replayOptions = tk.Canvas(self, width=400, height=80, bg='grey')
        replayOptions.grid(column=1, row=2)

        label = tk.Label(replayOptions, text='Game Replay')
        replayOptions.create_window(200, 20,window=label)

        manReplay = tk.Button(replayOptions, text='Manual Replay')
        replayOptions.create_window(100, 50, window=manReplay)

        autoReplay = tk.Button(replayOptions, text='Auto Replay')
        replayOptions.create_window(290, 50, window=autoReplay)

        delay = 2
        timeDelay = tk.Entry(replayOptions, textvariable=delay, width=3)
        replayOptions.create_window(340, 50, window=timeDelay)


    def createBoard(self):
        board = tk.Canvas(self, width=500, height=500, bg='#987554')
        board.grid(column=1, row=1)

        g1 = tk.Button(board, text='O')
        g1.config(command=lambda : Board.onButtonPress(g1))
        board.create_window(20, 20, window=g1)
        g4 = tk.Button(board, text='O')
        g4.config(command=lambda: Board.onButtonPress(g4))
        board.create_window(245, 20, window=g4)
        g7 = tk.Button(board, text='O')
        g7.config(command=lambda: Board.onButtonPress(g7))
        board.create_window(480, 20, window=g7)
        board.create_line((20, 20), (245, 20), fill='black')
        board.create_line((245, 20), (480, 20), fill='black')

        f2 = tk.Button(board, text='O')
        f2.config(command=lambda: Board.onButtonPress(f2))
        board.create_window(105, 90, window=f2)
        f4 = tk.Button(board, text='O')
        f4.config(command=lambda: Board.onButtonPress(f4))
        board.create_window(245, 90, window=f4)
        f6 = tk.Button(board, text='O')
        f6.config(command=lambda: Board.onButtonPress(f6))
        board.create_window(385, 90, window=f6)

        board.create_line((105, 90), (245, 90), fill='black')
        board.create_line((245, 90), (385, 90), fill='black')


        e3 = tk.Button(board, text='O')
        e3.config(command=lambda: Board.onButtonPress(e3))
        board.create_window(175, 160, window=e3)
        e4 = tk.Button(board, text='O')
        e4.config(command=lambda: Board.onButtonPress(e4))
        board.create_window(245, 160, window=e4)
        e5 = tk.Button(board, text='O')
        e5.config(command=lambda: Board.onButtonPress(e5))
        board.create_window(315, 160, window=e5)

        board.create_line((175, 160), (245, 160), fill='black')
        board.create_line((245, 160), (315, 160), fill='black')

        d1 = tk.Button(board, text='O')
        d1.config(command=lambda: Board.onButtonPress(d1))
        board.create_window(20, 245, window=d1)
        d2 = tk.Button(board, text='O')
        d2.config(command=lambda: Board.onButtonPress(d2))
        board.create_window(105, 245, window=d2)
        d3 = tk.Button(board, text='O')
        d3.config(command=lambda: Board.onButtonPress(d3))
        board.create_window(175, 245, window=d3)
        d5  = tk.Button(board, text='O')
        d5.config(command=lambda: Board.onButtonPress(d5))
        board.create_window(315, 245, window=d5)
        d6 = tk.Button(board, text='O')
        d6.config(command=lambda: Board.onButtonPress(d6))
        board.create_window(385, 245, window=d6)
        d7 = tk.Button(board, text='O')
        d7.config(command=lambda: Board.onButtonPress(d7))
        board.create_window(480, 245, window=d7)

        board.create_line((20, 245), (105, 245), fill='black')
        board.create_line((105, 245), (175, 245), fill='black')
        board.create_line((315, 245), (385, 245), fill='black')
        board.create_line((385, 245), (480, 245), fill='black')

        c3 = tk.Button(board, text='O')
        c3.config(command=lambda: Board.onButtonPress(c3))
        board.create_window(175, 340, window=c3)
        c4 = tk.Button(board, text='O')
        c4.config(command=lambda: Board.onButtonPress(c4))
        board.create_window(245, 340, window=c4)
        c5 = tk.Button(board, text='O')
        c5.config(command=lambda: Board.onButtonPress(c5))
        board.create_window(315, 340, window=c5)

        board.create_line((175, 340), (245, 340), fill='black')
        board.create_line((245, 340), (315, 340), fill='black')

        b2 = tk.Button(board, text='O')
        b2.config(command=lambda: Board.onButtonPress(b2))
        board.create_window(105, 410, window=b2)
        b4 = tk.Button(board, text='O')
        b4.config(command=lambda: Board.onButtonPress(b4))
        board.create_window(245, 410, window=b4)
        b6 = tk.Button(board, text='O')
        b6.config(command=lambda: Board.onButtonPress(b6))
        board.create_window(385, 410, window=b6)

        board.create_line((105, 410), (245, 410), fill='black')
        board.create_line((245, 410), (385, 410), fill='black')

        a1 = tk.Button(board, text='O')
        a1.config(command=lambda: Board.onButtonPress(a1))
        board.create_window(20, 480, window=a1)
        a4 = tk.Button(board, text='O')
        a4.config(command=lambda: Board.onButtonPress(a4))
        board.create_window(245, 480, window=a4)
        a7 = tk.Button(board, text='O')
        a7.config(command=lambda: Board.onButtonPress(a7))
        board.create_window(480, 480, window=a7)

        board.create_line((20, 480), (245, 480), fill='black')
        board.create_line((245, 480), (480, 480), fill='black')

        board.create_line((20, 20), (20, 245), fill='black')
        board.create_line((245, 20), (245, 90), fill='black')
        board.create_line((480, 20), (480, 245), fill='black')
        board.create_line((105, 90), (105, 245), fill='black')
        board.create_line((245, 90), (245, 160), fill='black')
        board.create_line((385, 90), (385, 245), fill='black')
        board.create_line((175, 160), (175, 245), fill='black')
        board.create_line((315, 160), (315, 245), fill='black')
        board.create_line((175, 245), (175, 340), fill='black')
        board.create_line((315, 245), (315, 340), fill='black')
        board.create_line((105, 245), (105, 410), fill='black')
        board.create_line((245, 340), (245, 480), fill='black')
        board.create_line((385, 245), (385, 410), fill='black')
        board.create_line((20, 245), (20, 480), fill='black')
        board.create_line((245, 410), (245, 480), fill='black')
        board.create_line((480, 245), (480, 480), fill='black')

    def setUp(self):
        self.createBoard()
        self.createPieces()
        self.replayOptions()

    def onButtonPress(button):
        if button['text'] == "O":
            button.config(text = "*")

