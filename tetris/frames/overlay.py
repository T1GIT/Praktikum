import random as rnd
import tkinter as tk

from config import Configuration as conf


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

    def generate(self):  # Artem's task
        """
        Draws next dropping frames in the overlay
        """
        self.dtl_type = rnd.randint(0, len(conf.DTL_TYPES) - 1)
        # TODO: Must to draw this figure

    def pop(self):
        last_type = self.dtl_type
        self.generate()
        return last_type


class Counter(tk.Frame):
    def __init__(self, overlay):
        self.overlay = overlay
        super().__init__(overlay,
                         width=conf.HEIGHT // 4,
                         bg=conf.BG_CLR)
        self.pack(fill=tk.BOTH, pady=conf.HEIGHT // 10)

        def counter_lbl(text):
            lbl = tk.Label(self,
                           text=text, fg=conf.TXT_CLR, bg=conf.BG_CLR,
                           font=("Ariel", conf.HEIGHT // 40))
            lbl.pack()
            return lbl

        self.score = counter_lbl("SCORE")
        self.score_msr = counter_lbl("0")
        self.lvl = counter_lbl("LEVEL")
        self.lvl_msr = counter_lbl("1")

    def raise_score(self, delta=1):
        self.score_msr["text"] = str(int(self.score_msr["text"]) + delta)

    def raise_level(self):
        self.lvl_msr["text"] = str(int(self.lvl_msr["text"]) + 1)


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
