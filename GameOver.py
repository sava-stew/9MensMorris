import tkinter as tk

class GameOver():
    def __init__(self):
        self.winner = None
        self.reset= False

    #function added to avoid clicking close button for each window opened
    def quit(self):
        quit()
        return False


    def replay(self, window):
        self.reset = True
        window.lower()
        window.quit()

    def gameOverWindow(self, player):
        window = tk.Tk() 
        
        window.title('Game Over!')

        window_width = 400
        window_height = 150
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        window.columnconfigure(0, weight=1)
        window.columnconfigure(1, weight=2)
        window.columnconfigure(2, weight=1)
        window.rowconfigure(0, weight=1)
        window.rowconfigure(1, weight=1)

        window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        winner_label = tk.Label(window, text=player + ' player has won!')
        winner_label.grid(column=1, row=0)

        options = tk.Canvas(window)
        options.columnconfigure(0, weight=1)
        options.columnconfigure(1, weight=1)
        options.rowconfigure(0, weight=1)
        options.grid(column=1, row=1)

        quit_button = tk.Button(options, text='Close', command=self.quit)
        quit_button.grid(column=0, row=0)

        replayButton = tk.Button(options, text="Watch Replay", command=lambda: self.replay(window))
        replayButton.grid(column=1, row=0)

        # Overrides default exit button to close all windows
        window.protocol("WM_DELETE_WINDOW", self.quit)

        return window

    def gameOver(self, blackPieces, whitePieces):
        if blackPieces < 3:
            self.winner = 'White'
            window = self.gameOverWindow(self.winner)
            window.mainloop()
            return True
        elif whitePieces < 3:
            self.winner = 'Black'
            window = self.gameOverWindow(self.winner)
            window.mainloop()
            return True
        else:
            self.winner = None  # Game not over
            return False

    def replayGameOver(self, winner):
        window = self.gameOverWindow(winner)
        window.mainloop()
