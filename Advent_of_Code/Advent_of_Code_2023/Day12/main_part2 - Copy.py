import numpy as np
import time
import itertools

def reading_input_data(f):
    print("Reading input data...", end = "")
    data = np.array([], dtype=int)
    only_once = False
    for each_line in f:
        temp = temp1 = temp2 = temp3 = np.array([], dtype=int)
        counter = 0
        # Lets read in all the key information
        each_line = (each_line.strip("\n")).split()
        for i in range(len(each_line[0][:])):
            if each_line[0][i] == ".": # operational
                temp = np.append(temp, 0)
            elif each_line[0][i] == "#": # broken
                temp = np.append(temp, 1)
            elif each_line[0][i] == "?": # unknown
                temp = np.append(temp, 9)
            counter += 1
        temp1 = temp
        for i in range(4):
            if i != 4:
                temp1 = np.append(temp1, 9)
            temp1 = np.append(temp1, temp)
        temp = temp1
        temp = np.insert(temp, 0, (counter*5) + 4, axis=0)
        temp2 = each_line[1][:].split(",")
        for i in range(len(temp2)):
            try:
                temp3 = np.append(temp3, int(temp2[i]))
            except:
                continue
        for i in range(5):
            temp = np.append(temp, temp3)
        if only_once == True:
            data += [list(temp)]
        else:
            data = [list(temp)]
            only_once = True
    del(each_line, only_once, temp, temp1, temp2, temp3, counter)
    print("[complete]", end="\n")
    print(" ")
    print("The input data is:", "\n", "", data)
    print("There are", len(data),"lines to unscramble!")
    return data

def combinations(index_of_unknowns, number_of_unknowns): # Maybe counld change to an actual iteration where I check that the resultant combination has at least the correct number of "#" and "."
    # This is too memory intensive
    print("Producing combinations!")
    for i in range(number_of_unknowns + 1):
        yield from itertools.combinations(index_of_unknowns, i)

def count_combinations(data, temp):
    match, counter = False, 0
    counter_index = np.array([], dtype=int)
    for i in range(len(temp) - 1):
        if temp[i] == 1:
            counter += 1
        if temp[i] == 1 and temp[i + 1] == 0:
            counter_index = np.append(counter_index, counter)
            counter = 0
            if counter_index[len(counter_index) - 1] != data[data[0] + 1 -1 + len(counter_index)]:
                return match
        if i == len(temp) - 2:
            if temp[i + 1] == 1:
                counter += 1
                counter_index = np.append(counter_index, counter)
                counter = 0
    if np.array_equal(counter_index, data[data[0] + 1:len(data)]) == True:
        match = True
    else:
        match = False
    del(counter, counter_index, temp)
    return match

def unscramble(data):
    number_of_combinations, number_of_unknowns = 0, 0
    temp = np.array(data[1:data[0] + 1], dtype=int)
    data_template = np.array(data[1:data[0] + 1], dtype=int)
    index_of_unknowns = np.array([], dtype=int)
    options = np.array([0,1],dtype=int)
    # ref characters: !! "."0 # operational !! "#"1 # broken !! "?"9 # unknown
    for i in range(len(data_template)):
        if data_template[i] == 9:
            number_of_unknowns += 1
            index_of_unknowns = np.append(index_of_unknowns, i)
            data_template[i] = options[0]
    # Lets find our possible combinations for this number of unknowns
    current_combinations = list(combinations(index_of_unknowns, number_of_unknowns))
    #print(current_combinations)
    for i in range(len(current_combinations)):
        # Now update each combination and check
        temp = np.array(data_template)
        for j in range(len(current_combinations[i])):
            temp[current_combinations[i][j]] = options[1]
        match = False
        if np.sum(temp) == np.sum(data[data[0] + 1:len(data)]):  # If they do not have the same number of broken springs then cannot be a solution
            match = count_combinations(data, temp)
        if match == True:
            number_of_combinations += 1
    del(temp, current_combinations, data_template, options, index_of_unknowns, number_of_unknowns)
    return number_of_combinations

def main():
    ts0 = time.time()
    print("Starting time:", ts0)
    print(" ")
    total_combinations, combinations = 0, 0
    f = open(r'D:\Advent_of_Code\Advent_of_Code_2023\Day12\Puzzle_Input_d.txt', 'r')
    # Read all of the input data from Puzzle Input and organise it
    data = reading_input_data(f)
    # take one line at a time and figure it out
    for i in range(len(data)):
        if i%2 == 0:
            print("Complete processing of ",(i//len(data))*100,"% of data")
        number_of_combinations = unscramble(data[i])
        total_combinations = np.append(total_combinations, number_of_combinations)
    print(total_combinations)
    print("The total number of combinations is",np.sum(total_combinations),"for", len(data), "sets of spring rows")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()