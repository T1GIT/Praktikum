import tkinter as tk

from config import Configuration as conf


class Game(tk.Canvas):
    def __init__(self, window):
        self.window = window
        super().__init__(master=window,
                         width=conf.SIZE // 2,
                         height=conf.SIZE,
                         bg=conf.FG_CLR,
                         highlightthickness=0)
        self.pack_propagate(False)
        self.config(highlightbackground=conf.BG_CLR)
        self.pack(side=tk.LEFT)

    def start(self):
        self.window.overlay.counter.raise_score()
        self.window.overlay.counter.raise_lvl()


class Detail:
    TYPES = [
        [
            [1, 1, 1, 1]
        ], [
            [1, 1, 1],
            [0, 1, 0]
        ], [
            [1, 1],
            [1, 1]
        ], [
            [1, 1, 1, 1],
            [1, 0, 0, 0]
        ], [
            [0, 1, 1],
            [1, 1, 0]
        ]
    ]

    def __init__(self, detail_type: int):
        """
        Creates new figure and draw it into the field
        :param type: | - 0, ┳ - 2, ■ - 3, ┏ - 4, ⚡ - 5
        """
        pass

    def rotate(self):
        pass

    def move(self, direction: int):  # 0 - down, 1 - left, 2 - right
        pass

    def fall(self):
        pass

