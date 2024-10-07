import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Label

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

        g1 = tk.Button(canvas, text='O', command=None)
        canvas.create_window(20, 20, window=g1)
        g4 = tk.Button(canvas, text='O', command=None)
        canvas.create_window(245, 20, window=g4)
        g7 = tk.Button(canvas, text='O', command=None)
        canvas.create_window(480, 20, window=g7)
        canvas.create_line((20, 20), (245, 20), fill='black')
        canvas.create_line((245, 20), (480, 20), fill='black')

        f2 = tk.Button(canvas, text='O', command=None)
        canvas.create_window(105, 90, window=f2)
        f4 = tk.Button(canvas, text='O', command=None)
        canvas.create_window(245, 90, window=f4)
        f6 = tk.Button(canvas, text='O', command=None)
        canvas.create_window(385, 90, window=f6)
        canvas.create_line((105, 90), (245, 90), fill='black')
        canvas.create_line((245, 90), (385, 90), fill='black')


        e3 = tk.Button(canvas, text='O', command=None)
        canvas.create_window(175, 160, window=e3)
        e4 = tk.Button(canvas, text='O', command=None)
        canvas.create_window(245, 160, window=e4)
        e5 = tk.Button(canvas, text='O', command=None)
        canvas.create_window(315, 160, window=e5)
        canvas.create_line((175, 160), (245, 160), fill='black')
        canvas.create_line((245, 160), (315, 160), fill='black')

        d1 = tk.Button(canvas, text='O', command=None)
        canvas.create_window(20, 245, window=d1)
        d2 = tk.Button(canvas, text='O', command=None)
        canvas.create_window(105, 245, window=d2)
        d3 = tk.Button(canvas, text='O', command=None)
        canvas.create_window(175, 245, window=d3)
        d5  = tk.Button(canvas, text='O', command=None)
        canvas.create_window(315, 245, window=d5)
        d6 = tk.Button(canvas, text='O', command=None)
        canvas.create_window(385, 245, window=d6)
        d7 = tk.Button(canvas, text='O', command=None)
        canvas.create_window(480, 245, window=d7)
        canvas.create_line((20, 245), (105, 245), fill='black')
        canvas.create_line((105, 245), (175, 245), fill='black')
        canvas.create_line((315, 245), (385, 245), fill='black')
        canvas.create_line((385, 245), (480, 245), fill='black')

        c3 = tk.Button(canvas, text='O', command=None)
        canvas.create_window(175, 340, window=c3)
        c4 = tk.Button(canvas, text='O', command=None)
        canvas.create_window(245, 340, window=c4)
        c5 = tk.Button(canvas, text='O', command=None)
        canvas.create_window(315, 340, window=c5)
        canvas.create_line((175, 340), (245, 340), fill='black')
        canvas.create_line((245, 340), (315, 340), fill='black')

        b2 = tk.Button(canvas, text='O', command=None)
        canvas.create_window(105, 410, window=b2)
        b4 = tk.Button(canvas, text='O', command=None)
        canvas.create_window(245, 410, window=b4)
        b6 = tk.Button(canvas, text='O', command=None)
        canvas.create_window(385, 410, window=b6)
        canvas.create_line((105, 410), (245, 410), fill='black')
        canvas.create_line((245, 410), (385, 410), fill='black')

        a1 = tk.Button(canvas, text='O', command=None)
        canvas.create_window(20, 480, window=a1)
        a4 = tk.Button(canvas, text='O', command=None)
        canvas.create_window(245, 480, window=a4)
        a7 = tk.Button(canvas, text='O', command=None)
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

