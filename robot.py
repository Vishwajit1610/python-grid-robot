# ==============================================================================
# Helper Functions
# ==============================================================================

def print_grid():
    """Prints the current state of the grid to the console."""
    for inner_grid in grid:
        for item in inner_grid:
            print(item, end=" ")
        print()


def calculate_new_position(current_row, current_col, direction):
    """Calculates the theoretical next coordinates based on a direction."""
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
    """Checks if a given coordinate is within bounds and not an obstacle."""
    if ((new_row < 0 or new_col < 0) or (new_row >= len(grid) or new_col >= len(grid[0]))):
        return False
   
    elif (grid[new_row][new_col] == 'X'):
        return False

    return True


# ==============================================================================
# Main Execution
# ==============================================================================

# 8x8 environment for the robot.
grid = [['R', '□', '□', '□', '□', '□', '□', '□'],
        ['X', '□', 'X', '□', '□', '□', '□', '□'],
        ['□', '□', '□', '□', 'X', '□', '□', '□'],
        ['□', '□', '□', '□', '□', '□', '□', '□'],
        ['X', '□', '□', '□', '□', '□', '□', '□'],
        ['□', '□', '□', '□', '□', 'X', '□', '□'],
        ['□', '□', '□', 'G', '□', '□', '□', '□'],
        ['□', '□', '□', '□', '□', '□', '□', '□']]

# Initial robot state.
robot_row = 0
robot_col = 0 

# A hardcoded list of moves to test the execution engine.
# This will be replaced by the A* algorithm's output.
moves = ['right', 'down', 'down', 'right', 'down', 'right', 'down', 'down', 'down']

# State flag for graceful termination.
# Ensures the final grid state is printed before the loop exits.
goal_reached = False

print("Initial State:")
print_grid()
print("\nExecuting moves...")

# The main loop that processes the hardcoded move sequence.
for move in moves:
    
    next_row, next_col = calculate_new_position(robot_row, robot_col, move)
    is_valid = is_move_valid(next_row, next_col)

    # For debugging:
    print(f"Move: {move}, Next: ({next_row},{next_col}), Valid: {is_valid}")

    if (is_valid):
        # Erase the robot from its old position.
        grid[robot_row][robot_col] = '□'

        # Update the robot's state variables.
        robot_row = next_row
        robot_col = next_col

        # Check if the new square is the goal BEFORE drawing the robot.
        if (grid[next_row][next_col] == 'G'):
            goal_reached = True
            
        # Draw the robot in its new position.
        grid[robot_row][robot_col] = 'R'
        print_grid()

    # After the move is fully processed and printed, check the flag to exit.
    if (goal_reached):
        print("You have reached the goal!")
        break



    
