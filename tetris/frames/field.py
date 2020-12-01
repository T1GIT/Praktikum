import tkinter as tk

from config import Configuration as conf


class Field:
    def __init__(self, canvas):
        """
        Creates new figure and draw it into the field
        :param canvas: where should draw figures
        """
        self.cvs = canvas
        self.fallen = [[None] * conf.FIELD_WIDTH for _ in range(conf.FIELD_HEIGHT)]
        self.moving = None
        self.is_fallen = False

    def spawn(self, dtl_type: int):
        """
        Draws and remembers new moving element.
        :param dtl_type: number of the detail type
        """
        template = conf.DTL_TYPES[dtl_type]
        width = len(template[0])
        height = len(template)
        left_margin = (conf.FIELD_WIDTH - width) // 2
        self.moving = [[None] * width for _ in range(height)]
        for row_ind, row in enumerate(template):
            for col_ind, col in enumerate(row):
                if col == 1:
                    block = self.draw_block(
                        canvas=self.cvs,
                        x=left_margin + col_ind,
                        y=-height + row_ind,
                        color=dtl_type
                    )
                    self.moving[row_ind][col_ind] = block

    def clear_full(self):
        """
        Erase full lines from the canvas and removes its objects from the memory.
        Increases the score and the level
        """
        fulls = 0
        counter = 0
        while counter < conf.FIELD_HEIGHT:
            if None not in self.fallen[counter]:
                for i in self.fallen:
                    if self.fallen[counter] == i:
                        break
                    for j in i:
                        if j is not None:
                            self.cvs.move(j, 0, conf.DTL_SIZE)
                for i in self.fallen[counter]:
                    self.cvs.delete(i)
                self.fallen.remove(self.fallen[counter])
                self.fallen.insert(0, [None] * conf.FIELD_WIDTH)
                fulls += 1
            counter += 1
        return fulls

    def is_lose(self) -> bool:
        """
        Checks if game is finished.
        :return: True if the top stroke has part of a detail, else - False.
        """
        for k in self.fallen[0]:
            if k is not None:
                return True
        return False

    def left(self):
        if self.moving is None:
            return False
        for q in self.moving:
            for k in q:
                if k is not None:
                    x = int(self.cvs.coords(k)[2] // conf.DTL_SIZE)
                    y = int(self.cvs.coords(k)[3] // conf.DTL_SIZE)
                    if 0 <= y < 20 and 0 <= x < 20:
                        if self.cvs.coords(k)[2] < conf.DTL_SIZE or self.fallen[y][x - 1] is not None:
                            return False
        for i in self.moving:
            for j in i:
                if j is not None:
                    self.cvs.move(j, -conf.DTL_SIZE, 0)
        return True

    def right(self):
        if self.moving is None:
            return False
        for q in self.moving:
            for k in q:
                if k is not None:
                    x = int(self.cvs.coords(k)[2] // conf.DTL_SIZE)
                    y = int(self.cvs.coords(k)[3] // conf.DTL_SIZE)
                    if 0 <= y < 20 and 0 <= x < 20:
                        if self.cvs.coords(k)[2] > conf.HEIGHT * conf.FIELD_WIDTH // conf.FIELD_HEIGHT - conf.DTL_SIZE or self.fallen[y][x + 1] is not None:
                            return False
        for i in self.moving:
            for j in i:
                if j is not None:
                    self.cvs.move(j, conf.DTL_SIZE, 0)
        return True

    def rotate(self):
        buf_len = 0
        if self.moving is None:
            return self
        if len(self.moving) > 2:
            buf_len = len(self.moving)
        elif len(self.moving[0]) > 2:
            buf_len = len(self.moving[0])
        if buf_len > 2:
            if not self.can_rotate():
                return False
            for row_ind, row in enumerate(self.moving):
                for col_ind, col in enumerate(row):
                    if col is not None:
                        dx = len(self.moving) - row_ind - col_ind - 1
                        dy = col_ind - row_ind
                        self.cvs.move(col, dx * conf.DTL_SIZE, dy * conf.DTL_SIZE)
            self.moving = [list(t) for t in zip(*reversed(self.moving))]

    def can_rotate(self):
        for row_ind, row in enumerate(self.moving):
            for col_ind, col in enumerate(row):
                if col is not None:
                    x = int(self.cvs.coords(col)[0] // conf.DTL_SIZE)
                    y = int(self.cvs.coords(col)[1] // conf.DTL_SIZE)
                    dx = x + len(self.moving) - row_ind - col_ind - 1
                    dy = y + col_ind - row_ind
                    if not 0 <= dx < conf.FIELD_WIDTH:
                        return False
                    elif dy < 0:
                        continue
                    elif dy >= conf.FIELD_HEIGHT:
                        return False
                    elif self.fallen[dy][dx] is not None:
                        return False
        return True

    def fall(self):
        if self.moving is not None:
            self.move()

    def falling(self):
        """
        Clears moving element and places its blocks into the fallen
        """
        for i in reversed(self.moving):
            for j in reversed(i):
                if j is not None:
                    x = int(self.cvs.coords(j)[2] // conf.DTL_SIZE)
                    y = int(self.cvs.coords(j)[3] // conf.DTL_SIZE)
                    if 0 <= y < 20 and 0 <= x < 20:
                        if self.fallen[y][x] is None:
                            self.fallen[y][x] = j
        self.moving = None
        return True

    def move(self):
        """
        Move element on the field
        """
        if self.is_fallen or self.moving is None:
            return False
        for q in reversed(self.moving):
            for k in q:
                if k is not None:
                    x = int(self.cvs.coords(k)[2] // conf.DTL_SIZE)
                    y = int(self.cvs.coords(k)[3] // conf.DTL_SIZE)
                    if 0 <= y < 20 and 0 <= x < 20:
                        if y > conf.FIELD_HEIGHT - 2 or self.fallen[y + 1][x] is not None:
                            self.falling()
                            return False
        for i in self.moving:
            for j in i:
                if j is not None:
                    self.cvs.move(j, 0, conf.DTL_SIZE)
        return True

    @staticmethod
    def draw_block(canvas: tk.Canvas, x: int, y: int, color: int):
        raw_x0 = x * conf.DTL_SIZE + conf.DTL_OFFSET
        raw_y0 = y * conf.DTL_SIZE + conf.DTL_OFFSET
        raw_x1 = raw_x0 + conf.DTL_SIZE - conf.DTL_BORDER_WIDTH
        raw_y1 = raw_y0 + conf.DTL_SIZE - conf.DTL_BORDER_WIDTH
        return canvas.create_rectangle(raw_x0, raw_y0, raw_x1, raw_y1,
                                       fill=conf.DTL_CLR[color],
                                       outline=conf.DTL_BRD_CLR[color],
                                       width=conf.DTL_BORDER_WIDTH)
