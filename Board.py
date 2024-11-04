import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import Label
#from PIL import Image, ImageTk
from Turn import Turn
from Player import Player

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
    'g1': ['open', 'noMill', 20, 20], #g1 g4 and g7 are all the same color, you should change noMill to Mill for g1 g4 and g7
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

black = Player()
white = Player()

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

    def createPieces(self, bank, num, y0, y1, color):
        bank.delete('all')
        for i in range(0, num, 1):
            piece = bank.create_rectangle((3, y0), (20, y1), fill=color)
            y0 += 25
            y1 += 25

    def banks(self):

        whiteBank = tk.Canvas(self, width=20)
        whiteBank.grid(column=0, row=1)
        self.createPieces(whiteBank, white.getBankPieces(), 20, 40, 'white')

        blackBank = tk.Canvas(self, width=20)
        blackBank.grid(column=2, row=1)
        self.createPieces(blackBank, black.getBankPieces(), 20, 40, 'black')


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

        turn = Turn()

        #draw lines
        board.create_line((20, 20), (480, 20), fill='black')
        board.create_line((105, 90), (385, 90), fill='black')
        board.create_line((175, 160), (315, 160), fill='black')
        board.create_line((20, 245), (175, 245), fill='black')
        board.create_line((315, 245), (480, 245), fill='black')
        board.create_line((175, 340), (315, 340), fill='black')
        board.create_line((105, 410), (385, 410), fill='black')
        board.create_line((20, 480), (480, 480), fill='black')

        board.create_line((20, 20), (20, 480), fill='black')
        board.create_line((245, 20), (245, 160), fill='black')
        board.create_line((480, 20), (480, 480), fill='black')
        board.create_line((105, 90), (105, 410), fill='black')
        board.create_line((385, 90), (385, 410), fill='black')
        board.create_line((175, 160), (175, 340), fill='black')
        board.create_line((315, 160), (315, 340), fill='black')
        board.create_line((245, 340), (245, 480), fill='black')

        #draw board
        #'O' button for open,
        #black button for black
        #white button for white
        print(type(placements["g1"]))
        #add Buttons to dict
        for value in placements.values():
            print(type(value))
            value.append(tk.Button(board, text='O'))

        self.drawButtons(board, turn)

    def drawButtons(self, canvas, turn):
        for placement in placements.values():
            #print(type(placement[4]))
            placement[4].config(command=lambda i=placement: Board.onButtonPress(self, i, canvas, turn))
            if placement[0] == "open":
                canvas.create_window(placement[2], placement[3], window=placement[4])
            elif placement[0] == "white":
                placement[4].config(text="", height=3, width=5, bg="white")
                canvas.create_window(placement[2], placement[3], window=placement[4])
            elif placement[0] == "black":
                placement[4].config(text="", height=3, width=5, bg="black")
                canvas.create_window(placement[2], placement[3], window=placement[4])
        return

    def setUp(self):
        self.createBoard()
        self.banks()
        self.replayOptions()

    def onButtonPress(self, button, canvas, turn):
        #print(button)
        if button[0] == "open" and turn.getTurn() == 'black' and black.getBankPieces() != 0:
            #button.config(text="",height=3,width=5,bg="black")
            black.bankUpdate()
            button[0] = "black"
            turn.changeTurn()
        elif button[0] == "open" and turn.getTurn() == 'white' and white.getBankPieces() != 0:
            #button.config(text="",height=3,width=5,bg="white")
            white.bankUpdate()
            button[0] = "white"
            turn.changeTurn()
        self.banks()
        self.checkMills()
        self.drawButtons(canvas, turn)

    def checkMills(self):
        mills = [('g1','g4','g7'),
                 ('f2','f4','f6'),
                 ('e3','e4','e5'),
                 ('d1','d2','d3'),
                 ('d5','d6','d7'),
                 ('c3','c4','c5'),
                 ('b2','b4','b6'),
                 ('a1','a4','a7'),
                 ('g1','d1','a1'),
                 ('f2','d2','b2'),
                 ('e3','d3','c3'),
                 ('g4','f4','e4'),
                 ('c4','b4','a4'),
                 ('e5','d5','c5'),
                 ('f6','d6','b6'),
                 ('g7','d7','a7')]

        for mill in mills:
            if placements[mill[0]][0] == "white" and placements[mill[1]][0] == "white" and placements[mill[2]][0] == "white":
                placements[mill[0]][1] = "whiteMill"
                placements[mill[1]][1] = "whiteMill"
                placements[mill[2]][1] = "whiteMill"
            elif placements[mill[0]][0] == "black" and placements[mill[1]][0] == "black" and placements[mill[2]][0] == "black":
                placements[mill[0]][1] = "blackMill"
                placements[mill[1]][1] = "blackMill"
                placements[mill[2]][1] = "blackMill"

        return

