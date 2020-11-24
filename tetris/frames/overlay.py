import random as rnd
import tkinter as tk

from config import Configuration as Conf


class Overlay(tk.Frame):
    def __init__(self, window):
        self.window = window
        super().__init__(window,
                         width=Conf.OVERLAY_WIDTH,
                         height=Conf.WIN_HEIGHT,
                         bg=Conf.BG_CLR)
        self.pack_propagate(False)
        self.config(highlightbackground=Conf.BG_CLR)
        self.pack(side=tk.RIGHT, fill=tk.Y)
        self.next = Next(self)
        self.counter = Counter(self)
        self.start = Button(self)


class Next(tk.Frame):
    def __init__(self, overlay):
        self.overlay = overlay
        super().__init__(overlay,
                         width=Conf.WIN_HEIGHT // 4,
                         bg=Conf.BG_CLR)
        self.pack(fill=tk.BOTH)
        self.next = tk.Label(self,
                             text="NEXT", fg=Conf.TXT_CLR, bg=Conf.BG_CLR,
                             font=("Ariel", Conf.WIN_HEIGHT // 30))
        self.next.pack(pady=Conf.WIN_HEIGHT // 30)
        self.size = Conf.WIN_HEIGHT // 6
        self.next_el = tk.Canvas(self,
                                 width=self.size,
                                 height=self.size,
                                 bg=Conf.BG_CLR, highlightthickness=0)
        self.next_el.pack()
        self.next_el.create_rectangle(0, 0, self.size - 1, self.size - 1, outline=Conf.FG_CLR)
        self.template = [[]]
        self.dtl_type = -1

    def generate(self):
        """
        Draws next dropping frames in the overlay
        """
        self.dtl_type = rnd.randint(0, len(Conf.DTL_TYPES) - 1)
        self.template = Conf.DTL_TYPES[self.dtl_type]
        for _ in range(rnd.randint(0, 3)):
            self.template = [list(t) for t in zip(*reversed(self.template))]
        # TODO: Must to draw this figure

    def pop(self):
        last_temp = self.template
        last_type = self.dtl_type
        self.generate()
        return last_temp, last_type


class Counter(tk.Frame):
    def __init__(self, overlay):
        self.overlay = overlay
        super().__init__(overlay,
                         width=Conf.WIN_HEIGHT // 4,
                         bg=Conf.BG_CLR)
        self.pack(fill=tk.BOTH, pady=Conf.WIN_HEIGHT // 20)

        def counter_lbl(text):
            lbl = tk.Label(self,
                           text=text, fg=Conf.TXT_CLR, bg=Conf.BG_CLR,
                           font=("Ariel", Conf.WIN_HEIGHT // 40))
            lbl.pack()
            return lbl

        self.score = counter_lbl("SCORE")
        self.score_msr = counter_lbl("0")
        self.lvl = counter_lbl("LEVEL")
        self.lvl_msr = counter_lbl("1")

    def raise_score(self, delta):
        self.score_msr["text"] = str(int(self.score_msr["text"]) + delta)

    def raise_level(self):
        self.lvl_msr["text"] = str(int(self.lvl_msr["text"]) + 1)

    def get_interval(self) -> int:
        level = int(self.lvl_msr["text"])
        return int((0.8 - ((level - 1) * 0.007)) ** (level - 1) * 1000)


class Button(tk.Button):
    def __init__(self, overlay):
        self.overlay = overlay
        super().__init__(overlay,
                         text="START", font=("Ariel", Conf.WIN_HEIGHT // 40),
                         width=10,
                         height=1,
                         fg=Conf.BG_CLR, bg=Conf.FG_CLR,
                         relief=tk.FLAT,
                         command=self.click)
        self.pack(side=tk.BOTTOM, pady=Conf.WIN_HEIGHT // 20)

    def click(self):
        self.overlay.window.game.start()
