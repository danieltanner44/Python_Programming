import time
import numpy as np
from my_modules.development import fstring
from my_modules.development import print_array

def read_input_data(filename):
    warehouse_initial_map, directions = [], []
    with (open(filename, 'r') as f):
        for line in f:
            temp = line.strip()
            if len(temp) == 0:
                continue
            elif temp[0] == "#":  # Reading warehouse data
                warehouse_initial_map.append(list(temp))
            elif temp[0] in ["^","v","<",">"]:
                directions.extend(list(temp))
    warehouse_initial_map = np.array(warehouse_initial_map, dtype=np.str_)
    return warehouse_initial_map, directions

def process_robot_movement(warehouse_map, directions):
    # Find the robot starting position
    current_position = np.where(warehouse_map == "@")
    current_position = (current_position[0][0], current_position[1][0])

    # Dictionary to translate the directions into map steps
    next_step = {"^": (-1, 0),"v": (1, 0),"<": (0, -1),">": (0, 1)}

    # Now loop over each direction in the robot instructions
    for step in directions:
        # Establish the position of the next step based on the current direction instruction
        next_position = (current_position[0] + next_step[step][0], current_position[1] + next_step[step][1])
        # Determine what lies in the space of the potential next step
        next_position_contents = warehouse_map[next_position]
        if next_position_contents == ".":
            # Nothing in robot path so move there
            warehouse_map[current_position] = "."   # Leave a space in the position the robot left
            warehouse_map[next_position] = "@"      # Move the robot position marker to the next position
            current_position = next_position        # Make the move, i.e., update the current position
        elif next_position_contents in ["O", "[", "]"]:
            # Need to assess if the box can be pushed or is ultimately against a wall
            warehouse_map, space_to_push_box = check_for_space_behind_boxes(current_position, next_position, warehouse_map, step)
            if space_to_push_box:
                # The box(es) have been pushed so move to the new location
                current_position = next_position
    return warehouse_map

def check_for_space_behind_boxes(current_position, next_position, warehouse_map, step):
    # Dictionary to translate the directions into map steps
    next_step = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
    # Consider sideways movement first as simpler (boxes only present one face to robot)
    # Doubling of the warehouse space and contents is only applied horizontally
    # So boxes the robot encounters horizontally only present a size of 1 space
    if step in ["<", ">"]:
        if step == "<":
            # Find the nearest space in the push direction
            space_position = np.where(warehouse_map[current_position[0], 0:current_position[1] + 1] == ".")
            # Find the nearest wall in the push direction
            wall_position = np.where(warehouse_map[current_position[0], 0:current_position[1] + 1] == "#")
            # If there is a space, and it is closer than the nearest wall then move them
            if len(space_position[0]) != 0 and space_position[0][-1] > wall_position[0][-1]:
                temp_string = warehouse_map[current_position[0], :current_position[1] + 1]
                # Move boxes along one space
                temp_string[space_position[0][-1]:-1] = temp_string[space_position[0][-1] + 1:]
                # Show the final position as being empty again
                temp_string[-1] = "."
                warehouse_map[current_position[0], 0:current_position[1] + 1] = temp_string
                space_to_push_box = True
            else:
                space_to_push_box = False
                return warehouse_map, space_to_push_box
        elif step == ">":
            # Find the nearest space in the push direction
            space_position = np.where(warehouse_map[current_position[0], current_position[1]:] == ".")
            # Find the nearest wall in the push direction
            wall_position = np.where(warehouse_map[current_position[0], current_position[1]:] == "#")
            # If there is a space, and it is closer than the nearest wall then move them
            if len(space_position[0]) != 0 and space_position[0][0] < wall_position[0][0]:
                temp_string = warehouse_map[current_position[0], current_position[1]:]
                temp_string[1:space_position[0][0] + 1] = temp_string[0:space_position[0][0]]
                # Show the final position as being empty again
                temp_string[0] = "."
                warehouse_map[current_position[0], current_position[1]:] = temp_string
                space_to_push_box = True
            else:
                space_to_push_box = False
                return warehouse_map, space_to_push_box

    # For vertical robot encounters with boxes significantly more care is needed
    # Boxes can connect in some very broad and complex shapes
    # If no connected box is blocked by a wall then the boxes are definitely pushable
    # If any box is connected to a wall then none of them can be pushed

    elif step in ["^", "v"]:
        # Build a list of locations for all connected boxes (use numpy format)
        connected_boxes_move_from = [[], []]    # structure (array([]), array([])
        # Add the current box to start a processing list
        box_search_processing_list = [next_position]
        # Now search for all connected boxes
        while len(box_search_processing_list) != 0:
            # Start with current box
            current_box_to_check = box_search_processing_list.pop()
            current_box_to_check_contents = warehouse_map[current_box_to_check]

            # If any connecting space is a wall stop and don't move anything
            if current_box_to_check_contents == "#":
                space_to_push_box = False
                return warehouse_map, space_to_push_box
            # If the current box to check is part of a box add as a connected box to be moved
            elif current_box_to_check_contents in ["[", "]", "O"]:
                connected_boxes_move_from[0].extend([current_box_to_check[0]])
                connected_boxes_move_from[1].extend([current_box_to_check[1]])
                # Must add the second half of the box the robot encountered
                if current_box_to_check_contents == "[":
                    connected_boxes_move_from[0].extend([current_box_to_check[0]])
                    connected_boxes_move_from[1].extend([current_box_to_check[1] + 1])
                elif current_box_to_check_contents == "]":
                    connected_boxes_move_from[0].extend([current_box_to_check[0]])
                    connected_boxes_move_from[1].extend([current_box_to_check[1] - 1])
            # If the current space is a box add the spaced behind it (in the push direction) to the list to process next
            if current_box_to_check_contents == "[":
                box_search_processing_list.extend([(current_box_to_check[0] + next_step[step][0], current_box_to_check[1] + next_step[step][1])])
                box_search_processing_list.extend([(current_box_to_check[0] + next_step[step][0], current_box_to_check[1] + next_step[step][1] + 1)])
            elif current_box_to_check_contents == "]":
                box_search_processing_list.extend([(current_box_to_check[0] + next_step[step][0], current_box_to_check[1] + next_step[step][1] - 1)])
                box_search_processing_list.extend([(current_box_to_check[0] + next_step[step][0], current_box_to_check[1] + next_step[step][1])])
            elif current_box_to_check_contents == "O":
                box_search_processing_list.extend([(current_box_to_check[0] + next_step[step][0], current_box_to_check[1] + next_step[step][1])])

        # If we have not already returned then the boxes can be pushed
        space_to_push_box = True
        # Set up tuple with arrays for the boxes to move and where they go (1 unit in the step direction)
        connected_boxes_move_from = (np.array(connected_boxes_move_from[0]), np.array(connected_boxes_move_from[1]))
        # Copy the array of boxes to move and increment the row value by 1 in the step direction
        connected_boxes_move_to = (connected_boxes_move_from[0].copy(), connected_boxes_move_from[1].copy())
        for i in range(len(connected_boxes_move_from[0])):
            if step == "^":
                connected_boxes_move_to[0][i] = connected_boxes_move_from[0][i] - 1
            elif step == "v":
                connected_boxes_move_to[0][i] = connected_boxes_move_from[0][i] + 1

        # Move the boxes to the new locations and replace their old locations with "."
        warehouse_map[connected_boxes_move_from], warehouse_map[connected_boxes_move_to] = ".", warehouse_map[connected_boxes_move_from]
        # Update the robot locator so prints of the map are prettier
        warehouse_map[next_position], warehouse_map[current_position] = "@", "."
    return warehouse_map, space_to_push_box


