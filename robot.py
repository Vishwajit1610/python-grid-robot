import heapq as hq
import time
 
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


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def reconstruct__path(came_from, current):
    total_path = [current]

    while (current in came_from):

        current = came_from[current]
        total_path.insert(0, current)

    return total_path

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
        ['□', '□', '□', '□', '□', '□', '□', '□'],
        ['□', '□', '□', '□', '□', 'G', '□', '□']]

# Finding co-ordinates of the start and goal using enumerate loop.
for row_index, row in enumerate(grid):
    for col_index, col in enumerate(row):

        if (col == 'R'):
            start_pos = (row_index, col_index)
        
        if (col == 'G'):
            goal_pos = (row_index, col_index)

# List for possible directions for Robot.
directions = ['up', 'down', 'right', 'left']

# ==============================================================================
# Data Structures to manage A* Algorithm 

# Serves as Priority Queue
open_set = []

# Stores past trails to reconstruct the final path.
came_from = {}

# Stores the cost from start to any given node.
g_score = {start_pos : 0}

# ==============================================================================

# Stores the score which is the manhattan distance from the start pos to the goal pos
f_score = heuristic(start_pos, goal_pos)

# Pushing the f_score and the start pos into the open_set (Priority Queue)
hq.heappush(open_set, (f_score, start_pos))


# print("Initial State:")
# print_grid()
# print("\nExecuting moves...")

# Contains the A* Algorithm Engine
while (open_set):
    current_f_score, current_pos = hq.heappop(open_set)
    
    if (current_pos == goal_pos):

        final_path = reconstruct__path(came_from, current_pos)
        print(F"Path: {final_path}")
        print(f"Number of motions: {len(final_path) - 1}")

        print("\nStarting...")
        print_grid()  
        print()
        time.sleep(1.5)

        # Robot Animation Code
        for i in range(1, len(final_path)):
            prev_pos = final_path[i - 1]
            pos = final_path[i]

            grid[prev_pos[0]][prev_pos[1]] = '●'

            # Draw the robot at the new position
            grid[pos[0]][pos[1]] = 'R'

            print_grid()
            print()
            time.sleep(1.5)
    
        print("Hurray! The Robot reached the Goal!!")
        break


    for direction in directions:
        neighbor_pos = calculate_new_position(current_pos[0], current_pos[1], direction)

        if (is_move_valid(neighbor_pos[0], neighbor_pos[1])):

            tentative_g_score = g_score[current_pos] + 1

            if (tentative_g_score < g_score.get(neighbor_pos, float('inf'))):
                
                came_from[neighbor_pos] = current_pos
                g_score[neighbor_pos] = tentative_g_score

                f_score = tentative_g_score + heuristic(neighbor_pos, goal_pos)

                hq.heappush(open_set, (f_score, neighbor_pos))

