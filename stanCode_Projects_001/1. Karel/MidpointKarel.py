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
    # 斜線1
    put_beeper()
    while front_is_clear():
        move_to_ne()
        put_beeper()
    turn_right()

    # 回右下
    while front_is_clear():
        move()
    put_beeper()
    turn_right()

    while front_is_clear():
        move()
        if on_beeper():
            put_beeper()
        else:
            turn_right()
            move()
            turn_left()
            put_beeper()

    clean_bp()
    # 全都拿走一顆
    find_bp()
    # 找到唯一的那顆
    # 放回第一行


def find_bp():
    turn_right()
    while not on_beeper():
        while front_is_clear():
            move()
            if on_beeper():
                turn_right()
                pick_beeper()
                while front_is_clear():
                    move()
                put_beeper()
        if not on_beeper():
            turn_around()
        while front_is_clear():
            move()
        if not on_beeper():
            turn_right()
            if front_is_clear():
                move()
            turn_right()


def clean_bp():
    back_to_sp()
    pick_beeper()
    while front_is_clear():
        turn_right()
        while front_is_clear():
            move()
            if on_beeper():
                pick_beeper()
        turn_around()

        while front_is_clear():
            move()
        if on_beeper():
            pick_beeper()
        turn_right()
        move()
    turn_right()
    if on_beeper():
        pick_beeper()
    while front_is_clear():
        move()
        if on_beeper():
            pick_beeper()
    back_to_sp()


def back_to_sp():
    # Back to (1,1), facing North
    while not facing_west():
        turn_left()
    while front_is_clear():
        move()
    turn_left()
    while front_is_clear():
        move()
    turn_around()


def move_to_ne():
    while not facing_east():
        turn_left()
    move()
    turn_left()
    move()
    turn_right()


def turn_right():
    # Karel turns left for 3 times.
    turn_left()
    turn_left()
    turn_left()


def turn_around():
    # Karel turns left twice.
    turn_left()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
