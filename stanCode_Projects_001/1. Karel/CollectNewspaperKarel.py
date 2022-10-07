from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
Name: Chunya Tsai
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""


def main():
    """
    Karel goes out to pick up the beeper, then put it in the initial position
    """
    take_newspaper()
    back_and_read()


def take_newspaper():
    """
    Karel goes out to pick up the beeper
    pre-condition: Karel is on the initial position, facing East
    post-condition: Karel stand in the doorway, facing West
    """
    while front_is_clear():
        move()
    turn_right()
    while not left_is_clear():
        move()
    turn_left()
    while not on_beeper():
        move()
    pick_beeper()
    turn_left()
    turn_left()


def back_and_read():
    """
    #Karel leave the beeper to the initial position
    #pre-condition: Karel stands in the doorway, facing West
    #post-condition: Karel is on the initial position, facing East
    """
    while not on_beeper():
        while front_is_clear():
            move()
        turn_right()
        while front_is_clear():
            move()
        turn_right()
        put_beeper()


def turn_right():
    # Karel turns left for 3 times.
    turn_left()
    turn_left()
    turn_left()









# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
