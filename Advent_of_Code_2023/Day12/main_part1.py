import numpy as np
import time

def reading_input_data(f):
    print("Reading input data...", end = "")
    data = np.array([], dtype=int)
    only_once = False
    for each_line in f:
        temp = np.array([], dtype=int)
        counter = 0
        # Lets read in all the key information
        each_line = (each_line.strip("\n")).split()
        for i in range(len(each_line[0][:])):
            if each_line[0][i] == ".":
                temp = np.append(temp, 0)
            elif each_line[0][i] == "#":
                temp = np.append(temp, 1)
            elif each_line[0][i] == "?":
                temp = np.append(temp, 9)
            counter += 1
        temp = np.insert(temp, 0, counter, axis=0)
        for i in range(len(each_line[1][:])):
            try:
                temp = np.append(temp, int(each_line[1][i]))
            except:
                continue
        if only_once == True:
            data += [list(temp)]
        else:
            data = [list(temp)]
            only_once = True
    del(each_line, only_once, temp)
    print("[complete]", end="\n")
    print(" ")
    print("The input data is:", "\n", "", data)
    print("There are", len(data),"lines to unscramble!")
    return data

def unscramble(data):
    for i in range(len(data)):
        output = i
    return output

def main():
    ts0 = time.time()
    print("Starting time:", ts0)
    print(" ")
    f = open(r'D:\Advent_of_Code\Advent_of_Code_2023\Day12\Puzzle_Input_d.txt', 'r')
    # Read all of the input data from Puzzle Input and organise it
    data = reading_input_data(f)
    output = np.array([0]*len(data), dtype=int)
    # take one line at a time and figure it out
    for i in range(len(data)):
        output[i] = unscramble(data[i])

    #print("The total distances between the",num_galaxy_pairs,"galaxy pairs is:", total_distance)
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()