from karel.stanfordkarel import *

"""
File: MidpointKarel.py
Name: Chunya Tsai
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    """
    將1st Street放滿beepers, 從street兩端開始拿取beeper逼近中點, 最後一個拿起的beeper即為中點
    """

    # Input the beepers for all corners of 1st Street except the leftmost and the rightmost one.
    while front_is_clear():
        move()
        if front_is_clear():
            put_beeper()
    turn_around()
    if front_is_clear():
        move()

    # Start picking the beepers from the edge of 1st Street.
    while on_beeper():
        while on_beeper():
            if front_is_clear():
                move()
        turn_around()
        move()
        pick_beeper()
        move()
    turn_around()

    # Back to the position of the last beeper which is the corner closest to the center.
    if front_is_clear():
        move()
    put_beeper()


def turn_around():
    # Karel turns left twice.
    turn_left()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
