import tkinter as tk

from config import Configuration as Conf
from frames.game import Game
from frames.overlay import Overlay


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        width = Conf.WIN_WIDTH
        height = Conf.WIN_HEIGHT
        self.geometry(f"{width}x{height}")
        self.resizable(width=False, height=False)
        self.title("TETRIS")
        self.overlay = Overlay(self)
        self.game = Game(self)

