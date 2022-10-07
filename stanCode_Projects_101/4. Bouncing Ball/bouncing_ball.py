"""
File: bouncing_ball.py
Name: Chunya Tsai
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
X_START = 30
Y_START = 40
OPEN = 1

window = GWindow(800, 500, title='bouncing_ball.py')
circle = GOval(SIZE, SIZE)
circle.filled = True
COUNT = 1


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global COUNT
    global OPEN
    window.add(circle, X_START, Y_START)
    onmouseclicked(move)


def move(start):
    global COUNT
    global OPEN
    vy = 1
    if COUNT <= 3:
        if OPEN == 1:
            OPEN = 0
            COUNT += 1
            window.add(circle, X_START, Y_START)
            while True:
                circle.move(VX, vy)
                vy += GRAVITY
                if circle.y <= 0 or circle.y + SIZE >= window.height:
                    vy = -REDUCE * vy
                if circle.x >= window.width or circle.x + SIZE >= window.width:
                    window.add(circle, X_START, Y_START)
                    OPEN = 1
                    break
                pause(DELAY)


if __name__ == "__main__":
    main()
