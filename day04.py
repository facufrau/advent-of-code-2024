# --- Day 4: Ceres Search ---

with open("input04.txt") as file:
    grid = [list(x.strip()) for x in file.readlines()]
    word = "XMAS"

# Part one
def count_HV(grid, word, v):
    count = 0
    if v[0] != 0: # Vertical
        search_grid = grid[::v[0]]
        for i in range(len(search_grid[0])):
            str_to_look = ''.join([x[i] for x in search_grid])
            count += str_to_look.count(word)
    else: # Horizontal
        for i in range(len(grid)):
            str_to_look = ''.join(grid[i][::v[1]])
            count += str_to_look.count(word)
    return count

def count_diag(grid, word, v):
    strs_list = []
    count = 0
    # Direction down-right and up-left (reversed)
    if v[1] == 1:
        iterator_h = range(len(grid))
        iterator_v = range(1, len(grid))
        # Top row, left to right
        for j in iterator_h:
            x, y = j, 0
            str_to_look = ""
            while x < len(grid) and y < len(grid):
                str_to_look += grid[y][x]
                x += v[1]
                y += v[0]
            if len(str_to_look) >= len(word):
                strs_list.append(str_to_look)
                strs_list.append(str_to_look[::-1])
        # First column top to bottom
        for i in iterator_v:
            x, y = 0, i
            str_to_look = ""
            while x < len(grid) and y < len(grid):
                str_to_look += grid[y][x]
                x += v[1]
                y += v[0]
            if len(str_to_look) >= len(word):
                strs_list.append(str_to_look)
                strs_list.append(str_to_look[::-1])
    # Direction down-left and up-right (reversed)
    elif v[1] == -1:
        iterator_h = range(len(grid)-1, -1, -1)
        iterator_v = range(1, len(grid))
        # Top row, right to left
        for j in iterator_h:
            x, y = j, 0
            str_to_look = ""
            while x >= 0 and y < len(grid):
                str_to_look += grid[y][x]
                x += v[1]
                y += v[0]
            if len(str_to_look) >= len(word):
                strs_list.append(str_to_look)
                strs_list.append(str_to_look[::-1])
        # First column, top to bottom
        for i in iterator_v:
            x, y = len(grid) - 1, i
            str_to_look = ""
            while x >= 0 and y < len(grid):
                str_to_look += grid[y][x]
                x += v[1]
                y += v[0]
            if len(str_to_look) >= len(word):
                strs_list.append(str_to_look)
                strs_list.append(str_to_look[::-1])

    for string in strs_list:
        count += string.count(word)
    return count

def count_words(grid, word):
    vectors = [        (-1, 0),
               ( 0,-1),        ( 0, 1),
               ( 1,-1),( 1, 0),( 1, 1)]
    total = 0
    for v in vectors:
        if 0 in v:  # Horizontal or vertical lookup
            total += count_HV(grid, word, v)
        else:       # Diagonals lookup
            total += count_diag(grid, word, v)
    return total

print(f"Part one answer -->  {count_words(grid, word)}")

# Part two
def check_xmas(grid, x, y):
    # For checking the central letter
    if grid[y][x] != 'A':
        return False
    # Checking the X form around central letter
    top_left = grid[y-1][x-1]
    top_right = grid[y-1][x+1]
    bottom_left = grid[y+1][x-1]
    bottom_right = grid[y+1][x+1]
    if top_left == 'M' and bottom_right == 'S':
        if top_right == 'M' and bottom_left == 'S':
            return True
        elif top_right == 'S' and bottom_left == 'M':
            return True
    elif top_right == 'M' and bottom_right == 'M' and top_left == 'S' and bottom_left == 'S':
        return True
    elif bottom_left == 'M' and bottom_right == 'M' and top_left == 'S' and top_right == 'S':
        return True
    return False


def count_xmas_grid(grid):
    delta_x = range(1, len(grid[0]) - 1)
    delta_y = range(1, len(grid) - 1)
    total = 0
    for y in delta_y:
        for x in delta_x:
            if check_xmas(grid, x, y):
                total += 1
    return total

print(f"Part two answer -->  {count_xmas_grid(grid)}")
