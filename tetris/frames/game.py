import tkinter as tk
import time

from config import Configuration as Conf
from field import Field


class Game(tk.Canvas):
    def __init__(self, window):
        self.window = window
        super().__init__(master=window,
                         width=Conf.WIN_WIDTH - Conf.OVERLAY_WIDTH,
                         height=Conf.WIN_HEIGHT,
                         bg=Conf.FG_CLR,
                         highlightthickness=0)
        self.pack_propagate(False)
        self.config(highlightbackground=Conf.BG_CLR)
        self.pack(side=tk.LEFT)
        self.field = Field(self)
        self.counter = self.window.overlay.counter
        self.next = self.window.overlay.next
        self.pause = False
        self.interval = self.counter.get_interval()
        self.lines = 0

    def key_press(self, event):
        char = event.keysym.lower()
        fld = self.field
        if char == 'left':
            if fld.can_move(-1, 0):
                fld.left()
        elif char == 'right':
            if fld.can_move(1, 0):
                fld.right()
        elif char == 'up':
            if fld.can_rotate():
                fld.rotate()
        elif char == 'down':
            if fld.can_move():
                fld.move()
        elif char == "p":
            self.pause = not self.pause
        elif char == "r":
            self.reset()

    def start(self):
        """
        Starts after clicking "START".
        """
        self.window.overlay.start.pack_forget()
        self.next.generate()
        self.field.spawn(*self.next.pop())
        self.window.bind('<KeyPress>', self.key_press)
        self.process()

    def process(self):
        self.interval = 10
        if not self.pause:
            print(self.field.can_move())
            if self.field.can_move():
                self.field.move()
            else:
                print(self.field.fallen[0])
                self.field.fall()
                print(self.field.fallen[0])
                new_lines = self.field.clear_full()
                self.counter.raise_score(Conf.POINTS_FOR_LINES[new_lines])
                self.lines += new_lines
                if self.lines >= Conf.LEVEL_CONDITION:
                    self.lines -= Conf.LEVEL_CONDITION
                    self.counter.raise_level()
                    self.interval = self.counter.get_interval()
                self.field.spawn(*self.next.pop())
        if not self.field.is_lose():
            self.window.after(self.interval, self.process)
