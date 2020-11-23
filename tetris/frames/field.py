import tkinter as tk

from config import Configuration as conf


class Field:
    def __init__(self, canvas):
        """
        Creates new figure and draw it into the field
        :param canvas: where should draw figures
        """
        self.cvs = canvas
        self.fallen = [[None] * conf.FIELD_WIDTH] * conf.FIELD_HEIGHT
        self.moving = None

    def spawn(self, dtl_type: int):
        """
        Draws and remembers new moving element.
        :param dtl_type: number of the detail type
        """
        template = conf.DTL_TYPES[dtl_type]
        width = len(template[0])
        height = len(template)
        left_margin = (conf.FIELD_WIDTH - width) // 2
        self.moving = [[None] * width] * height
        for row_ind, row in enumerate(template):
            for col_ind, col in enumerate(row):
                if col == 1:
                    block = self.draw_block(
                        canvas=self.cvs,
                        x=left_margin + col_ind,
                        y=-height + row_ind,
                        color=dtl_type
                    )
                    block.x = col_ind
                    block.y = row_ind
                    self.moving[row_ind][col_ind] = block

    def clear_full(self):  # TODO: Artem's task
        """
        Erase full lines from the canvas and removes its objects from the memory.
        Increases the score and the level
        """

    def is_lose(self) -> bool:  # TODO: Artem's task
        """
        Checks if game is finished.
        :return: True if the top stroke has part of a detail, else - False.
        """
        pass

    def left(self):
        print("left")
        pass

    def right(self):
        print("Right")
        pass

    def rotate(self):
        # ...
        return[list(t) for t in zip(*reversed(self.moving))]

    def fall(self):
        """
        Clears moving element and places its blocks into the fallen
        """
        print("Fall")
        pass

    def move(self):
        pass

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
