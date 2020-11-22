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

    def set_next(self, detail: Field):
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

    def start(self):  # TODO: Artem's task
        """
        Starts after clicking "START".
        """
        """
        TODO: Here is initialising of the game
        """
        self.window.overlay.start.pack_forget()
        self.window.bind('<KeyPress>', self.key_press)
        # Examples TODO: Remove after reading\
        self.up_score()
        self.up_lvl()
        self.set_next(Field(1))  # Isn't ready
        Field.draw_block(self, 0, 0, 1)
        Field.draw_block(self, 1, 0, 2)
        Field.draw_block(self, 0, 1, 3)
        Field.draw_block(self, 2, 1, 4)
        """
        TODO: Here is the main process of the game
        (can allocate into the separate method
        """
