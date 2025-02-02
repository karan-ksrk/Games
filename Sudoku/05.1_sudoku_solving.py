import numpy as np 
board = [
        [0, 0, 4, 3, 0, 0, 2, 0, 9], 
        [0, 0, 5, 0, 0, 9, 0, 0, 1], 
        [0, 7, 0, 0, 6, 0, 0, 4, 3],
        [0, 0, 6, 0, 0, 2, 0, 8, 7],
        [1, 9, 0, 0, 0, 7, 4, 0, 0],
        [0, 5, 0, 0, 8, 3, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 1, 0, 5], 
        [0, 0, 3, 5, 0, 8, 6, 9, 0],
        [0, 4, 2, 9, 1, 0, 3, 0, 0]
]
def show(board):
    for i in range(len(board)):
        if i%3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
        for j in range(len(board[0])):
            if j%3 == 0 and j != 0:
                print(" | ", end="")
            if j==8:
                print(str(board[i][j]))
            else:
                print(str(board[i][j]) + " ", end="")

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

def valid(board, num, pos):
    # check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    
    # check column
    for j in range(len(board[0])):
        if board[i][pos[1]] == num and pos[0] != j:
            return False
    
    # check box
    box_i = pos[0]//3 #row
    box_j = pos[1]//3 #column

    for i in range(box_i*3, box_i*3+3):
        for j in range(box_j*3, box_j*3+3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True

def solve_board(board):
    find  = find_empty(board)
    if not find:
        return True
    else:
        row, col = find
    
    for i in range(1, 10):
        if valid(board, i , (row, col)):
            board[row][col]  = i

            if solve_board(board):
                return True
            
            board[row][col] = 0
    return False

show(board)
solve_board(board)
print("#######################################")
show(board)