from tetris.frames.window import Window


class Tetris:
    def __init__(self):
        self.root = Window()

    def start(self):
        self.root.mainloop()


if __name__ == "__main__":
    tetris = Tetris()
    tetris.start()
    # arr =[
    #     [1, 2, 3],
    #     [4, 5, 6],
    #     [7, 8, 9]
    # ]
    # for i in range(len(arr)):
    #     for j in range(len(arr[i])):
    #         print(arr[i][j])
