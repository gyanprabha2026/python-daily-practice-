# Day 30 - N Queens Problem (Backtracking)

def solve_n_queens(n):
    board = [["." for _ in range(n)] for _ in range(n)]
    solutions = []

    def backtrack(row):
        if row == n:
            # Deep copy of board
            solutions.append(["".join(r) for r in board])
            return

        for col in range(n):
            if is_safe(row, col):
                board[row][col] = "Q"      # Place queen
                backtrack(row + 1)         # Explore next row
                board[row][col] = "."      # Backtrack (remove queen)

    def is_safe(row, col):
        # Check column
        for i in range(row):
            if board[i][col] == "Q":
                return False

        # Check upper left diagonal
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        # Check upper right diagonal
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == "Q":
                return False
            i -= 1
            j += 1

        return True

    backtrack(0)
    return solutions


# -------- Test --------
n = 4
result = solve_n_queens(n)

print(f"Total Solutions for {n}-Queens:", len(result))
for sol in result:
    print()
    for row in sol:
        print(row)
