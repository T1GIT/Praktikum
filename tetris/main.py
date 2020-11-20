from tetris.elements import Window


class Configuration:
    # Settings
    BG_CLR = "black"
    FG_CLR = "gray"
    TXT_CLR = "white"
    ELEMENTS = ["red", "blue", "yellow", "pink", "green"]
    START_INTERVAL = 100  # ms
    SIZE = 500


class Tetris:
    def __init__(self):
        self.root = Window(Configuration)

    def start(self):
        self.root.mainloop()


if __name__ == "__main__":
    tetris = Tetris()
    tetris.start()
