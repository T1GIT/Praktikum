import random as rnd
import tkinter as tk

from config import Configuration as conf
from frames.field import Field as fl


class Overlay(tk.Frame):
    def __init__(self, window):
        self.window = window
        super().__init__(window,
                         width=conf.OVERLAY_WIDTH,
                         height=conf.HEIGHT,
                         bg=conf.BG_CLR)
        self.pack_propagate(False)
        self.config(highlightbackground=conf.BG_CLR)
        self.pack(side=tk.RIGHT, fill=tk.Y)
        self.next = Next(self)
        self.counter = Counter(self)
        self.start = Button(self)


class Next(tk.Frame):
    def __init__(self, overlay):
        self.overlay = overlay
        super().__init__(overlay,
                         width=conf.HEIGHT // 4,
                         bg=conf.BG_CLR)
        self.pack(fill=tk.BOTH)
        self.next = tk.Label(self,
                             text="NEXT", fg=conf.TXT_CLR, bg=conf.BG_CLR,
                             font=("Ariel", conf.HEIGHT // 30))
        self.next.pack(pady=conf.HEIGHT // 30)
        self.overlay._width = min(conf.OVERLAY_WIDTH * 3 // 4, conf.MAX_OVERLAY_WIDTH)
        self.next_el = tk.Canvas(self,
                                 width=self.overlay._width,
                                 height=self.overlay._width,
                                 bg=conf.BG_CLR, highlightthickness=0)
        self.next_el.pack()
        self.next_el.create_rectangle(0, 0, self.overlay._width - 1, self.overlay._width - 1, outline=conf.FG_CLR)
        self.dtl_type = None
        self.block = []

    def generate(self):
        """
        Draws next dropping frames in the overlay
        """
        ext = 0
        self.dtl_type = rnd.randint(0, len(conf.DTL_TYPES) - 1)
        width = len(conf.DTL_TYPES[self.dtl_type][0])
        left_margin = 2 - width / 2
        if width < 3:
            ext = 1
        elif width > 3:
            ext = -1
        for row_ind, row in enumerate(conf.DTL_TYPES[self.dtl_type]):
            for col_ind, col in enumerate(row):
                if col == 1:
                    self.block.append(fl.draw_block(
                        canvas=self.next_el,
                        x=left_margin + col_ind,
                        y=ext + row_ind,
                        color=self.dtl_type
                    ))

    def pop(self):
        last_type = self.dtl_type
        for el in self.block:
            self.next_el.delete(el)
        self.block = []
        self.generate()
        return last_type


class Counter(tk.Frame):
    def __init__(self, overlay):
        self.overlay = overlay
        super().__init__(overlay,
                         width=conf.HEIGHT // 4,
                         bg=conf.BG_CLR)
        self.pack(fill=tk.BOTH, pady=conf.HEIGHT // 10)
        self.score_ind = 0
        self.level_ind = conf.START_LEVEL

        def counter_lbl(text):
            lbl = tk.Label(self,
                           text=text, fg=conf.TXT_CLR, bg=conf.BG_CLR,
                           font=("Ariel", conf.HEIGHT // 40))
            lbl.pack()
            return lbl

        self.score = counter_lbl("SCORE")
        self.score_msr = counter_lbl("0")
        self.lvl = counter_lbl("LEVEL")
        self.lvl_msr = counter_lbl(str(conf.START_LEVEL))

    def raise_score(self, delta=1):
        self.score_msr["text"] = str(int(self.score_msr["text"]) + delta)
        self.score_ind += (delta // 100)

    def raise_level(self):
        self.lvl_msr["text"] = str(int(self.lvl_msr["text"]) + 1)
        self.level_ind += 1


class Button(tk.Button):
    def __init__(self, overlay):
        self.overlay = overlay
        super().__init__(overlay,
                         text="START", font=("Ariel", conf.HEIGHT // 40),
                         width=self.overlay._width // 10,
                         fg=conf.BG_CLR, bg=conf.FG_CLR,
                         relief=tk.FLAT,
                         command=self.click)
        self.pack(side=tk.BOTTOM, pady=self.overlay._width // 6)

    def click(self):
        self.overlay.window.game.start()
