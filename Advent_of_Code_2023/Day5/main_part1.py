import numpy as np

# Lets read all of the input data
f = open(r'D:\Advent_of_Code\Advent_of_Code_2023\Day5\Puzzle_Input.txt', 'r')
maps = []
location_number = 0
counter = np.zeros(2,int)
number_of_maps =[]
for each_line in f:
    each_line = each_line.rstrip("\n").split()
    # Lets read in all the key information
    if not each_line:
        # Move tp create new map
        counter[0] += 1
        number_of_maps.append(counter[1])
        next(f)
    elif each_line[0] == "seeds:":
        seeds_list = each_line[1:len(each_line)]
    else:
        maps.append(each_line)
    counter[1] += 1
number_of_maps.append(counter[1])
number_of_maps = np.diff(number_of_maps) - 1

# Create a function to map between input and output ranges
def mapping_function(input_number_to_map, j, maps, number_of_maps):
    for k in range(0,number_of_maps[j]):
        offset = sum(number_of_maps[0:j]) + k
        if (input_number_to_map >= int(maps[offset][1])) and (input_number_to_map <= (int(maps[offset][1]) + int(maps[offset][2]))):
            # Value in this input range
            input_number_to_map = (int(maps[offset][0]) + input_number_to_map - int(maps[offset][1]))
            return input_number_to_map
    return input_number_to_map

# Main loops across all seeds and maps - For each seed walk through each map
for i in range(0, len(seeds_list)):
    for j in range(0,len(number_of_maps)):
        if j == 0:
            input_number_to_map = int(seeds_list[i])
        input_number_to_map = mapping_function(input_number_to_map, j, maps, number_of_maps)
    # Keep count to see which is the minimum location number
    if i == 0:
        location_number = input_number_to_map
    else:
        location_number = min(location_number, input_number_to_map)
    print("Seed ",i + 1," maps to location: ", location_number)
print("The minimum location number is: ", location_number)
f.close()