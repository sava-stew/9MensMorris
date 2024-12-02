import tkinter as tk

class SetUp():
    gameType = 9
    placements = {}
    mills = []

    nineMensPlacements = {
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

    twelveMensPlacements = {
        'g1': ['open', 'noMill', 20, 20, "g1", ["g4","d1","f2","e3","d7"]],
        'g4': ['open', 'noMill', 245, 20, "g4", ["g1","g7","f4"]],
        'g7': ['open', 'noMill', 480, 20, "g7", ["g4","d4","f6","e5","d1"]],
        'f2': ['open', 'noMill', 105, 90, "f2", ["f4","d2","e3","c5"]],
        'f4': ['open', 'noMill', 245, 90, "f4", ["f2","g4","f6","e4"]],
        'f6': ['open', 'noMill', 385, 90, "f6", ["f4","d6","e5","c3"]],
        'e3': ['open', 'noMill', 175, 160, "e3", ["e4","d3","f2","g1"]],
        'e4': ['open', 'noMill', 245, 160, "e4", ["e3","f4","e5"]],
        'e5': ['open', 'noMill', 315, 160, "e5", ["e4","d5","f6","g7"]],
        'd1': ['open', 'noMill', 20, 245, "d1", ["g1","d2","a1","g7"]],
        'd2': ['open', 'noMill', 105, 245, "d2", ["d1","f2","d3","b2"]],
        'd3': ['open', 'noMill', 175, 245, "d3", ["d2","e3","c3"]],
        'd5': ['open', 'noMill', 315, 245, "d5", ["e5","d6","c5"]],
        'd6': ['open', 'noMill', 385, 245, "d6", ["d5","f6","d7","b6"]],
        'd7': ['open', 'noMill', 480, 245, "d7", ["d6","g7","a7","g1"]],
        'c3': ['open', 'noMill', 175, 340, "c3", ["d3","c4","f6","a1"]],
        'c4': ['open', 'noMill', 245, 340, "c4", ["c3","c5","b4"]],
        'c5': ['open', 'noMill', 315, 340, "c5  ", ["c4","d5","f2","a7"]],
        'b2': ['open', 'noMill', 105, 410, "b2", ["d2","b4"]],
        'b4': ['open', 'noMill', 245, 410, "b4", ["b2","c4","a4","b6"]],
        'b6': ['open', 'noMill', 385, 410, "b6", ["b4","d6","a7"]],
        'a1': ['open', 'noMill', 20, 480, "a1", ["a4","d1","b2","c3"]],
        'a4': ['open', 'noMill', 245, 480, "a4", ["a1","b4","a7"]],
        'a7': ['open', 'noMill', 480, 480, "a7", ["a4","d7","b6","c5"]]
    }

    nineMensMills = [('g1', 'g4', 'g7'),
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

    twelveMensMills = [('g1', 'g4', 'g7'),
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
                       ('g7', 'd7', 'a7'),
                       ('a1', 'b2', 'c3'),
                       ('g1', 'f2', 'e3'),
                       ('g7', 'f6', 'e5'),
                       ('a7', 'b6', 'c5')
                       ]

    def quit(self):
        quit()

    def setUpBoard(self, num):
        self.gameType = num
        if self.gameType == 9:
            self.placements = self.nineMensPlacements
            self.mills = self.nineMensMills
        else:
            self.placements = self.twelveMensPlacements
            self.mills = self.twelveMensMills

    def closeWindow(self, window):
        window.quit()

    def setUpWindow(self):
        window=tk.Tk()

        window.title('Game Options')

        window_width = 400
        window_height= 150
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        center_x = int(screen_width/2 - window_width/2)
        center_y = int(screen_height/2 - window_height/2)

        window.columnconfigure(0, weight=1)
        window.columnconfigure(1, weight=1)
        window.columnconfigure(2, weight=1)
        window.rowconfigure(0, weight=1)
        window.rowconfigure(1, weight=1)

        window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        gameSelect = tk.Label(window, text='Please select which game you would like to play')
        gameSelect.grid(column=1, row=0)

        options = tk.Canvas(window)
        options.columnconfigure(0, weight=1)
        options.columnconfigure(1, weight=1)
        options.rowconfigure(0, weight=1)
        options.grid(column=1, row=1)

        nineMens = tk.Button(options, text='9 Mens Morris', command=lambda: [self.setUpBoard(9), self.closeWindow(window)])
        nineMens.grid(column=0, row=0)
        twelveMens = tk.Button(options, text='12 Mens Morris', command=lambda: [self.setUpBoard(12), self.closeWindow(window)])
        twelveMens.grid(column=1, row=0)

        window.protocol("WM_DELETE_WINDOW", self.quit)

        window.mainloop()




