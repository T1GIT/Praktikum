from math import sin, cos, radians, degrees
from tkinter import *

c_size = [500, 500]  # c = canvas
center = [c_size[0] / 2, c_size[1] / 2]
root = Tk()
cvs = Canvas(root, width=c_size[0], height=c_size[1], bg="white")
cvs.pack()


# Motion settings
accuracy = 9  # (1, 10)
speed = 5  # (1, 10)
clockwise = False

# Checking parameters
assert 0 < accuracy < 10, "Accuracy is out of range"
assert 0 < speed < 10, "Speed is out of range"
assert type(clockwise) is bool, "Type of clockwise is not boolean"

_step = (-1 if clockwise else 1) * (4 - (accuracy / 2.5))
_interval = round(abs(_step) * 10 / speed * 5)


# Axis / coordinates
def raw_coor(x, y):
    return [center[0] + x, center[1] - y]


def norm_coor(x, y):
    return [x - center[0], y + center[1]]


def obj_coor(obj):
    x0 = (cvs.coords(obj)[0] + cvs.coords(obj)[2]) / 2
    y0 = (cvs.coords(obj)[1] + cvs.coords(obj)[3]) / 2
    return x0, y0


# Figures
def circle(x=0, y=0, radius=1, fill="white", outline="black"):
    diam = radius * 2
    x, y = raw_coor(x, y)
    x1 = x - radius
    y1 = y - radius
    x2 = x1 + diam
    y2 = y1 + diam
    return cvs.create_oval(x1, y1, x2, y2, fill=fill, outline=outline)


def from_polar(grad=0, processor=lambda x: x, x0=0, y0=0):
    rad = radians(grad)
    r = processor(rad)
    x = r * cos(rad) + x0
    y = r * sin(rad) + y0
    return x, y


# Moving
def move(obj, x_dist, y_dist, tail=False, color="black"):
    if tail:
        def motion():
            x0, y0 = obj_coor(obj)
            cvs.move(obj, x_dist, y_dist)
            x1, y1 = obj_coor(obj)
            cvs.create_line(x0, y0, x1, y1, fill=color)
    else:
        def motion():
            cvs.move(obj, x_dist, y_dist)
    return motion()


def move_to(obj, x, y, tail=False, color="black"):
    if tail:
        def motion():
            x0, y0 = obj_coor(obj)
            x1, y1, x2, y2 = cvs.coords(obj)
            half_x_obj = (x2 - x1) / 2
            half_y_obj = (y2 - y1) / 2
            cvs.moveto(obj, *raw_coor(x - half_x_obj, y + half_y_obj))
            x1, y1 = obj_coor(obj)
            cvs.create_line(x0, y0, x1, y1, fill=color)
    else:
        def motion():
            x1, y1, x2, y2 = cvs.coords(obj)
            half_x_obj = (x2 - x1) / 2
            half_y_obj = (y2 - y1) / 2
            cvs.moveto(obj, *raw_coor(x - half_x_obj, y + half_y_obj))
    return motion()


def to_center(obj):
    move_to(obj, 0, 0)


def loop(animation):
    def loop_move():
        animation()
        root.after(_interval, loop_move)
    return loop_move()
