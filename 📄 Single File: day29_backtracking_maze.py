# Day 29 - Backtracking Proper (Rat in a Maze)


def solve_maze(maze):
    n = len(maze)
    solution = [[0] * n for _ in range(n)]

    if backtrack(maze, 0, 0, solution):
        print("Path Found:")
        for row in solution:
            print(row)
    else:
        print("No Path Found")


def backtrack(maze, x, y, solution):
    n = len(maze)

    # Base Case: reached destination
    if x == n - 1 and y == n - 1 and maze[x][y] == 1:
        solution[x][y] = 1
        return True

    if is_safe(maze, x, y):
        solution[x][y] = 1

        # Move Right
        if backtrack(maze, x, y + 1, solution):
            return True

        # Move Down
        if backtrack(maze, x + 1, y, solution):
            return True

        # Backtrack (Undo)
        solution[x][y] = 0
        return False

    return False


def is_safe(maze, x, y):
    n = len(maze)
    return 0 <= x < n and 0 <= y < n and maze[x][y] == 1


# -------- Test --------
maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]

solve_maze(maze)
