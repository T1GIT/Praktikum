from frames.window import Window


class Tetris:
    def __init__(self):
        self.root = Window()

    def start(self):
        self.root.mainloop()


if __name__ == "__main__":
    tetris = Tetris()
    tetris.start()
