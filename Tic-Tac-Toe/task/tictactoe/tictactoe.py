def print_grid(grid):
    print("---------")
    for i in grid:
        print("| ", end="")
        for j in i:
            print(j, "", end="")
        print("|")
    print("---------")


def move(grid, move_no):
    f = 0
    while f != 1:
        a, b = input("Enter the coordinates:").split()
        if a.isnumeric() and b.isnumeric():
            a = int(a)
            b = int(b)
            if 4 > a > 0 and 0 < b < 4:
                if grid[a - 1][b - 1] == "_":
                    if move_no % 2 == 0:
                        grid[a - 1][b - 1] = "X"
                    else:
                        grid[a - 1][b - 1] = "O"
                    f = 1
                else:
                    print("This cell is occupied! Choose another one!")
            else:
                print("Coordinates should be from 1 to 3!")
        else:
            print("You should enter numbers!")

def check(grid):
    cells = ""
    for i in grid:
        for j in i:
            cells = cells + j
    if (abs(cells.count("X") - cells.count("O")) > 1 or
    (((cells[0] == "X" and (cells[0] == cells[1] == cells[2])) or
        (cells[3] == "X" and (cells[3] == cells[4] == cells[5])) or
        (cells[6] == "X" and (cells[6] == cells[7] == cells[8])) or
        (cells[0] == "X" and (cells[0] == cells[4] == cells[8])) or
        (cells[2] == "X" and (cells[2] == cells[4] == cells[6])) or
        (cells[0] == "X" and (cells[0] == cells[3] == cells[6])) or
        (cells[1] == "X" and (cells[1] == cells[4] == cells[7])) or
        (cells[2] == "X" and (cells[2] == cells[5] == cells[8]))) and
        ((cells[0] == "O" and (cells[0] == cells[1] == cells[2])) or
        (cells[3] == "O" and (cells[3] == cells[4] == cells[5])) or
        (cells[6] == "O" and (cells[6] == cells[7] == cells[8])) or
        (cells[0] == "O" and (cells[0] == cells[4] == cells[8])) or
        (cells[2] == "O" and (cells[2] == cells[4] == cells[6])) or
        (cells[0] == "O" and (cells[0] == cells[3] == cells[6])) or
        (cells[1] == "O" and (cells[1] == cells[4] == cells[7])) or
        (cells[2] == "O" and (cells[2] == cells[5] == cells[8]))))):
        print("Impossible")
        return 0
    elif ((cells[0] == "X" and (cells[0] == cells[1] == cells[2])) or
        (cells[3] == "X" and (cells[3] == cells[4] == cells[5])) or
        (cells[6] == "X" and (cells[6] == cells[7] == cells[8])) or
        (cells[0] == "X" and (cells[0] == cells[4] == cells[8])) or
        (cells[2] == "X" and (cells[2] == cells[4] == cells[6])) or
        (cells[0] == "X" and (cells[0] == cells[3] == cells[6])) or
        (cells[1] == "X" and (cells[1] == cells[4] == cells[7])) or
        (cells[2] == "X" and (cells[2] == cells[5] == cells[8]))):
        print("X wins")
        return 0
    elif ((cells[0] == "O" and (cells[0] == cells[1] == cells[2])) or
        (cells[3] == "O" and (cells[3] == cells[4] == cells[5])) or
        (cells[6] == "O" and (cells[6] == cells[7] == cells[8])) or
        (cells[0] == "O" and (cells[0] == cells[4] == cells[8])) or
        (cells[2] == "O" and (cells[2] == cells[4] == cells[6])) or
        (cells[0] == "O" and (cells[0] == cells[3] == cells[6])) or
        (cells[1] == "O" and (cells[1] == cells[4] == cells[7])) or
        (cells[2] == "O" and (cells[2] == cells[5] == cells[8]))):
        print("O wins")
        return 0
    elif "_" in cells:
        print("Game not finished")
        return 1
    elif "_" not in cells:
        print("Draw")
        return 0


# cells = input("Enter cells: ")
grid = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
# for i in range(9):
#     if i % 3 == 0:
#         sub = cells[i:i+3]
#         lst = []
#         for k in sub:
#             lst.append(k)
#         grid.append(lst)

print_grid(grid)
f = 1
for i in range(9):
    move(grid, i)
    print_grid(grid)
    f = check(grid)
    if f == 0:
        break
