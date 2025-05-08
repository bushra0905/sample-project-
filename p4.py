Aim: Implement a solution for a Constraint Satisfaction Problem using Branch and Bound and Backtracking for n-queens problem or a graph coloring problem

N = 4  
def print_board(board):
    for row in board:
        print(" ".join('Q' if x == 1 else '.' for x in row))
    print()

def is_safe(board, row, col):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, col):
    if col >= N:
        return True

    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1

            if solve_n_queens(board, col + 1):
                return True

            board[i][col] = 0  # Backtrack

    return False

# Initialize the board
board = [[0 for _ in range(N)] for _ in range(N)]

# Solve and print the solution
if solve_n_queens(board, 0):
    print_board(board)
else:
    print("No solution exists.")
