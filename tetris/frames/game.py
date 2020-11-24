import tkinter as tk

from config import Configuration as conf
from field import Field


class Game(tk.Canvas):
    def __init__(self, window):
        self.window = window
        super().__init__(master=window,
                         width=conf.HEIGHT * conf.FIELD_WIDTH // conf.FIELD_HEIGHT,
                         height=conf.HEIGHT,
                         bg=conf.FG_CLR,
                         highlightthickness=0)
        self.pack_propagate(False)
        self.config(highlightbackground=conf.BG_CLR)
        self.pack(side=tk.LEFT)
        self.field = Field(self)
        self.counter = self.window.overlay.counter
        self.next = self.window.overlay.next

    def key_press(self, event):
        if event.keysym == 'Left':
            self.field.left()
        elif event.keysym == 'Right':
            self.field.right()
        elif event.keysym == 'Up':
            self.field.rotate()
        elif event.keysym == 'Down':
            self.field.fall()

    def start(self):  # TODO: Artem's task
        """
        Starts after clicking "START".
        """
        """
        TODO: Here is initialising of the game
        """
        self.window.overlay.start.pack_forget()
        self.next.generate()
        self.window.bind('<KeyPress>', self.key_press)
        # -----------------------------------------------------Examples TODO: Remove after reading
        self.counter.raise_score()
        self.counter.raise_level()
        self.field.spawn(self.next.pop())
        # ----------------------------------------------------End of examples
        """
        TODO: Here is the main process of the game
        (can allocate into the separate method
        """
