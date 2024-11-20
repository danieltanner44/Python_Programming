import numpy as np
import time

ts0 = time.time()
print("Starting time:", time.ctime())
# Lets read all of the input data
f = open(r'D:\Advent_of_Code\Advent_of_Code_2023\Day5\Puzzle_Input.txt', 'r')
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
f.close()
maps = np.delete(maps, 0, 0)
maps = np.int64(maps)
maps = np.column_stack((maps, maps[:, 1] + maps[:, 2]))
maps = np.column_stack((maps, maps[:, 0] - maps[:, 1]))
number_of_maps = np.delete(number_of_maps,0)
number_of_maps = np.append(number_of_maps, counter[1])
number_of_maps = np.diff(number_of_maps)
del(counter)

ts1 = time.time()
print(" ")
print("Inputs read")
print("Total number of seeds to process is:", sum(seeds_list[1::2]))
print(" ")
print("Elapsed time:", round((ts1 - ts0)/3600,2), "hours or", round((ts1 - ts0),1),"seconds!")

# Create a function to map between input and output ranges
# Main Loop!
# Create full list of seeds
print("There are",round(len(seeds_list)/2), "sets of seed numbers that must be iterated!")
print(" ")
seed_input_numbers = np.array([], dtype=np.int64)
input_number_to_map = np.array([], dtype=np.int64)
only_once = False
number_of_maps_accumulator = np.insert(np.add.accumulate(number_of_maps), 0, 0)
for z in range(0, len(seeds_list), 2):
    print(str(int((z + 2) / 2)), ") This set of seed numbers is: ", seeds_list[z+1], "long!")
    print("     This is", (100*seeds_list[z+1]//sum(seeds_list[1::2])),"% of the total number of seeds...")
    print("     Once complete", (100*sum(seeds_list[1:z+2:2])//sum(seeds_list[1::2])),"% of the total number of seeds will have been processed!")
    print(" ")
    if (seeds_list[z+1]) > 10000000:
        num_chunks = 10
    else:
        num_chunks = 1
    for y in range(num_chunks):
        seed_input_numbers = np.array(np.arange(seeds_list[z] + y*round((seeds_list[z + 1] / num_chunks)), seeds_list[z] + ((y+1) * round(seeds_list[z + 1] / num_chunks)),step=1, dtype=np.int64))
        print("     Breaking this into", num_chunks, "chunks of approximate length", round(seeds_list[z+1]/num_chunks),"- Processing Chunk", y + 1,"...")
        for input_number_to_map in seed_input_numbers:
            for j in range(len(number_of_maps)):
                for k in range(number_of_maps[j]):
                    offset = number_of_maps_accumulator[j] + k
                    if maps[offset,1] <= input_number_to_map <= maps[offset,3]:
                        # Am in current range so lets map and leave
                        input_number_to_map = maps[offset,4] + input_number_to_map
                        break
            if only_once == False:
                location_number, only_once = input_number_to_map, True
            location_number = min(location_number, input_number_to_map)
            #print("Seed ", i + 1, " has value ", seed_input_numbers[i], " and maps to location: ", location_number)
    print("     The minimum location number is: ", location_number)
    ts2 = time.time()
    print("     Elapsed time:", round((ts2 - ts0)/3600,2), "hours or", round((ts2 - ts0),1),"seconds!")
    print(" ")
print("Finishing time:", time.ctime())