from math import sin, cos, radians, degrees
from tkinter import *

from xy_interact import c_size, _step, cvs, move, move_to, center, circle, from_polar, norm_coor, raw_coor, root, to_center, loop, clockwise

# Settings
big_rad = 200
pos = 0
wave_freq = 20
wave_amp = 30

# Objects
# big_ball = circle(radius=big_rad, fill='red')
small_ball = circle(x=200, radius=10)


def task_1():
    """Circle"""
    def action():
        global pos
        def processor(rad): return big_rad
        x, y = from_polar(pos, processor)
        move_to(small_ball, x, y)
        pos += _step

    loop(action)


def task_2():
    """Harmonic circle sinusoid"""
    def action():
        global pos
        def processor(rad): return sin(rad * wave_freq) * wave_amp + big_rad
        x, y = from_polar(pos, processor)
        move_to(small_ball, x, y, True)
        pos += _step

    loop(action)


def task_3():  # Не готово
    """Nonharmonic circle sinusoid"""
    def action():
        global pos
        def processor(rad): return sin(rad * wave_freq) * wave_amp + big_rad
        x, y = from_polar(pos, processor)
        move_to(small_ball, x, y, True)
        pos += _step

    loop(action)


def task_4():
    """Flower"""
    to_center(small_ball)

    def action():
        global pos
        def processor(rad): return sin(6 * rad) * big_rad
        x, y = from_polar(pos, processor)
        move_to(small_ball, x, y, True)
        pos += _step

    loop(action)


def task_5():
    """Apple"""
    to_center(small_ball)
    pos = 90

    def action():
        nonlocal pos

        def processor(rad): return (1 - sin(rad)) * (big_rad / 2)

        x, y = from_polar(pos, processor)
        move_to(small_ball, x, y, True)
        pos += _step

    loop(action)


def task_6():
    """Spiral"""
    to_center(small_ball)

    def action():
        global pos
        def processor(rad): return rad * 5
        x, y = from_polar(pos, processor)
        move_to(small_ball, x, y, True)
        pos += _step

    loop(action)


def task_7():
    """Sinusoidal spiral"""
    to_center(small_ball)

    def action():
        global pos
        def processor(rad): return rad * 5 + sin(rad * wave_freq) * wave_amp / 5
        x, y = from_polar(pos, processor)
        move_to(small_ball, x, y, True)
        pos += _step

    loop(action)


def task_8():
    """Flower two"""
    to_center(small_ball)

    def action():
        global pos
        def processor(rad): return rad * 5 + sin(rad * wave_freq) * wave_amp / 5 * -rad
        x, y = from_polar(pos, processor)
        move_to(small_ball, x, y, True)
        pos += _step

    loop(action)


def task_9():
    """Flower three"""
    to_center(small_ball)

    def action():
        global pos

        def processor(rad): return rad * 5 + sin(rad * wave_freq) * wave_amp / 5 * (-rad / 5)

        x, y = from_polar(pos, processor)
        move_to(small_ball, x, y, True)
        pos += _step

    loop(action)


def task_10():
    """Heart"""
    pos = 90
    move_to(small_ball, 0, big_rad * (4/5))

    def action():
        nonlocal pos

        def processor(rad):
            return (2 - 2 * sin(rad) + sin(rad) * ((abs(cos(rad))) ** (1/2) / (sin(rad) + 1.4))) * big_rad / 2

        x, y = from_polar(pos, processor)
        move_to(small_ball, x, y + big_rad * (4/5), True)
        pos += _step

    loop(action)


def task_11():
    """Bernulli's lemniskate"""
    def action():
        global pos, _step

        if 45 <= ((pos - 90) % 180) <= 135:
            def processor(rad): return 4 * cos(2 * rad) * big_rad / 4
        else:
            def processor(rad): return 0
            pos -= 180
            _step = -_step

        x, y = from_polar(pos, processor)
        move_to(small_ball, x, y, True)
        pos += _step

    loop(action)


def task_12():
    """Clover filled"""
    def action():
        to_center(small_ball)

        global pos

        def processor(rad): return 4 * sin(2 * rad) * big_rad / 4

        x, y = from_polar(pos, processor)
        move_to(small_ball, x, y, True)
        pos += _step

    loop(action)


def task_13():  # Не готово
    """Clover 3-list"""
    to_center(small_ball)

    def action():
        global pos

        temp = abs(pos % 360)

        if 45 <= temp <= 135:
            def processor(rad): return 4 * sin(2 * rad) * big_rad / 4
        elif 180 <= temp <= 255:
            def processor(rad): return
        else:
            def processor(rad): return 0
            pos = pos + 45 if clockwise else -45

        x, y = from_polar(pos, processor)
        move_to(small_ball, x, y, True)
        pos += _step

    loop(action)


TASK_TO_RUN = 12


eval(f'task_{TASK_TO_RUN}()')

root.mainloop()
