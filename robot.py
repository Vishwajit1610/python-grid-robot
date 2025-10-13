grid = [['R', '□', '□', '□', '□', '□', '□', '□'],
        ['X', '□', 'X', '□', '□', '□', '□', '□'],
        ['□', '□', '□', '□', 'X', '□', '□', '□'],
        ['□', '□', '□', '□', '□', '□', '□', '□'],
        ['X', '□', '□', '□', '□', '□', '□', '□'],
        ['□', '□', '□', '□', '□', 'X', '□', '□'],
        ['□', '□', '□', 'G', '□', '□', '□', '□'],
        ['□', '□', '□', '□', '□', '□', '□', '□']]


for inner_grid in grid:
    for item in inner_grid:
        print(item, end=" ")
    print()


robot_row = 0
robot_col = 0 


def calculate_new_position(current_row, current_col, direction):

    new_row = current_row
    new_col = current_col

    if (direction == 'up'):
        new_row = current_row - 1
    
    elif (direction == 'down'):
        new_row = current_row + 1

    elif (direction == 'right'):
        new_col = current_col + 1

    elif (direction == 'left'):
        new_col = current_col - 1
    
    else:
        return current_row, current_col

    return new_row, new_col


def is_move_valid(new_row, new_col):

    if ((new_row < 0 or new_col < 0) or (new_row >= len(grid) or new_col >= len(grid[0]))):
        return False

    elif (grid[new_row][new_col] == 'X'):
        return False

    return True




