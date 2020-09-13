from math import sin, cos, radians, degrees
from tkinter import *

from xy_interact import c_size, _step, cvs, move, move_to, center, circle, from_polar, norm_coor, raw_coor, root, \
    loop, _interval

# Settings
big_rad = 200
pos = 0
wave_freq = 20
wave_amp = 30

# Objects
big_ball = circle(radius=big_rad, fill='red')
small_ball = circle(x=200, radius=10)


def task_1():
    def action():
        global pos
        def processor(rad): return big_rad
        x, y = from_polar(pos, processor)
        move_to(small_ball, x, y)()
        pos += _step

    loop(action, _interval)


def task_2():
    def action():
        global pos
        def processor(rad): return sin(rad * wave_freq) * wave_amp + big_rad
        x, y = from_polar(pos, processor)
        move_to(small_ball, x, y, True)()
        pos += _step

    loop(action, _interval)


def task_3():
    move_to(small_ball, 0, 0)()

    def action():
        global pos
        def processor(rad): return abs(sin(3 * rad)) ** (1 / 2) * big_rad
        x, y = from_polar(pos, processor)
        move_to(small_ball, x, y, True)()
        pos += _step

    loop(action, _interval)

def task_3():
    move_to(small_ball, 0, 0)()

    def action():
        global pos
        def processor(rad): return abs(sin(3 * rad)) ** (1 / 2) * big_rad
        x, y = from_polar(pos, processor)
        move_to(small_ball, x, y, True)()
        pos += _step

    loop(action, _interval) 


# task_1()
# task_2()
task_3()

root.mainloop()
