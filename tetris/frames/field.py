import tkinter as tk

from tetris.config import Configuration as conf


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

    def clear_full(self):  # TODO: Artem's task
        """
        Erase full lines from the canvas and removes its objects from the memory.
        Increases the score and the level
        """
        fulls = 0
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
                    # print(self.cvs.coords(j)[2] // conf.DTL_SIZE, self.cvs.coords(j)[3] // conf.DTL_SIZE)
                    self.cvs.move(j, conf.DTL_SIZE, 0)
        return True

    def rotate(self):
        # ...
        return [list(t) for t in zip(*reversed(self.moving))]

    def fall(self):
        """
        Clears moving element and places its blocks into the fallen
        """
        self.is_fallen = True
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
        if self.is_fallen:
            return False
        for q in reversed(self.moving):
            for k in q:
                if k is not None:
                    x = int(self.cvs.coords(k)[2] // conf.DTL_SIZE)
                    y = int(self.cvs.coords(k)[3] // conf.DTL_SIZE)
                    if 0 <= y < 20 and 0 <= x < 20:
                        if y > conf.FIELD_HEIGHT - 2 or self.fallen[y + 1][x] is not None:
                            self.fall()
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
