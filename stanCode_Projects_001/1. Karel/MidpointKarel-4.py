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
    由於對角線交點為正方形中點，找出對角線交點後對應至1st Street即為底邊中點
    作法： 沿著對角線放beepers, 放完後檢查一次所有位置, 將所於有有beeper的位置撿起一個beeper, 剩下的唯一一個beeper即為正方形中點
    補充: 若正方形邊長為2的倍數, 即兩條對角線不會有焦點, 正方形中點會趨近於4個beeper(2x2)相連的位置, 所以在放置第二條對角線的beeper時,
    不等往左上移動完後才放beeper, 而是先往西移動, 確認該位置沒有beeper後才往北走放置beeper, 若往西移動式發現該位置已有beeper則直接放置,
    是該位置為趨近中點的位置
    """

    # 將對角線西南到東北放滿beepers
    put_beeper()
    while front_is_clear():
        move_to_ne()
        put_beeper()
    turn_right()

    # 回右下角放置一個beeper, 面向西
    while front_is_clear():
        move()
    put_beeper()
    turn_right()

    # 往西北方移動, 在第2條對角線上放beepers
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
    find_bp()


def find_bp():
    """
    檢查所有位置, 找到beeper後撿起, 自該位置出發往南走到底, 並放置1個beeper
    """
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
    """
    檢查所有位置一次, 若該位置有beeper, 則撿起一個beeper
    """
    back_to_sp()
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
    # 往西北方走一格
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
