import numpy as np
import time
import math

def reading_input_data(f):
    print("Reading input data...", end = "")
    print("[complete]", end="\n")
    print(" ")
    # Lets read all of the input data
    symbol_list = {"\n","(",")",","}
    directions = []
    data = np.array([])
    starting_list = np.array([], dtype=int)
    finishing_list = np.array([], dtype=int)
    number_of_maps = 0
    only_once = False
    for each_line in f:
        # Lets read in all the key information
        if number_of_maps >= 2:
            each_line = each_line.split()
            temp = each_line[0]
            if temp[2] == "A":
                starting_list = np.append(starting_list, (number_of_maps - 2))
            if temp[2] == "Z":
                finishing_list = np.append(finishing_list, (number_of_maps - 2))
            for symbol in symbol_list:
                each_line = [element.replace(symbol, "") for element in each_line]
            if only_once == False:
                data = each_line
                only_once = True
            else:
                data = np.vstack((data, each_line))
            number_of_maps += 1
        elif number_of_maps == 0:
            temp1 = each_line.strip("\n")
            number_of_maps += 1
            continue
        elif number_of_maps == 1:
            number_of_maps += 1
            continue
    # Tidy up input data
    starting_list = starting_list
    finishing_list = finishing_list
    [directions.append(letter) for letter in temp1]
    data = np.delete(data, 1, 1)
    side = {"L" : 1, "R" : 2}
    directions_int = np.array([], dtype=int)
    for i in range(0,len(directions)):
        directions_int = np.append(directions_int, side.get(directions[i]))
    my_list = dict(zip(data[:,0],range(np.shape(data)[0])))
    for i in range(np.shape(data)[0]):
        for j in range(np.shape(data)[1]):
            data[i,j] = my_list.get(data[i,j])
    print("List of starting nodes is:", starting_list)
    print("List of finishing nodes is:", finishing_list)
    del (temp, temp1, symbol_list, directions, only_once, number_of_maps, each_line, side)
    return data, my_list, directions_int, starting_list, finishing_list

def stepping(data, directions_int, starting_list, finishing_list):
    number_of_steps, done = 0, False
    current_row = starting_list
    i_range = range(len(directions_int))
    num_i_range = len(i_range)
    j_range = range(len(starting_list))
    n_cycle = np.ones(len(starting_list), dtype=int)
    found_node = np.ones(len(starting_list), dtype=int)
    print(" ")
    print("Stepping through all maps...")
    while done == False:
        for i in i_range:
            current_row[:] = data[current_row[:], directions_int[i % num_i_range]]
            for j in j_range:
                for k in j_range:
                    if current_row[j] == finishing_list[k]:
                        if found_node[j] == 1:
                            print("Found node:", j, "with this n_cycle", number_of_steps + i, "finishing value is:", current_row[j])
                            found_node[j] = 0
                            n_cycle[j] = number_of_steps + i + 1
                            print("Nodes found so far:", found_node)
                        if np.sum(found_node) == 0:
                            return done, n_cycle
        number_of_steps += num_i_range
        if number_of_steps % 1000 == 0:
            print("Number of search cycles is:", number_of_steps)
    del(current_row)

def main():
    ts0 = time.time()
    print("Starting time:", ts0)
    print(" ")
    f = open(r'D:\Advent_of_Code\Advent_of_Code_2023\Day8\Puzzle_Input.txt', 'r')
    # Read all of the input data from Puzzle Input and organise it
    data, my_list, directions_int, starting_list, finishing_list = reading_input_data(f)
    # Step through the data and see how many steps it takes to complete the puzzle
    done, n_cycle = stepping(data, directions_int, starting_list, finishing_list)
    print("The number of steps required to complete the puzzle are:", math.lcm(*n_cycle))
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()