def is_valid(board, row, col, num):
    block_row, block_col = row // 2, col // 2

    for i in range(4):
        if board[row][i] == num or board[i][col] == num:
            return False

    for i in range(block_row * 2, block_row * 2 + 2):
        for j in range(block_col * 2, block_col * 2 + 2):
            if board[i][j] == num:
                return False

    return True

def solve_sudoku(board):
    for row in range(4):
        for col in range(4):
            if board[row][col] == 0:
                for num in range(1, 5):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    # Read input
    board = []
    for _ in range(4):
        board.append(list(map(int, input().split())))

    # Solve the Sudoku
    if solve_sudoku(board):
        print_board(board)
    else:
        print("No solution exists")
