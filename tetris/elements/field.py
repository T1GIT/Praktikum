import tkinter as tk

from config import Configuration as conf


class Field:
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
    DTL_SIZE = conf.HEIGHT // conf.FIELD_HEIGHT

    def __init__(self, canvas):
        """
        Creates new figure and draw it into the field
        :param canvas: where should draw figures
        """
        self.cvs = canvas

    def spawn(self):  # TODO: Artem's task
        """
        Draw and remember new moving element.
        """
        pass

    def clear_full(self):  # TODO: Artem's task
        """
        Erase full lines from the canvas and removes its objects from the memory.
        Increments the Score
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
        print("Rotate")
        pass

    def fall(self):
        print("Fall")
        pass

    def move(self):
        pass

    @staticmethod
    def draw_block(canvas: tk.Canvas, x: int, y: int, color: int):
        raw_x0 = x * Field.DTL_SIZE + conf.DTL_OFFSET
        raw_y0 = y * Field.DTL_SIZE + conf.DTL_OFFSET
        raw_x1 = raw_x0 + Field.DTL_SIZE - conf.DTL_OFFSET * 2
        raw_y1 = raw_y0 + Field.DTL_SIZE - conf.DTL_OFFSET * 2

        canvas.create_rectangle(raw_x0, raw_y0, raw_x1, raw_y1,
                                fill=conf.DTL_CLR[color],
                                outline=conf.DTL_BRD_CLR[color],
                                width=conf.DTL_OFFSET * 2)

