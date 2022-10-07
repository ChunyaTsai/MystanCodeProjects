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
    Since the numbers of avenues and streets are the same,
    Karel goes East once for every 2 steps he heads to North.
    Upon Karel arrives the top position, backs to the bottom of the Avenue. Then, put a beeper.
    """
    turn_left()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            turn_right()
            move()
            turn_left()
    back_to_bottom()
    put_beeper()


def turn_right():
    # Karel will turn left for 3 times.
    turn_left()
    turn_left()
    turn_left()


def back_to_bottom():
    """
    Pre-condition: Karel is facing North.
    Post-condition: Karel will go back to the bottom of the Avenue, facing South.
    """
    turn_left()
    turn_left()
    while front_is_clear():
        move()

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
