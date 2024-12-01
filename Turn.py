import tkinter as tk
from tkinter import ttk

class Turn():
    def __init__(self, game_type="human"):
        self.color = "white"
        self.type = game_type
        self.turnType = "human"

    def changeTurn(self):
        if self.color == "white":
            self.color = "black"
        else:
            self.color = "white"
        if self.type == "computer":
            if self.turnType == "human":
                self.turnType = "computer"
            else:
                self.turnType = "human"
        return

    def getTurn(self):
        return self.color

    def getTurnType(self):
        return self.turnType
