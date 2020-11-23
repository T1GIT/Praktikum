import tkinter as tk

from tetris.config import Configuration as conf
from tetris.frames.game import Game
from tetris.frames.overlay import Overlay


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        width = conf.HEIGHT * conf.FIELD_WIDTH // conf.FIELD_HEIGHT + conf.OVERLAY_WIDTH
        height = conf.HEIGHT
        self.geometry(f"{width}x{height}")
        self.resizable(width=False, height=False)
        self.title("TETRIS")
        self.overlay = Overlay(self)
        self.game = Game(self)

