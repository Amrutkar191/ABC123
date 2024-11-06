def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queens_util(board, col, n, solutions):
    if col >= n:
        positions = [row.index(1) + 1 for row in board]
        solutions.append(positions)
        return True

    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            res = solve_n_queens_util(board, col + 1, n, solutions) or res
            board[i][col] = 0

    return res

def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)

    if not solutions:
        print("No solution exists")
    else:
        print(f"Total number of solutions: {len(solutions)}")
        for idx, solution in enumerate(solutions, 1):
            print(f"Solution {idx}: {solution}")

n = int(input("Enter the value of N for the N*N Queens matrix: "))
solve_n_queens(n)
