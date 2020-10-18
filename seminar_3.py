import tkinter as tk
import time


class Poll(tk.Tk):
    # Settings
    BG = "black"
    START_INTERVAL = 200  # ms
    STICK_LEN = 40  # px (in the start)
    MARGIN = 20  # px
    GAMMA = 7  # [1; 10]
    CONTRAST = 7  # [1; 10]

    assert 0 <= GAMMA <= 10, "Gamma is out of range"
    assert 0 <= CONTRAST <= 10, "Contrast is out of range"
    CONTRAST /= 3
    HALF_STICK = STICK_LEN // 2

    def __init__(self, size):
        super().__init__()
        self.wm_title("Practicum of programming")
        self.size = size
        self.center = (size // 2 + 1, size // 2 + 1)
        self.cvs = tk.Canvas(self, width=size, height=size, bg=Poll.BG)
        self.engaged_points = set()
        self.empty_points = {(0, 0)}
        self.out = False
        self.paused = False
        self.zoom = 1
        self.interval = Poll.START_INTERVAL
        self.color = self.num_to_color(1)
        self.repeat = 1
        self.onstep = 0
        self.amount = 0

        self.cvs.bind("<Button-1>", self.start_pause)

    def start_pause(self, event):
        self.paused = not self.paused

    def to_raw(self, x, y):
        x = self.center[0] + x * self.zoom
        y = self.center[1] - y * self.zoom
        return x, y

    def to_nor(self, x, y):
        x = (x - self.center[0]) / self.zoom
        y = (y - self.center[1]) / -self.zoom
        return x, y

    def get_points(self, x, y):
        orient = self.repeat % 2
        if orient > 0:
            x1 = x - Poll.HALF_STICK
            x2 = x + Poll.HALF_STICK
            y1 = y2 = y
        else:
            y1 = y - Poll.HALF_STICK
            y2 = y + Poll.HALF_STICK
            x1 = x2 = x
        return (x1, y1), (x2, y2)

    def create_stick(self, x, y):
        if (x, y) not in self.engaged_points:
            self.engaged_points.add((x, y))
            p1, p2 = self.get_points(x, y)
            points = {p1, p2}
            total = points & self.empty_points
            for point in total:
                self.empty_points.discard(point)
                self.engaged_points.add(point)
            for point in points - total:
                self.empty_points.add(point)
            self.cvs.create_line(*self.to_raw(*p1), *self.to_raw(*p2), fill=self.color)
            self.onstep += 1
            self.amount += 1
            del (points, total, p1, p2)

    def loop(self):
        if not self.paused:
            for point in set(self.empty_points):
                if not self.out and abs(point[0]) + Poll.HALF_STICK >= self.size / 2:
                    self.out = True
                self.empty_points.discard(point)
                self.create_stick(*point)
            if self.out:
                zoom = (self.size - Poll.MARGIN * 2) / (self.repeat / 2 * Poll.STICK_LEN) / self.zoom
                self.zoom *= zoom
                self.cvs.scale("all", *self.center, zoom, zoom)
                self.interval = round(poll.interval * zoom)
                del zoom

            print(f"{str(self.repeat) + ')':<6} on step: {self.onstep:<7} all: {self.amount}")

            self.color = self.num_to_color(self.onstep)
            self.repeat += 1
            self.onstep = 0
            del point

        self.after(self.interval, self.loop)

    def start(self):
        self.loop()
        self.cvs.pack()
        self.mainloop()

    @staticmethod
    def num_to_color(num):
        FULL_CH = 255
        HALF_CH = FULL_CH / 2
        value = (1/num) ** (1/Poll.GAMMA) * FULL_CH
        value = value - HALF_CH
        minus = value < 0
        value = (abs(value) / HALF_CH) ** (1 / Poll.CONTRAST) * HALF_CH
        value = -value if minus else value
        value += HALF_CH
        value = round(value)
        RED = FULL_CH - value
        GREEN = 100
        BLUE = value
        return '#%02x%02x%02x' % (RED, GREEN, BLUE)


if __name__ == "__main__":
    poll = Poll(1000)
    poll.start()
