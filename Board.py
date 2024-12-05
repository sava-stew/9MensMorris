import tkinter as tk
from tkinter import ttk, simpledialog
from tkinter import *
from tkinter.ttk import Label
from Turn import Turn
from Player import Player
from GameOver import GameOver
import random

black = Player()
white = Player()
game = GameOver()

class Board(tk.Tk):
    placements = {}
    mills = []
    gameType = 0


    def __init__(self, setUp):
        super().__init__()
        self.placements = dict(setUp.placements)
        self.mills = list(setUp.mills)
        self.gameType = setUp.gameType
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

    def replayOptions(self):
        delay = IntVar()
        replayOptions = tk.Canvas(self, width=400, height=80, bg='grey')
        replayOptions.grid(column=1, row=2)

        label = tk.Label(replayOptions, text='Game Replay')
        replayOptions.create_window(200, 20,window=label)

        manReplay = tk.Button(replayOptions, text='Manual Replay')
        replayOptions.create_window(100, 50, window=manReplay)

        options = [
            2,
            4,
            6,
            8,
            10
        ]

        delay.set(2)

        drop = ttk.OptionMenu(replayOptions, delay, options[0], *options)
        replayOptions.create_window(340, 50, window=drop)

        autoReplay = tk.Button(replayOptions, text='Auto Replay')
        replayOptions.create_window(290, 50, window=autoReplay)

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

        if (self.gameType == 12):
            board.create_line((20, 20), (175, 160), fill='black')
            board.create_line((480, 20), (315, 160), fill='black')
            board.create_line((20, 480), (175, 340), fill='black')
            board.create_line((480, 480), (315, 340), fill='black')

        #draw board
        #add Buttons to dict
        for value in self.placements.values():
            value.append(tk.Button(board, text='O'))

        self.drawButtons(board, turn)

    def drawButtons(self, canvas, turn, origin=""):
        if canvas is None:
            raise ValueError("Canvas is None! Ensure it's properly initialized.")

        print(f"Canvas: {canvas}")  # 输出 canvas 对象，检查它是否有效

        for placement in self.placements.values():
            if placement[6] is None:
                placement[6] = tk.Button(canvas)  # 确保按钮是有效的

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
        #self.replayOptions()

    def onButtonPress(self, button, canvas, turn, origin):
        # 确保 canvas 是有效的
        if canvas is None:
            raise ValueError("Canvas is None! Ensure it's properly initialized.")

        # 获取当前回合
        whoseTurn = turn.getTurn()

        # 根据回合选择玩家的棋子
        if whoseTurn == "white":
            bankPieces = white.getBankPieces()
            boardPieces = white.getPlayerPieces()
        else:
            bankPieces = black.getBankPieces()
            boardPieces = black.getPlayerPieces()

        # 如果 origin 为空，则尝试放置棋子
        if origin == "":
            if bankPieces != 0:
                if button[0] == "open":
                    # 白色棋子或黑色棋子的放置逻辑
                    if whoseTurn == "black" and black.getBankPieces() != 0:
                        black.bankUpdate()
                        button[0] = "black"
                        self.writeToFile(whoseTurn + ': ' + button[4] + '\n')
                        turn.changeTurn()
                    elif whoseTurn == "white" and white.getBankPieces() != 0:
                        white.bankUpdate()
                        button[0] = "white"
                        self.writeToFile(whoseTurn + ': ' + button[4] + '\n')
                        turn.changeTurn()
            else:
                # 如果没有棋子，则尝试更改棋子位置
                if button[0] == whoseTurn:
                    origin = button[4]  # 更新起始位置
        else:
            # 当 origin 非空时，尝试移动棋子
            if button[0] == whoseTurn:
                origin = button[4]  # 更新起始位置
            elif boardPieces > 3 and button[4] in self.placements[origin][5]:
                if self.move_piece(origin, button[4]):
                    self.writeToFile(whoseTurn + ': ' + origin + ' to ' + button[4] + '\n')
                    origin = ""  # 移动后清空 origin
                    turn.changeTurn()
            elif boardPieces <= 3:
                if self.move_piece(origin, button[4]):
                    self.writeToFile(whoseTurn + ': ' + origin + ' to ' + button[4] + '\n')
                    origin = ""  # 移动后清空 origin
                    turn.changeTurn()

        # 更新界面
        self.currentTurn(turn.getTurn())
        self.banks()
        self.checkMills()

        # 确保 canvas 被正确传递给 drawButtons
        self.drawButtons(canvas, turn, origin)

        # 检查游戏是否结束
        game.gameOver(black.getPlayerPieces(), white.getPlayerPieces())

    def checkMills(self):
        # list of mills has been moved to be a class-level variable to allow for differences
        # between 9 mens morris and 12 mens morris

        whiteMills = []
        blackMills = []

        for mill in self.mills:
            if self.placements[mill[0]][0] == "white" and self.placements[mill[1]][0] == "white" and self.placements[mill[2]][
                0] == "white":
                if self.placements[mill[0]][1] != "whiteMill" or self.placements[mill[1]][1] != "whiteMill" or \
                        self.placements[mill[2]][1] != "whiteMill":
                    self.writeToFile('white mill: ' + self.placements[mill[0]][4] + ', ' + self.placements[mill[1]][4] + ', ' + self.placements[mill[2]][4] + '\n')
                    self.removeOpponentPiece("black")
                whiteMills.append(mill)
            elif self.placements[mill[0]][0] == "black" and self.placements[mill[1]][0] == "black" and self.placements[mill[2]][0] == "black":
                if self.placements[mill[0]][1] != "blackMill" or self.placements[mill[1]][1] != "blackMill" or self.placements[mill[2]][1] != "blackMill":
                    self.writeToFile('black mill: ' + self.placements[mill[0]][4] + ', ' + self.placements[mill[1]][4] + ', ' + self.placements[mill[2]][4] + '\n')
                    self.removeOpponentPiece("white")
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

            if self.gameType == 9:
                if to_pos not in self.placements[from_pos][5]:
                    print(f"Invalid move for 9 Men's Morris: {to_pos} is not directly connected to {from_pos}.")
                    return False
                elif self.gameType == 12:
                    if to_pos not in self.placements[from_pos][5]:
                        print(f"Invalid move for 12 Men's Morris: {to_pos} is not connected to {from_pos}.")
                        return False

            self.placements[to_pos][0] = self.placements[from_pos][0]
            self.placements[to_pos][6].config(text="", height=3, width=5, bg=self.placements[to_pos][0])

            self.placements[from_pos][0] = 'open'
            self.placements[from_pos][6].config(text="O", height=1, width=3, bg="SystemButtonFace")

            return True
        else:
            print("Invalid move: the target position is not open or the source position does not have a piece.")
            return False

    def removeOpponentPiece(self, opponent_color):
        # 获取所有可以移除的棋子，排除已形成"mill"的棋子
        removable_pieces = [key for key, value in self.placements.items() if
                            value[0] == opponent_color and value[1] != f"{opponent_color}Mill"]

        # 如果没有可移除的棋子，尝试移除所有棋子
        if not removable_pieces:
            removable_pieces = [key for key, value in self.placements.items() if value[0] == opponent_color]

        # 如果没有棋子可移除，打印提示信息并返回
        if not removable_pieces:
            print(f"No pieces to remove for {opponent_color}.")
            return

        # 使用弹窗让用户选择移除的棋子
        piece_to_remove = simpledialog.askstring("Remove Piece",
                                                 f"Select a piece to remove from {opponent_color}:\n" + "\n".join(
                                                     removable_pieces))

        # 如果用户输入无效，给出提示并返回
        if not piece_to_remove or piece_to_remove not in removable_pieces:
            print(f"Invalid or empty piece selected: {piece_to_remove}.")
            return

        # 更新棋盘上的位置为 'open'，表示棋子已被移除
        self.placements[piece_to_remove][0] = 'open'

        # 确保该位置有关联的 Tkinter 按钮并更新其显示
        if len(self.placements[piece_to_remove]) > 6:  # 确保索引 6 存在，避免索引错误
            button = self.placements[piece_to_remove][6]
            if button:
                button.config(text="O", height=1, width=3, bg="SystemButtonFace")

        # 更新玩家的棋子数量
        if opponent_color == "white":
            white.pieceUpdate()  # 更新白色玩家的棋子数量
            self.writeToFile(f'black removed: {piece_to_remove}\n')  # 记录动作到文件
        elif opponent_color == "black":
            black.pieceUpdate()  # 更新黑色玩家的棋子数量
            self.writeToFile(f'white removed: {piece_to_remove}\n')  # 记录动作到文件

        # 打印移除棋子的日志
        print(f"Removed {opponent_color} piece at {piece_to_remove}.")

    def AutoPlay(self, canvas, turn, origin):
        print("it's the computer's turn")
        choice = random.choice(list(self.placements.keys()))
        self.onButtonPress(self.placements[choice], canvas, turn, origin)
        
    def writeToFile(self, turnInfo):
        self.gamefile = open('gamefile.txt', 'a')
        self.gamefile.write(turnInfo)
        self.gamefile.close()

