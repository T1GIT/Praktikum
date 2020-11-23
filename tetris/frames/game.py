import tkinter as tk
import random as rnd

from tetris.config import Configuration as conf
from tetris.frames.field import Field


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
        self.window.overlay.start.pack_forget()
        self.next.generate()
        self.window.bind('<KeyPress>', self.key_press)
        self.field.spawn(self.next.pop())

        def action():
            if not self.field.is_lose():
                if not self.field.move():
                    self.field.is_fallen = False
                    self.field.spawn(self.next.pop())
            if self.field.clear_full():
                self.window.overlay.counter.raise_score()
                if int(self.window.overlay.counter.score_msr["text"] % 8 == 0):
                    self.window.overlay.counter.raise_level()
        self.loop(action)

    def loop(self, animation):
        def loop_move():
            animation()
            self.window.after(conf.START_INTERVAL, loop_move)

        return loop_move()
