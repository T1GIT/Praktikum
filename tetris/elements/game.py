import tkinter as tk

from config import Configuration as conf
from detail import Detail


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
        Rises up score number in the side panel.
        """
        self.window.overlay.counter.raise_score(delta)

    def up_lvl(self):
        """
        Rises up level number in the side panel.
        """
        self.window.overlay.counter.raise_lvl()

    def set_next(self, detail: Detail):
        """
        Rising up score number in the side panel.
        :param detail: object to draw.
        """
        self.window.overlay.next.set(detail)

    def key_press(self, event):
        if event.keysym == 'Left':
            self.detail.left()
        elif event.keysym == 'Right':
            self.detail.right()
        elif event.keysym == 'Up':
            self.detail.rotate()
        elif event.keysym == 'Down':
            self.detail.fall()
        
    def spawn(self, detail: Detail):  # TODO: Artem's task
        """
        Draw and remember new moving element.
        :param detail: object that will appear on the top.
        """
        pass

    def is_lose(self) -> bool:  # TODO: Artem's task
        """
        Checks if game is finished.
        :return: True if the top stroke has part of a detail, else - False.
        """
        pass

    def clear_full(self):  # TODO: Artem's task
        """
        Erase full lines from the canvas and removes its objects from the memory.
        Increments the Score
        """

    def start(self):  # TODO: Artem's task
        """
        Starts after clicking "START".
        """
        """
        TODO: Here is initialising of the game
        """
        self.window.overlay.start.pack_forget()
        self.window.bind('<KeyPress>', self.key_press)
        # Examples TODO: Remove after reading
        self.detail = Detail(1)
        self.up_score()
        self.up_lvl()
        self.set_next(Detail(1))  # Isn't ready
        """
        TODO: Here is the main process of the game
        (can allocate into the separate method
        """
