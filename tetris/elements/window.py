import tkinter as tk

from config import Configuration as conf
from elements.game import Game
from elements.overlay import Overlay


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        width = conf.SIZE * 3 // 4
        height = conf.SIZE
        self.geometry(f"{width}x{height}")
        self.resizable(width=False, height=False)
        self.title("TETRIS")
        self.overlay = Overlay(self)
        self.game = Game(self)

