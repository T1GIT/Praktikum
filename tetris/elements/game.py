import tkinter as tk

from config import Configuration as conf


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

    def up_score(self, delta=1):
        """
        Rises up score number in the side panel
        """
        self.window.overlay.counter.raise_score(delta)

    def up_lvl(self):
        """
        Rises up level number in the side panel
        """
        self.window.overlay.counter.raise_lvl()

    def set_next(self, element: Detail):
        """
        Rising up score number in the side panel
        """
        self.window.overlay.next.set(element)

    def start(self):
        """
        Starts after clicking "START"
        """
        # Examples
        self.up_score()
        self.up_lvl()
        self.set_next(Detail(1))  # Isn't ready
