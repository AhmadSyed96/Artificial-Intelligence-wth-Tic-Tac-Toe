# write your code here
import numpy as np
from math import inf

magic_matrix = np.array([["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]])
coord_matrix = np.array([["1 3", "2 3", "3 3"], ["1 2", "2 2", "3 2"], ["1 1", "2 1", "3 1"]])
winner = []

def find_best_move(player="player1"):
    global magic_matrix
    if player == "player1":
        comp_letter = "X"
        opp_letter = "O"
    else:
        comp_letter = "O"
        opp_letter = "X"

    check_val = -100
    best_move = None
    empty_search = np.where(magic_matrix == "_")
    empty_indicies = list(zip(empty_search[0], empty_search[1]))
    for empty in empty_indicies:
        magic_matrix[empty] = comp_letter
        val = minimax(comp_letter, opp_letter, False)
        if val > check_val:
            check_val = val
            best_move = empty
        magic_matrix[empty] = "_"
    print("Making move level \"hard\"")
    magic_matrix[best_move] = comp_letter


def minimax(cletter, oletter, isMaximizing):
    global magic_matrix
    global winner

    # check terminal state
    if terminal():
        #set score accordingly
        if cletter in winner:
            score = 1
            winner.clear()
            return score
        if oletter in winner:
            score = -1
            winner.clear()
            return score
        else:
            score = 0
            return score

    # remaining empty spots
    empty_search = np.where(magic_matrix == "_")
    empty_indicies = list(zip(empty_search[0], empty_search[1]))

    if isMaximizing:
        best = -inf
        for index in empty_indicies:
            magic_matrix[index] = cletter

            score = minimax(cletter, oletter, not isMaximizing)
            if score > best:
                best = score
            magic_matrix[index] = "_"
        return best

    else:
        best = inf
        for index in empty_indicies:
            magic_matrix[index] = oletter

            score = minimax(cletter, oletter, not isMaximizing)
            if score < best:
                best = score
            magic_matrix[index] = "_"
        return best



def your_turn(player="player1"):
    global magic_matrix
    while True:

        coord_input = input("Enter the coordinates: ")
        try:
            int(coord_input[0])
        except ValueError:
            print("You should enter numbers!")
            continue
        coord_search = np.where(coord_matrix == coord_input)
        coord_index = list(zip(coord_search[0], coord_search[1]))

        try:
            if magic_matrix[coord_index[0]] == "_":
                if player == "player1":
                    magic_matrix[coord_index[0]] = "X"
                else:
                    magic_matrix[coord_index[0]] = "O"
                return
            else:
                print("This cell is occupied! Choose another one!")
                continue
        except ValueError:
            print("You should enter numbers!")
            continue
        except IndexError:
            print("Coordinates should be from 1 to 3!")
            continue

def check_board():
    global magic_matrix
    if np.any((np.all(["X", "X", "X"] == magic_matrix, axis=1))) or np.any(
            (np.all(["X", "X", "X"] == magic_matrix, axis=0))) or (
            ["X", "X", "X"] == magic_matrix.diagonal()).all() or (
            ["X", "X", "X"] == np.fliplr(magic_matrix).diagonal()).all():
        winner.append("X")
        print("X wins")
        return True
    elif np.any((np.all(["O", "O", "O"] == magic_matrix, axis=1))) or np.any(
            (np.all(["O", "O", "O"] == magic_matrix, axis=0))) or (
            ["O", "O", "O"] == magic_matrix.diagonal()).all() or (
            ["O", "O", "O"] == np.fliplr(magic_matrix).diagonal()).all():
        winner.append("O")
        print("O wins")
        return True
    elif np.count_nonzero(magic_matrix == "_") == 0:
        print("Draw")
        return True

def terminal():
    global magic_matrix
    if np.any((np.all(["X", "X", "X"] == magic_matrix, axis=1))) or np.any(
            (np.all(["X", "X", "X"] == magic_matrix, axis=0))) or (
            ["X", "X", "X"] == magic_matrix.diagonal()).all() or (
            ["X", "X", "X"] == np.fliplr(magic_matrix).diagonal()).all():
        winner.append("X")
        return True
    elif np.any((np.all(["O", "O", "O"] == magic_matrix, axis=1))) or np.any(
            (np.all(["O", "O", "O"] == magic_matrix, axis=0))) or (
            ["O", "O", "O"] == magic_matrix.diagonal()).all() or (
            ["O", "O", "O"] == np.fliplr(magic_matrix).diagonal()).all():
        winner.append("O")
        return True
    elif np.count_nonzero(magic_matrix == "_") == 0:
        return True

def print_board(matrix):
    print("-" * 9)
    for line in matrix:
        print("| " + " ".join(line) + " |")
    print("-" * 9)

def execution(player1, player2):
    global magic_matrix
    while True:
        # x moves
        if player1 == "user":
            your_turn()
            print_board(magic_matrix)
            if check_board():
                break
        else:
            find_best_move()
            # comp_turn ()
            print_board(magic_matrix)
            if check_board():
                break

        # O moves
        if player2 == "user":
            your_turn("player2")
            print_board(magic_matrix)
            if check_board():
                break
        else:
            find_best_move("player2")
            # comp_turn("player2")
            print_board(magic_matrix)
            if check_board():
                break
#####################################################################################

print_board(magic_matrix)

while True:
    start_menu = input("Input command: ")
    if start_menu == "exit":
        break
    if len(start_menu.split()) == 3:
        players = start_menu.split()[1:]
        execution(players[0], players[1])
        magic_matrix.fill("_")
    else:
        print("Bad parameters!\n")
        continue
