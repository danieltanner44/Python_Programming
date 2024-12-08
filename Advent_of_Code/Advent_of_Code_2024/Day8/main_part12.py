import time
import numpy as np
from my_modules.development import fstring
from my_modules.development import print_array
from my_modules.development import determine_num_duplicates_in_list
import math

def read_input_data(filename):
    signal_map = []
    with open(filename, 'r') as f:
        for line in f:
            signal_map.append(list(line.strip()))
    element_list = [element for line in signal_map for element in line if element != "."]
    antenna_dict = determine_num_duplicates_in_list(element_list)
    signal_map = np.array(signal_map, dtype=np.str_)
    return signal_map, antenna_dict

def find_antinodes(signal_map, antenna_dict):
    # This is the Part 1 Logic to count the number of antinodes
    antinode_counter = 0
    antinode_map = signal_map.copy()
    map_shape = np.shape(signal_map)
    # Loop over all sets of identical antenna
    for antenna_id in antenna_dict:
        # Find their locations
        antenna_locations = np.where(signal_map == antenna_id)
        # Look at the combinations of every antenna with all others
        for i in range(len(antenna_locations[0])):
            for j in range(len(antenna_locations[0])):
                if i != j:
                    # The antinode location is twice the distance away
                    # This only finds one antinode the other will be found for the opposite ordering of antenna
                    antinode_location = (2*antenna_locations[0][j] - antenna_locations[0][i],
                                         2*antenna_locations[1][j] - antenna_locations[1][i])
                    # Check if antinode locations are still on map
                    if not (antinode_location[0] < 0 or antinode_location[1] < 0 or
                            antinode_location[0] >= map_shape[0] or antinode_location[1] >= map_shape[1]):
                        # Antinode location is valid so place on map
                        # No need to count if it is already an antinode as only interested in unique locations
                        if antinode_map[antinode_location[0], antinode_location[1]] != "#":
                            antinode_map[antinode_location[0], antinode_location[1]] = "#"
                            antinode_counter += 1
    return antinode_map, antinode_counter

def find_resonant_antinodes(signal_map, antenna_dict):
    # This is the Part 2 Logic to count the number of resonant antinodes
    resonant_antinode_counter = 0
    resonant_antinode_map = signal_map.copy()
    map_shape = np.shape(signal_map)
    # Loop over all sets of identical antenna
    for antenna_id in antenna_dict:
        # Find their locations
        antenna_locations = np.where(signal_map == antenna_id)
        # Look at the combinations of every antenna with all others
        for i in range(len(antenna_locations[0])):
            for j in range(len(antenna_locations[0])):
                if i != j:
                    # The antinode location is twice the distance away
                    # This only finds one antinode the other will be found for the opposite ordering of antenna
                    resonant_antinode_direction = (antenna_locations[0][j] - antenna_locations[0][i],
                                         antenna_locations[1][j] - antenna_locations[1][i])
                    hcf = math.gcd(resonant_antinode_direction[0], resonant_antinode_direction[1])
                    # Find the smallest integer step possible for direction between antennas
                    step = (resonant_antinode_direction[0]//hcf, resonant_antinode_direction[1]//hcf)
                    # Now walk in the direction set by the two antennas, first backward and then forward
                    for direction in [-1,1]:
                        starting_location = (antenna_locations[0][j], antenna_locations[1][j])
                        # Walk until you exit the map
                        while True:
                            # The next location is the current one plus the step in the direction you are facing
                            new_location = (starting_location[0] + step[0]*direction,starting_location[1] + step[1]*direction)
                            # Check if resonant antinode location is still on map
                            if (new_location[0] < 0 or new_location[1] < 0 or
                                    new_location[0] >= map_shape[0] or new_location[1] >= map_shape[1]):
                                # If not break so can walk in other direction or stop walking
                                break
                            else:
                                # Antinode location is valid so place on map
                                # No need to count if it is already an antinode as only interested in unique locations
                                if resonant_antinode_map[new_location[0], new_location[1]] != "#":
                                    resonant_antinode_map[new_location[0], new_location[1]] = "#"
                                    resonant_antinode_counter += 1
                                starting_location = new_location
    return resonant_antinode_map, resonant_antinode_counter

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2024\Day8\Puzzle_Input.txt"
    signal_map, antenna_dict = read_input_data(filename)

    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=======================  Puzzle Input  =======================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"The signal map has shape {np.shape(signal_map)}, and is:", "bk", "wt"))
    print_array(signal_map)
    print(fstring(f"The map contains the following number of antenna: ", "bk", "wt"))
    [print(f"Antenna ID: {key}, Quantity: {value}") for key, value in antenna_dict.items()]
    print(fstring(f"====================  Puzzle Input - End =====================", "bk", "bl"))

    print(" ", end="\n\n")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=========================  PART ONE  =========================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))

    antinode_map, antinode_counter = find_antinodes(signal_map, antenna_dict)
    num_antinodes_in_unique_locations = len(np.where(antinode_map == "#")[0])
    part_one_ans = str(antinode_counter)

    print(fstring(f"The antinode map is: ", "bk", "wt"))
    print_array(antinode_map)
    print(fstring(f"There are {antinode_counter} antinodes, with {antinode_counter - num_antinodes_in_unique_locations} overlapped.", "bk", "wt"))
    print(fstring(f"======================  PART ONE - END  ======================", "bk", "bl"))

    print(" ", end="\n\n")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=========================  PART TWO  =========================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))

    resonant_antinode_map, resonant_antinode_counter = find_resonant_antinodes(signal_map, antenna_dict)
    num_resonant_antinodes_in_unique_locations = len(np.where(resonant_antinode_map == "#")[0])
    part_two_ans = str(resonant_antinode_counter)

    print(fstring(f"The resonant antinode map is: ", "bk", "wt"))
    print_array(resonant_antinode_map)
    print(fstring(
        f"There are {resonant_antinode_counter} resonant antinodes, with {resonant_antinode_counter - num_resonant_antinodes_in_unique_locations} overlapped.",
        "bk", "wt"))

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