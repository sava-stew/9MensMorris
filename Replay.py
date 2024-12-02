import tkinter as tk
from tkinter import *
from tkinter import ttk

class Replay():
    def replayWindow(self):
        window = tk.Tk()

        window.title('Replay Options')

        window_width = 600
        window_height= 150
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        center_x = int(screen_width/2 - window_width/2)
        center_y = int(screen_height/2 - window_height/2)

        window.columnconfigure(0, weight=1)
        window.columnconfigure(1, weight=2)
        window.columnconfigure(2, weight=1)
        window.rowconfigure(0, weight=1)
        window.rowconfigure(1, weight=1)

        window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        replayInstructions = tk.Label(window, text='Please select a method of replaying the game.\n')
        replayInstructions.grid(column=1, row=0)

        manReplay = tk.Button(window, text='Manual Replay')
        manReplay.grid(column=0, row=1)

        auto = tk.Canvas(window)
        auto.grid(column=2, row=1)

        auto.columnconfigure(0, weight=1)
        auto.columnconfigure(1, weight=1)
        auto.rowconfigure(0, weight=1)

        options = [
            2,
            4,
            6,
            8,
            10
        ]

        delay = IntVar()
        delay.set(2)

        autoReplay = tk.Button(auto, text='Auto Replay')
        autoReplay.grid(column=0, row=0)

        drop = ttk.OptionMenu(auto, delay, options[0], *options)
        drop.grid(column=1, row=0)

        #overrides default exit button to close all windows
        window.protocol("WM_DELETE_WINDOW", self.quit)

        return window

    def replay(self):
        window = self.replayWindow()
        window.mainloop()