def calculate_sum_gps(warehouse_map, symbol):
    sum_gps = 0
    box_locations = np.transpose(np.where(warehouse_map == symbol))
    for row, col in box_locations:
        sum_gps += (row*100) + col
    return sum_gps

def build_double_map(warehouse_map):
    warehouse_map_shape = np.shape(warehouse_map)
    warehouse_double_map_shape = (warehouse_map_shape[0], warehouse_map_shape[1] * 2)
    warehouse_double_map = np.full(warehouse_double_map_shape, fill_value="X", dtype=np.str_)
    for row in range(warehouse_map_shape[0]):
        for col in range(warehouse_map_shape[1]):
            if warehouse_map[row,col] == "@":
                warehouse_double_map[row, 2*col:2*col + 2] = ["@","."]
            elif warehouse_map[row,col] == "O":
                warehouse_double_map[row, 2 * col:2 * col + 2] = ["[","]"]
            else:
                warehouse_double_map[row, 2 * col:2 * col + 2] = warehouse_map[row,col]
    return warehouse_double_map

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2024\Day15\Puzzle_Input.txt"
    warehouse_initial_map, directions = read_input_data(filename)

    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=======================  Puzzle Input  =======================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"The initial layout of the warehouse is as follows: ", "bk", "wt"))
    print_array(warehouse_initial_map)
    print(fstring(f"There are {len(directions)} robot directions, as follows: ", "bk", "wt"))
    print(directions)
    print(fstring(f"====================  Puzzle Input - End =====================", "bk", "bl"))

    print(" ", end="\n\n")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=========================  PART ONE  =========================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))

    warehouse_map = warehouse_initial_map.copy()
    warehouse_map = process_robot_movement(warehouse_map, directions)
    symbol = "O"
    sum_gps = calculate_sum_gps(warehouse_map, symbol)
    part_one_ans = str(sum_gps)

    print(fstring(f"After {len(directions)} moves the robot has achieved the following: ", "bk", "wt"))
    print_array(warehouse_map)
    print(fstring(f"The sum of the gps coordinates is: {part_one_ans}", "bk","wt"))
    print(fstring(f"======================  PART ONE - END  ======================", "bk", "bl"))

    print(" ", end="\n\n")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=========================  PART TWO  =========================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))

    warehouse_map = warehouse_initial_map.copy()
    warehouse_double_map = build_double_map(warehouse_map)
    warehouse_double_map = process_robot_movement(warehouse_double_map, directions)
    symbol = "["
    sum_gps = calculate_sum_gps(warehouse_double_map, symbol)
    part_two_ans = str(sum_gps)

    print(fstring(f"After {len(directions)} moves the robot has achieved the following: ", "bk", "wt"))
    print_array(warehouse_double_map)
    print(fstring(f"The sum of the gps coordinates is: {part_two_ans}", "bk", "wt"))
    print(fstring(f"======================  PART TWO - END  ======================", "bk", "bl"))

    print(" ", end="\n\n")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=========================  ANSWERS  ==========================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))
    print(f'{fstring("Part One:", "bk", "wt")}')
    print(f'The total calibration result is: {fstring(part_one_ans, "wt", "bk")}')
    print(fstring(f"==============================================================", "bk", "bl"))
    print(f'{fstring("Part Two:", "bk", "wt")}')
    print(f'The total calibration result is: {fstring(part_two_ans, "wt", "bk")}')
    print(fstring(f"==============================================================", "bk", "bl"))
    print(" ")

    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()