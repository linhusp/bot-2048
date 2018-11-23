from PIL import ImageOps
import pyscreenshot as ImageGrab
# on Windows use 'from PIL import ImageGrab' instead
import pyautogui
import time
import func

# use this cmd to find out the coordinate of each tile
# print(pyautogui.displayMousePosition()

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3


class Position:
    # value of x and y of each tile on the screen
    # you should custom this class
    p00 = [360, 570]
    p01 = [490, 570]
    p02 = [620, 570]
    p03 = [750, 570]
    p10 = [360, 700]
    p11 = [490, 700]
    p12 = [620, 700]
    p13 = [750, 700]
    p20 = [360, 830]
    p21 = [490, 830]
    p22 = [620, 830]
    p23 = [750, 830]
    p30 = [360, 960]
    p31 = [490, 960]
    p32 = [620, 960]
    p33 = [750, 960]

    p_list = [[p00, p01, p02, p03],
              [p10, p11, p12, p13],
              [p20, p21, p22, p23],
              [p30, p31, p32, p33]]


value_map = {
    193: 0,
    228: 2,
    224: 4,
    188: 8,
    171: 16,
    156: 32,
    136: 64,
    204: 128,
    200: 256,
    196: 512,
    192: 1024,
    189: 2048,
}

curr_board = []
for i in range(4):
    curr_board.append([0] * 4)


# TODO: alpha-beta cutting
priority_list = [[50, 30, 15, 5],
                 [25, 5, 0, 0],
                 [15, 0, 0, 0],
                 [5, 0, 0, 0]]


def main():
    time.sleep(2)
    while True:
        update_board(value_map, curr_board)
        process(get_move(best_move(curr_board)))
        time.sleep(0.1)


def update_board(value_map, board):
    gray_image = ImageOps.grayscale(ImageGrab.grab())

    for i in range(4):
        for j in range(4):
            x = Position.p_list[i][j][0]
            y = Position.p_list[i][j][1]
            # convert ( r, g, b ) value to ( gray ), ez-er to handle
            gray_pixel = gray_image.getpixel((x, y))
            value = value_map[gray_pixel]
            if value != 0:
                board[i][j] = value


def process(move):
    pyautogui.keyDown(move)
    print(move)
    # slow down key-pushing, so the browser can get the signal
    time.sleep(0.05)
    pyautogui.keyUp(move)


def get_move(move_number):
    if move_number == UP:
        return "up"
    elif move_number == DOWN:
        return "down"
    elif move_number == LEFT:
        return "left"
    return "right"


def best_move(board):
    moves_score = [0] * 4

    for i in range(4):
        if can_move(board, i):
            moves_score[i] = get_priority_score(
                get_next_board(board, i),
                priority_list
            )
        else:
            moves_score[i] = 0

    # print(moves_score)
    return moves_score.index(max(moves_score))


def get_priority_score(board, priority):
    score = 0
    for i in range(4):
        for j in range(4):
            score += board[i][j] * priority[i][j]
    return score


def can_move(board, move):
    return board != get_next_board(board, move)


def get_next_board(board, move):
    if move == LEFT:
        return move_left(board)
    if move == RIGHT:
        return move_right(board)
    if move == UP:
        return move_up(board)
    return move_down(board)


def move_left(board):
    board = func.swipe_left(board)
    if func.merge(board):
        return func.swipe_left(board)
    return board


def move_right(board):
    return func.reverse(move_left(func.reverse(board)))


def move_up(board):
    return func.transpose(move_left(func.transpose(board)))


def move_down(board):
    return func.transpose(move_right(func.transpose(board)))


def print_board(board):
    for row in board:
        print("[%s\t|%s\t|%s\t|%s\t]" % (row[0], row[1], row[2], row[3]))


main()
