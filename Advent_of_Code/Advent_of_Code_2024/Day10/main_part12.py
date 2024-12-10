import time
import numpy as np
from my_modules.development import fstring
from my_modules.development import print_array
from my_modules.development import determine_num_duplicates_in_list
import math

def read_input_data(filename):
    map = []
    with open(filename, 'r') as f:
        for line in f:
            map.append([int(element) for element in list(line.strip())])
    map = np.array(map, dtype=np.int8)
    return map

def find_heights_around_me(map, current_location, current_height):
    next_locations = []
    map_shape = np.shape(map)
    for row_index, col_index in [(-1,0), (1, 0), (0,-1), (0, 1)]:
        row_index += current_location[0]
        col_index += current_location[1]
        # Check if indices are still on map:
        if row_index >= 0 and col_index >= 0 and row_index < map_shape[0] and col_index < map_shape[1]:
            if map[row_index, col_index] == current_height + 1: # Look for the next height from current height
                next_locations.append((row_index, col_index))
    return next_locations

def find_trailhead_paths(map):
    all_trailhead_paths = []
    # All trailheads start at a height of 0 (so find them on the map)
    trailhead_locations = np.where(map == 0)
    num_trailheads = len(trailhead_locations[0])

    # Loop over each trailhead in turn and find all paths that lead to a summit (height 9)
    for trailhead_index in range(num_trailheads):
        trailhead_paths = []  # Keep track of the paths
        paths_to_process = [] # Set up a list of paths and process one step at a time
        # The current location is the starting location of the trailhead
        current_location = (trailhead_locations[0][trailhead_index],trailhead_locations[1][trailhead_index])
        current_height = map[current_location]  # Current height of step we are on (always 0 at starting point)
        # Now start a list to process steps as paths can diverge
        # To start the list add the trailhead starting point and its current height
        paths_to_process.append([[current_location, current_height]])
        # Now keep processing until the paths to process is empty
        while len(paths_to_process) != 0: # Walk the paths
            # Remove/pop the last path from the paths_to_process list and process its next steps
            path = paths_to_process.pop()
            current_location, current_height = path[-1]
            # Find any valid next locations that can be reached
            # These are locations that are 1 height higher in any of the cardinal directions
            next_locations = find_heights_around_me(map, current_location, current_height)
            # Now process each of the possible next locations
            if len(next_locations) == 0:
                # No more steps to make and not at height 9 so just stop (already popped from paths_to_process list)
                continue
            else:
                # Increment the height of the next step
                current_height += 1
            for location in next_locations:
                # Add each new viable location as the next step on the original path
                if current_height != 9:
                    # We popped the original path but now add back a new path for each possible next location
                    # This is the original path plus the next location
                    paths_to_process.append(path + [[location, current_height]])
                else:
                    # If we have reached the summit store the path but it is no longer on the process list
                    trailhead_paths.append(path + [[location, current_height]])
        # This is a master list of all paths from trailheads to summits
        # [[list of all paths from trailhead 0 to summits], [list of all paths from trailhead 1 to summits], ...]
        all_trailhead_paths.append(trailhead_paths)
    return all_trailhead_paths

def determine_trailhead_scores(all_trailhead_paths):
    # Store all data on trailhead scores and ratings as well as the values themselves
    all_trailhead_scores, sum_trailhead_scores = [], 0
    all_trailhead_ratings, sum_trailhead_ratings = [], 0
    for trailhead_index, paths_from_trailhead in enumerate(all_trailhead_paths):
        trailhead_starting_point = paths_from_trailhead[0][0]
        finishing_points = []
        all_trailhead_ratings.append([trailhead_index, len(paths_from_trailhead)])
        # The trailhead rating is the total number of paths from each trailhead to a summit (for non-unique summits)
        sum_trailhead_ratings += len(paths_from_trailhead)
        for path in paths_from_trailhead:
            # All paths from paths_from_trailhead have the same starting point
            # Capture the endpoint tuple positions to finishing_points
            finishing_points.append(path[-1][0])
        # The length of the set provides the number of unique summits
        finishing_points = set(finishing_points)
        all_trailhead_scores.append([trailhead_index, len(finishing_points)])
        # The trailhead scores are the total number of paths from each trailhead to a unique summit
        sum_trailhead_scores += len(finishing_points)
        location = f"({trailhead_starting_point[0][0]},{trailhead_starting_point[0][1]})"
        print(f"Trailhead ID: {trailhead_index}, Location: {location}, Trailhead Score: {len(finishing_points)}, Trailhead Rating: {len(paths_from_trailhead)}")
    return all_trailhead_scores, sum_trailhead_scores, all_trailhead_ratings, sum_trailhead_ratings

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2024\Day10\Puzzle_Input.txt"
    map = read_input_data(filename)

    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=======================  Puzzle Input  =======================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"The initial map has shape {np.shape(map)} and is: ", "bk", "wt"))
    print_array(map)
    print(fstring(f"====================  Puzzle Input - End =====================", "bk", "bl"))

    print(" ", end="\n\n")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"======================  PART ONE & TWO  ======================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))

    # Find all possible path from each trailhead that make it to any summit (height 9)
    all_trailhead_paths = find_trailhead_paths(map)
    all_trailhead_scores, sum_trailhead_scores, all_trailhead_ratings, sum_trailhead_ratings = determine_trailhead_scores(all_trailhead_paths)
    part_one_ans = str(sum_trailhead_scores)
    part_two_ans = str(sum_trailhead_ratings)
    print(fstring(f"===================  PART ONE & TWO - End  ===================", "bk", "bl"))

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