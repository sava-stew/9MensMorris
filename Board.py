import tkinter as tk
from tkinter import ttk, simpledialog
from tkinter import *
from tkinter.ttk import Label
from Turn import Turn
from Player import Player

placements = {

    'g1': ['open', 'noMill', 20, 20, "g1", ["g4","d1"]],
    'g4': ['open', 'noMill', 245, 20, "g4", ["g1","g7","f4"]],
    'g7': ['open', 'noMill', 480, 20, "g7", ["g4","d4"]],
    'f2': ['open', 'noMill', 105, 90, "f2", ["f4","d2"]],
    'f4': ['open', 'noMill', 245, 90, "f4", ["f2","g4","f6","e4"]],
    'f6': ['open', 'noMill', 385, 90, "f6", ["f4","d6"]],
    'e3': ['open', 'noMill', 175, 160, "e3", ["e4","d3"]],
    'e4': ['open', 'noMill', 245, 160, "e4", ["e3","f4","e5"]],
    'e5': ['open', 'noMill', 315, 160, "e5", ["e4","d5"]],
    'd1': ['open', 'noMill', 20, 245, "d1", ["g1","d2","a1"]],
    'd2': ['open', 'noMill', 105, 245, "d2", ["d1","f2","d3","b2"]],
    'd3': ['open', 'noMill', 175, 245, "d3", ["d2","e3","c3"]],
    'd5': ['open', 'noMill', 315, 245, "d5", ["e5","d6","c5"]],
    'd6': ['open', 'noMill', 385, 245, "d6", ["d5","f6","d7","b6"]],
    'd7': ['open', 'noMill', 480, 245, "d7", ["d6","g7","a7"]],
    'c3': ['open', 'noMill', 175, 340, "c3", ["d3","c4"]],
    'c4': ['open', 'noMill', 245, 340, "c4", ["c3","c5","b4"]],
    'c5': ['open', 'noMill', 315, 340, "c5", ["c4","d5"]],
    'b2': ['open', 'noMill', 105, 410, "b2", ["d2","b4"]],
    'b4': ['open', 'noMill', 245, 410, "b4", ["b2","c4","a4","b6"]],
    'b6': ['open', 'noMill', 385, 410, "b6", ["b4","d6"]],
    'a1': ['open', 'noMill', 20, 480, "a1", ["a4","d1"]],
    'a4': ['open', 'noMill', 245, 480, "a4", ["a1","b4","a7"]],
    'a7': ['open', 'noMill', 480, 480, "a7", ["a4","d7"]]
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

    def currentTurn(self, turn):
        currentTurn = tk.Label(self, text='Current turn: ' + turn)
        text_var = tk.StringVar()
        text_var.set('Current turn: ' + turn)
        currentTurn.grid(column=1, row=0)

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
        #add Buttons to dict
        for value in placements.values():
            value.append(tk.Button(board, text='O'))

        self.drawButtons(board, turn)

    def drawButtons(self, canvas, turn, origin=""):
        for placement in placements.values():
            placement[6].config(command=lambda i=placement: Board.onButtonPress(self, i, canvas, turn, origin))
            if placement[0] == "open":
                canvas.create_window(placement[2], placement[3], window=placement[6])
            elif placement[0] == "white":
                placement[6].config(text="", height=3, width=5, bg="white")
                canvas.create_window(placement[2], placement[3], window=placement[6])
            elif placement[0] == "black":
                placement[6].config(text="", height=3, width=5, bg="black")
                canvas.create_window(placement[2], placement[3], window=placement[6])
        return

    def setUp(self):
        self.createBoard()
        self.currentTurn('white')
        self.banks()
        self.replayOptions()

    def onButtonPress(self, button, canvas, turn, origin):
        whoseTurn = turn.getTurn()
        if whoseTurn == "white":
            bankPieces = white.getBankPieces()
            boardPieces = white.getPlayerPieces()
        else:
            bankPieces = black.getBankPieces()
            boardPieces = black.getPlayerPieces()

        if origin == "":
            if bankPieces != 0:
                if button[0] == "open" and whoseTurn == 'black' and black.getBankPieces() != 0:
                    black.bankUpdate()
                    button[0] = "black"
                    turn.changeTurn()
                elif button[0] == "open" and whoseTurn == 'white' and white.getBankPieces() != 0:
                    white.bankUpdate()
                    button[0] = "white"
                    turn.changeTurn()
            else:
                if button[0] == whoseTurn:
                    origin = button[4]
        else:
            if button[0] == whoseTurn:
                origin = button[4]
            elif boardPieces > 3 and button[4] in placements[origin][5]:
                if self.move_piece(origin, button[4]):
                    origin = ""
                    turn.changeTurn()
            elif boardPieces <= 3:
                if self.move_piece(origin, button[4]):
                    origin = ""
                    turn.changeTurn()

        self.currentTurn(turn.getTurn())
        self.banks()
        self.checkMills()
        self.drawButtons(canvas, turn, origin)

    def checkMills(self):
        mills = [('g1', 'g4', 'g7'),
                 ('f2', 'f4', 'f6'),
                 ('e3', 'e4', 'e5'),
                 ('d1', 'd2', 'd3'),
                 ('d5', 'd6', 'd7'),
                 ('c3', 'c4', 'c5'),
                 ('b2', 'b4', 'b6'),
                 ('a1', 'a4', 'a7'),
                 ('g1', 'd1', 'a1'),
                 ('f2', 'd2', 'b2'),
                 ('e3', 'd3', 'c3'),
                 ('g4', 'f4', 'e4'),
                 ('c4', 'b4', 'a4'),
                 ('e5', 'd5', 'c5'),
                 ('f6', 'd6', 'b6'),
                 ('g7', 'd7', 'a7')]

        for mill in mills:
            if placements[mill[0]][0] == "white" and placements[mill[1]][0] == "white" and placements[mill[2]][
                0] == "white":
                if placements[mill[0]][1] != "whiteMill" or placements[mill[1]][1] != "whiteMill" or \
                        placements[mill[2]][1] != "whiteMill":
                    self.removeOpponentPiece("black")
                placements[mill[0]][1] = "whiteMill"
                placements[mill[1]][1] = "whiteMill"
                placements[mill[2]][1] = "whiteMill"
            elif placements[mill[0]][0] == "black" and placements[mill[1]][0] == "black" and placements[mill[2]][
                0] == "black":
                if placements[mill[0]][1] != "blackMill" or placements[mill[1]][1] != "blackMill" or \
                        placements[mill[2]][1] != "blackMill":
                    self.removeOpponentPiece("white")
                placements[mill[0]][1] = "blackMill"
                placements[mill[1]][1] = "blackMill"
                placements[mill[2]][1] = "blackMill"

        return

    def move_piece(self, from_pos, to_pos):

        if from_pos not in placements or to_pos not in placements:
            print(f"Position {from_pos} or {to_pos} does not exist.")
            return False

        if placements[from_pos][0] != 'open' and placements[to_pos][0] == 'open':

            placements[to_pos][0] = placements[from_pos][0]
            placements[to_pos][6].config(text="", height=3, width=5, bg=placements[to_pos][0])

            placements[from_pos][0] = 'open'
            placements[from_pos][6].config(text="O", height=1, width=3, bg="SystemButtonFace")

            return True
        else:
            print("Invalid move: the target position is not open or the source position does not have a piece.")
            return False

    def removeOpponentPiece(self, opponent_color):
        removable_pieces = [key for key, value in placements.items() if
                            value[0] == opponent_color and value[1] != f"{opponent_color}Mill"]
        if not removable_pieces:
            removable_pieces = [key for key, value in placements.items() if value[0] == opponent_color]

        if not removable_pieces:
            print(f"No pieces to remove for {opponent_color}.")
            return

        piece_to_remove = simpledialog.askstring("Remove Piece",
                                                 f"Select a piece to remove from {opponent_color}:\n" + "\n".join(
                                                     removable_pieces))

        if piece_to_remove in removable_pieces:
            placements[piece_to_remove][0] = 'open'
            placements[piece_to_remove][6].config(text="O", height=1, width=3, bg="SystemButtonFace")
            if opponent_color == "white":
                white.pieceUpdate()
            elif opponent_color == "black":
                black.pieceUpdate()
            print(f"Removed {opponent_color} piece at {piece_to_remove}.")
        else:
            print("Invalid piece selected.")
