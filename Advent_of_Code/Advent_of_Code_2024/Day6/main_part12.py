import time
import numpy as np
from my_modules.development import fstring
from my_modules.development import print_array

def read_input_data(filename):
    guard_map = []
    with open(filename, 'r') as f:
        for line in f:
            guard_map.append(list(line.strip()))
    guard_map = np.array(guard_map, dtype=np.dtype('U128'))
    return guard_map

def predict_guard_route(guard_map):
    guard_route = np.array(guard_map.copy(), np.str_)
    map_shape = np.shape(guard_route)
    current_position = np.where(guard_route == "^")
    guard_route[current_position] = "Xu"
    current_direction = "u" # Up
    # Dictionary  to allow us to call the next direction (from our current direction) when a turn is needed
    turn = {"u" : "r", "r" : "d", "d" : "l", "l" : "u"} # Up -> right, down-> left, ...
    direction = {"u": [-1, 0], "r": [0, 1], "d": [1, 0], "l": [0, -1]}  # Up, right, down, left
    # From our starting point keep stepping until guard either: 1) leaves the map or 2) enters infinite loop
    while True:
        # Find the next position based on current direction
        for i in range(4):  # Try all four directions until the guard is free to step forward
            # Set the position
            new_position = (
            current_position[0] + direction[current_direction][0],
            current_position[1] + direction[current_direction][1])

            # Check if new position is off the map
            in_map = True  # Assume the new point is in the map and then check
            if (new_position[0] < 0 or new_position[1] < 0 or
                    new_position[0] >= map_shape[0] or new_position[1] >= map_shape[1]):
                in_map = False
                # If off the map just no need to check other directions
                break

            # Check if path is obstructed
            if guard_route[new_position] == "#":
                # If blocked turn and try again with a new step
                current_direction = turn[current_direction]
                continue
            else:
                # If the step is not blocked then use it
                break

        if in_map:
            # Each time the guard steps to a new position make sure it is marked as visited and appended with the current direction
            if guard_route[new_position][0][0] == "X": # Visited before
                # An infinite loop is detected if the guard visits this location again whilst travelling in the same direction
                if current_direction in list(guard_route[new_position][0][1:]):
                    exit_map_details = "loop"
                    return guard_route, exit_map_details
                else:
                    # If the guard was at this location before but not in the same direction then append direction and log as current position
                    guard_route[new_position] = guard_route[new_position] + current_direction
                    current_position = new_position
            else:
                # If the guard has not previously visited this location then mark as visited with our current direction appended
                guard_route[new_position] = f"X{current_direction}"
                current_position = new_position
        else:
            # If the step takes us out of the map then stop and return
            exit_map_details = f"Guard left map at {int(current_position[0][0]), int(current_position[1][0])} moving in the direction \"{current_direction}\""
            return guard_route, exit_map_details


def find_obstructions_to_create_loops(guard_map):
    # This is brute force: place an obstacle successively in each possible position and see if infinite loop results
    num_positions_for_loop = 0
    # Find all locations where an obstacle can be placed
    locations_to_place_obstructions = np.where(guard_map == ".")
    # Loop over each possible position, place the obstacle and check if an infinite loop results
    for index in range(len(locations_to_place_obstructions[0])):
        new_guard_map = guard_map.copy()
        # Set the obstruction location
        obstruction_location = (locations_to_place_obstructions[0][index], locations_to_place_obstructions[1][index])
        # Place it
        new_guard_map[obstruction_location] = "#"  # Place obstruction
        # Check if it is an infinite loop
        guard_route, exit_map_details = predict_guard_route(new_guard_map)
        if exit_map_details == "loop":
            num_positions_for_loop += 1
            print(f"{num_positions_for_loop}: Placing an obstruction at {int(obstruction_location[0]), int(obstruction_location[1])} causes infinite loop.")
    return num_positions_for_loop

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2024\Day6\Puzzle_Input.txt"
    guard_map = read_input_data(filename)

    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=======================  Puzzle Input  =======================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"The guard map has size {np.shape(guard_map)} and is as follows:", "bk", "wt"))
    print_array(guard_map)
    print(fstring(f"====================  Puzzle Input - End =====================", "bk", "bl"))

    print(" ", end="\n\n")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=========================  PART ONE  =========================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))
    guard_route, exit_map_details = predict_guard_route(guard_map)
    shape_guard_map = np.shape(guard_route)
    # Find locations the guard visited (first character is an "X")
    for row in range(shape_guard_map[0]):
        for col in range(shape_guard_map[1]):
            if guard_route[row, col][0][0] == "X":
                guard_route[row, col] = "X"
    num_locations_visited = len(np.where(guard_route == "X")[0])
    part_one_ans = str(num_locations_visited)
    print(fstring(f"The guard's route visits {num_locations_visited} locations and looks as follows:", "bk", "wt"))
    print_array(guard_route)
    print(fstring(exit_map_details, "bk", "wt"))
    print(fstring(f"======================  PART ONE - END  ======================", "bk", "bl"))

    print(" ", end="\n\n")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=========================  PART TWO  =========================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))
    num_positions_for_loop = find_obstructions_to_create_loops(guard_map)
    part_two_ans = str(num_positions_for_loop)
    print(fstring(f"======================  PART TWO - END  ======================", "bk", "bl"))

    print(" ", end="\n\n")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=========================  ANSWERS  ==========================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))
    print(f'{fstring("Part One:", "bk", "wt")}')
    print(f'The number of locations visited by the guard is: {fstring(part_one_ans, "wt", "bk")}')
    print(fstring(f"==============================================================", "bk", "bl"))
    print(f'{fstring("Part Two:", "bk", "wt")}')
    print(f'There are {fstring(part_two_ans, "wt", "bk")} locations that could lead to an infinite loop')
    print(fstring(f"==============================================================", "bk", "bl"))
    print(" ")

    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()