board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]]


def print_board(grid):
    for i in range(len(grid)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(grid[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ", end="")


def find_zero(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return [i, j]

    return None


def is_valid(grid, row, col, value):
    if grid[row][col] != 0:
        print(False)
        return False

    # Checks the row
    for i in range(len(grid[row])):
        if grid[row][i] == value:
            return False

    # Checks the column
    for i in range(len(grid[row])):
        if grid[i][col] == value:
            return False

    # Checks the box (by doing //3, we are effectively treating every 3 lines as a single line)
    box_x = col // 3
    box_y = row // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if grid[i][j] == value:
                return False

    return True


def solve(grid):
    find = find_zero(grid)
    if not find:
        return True
    else:
        row, col = find[0], find[1]

    for i in range(1, 10):
        if is_valid(grid, row, col, i):
            grid[row][col] = i

            if solve(grid):
                return True

            grid[row][col] = 0

    return False
solve(board)
print(board)