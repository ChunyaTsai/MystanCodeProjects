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
    Put a beeper for every 2 cells in the 1st Street.
    Then take these beepers to (1,1) to obtain the half width.
    Move these beepers from (1,1) to the other positions in the 1st street. (from (1,2) to (1,3), (1,4)...)
    To find midpoint.
    """

    # Put a beeper for every 2 cells in the 1st Street.
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()
    back_to_sp()
    turn_around()

    """
    Collect all beepers to (1,1).
    Post-condition: Karel is on (2,1) [or (1,1) for 1x1], facing East.
    """
    while front_is_clear():
        move()
        if on_beeper():
            pick_beeper()
            back_to_sp()
            put_beeper()
            turn_around()
    back_to_sp()
    turn_around()

    # Find the center of the 1st Street according to the numbers of beepers at (1,1) which is the half width.
    while on_beeper():
        pick_beeper()
        move()
        while on_beeper():
            move()
        put_beeper()
        back_to_sp()
        turn_around()

    # Go eastward from (1,1) to pick up all beepers. Then stay on the last beeper.
    if front_is_clear():
        move()
    while on_beeper():
        pick_beeper()
        if front_is_clear():
            move()
    turn_around()
    if front_is_clear():
        move()
    put_beeper()


def back_to_sp():
    # Go back to (1,1), facing West.
    if not facing_west():
        turn_around()
    while front_is_clear():
        move()


def turn_around():
    # Karel turns left twice.
    turn_left()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
