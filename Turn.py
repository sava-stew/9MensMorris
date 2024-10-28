import tkinter as tk
from tkinter import ttk



class Turn():
    def __init__(self):
        self.color = "white"

    def changeTurn(self):
        if self.color == "white":
            self.color = "black"
        else:
            self.color = "white"
        return

    def getTurn(self):
        return self.color
