import numpy as np
import time
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

def reading_input_data(fI):
    print("Reading input data...", end = "")
    print("[complete]", end="\n")
    print(" ")
    data = np.array([], dtype=int)
    number_of_lines, number_of_numbers = 0, 0
    only_once = False
    for each_line in fI:
        # Lets read in all the key information
        each_line = (each_line.strip("\n")).split()
        number_of_lines += 1
        number_of_numbers += len(each_line)
        if only_once == True:
            data = np.vstack((data, np.int64(each_line)))
        else:
            data = np.int64(each_line)
            only_once = True
    del(each_line, only_once)
    fI.close()
    print("Number of lines:",number_of_lines,"and size of data array:",np.shape(data))
    return data, number_of_lines

def process_extrapolation(data_i, i, fO):
    counter, extrapolated_value = 0, 0
    temp = temp1 = np.array(data_i, dtype=int)
    counter = 1
    while np.sum(np.abs(temp1)) != 0:
        temp1 = np.array(np.diff(temp1), dtype=int) # difference rows
        temp = np.array(np.vstack((temp, np.zeros(len(data_i)))), dtype=int) # Stick in row of zeros
        temp[counter, counter:counter + len(temp1) + 1] = temp1 # fill row with difference output
        counter += 1
    temp = np.insert(temp, 0, np.zeros((1, counter)),axis=1) # Add zeros to the start of the array
    temp = np.array(temp, dtype=int) # make integer array
    if np.sum(np.abs(temp1)) == 0:
        # Lets reconstruct
        for j in range(counter - 1): # Must not wrap over to top of array
            temp[counter - j - 2, np.shape(temp)[1] - len(temp1) - j - 2] = temp[counter - j - 2, np.shape(temp)[1] - len(temp1) - j - 1] - temp[counter - j - 1, np.shape(temp)[1] - len(temp1) - j - 1]
            extrapolated_value = temp[counter - j - 2, np.shape(temp)[1] - len(temp1) - j - 2]
    return extrapolated_value, counter

def main():
    total_extrapolated_values = np.array([(0)], dtype=int)
    ts0 = time.time()
    test_counter_index = counter_index = np.array([(0)], dtype=int)
    print("Starting time:", time.ctime())
    print(" ")
    fI = open(r'D:\Advent_of_Code\Advent_of_Code_2023\Day9\Puzzle_Input.txt', 'r')
    fO = open(r"D:\Advent_of_Code\Advent_of_Code_2023\Day9\output.txt", "w")
    # Read all of the input data from Puzzle Input and organise it
    data, number_of_lines = reading_input_data(fI)
    # Step through the data and see how many steps it takes to complete the puzzle
    i = number_of_lines
    for i in range(number_of_lines):
        data_i = data[i, :]
        extrapolated_value, counter = process_extrapolation(data_i, i, fO)
        counter_index = np.append(counter_index, counter)
        total_extrapolated_values = np.append(total_extrapolated_values, extrapolated_value)
    print("The total for the extrapolated values for the puzzle is:", np.sum(total_extrapolated_values))
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())
    fO.close()

if __name__ == "__main__":
    main()