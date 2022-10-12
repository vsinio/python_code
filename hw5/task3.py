# Создайте программу для игры в ""Крестики-нолики"".
board_lst = [0, 1, 2,
             3, 4, 5,
             6, 7, 8]

win_line = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]]


def print_board(boardlst):
    count = 1
    for i in boardlst:
        if count % 3 != 0:
            print(i, end=" ")
        elif count % 3 == 0:
            print(i)
        count += 1


def input_symbol(dig, symb):
    for i in board_lst:
        if dig == i:
            board_lst[i] = symb


def winner(board):
    winers = ""
    for i in win_line:
        if board[i[0]] == "X" and board[i[1]] == "X" and board[i[2]] == "X":
            winers += "X"
        if board[i[0]] == "O" and board[i[1]] == "O" and board[i[2]] == "O":
            winers += "O"

    return winers


def cross_zero():
    end = False
    player = 2
    while end == False:
        print_board(board_lst)
        if player % 2 == 0:
            print("Игрок 1, ваш ход!")
            b = "X"
            input_symbol(int(input("Введите число на поле: ")), b)
        else:
            print("Игрок 2, ваш ход!")
            b = "O"
            input_symbol(int(input("Введите число на поле: ")), b)

        player += 1
        win = winner(board_lst)
        if win == "":
            end == False
        else:
            print_board(board_lst)
            return f"{win} - Победитель!"


print(cross_zero())
