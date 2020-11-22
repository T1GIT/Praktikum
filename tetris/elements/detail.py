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

    def __init__(self, detail_type: int):
        """
        Creates new figure and draw it into the field
        :param detail_type: | - 0, ┳ - 2, ■ - 3, ┏ - 4, ⚡ - 5
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