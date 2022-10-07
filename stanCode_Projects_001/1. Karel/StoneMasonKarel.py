from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
Name: Chunya Tsai
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""


def main():
    """
    Karel inputs beepers to all pillars (in Avenue (1+4X)).
    """
    while front_is_clear():
        input_beeper()
        back_to_bottom()
        for i in range(4):
            move()
    input_beeper()
    back_to_bottom()


def input_beeper():
    """
    pre-condition: Karel is at the bottom of a pillar with unknown beepers, facing East.
    post-condition: Karel is on top of the pillar with fulled beepers, facing South.
    """
    turn_left()
    while not on_beeper():
        put_beeper()
    while front_is_clear():
        move()
        while not on_beeper():
            put_beeper()
    turn_around()


def back_to_bottom():
    """
    pre-condition: Karel is on top of a pillar, facing South.
    post-condition: Karel is at the bottom of the pillar, facing East.
    """
    while front_is_clear():
        move()
    turn_left()


def turn_around():
    # This function turns Karel to the left 2 times.
    turn_left()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
