import tkinter as tk
from tkinter import ttk, simpledialog
from tkinter import *
from tkinter.ttk import Label
from Turn import Turn
from Player import Player
from GameOver import GameOver
import random
import time

black = Player()
white = Player()
game = GameOver()

class Board(tk.Tk):


    def __init__(self, setUp):
        super().__init__()
        self.configure = setUp
        self.placements = dict(self.configure.placements)
        self.mills = list(self.configure.mills)
        self.gameType = self.configure.gameType
        self.opponent = setUp.opponent
        
        black.setPieces(self.gameType)
        white.setPieces(self.gameType)
        gamefile = open('gamefile.txt', 'w')
        gamefile.close()

        title = ' Men\'s Morris'
        if (self.gameType == 9):
            title = 'Nine' + title
        else:
            title = 'Twelve' + title
        self.title(title)

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

        #overrides default exit button to close all windows
        self.protocol("WM_DELETE_WINDOW", self.quit)

    def currentTurn(self, turn):
        currentTurn = tk.Label(self, text='Current turn: ' + turn)
        currentTurn.grid(column=1, row=0)

    def createPieces(self, bank, num, y0, y1, color):
        bank.delete('all')
        for i in range(0, num, 1):
            piece = bank.create_rectangle((3, y0), (20, y1), fill=color, outline='grey')
            y0 += 20
            y1 += 20

    def banks(self):
        whiteBank = tk.Canvas(self, width=20)
        whiteBank.grid(column=0, row=1)
        self.createPieces(whiteBank, white.getBankPieces(), 20, 40, 'white')

        blackBank = tk.Canvas(self, width=20)
        blackBank.grid(column=2, row=1)
        self.createPieces(blackBank, black.getBankPieces(), 20, 40, 'black')

    def createBoard(self):
        board = tk.Canvas(self, width=500, height=500, bg='#987554')
        board.grid(column=1, row=1)

        turn = Turn(game_type=self.opponent)

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

        if (self.gameType == 12):
            board.create_line((20, 20), (175, 160), fill='black')
            board.create_line((480, 20), (315, 160), fill='black')
            board.create_line((20, 480), (175, 340), fill='black')
            board.create_line((480, 480), (315, 340), fill='black')
        #draw board
        #add Buttons to dict
        for value in self.placements.values():
            value[6] = (tk.Button(board, text='O'))

        self.drawButtons(board, turn)

    def drawButtons(self, canvas, turn, origin=""):
        if canvas is None:
            raise ValueError("Canvas is None! Ensure it's properly initialized.")

        print(f"Canvas: {canvas}")

        for placement in self.placements.values():
            if placement[6] is None:
                placement[6] = tk.Button(canvas) 
                
            placement[6].config(command=lambda i=placement: Board.onButtonPress(self, i, canvas, turn, origin))

            if placement[0] == "open":
                canvas.create_window(placement[2], placement[3], window=placement[6])
            elif placement[0] == "white":
                placement[6].config(text="", height=3, width=5, bg="white")
                canvas.create_window(placement[2], placement[3], window=placement[6])
            elif placement[0] == "black":
                placement[6].config(text="", height=3, width=5, bg="black")
                canvas.create_window(placement[2], placement[3], window=placement[6])

        if turn.getTurnType() == "computer":
            self.AutoPlay(canvas, turn, origin)
        return

    def setUp(self):
        self.createBoard()
        self.currentTurn('white')
        self.banks()

    def onButtonPress(self, button, canvas, turn, origin):
        turn_complete = False
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
                    self.writeToFile(whoseTurn + ':place ' + button[4] + '\n')
                    turn_complete = True
                elif button[0] == "open" and whoseTurn == 'white' and white.getBankPieces() != 0:
                    white.bankUpdate()
                    button[0] = "white"
                    self.writeToFile(whoseTurn + ':place ' + button[4] + '\n')
                    turn_complete = True
            else:
                if button[0] == whoseTurn:
                    origin = button[4]
        else:
            if button[0] == whoseTurn:
                origin = button[4]
            elif boardPieces > 3 and button[4] in self.placements[origin][5]:
                if self.move_piece(origin, button[4]):
                    self.writeToFile(whoseTurn + ':move ' + origin + '-' + button[4] + '\n')
                    origin = ""
                    turn_complete = True
            elif boardPieces <= 3:
                if self.move_piece(origin, button[4]):
                    self.writeToFile(whoseTurn + ':move ' + origin + '-' + button[4] + '\n')
                    origin = ""
                    turn_complete = True

        self.checkMills(turn)
        if turn_complete:
            turn.changeTurn()
        self.currentTurn(turn.getTurn())
        self.banks()
        self.drawButtons(canvas, turn, origin)
        game.gameOver(black.getPlayerPieces(), white.getPlayerPieces())
        if (game.reset == True):
            game.reset = False
            self.resetButtons()
            self.replay()

    def checkMills(self, turn):
        whiteMills = []
        blackMills = []

        for mill in self.mills:
            if self.placements[mill[0]][0] == "white" and self.placements[mill[1]][0] == "white" and self.placements[mill[2]][
                0] == "white":
                if self.placements[mill[0]][1] != "whiteMill" or self.placements[mill[1]][1] != "whiteMill" or \
                        self.placements[mill[2]][1] != "whiteMill":
                    self.writeToFile('white:mill ' + self.placements[mill[0]][4] + '-' + self.placements[mill[1]][4] + '-' + self.placements[mill[2]][4] + '\n')
                    self.removeOpponentPiece("black", turn)
                whiteMills.append(mill)
            elif self.placements[mill[0]][0] == "black" and self.placements[mill[1]][0] == "black" and self.placements[mill[2]][0] == "black":
                if self.placements[mill[0]][1] != "blackMill" or self.placements[mill[1]][1] != "blackMill" or self.placements[mill[2]][1] != "blackMill":
                    self.writeToFile('black:mill ' + self.placements[mill[0]][4] + '-' + self.placements[mill[1]][4] + '-' + self.placements[mill[2]][4] + '\n')
                    self.removeOpponentPiece("white", turn)
                blackMills.append(mill)

        for placement in self.placements.values():
            #convert list of tuples to list, e.g. [(a,b,c)] -> [a,b,c]
            if placement[4] in list(sum(whiteMills, ())):
                placement[1] = "whiteMill"
            elif placement[4] in list(sum(blackMills, ())):
                placement[1] = "blackMill"
            else:
                placement[1] = "noMill"
        return

    def move_piece(self, from_pos, to_pos):

        if from_pos not in self.placements or to_pos not in self.placements:
            print(f"Position {from_pos} or {to_pos} does not exist.")
            return False

        if self.placements[from_pos][0] != 'open' and self.placements[to_pos][0] == 'open':

            self.placements[to_pos][0] = self.placements[from_pos][0]
            self.placements[to_pos][6].config(text="", height=3, width=5, bg=self.placements[to_pos][0])

            self.placements[from_pos][0] = 'open'
            self.placements[from_pos][6].config(text="O", height=1, width=3, bg="SystemButtonFace")

            return True
        else:
            print("Invalid move: the target position is not open or the source position does not have a piece.")
            return False

    def removeOpponentPiece(self, opponent_color, turn):
        removable_pieces = [key for key, value in self.placements.items() if
                            value[0] == opponent_color and value[1] != f"{opponent_color}Mill"]

        if not removable_pieces:
            removable_pieces = [key for key, value in self.placements.items() if value[0] == opponent_color]

        if not removable_pieces:
            print(f"No pieces to remove for {opponent_color}.")
            return

        # check if remover is computer
        if turn.getTurnType() == "computer":
            piece_to_remove = random.choice(removable_pieces)
        else:
            piece_to_remove = simpledialog.askstring("Remove Piece",
                                                 f"Select a piece to remove from {opponent_color}:\n" + "\n".join(
                                                     removable_pieces))

        if not piece_to_remove or piece_to_remove not in removable_pieces:
            print(f"Invalid or empty piece selected: {piece_to_remove}.")
            return

        self.placements[piece_to_remove][0] = 'open'

        if len(self.placements[piece_to_remove]) > 6: 
            button = self.placements[piece_to_remove][6]
            if button:
                button.config(text="O", height=1, width=3, bg="SystemButtonFace")

        if opponent_color == "white":
            white.pieceUpdate() 
            self.writeToFile('black:take ' + piece_to_remove + '\n')
        elif opponent_color == "black":
            black.pieceUpdate()  
            self.writeToFile('white:take ' + piece_to_remove + '\n')

        print(f"Removed {opponent_color} piece at {piece_to_remove}.")

    def AutoPlay(self, canvas, turn, origin):
        choice = random.choice(list(self.placements.keys()))
        self.onButtonPress(self.placements[choice], canvas, turn, origin)
        
    def writeToFile(self, turnInfo):
        self.gamefile = open('gamefile.txt', 'a')
        self.gamefile.write(turnInfo)
        self.gamefile.close()

    def resetButtons(self):
        for placement in self.placements.values():
            placement[0] = 'open'
            placement[6].config(text = 'O', height=1, width=1, bg='white')
            self.update_idletasks()
        self.update_idletasks()

    def replay(self):
        currentPlayer = None
        with open('gamefile.txt', 'r') as file:
            for line in file:
                time.sleep(1)
                line = line.strip('\n')
                print(line)
                command = line.split(':')
                currentPlayer = command[0]

                if 'place' in (command[1]):
                    playInfo = command[1].split(' ')
                    placement = (playInfo[1]).strip('\n')
                    print(placement + '\n')
                    self.placements[placement][0] = currentPlayer
                    self.placements[placement][6].config(text='', height=3, width=5, bg=currentPlayer)

                if 'move' in (command[1]):
                    playInfo = command[1].split(' ')
                    placements = playInfo[1].split('-')
                    start = placements[0]
                    end = placements[1]
                    print(start)
                    print(end)
                    self.placements[start][0] = 'open'
                    self.placements[start][6].config(text='O', height=1, width=1, bg='white')
                    self.update_idletasks()
                    self.placements[end][0] = command[0]
                    self.placements[end][6].config(text='', height=3, width=5, bg=currentPlayer)

                if 'take' in (command[1]):
                    playInfo = command[1].split(' ')
                    placement = playInfo[1]
                    placement = placement.strip('\n')
                    print(placement + '\n')
                    self.placements[placement][0] = 'open'
                    self.placements[placement][6].config(text='O', height=1, width=1, bg='white')

                self.update_idletasks()

        game.replayGameOver(currentPlayer)

