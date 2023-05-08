#!/usr/bin/python3
"""
Purpose: Tic Tac Toe game
"""

print("TIC TAC TOE GAME")

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

board_print = f"""{board[6]} | {board[7]} | {board[8]}\
    -----------\
    {board[3]} | {board[4]} | {board[5]}\
    -----------\
     {board[0]} | {board[1]} | {board[2]}"""

board_print_default = """
     7 | 8 | 9
    -----------
     4 | 5 | 6
    -----------
     1 | 2 | 3
"""

print("")
print(board_print_default)


def p1_input():
    global board_print
    for i in range(10):
        if i == p_in:
            board[i - 1] = "X"
            board_print = (
                f" {board[6]} | {board[7]} | {board[8]}\n"
                f"-----------\n"
                f" {board[3]} | {board[4]} | {board[5]}\n"
                f"-----------\n"
                f" {board[0]} | {board[1]} | {board[2]}"
            )
            print(board_print)


def p2_input():
    global board_print
    for i in range(10):
        if i == p_in:
            board[i - 1] = "O"
            board_print = (
                f" {board[6]} | {board[7]} | {board[8]}\n"
                f"-----------\n"
                f" {board[3]} | {board[4]} | {board[5]}\n"
                f"-----------\n"
                f" {board[0]} | {board[1]} | {board[2]}"
            )
            print(board_print)


def win_check_p1():
    # Check all the horizontal boxes.

    if board[0] == board[1] == board[2] == "X":
        return True

    elif board[3] == board[4] == board[5] == "X":
        return True

    elif board[6] == board[7] == board[8] == "X":
        return True

    # Check all the vertical boxes.
    elif board[0] == board[3] == board[6] == "X":
        return True

    elif board[1] == board[4] == board[7] == "X":
        return True

    elif board[2] == board[5] == board[8] == "X":
        return True

    # Check all the diagonal boxes.
    elif board[6] == board[4] == board[2] == "X":
        return True

    elif board[8] == board[4] == board[0] == "X":
        return True


def win_check_p2():
    # Check all the horizontal boxes.

    if board[0] == board[1] == board[2] == "O":
        return True

    elif board[3] == board[4] == board[5] == "O":
        return True

    elif board[6] == board[7] == board[8] == "O":
        return True

    # Check all the vertical boxes.
    elif board[0] == board[3] == board[6] == "O":
        return True

    elif board[1] == board[4] == board[7] == "O":
        return True

    elif board[2] == board[5] == board[8] == "O":
        return True

    # Check all the diagonal boxes.
    elif board[6] == board[4] == board[2] == "O":
        return True

    elif board[8] == board[4] == board[0] == "O":
        return True


def check_draw():
    pass


s = 0
p_in = 0  # Player input.
# A variable to check if the given value of p_in is not same.
t = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
i = 0
# This is the var that is used to check if the match is draw or not.
draw_var = 0
while s != 9:
    print("")

    t[i] = p_in
    p_in = int(input("> "))

    if p_in in t[0:14] or p_in < 1 or p_in > 9:
        print("Input not accepted. Try again.\n")
    else:
        if s % 2 == 0:
            p1_input()
            win_check_p1()

            if win_check_p1():
                print("")
                print("Player 1 has won.")
                draw_var = 1
                break
        elif s % 2 != 0:
            p2_input()
            win_check_p2()

            if win_check_p2():
                print("")
                print("Player 2 has won.")
                draw_var = 1
                break

        s += 1
    i += 1
    if i == 14:
        print("Multiple invalid inputs. Please re-start the game.")
        break

if draw_var == 0:
    print("")
    print("Draw.")
