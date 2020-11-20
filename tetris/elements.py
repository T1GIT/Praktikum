import tkinter as tk


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

    def __init__(self, type: int):
        """
        Creates new figure and draw it into the field
        :param type: | - 0, ┳ - 2, ■ - 3, ┏ - 4, ⚡ - 5
        """
        pass

    def rotate(self, clockwise: bool):
        pass

    def move(self, direction: int):  # 0 - down, 1 - left, 2 - right
        pass

    def fall(self):
        pass


class Window(tk.Tk):
    def __init__(self, conf):
        super().__init__()
        self.conf = conf
        self.geometry(f"{conf.SIZE}x{conf.SIZE}")
        self.resizable(width=False, height=False)
        self.title("TETRIS")
        self.cvs_game = Game(self)
        self.frm_overlay = Overlay(self)


class Game(tk.Canvas):
    def __init__(self, window):
        self.window = window
        self.conf = window.conf
        width = height = self.conf.SIZE
        super().__init__(self, width=width, height=height, bg=self.conf.FG_CLR)
        self.pack_propagate(False)
        self.config(highlightbackground=self.conf.BG_CLR)
        self.pack(side=tk.LEFT)


class Overlay(tk.Frame):
    def __init__(self, window):
        self.window = window
        self.conf = window.conf
        width = height = self.conf.SIZE
        super().__init__(self, width=width, height=height, bg=self.conf.BG_CLR)
        self.pack_propagate(False)
        self.config(highlightbackground=self.conf.BG_CLR)
        self.pack(side=tk.RIGHT)
        self.pnl_next = Next(self)


class Next:
    def __init__(self, overlay):
        self.conf = overlay.conf
        self.lbl_next = tk.Label(overlay, text="NEXT", fg=self.conf.TXT_CLR, bg=self.conf.BG_CLR, font=("Ariel", 16))
        self.lbl_next.pack(pady=10)
        size = self.conf.SIZE / 5
        self.cvs_el = tk.Canvas(overlay, width=size, height=size, bg="white")  # TODO: bg=class_root.BG_CLR

    def set(self, element):
        pass  # TODO: F: drawing next dropping element in the overlay
