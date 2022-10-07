from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
Name: Chunya Tsai
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""


def main():
    """
    Facing East, Karel keeps moving from (1,1). And turn around to the next street before hitting the sideline.
    Every 2 steps forward, Karel will put a beeper.
    """
    put_beeper()
    while left_is_clear():
        # Since the starting position is (1,1) and facing East,
        # I would like to check if there is only 1 street in this checkerboard before moving.

        # Put a beeper for every 2 steps.
        while front_is_clear():
            move()
            if front_is_clear():
                move()
                put_beeper()

        # Before turning around, check if Karel is on beeper.
        # To decide if we should put a beeper at the starting position on the next street
        if on_beeper():
            turn_around()
            if front_is_clear():
                move()
                put_beeper()
        else:
            turn_around()

            # If Karel faces North, it means that this is terminal point and Karel put a beeper on the previous step.
            # Therefore, we don't need to put a beeper on this position.
            if not facing_north():
                put_beeper()

    # If the numbers of street is odd, Karel should keep to put beepers on the last street.
    while front_is_clear():
        if not on_beeper():
            put_beeper()
        move()
        if front_is_clear():
            move()
            put_beeper()


def turn_around():
    # Karel will turn around and take a step to the North.
    if facing_east():
        turn_left()
        if front_is_clear():
            move()
            turn_left()
    else:
        # This function will be executed with westward or eastward moving.
        # That why we don't need to consider northward and southward.
        turn_right()
        if front_is_clear():
            move()
            turn_right()


def turn_right():
    # Karel will turn left for three times
    turn_left()
    turn_left()
    turn_left()





# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
