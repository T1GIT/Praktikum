import tkinter as tk

from config import Configuration as conf
from elements.game import Game, Detail


class Overlay(tk.Frame):
    def __init__(self, window):
        self.window = window
        super().__init__(window,
                         width=conf.SIZE // 4,
                         height=conf.SIZE,
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
                         width=conf.SIZE // 4,
                         bg=conf.BG_CLR)
        self.pack(fill=tk.BOTH)
        self.next = tk.Label(self,
                                 text="NEXT", fg=conf.TXT_CLR, bg=conf.BG_CLR,
                                 font=("Ariel", conf.SIZE // 30))
        self.next.pack(pady=conf.SIZE // 30)
        size = conf.SIZE // 6
        self.next_el = tk.Canvas(self, width=size, height=size, bg=conf.BG_CLR, highlightthickness=0)
        self.next_el.pack()
        self.next_el.create_rectangle(0, 0, size - 1, size - 1, outline=conf.FG_CLR)

    def set(self, element: Detail):
        pass  # TODO: F: drawing next dropping element in the overlay


class Counter(tk.Frame):
    def __init__(self, overlay):
        self.overlay = overlay
        super().__init__(overlay,
                         width=conf.SIZE // 4,
                         bg=conf.BG_CLR)
        self.pack(fill=tk.BOTH, pady=conf.SIZE // 10)

        def counter_lbl(text):
            lbl = tk.Label(self,
                           text=text, fg=conf.TXT_CLR, bg=conf.BG_CLR,
                           font=("Ariel", conf.SIZE // 40))
            lbl.pack()
            return lbl

        self.score = counter_lbl("SCORE")
        self.score_msr = counter_lbl("0")
        self.lvl = counter_lbl("LEVEL")
        self.lvl_msr = counter_lbl("1")

    def raise_score(self, delta=1):
        self.score_msr["text"] = str(int(self.score_msr["text"]) + delta)

    def raise_lvl(self):
        self.lvl_msr["text"] = str(int(self.lvl_msr["text"]) + 1)


class Button(tk.Button):
    def __init__(self, overlay):
        self.overlay = overlay
        super().__init__(overlay,
                         text="START", font=("Ariel", conf.SIZE // 40),
                         width=conf.SIZE // 50,
                         fg=conf.TXT_CLR, bg=conf.BG_CLR,
                         command=self.click)
        self.pack(side=tk.BOTTOM, pady=conf.SIZE // 50)

    def click(self):
        self.overlay.window.game.start()
