import numpy as np
import time

def reading_input_data(f):
    print("Reading input data...", end = "")
    print("[complete]", end="\n")
    print(" ")
    data = np.array([], dtype=int)
    num_galaxies = 0
    only_once = False
    for each_line in f:
        temp = np.array([], dtype=int)
        # Lets read in all the key information
        each_line = (each_line.strip("\n")).split()
        for i in range(len(each_line[0][:])):
            if each_line[0][i] == ".":
                temp = np.append(temp, 0)
            elif each_line[0][i] == "#":
                num_galaxies += 1
                temp = np.append(temp, num_galaxies)
        if only_once == True:
            data = np.vstack((data, temp))
        else:
            data = temp
            only_once = True
    del(each_line, only_once, temp)
    print("The input data is:", "\n", "", data)
    print("There are", num_galaxies,"galaxies!")
    return data, num_galaxies

def expansion(data):
    for i in range(np.shape(data)[0] - 1, 0, -1): # rows
        if np.sum(data[i,:]) == 0:
            data = np.insert(data, i, data[i,:], axis=0)
    for j in range(np.shape(data)[1] - 1, 0, -1): # columns
        if np.sum(data[:,j]) == 0:
            data = np.insert(data, j, data[:,j], axis=1)
    return data

def finding_distances(data, num_galaxies):
    num_galaxy_pairs = np.sum(range(num_galaxies))
    total_distance, pairs = 0, 0
    for z in range(1,num_galaxies + 1):
        for i in range(np.shape(data)[0]):
            for j in range(np.shape(data)[1]):
                if data[i,j] == z:
                    source_index = [i,j]
                if data[i,j] > z:
                    total_distance += abs(source_index[0] - i) + abs(source_index[1] - j)
                    pairs += 1
    return total_distance, num_galaxy_pairs

def main():
    ts0 = time.time()
    print("Starting time:", ts0)
    print(" ")
    f = open(r'D:\Advent_of_Code\Advent_of_Code_2023\Day11\Puzzle_Input.txt', 'r')
    # Read all of the input data from Puzzle Input and organise it
    data, num_galaxies = reading_input_data(f)
    # Step all of the characters and make masks to help step later
    data = expansion(data)
    total_distance, num_galaxy_pairs = finding_distances(data, num_galaxies)

    print("The total distances between the",num_galaxy_pairs,"galaxy pairs is:", total_distance)
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()