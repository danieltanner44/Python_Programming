import numpy as np
import time
import threading

ts0 = time.time()
delay = 0
# Lets read all of the input data
f = open(r'D:\Advent_of_Code\Advent_of_Code_2023\Day5\Puzzle_Input_d1.txt', 'r')
maps = np.array([0,0,0], dtype=np.int64)
counter = np.zeros(2, dtype=np.int64)
number_of_maps = np.zeros(1, dtype=np.int64)
for each_line in f:
    each_line = each_line.rstrip("\n").split()
    # Lets read in all the key information
    if not each_line:
        # Move tp create new map
        counter[0] += 1
        number_of_maps = np.append(number_of_maps, counter[1])
        next(f)
    elif each_line[0] == "seeds:":
        seeds_list = np.array(list(map(int, each_line[1:len(each_line)])), dtype=np.int64)
    else:
        maps = np.vstack((maps, each_line))
        counter[1] += 1
maps = np.delete(maps, 0, 0)
maps = np.int64(maps)
number_of_maps = np.delete(number_of_maps,0)
number_of_maps = np.append(number_of_maps, counter[1])
number_of_maps = np.diff(number_of_maps)
del(counter)

ts1 = time.time()
print("Inputs read")
print("Elapsed time (s): ", ts1-ts0)
time.sleep(delay)

# Create a function to map between input and output ranges
def mapping_function(input_number_to_map, j, maps, number_of_maps):
    for k in range(0,number_of_maps[j]):
        offset = sum(number_of_maps[0:j]) + k
        if (input_number_to_map >= int(maps[offset][1])) and (input_number_to_map <= (int(maps[offset][1]) + int(maps[offset][2]))):
            # Am in current range so lets map and leave
            input_number_to_map = (int(maps[offset][0]) + input_number_to_map - int(maps[offset][1]))
            return input_number_to_map
    # In none of the ranges so leave me unchanged
    return input_number_to_map

# Main Loop!
# Create full list of seeds
print("There are",round(len(seeds_list)/2), "sets of seed numbers that must be iterated!")
print(" ")
seed_input_numbers = np.array([], dtype=np.int64)
input_number_to_map = np.array([], dtype=np.int64)
only_once = 1
location_number = 10000
for z in range(0, len(seeds_list), 2):
    seed_input_numbers = np.array(np.arange(seeds_list[z], seeds_list[z] + seeds_list[z + 1], step=1, dtype = np.int64))
    print(str(int(z/2)),") This set of seed numbers is: ", len(seed_input_numbers), "long!")
    time.sleep(delay)
    for i in range(0, np.shape(seed_input_numbers)[0]):
        input_number_to_map = seed_input_numbers[i]
        for j in range(0, np.shape(number_of_maps)[0]):
            input_number_to_map = mapping_function(input_number_to_map, j, maps, number_of_maps)
        location_number = min(location_number, input_number_to_map)
        #print("Seed ", i + 1, " has value ", seed_input_numbers[i], " and maps to location: ", location_number)
    print("The minimum location number is: ", location_number)
    ts2 = time.time()
    print("Elapsed time is in seconds is: ", ts2 - ts0)
    print(" ")

f.close()