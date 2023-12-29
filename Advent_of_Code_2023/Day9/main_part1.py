import numpy as np
import time

def reading_input_data(f):
    print("Reading input data...", end = "")
    print("[complete]", end="\n")
    print(" ")
    data = np.array([], dtype=int)
    number_of_lines = 0
    only_once = False
    for each_line in f:
        # Lets read in all the key information
        each_line = (each_line.strip("\n")).split()
        number_of_lines += 1
        if only_once == True:
            data = np.vstack((data, np.int32(each_line)))
        else:
            data = np.int32(each_line)
            only_once = True
    del(each_line, only_once)
    return data, number_of_lines

def process_extrapolation(data_i, i):
    test_node = "de"
    if i == test_node:
        print(data_i)
    counter, extrapolated_value = 0, 0
    temp = temp1 = np.array(data_i, dtype=int)
    while np.sum(temp1) != 0:
        temp1 = np.array(np.diff(temp1), dtype=int)
        temp = np.array(np.vstack((temp, np.zeros(len(data_i)))), dtype=int)
        temp[counter + 1, 0:len(temp1)] = temp1
        counter += 1
    temp = np.hstack((temp, np.zeros((counter + 1, len(data_i)))))
    temp = np.array(temp, dtype=int)
    if i == test_node:
        print(temp)
    if np.sum(temp1) == 0:
        # Lets reconstruct
        for j in range(counter):
            temp[counter - j - 1, len(temp1) + j + 1] = temp[counter - j, len(temp1) + j] + temp[counter - j - 1, len(temp1) + j]
            extrapolated_value = temp[counter - j - 1, len(temp1) + j + 1]
            if i == test_node:
                print(temp)
    if data_i[len(data_i)-1]/extrapolated_value > 0.95 or data_i[len(data_i)-1]/extrapolated_value < 0:
        print(data_i[len(data_i)-1]/extrapolated_value, i)
    if i == test_node:
        print(temp)
        print(extrapolated_value)
    return extrapolated_value

def main():
    total_extrapolated_values = np.array([(0)], dtype=int)
    ts0 = time.time()
    print("Starting time:", ts0)
    print(" ")
    f = open(r'D:\Advent_of_Code\Advent_of_Code_2023\Day9\Puzzle_Input.txt', 'r')
    # Read all of the input data from Puzzle Input and organise it
    data, number_of_lines = reading_input_data(f)
    # Step through the data and see how many steps it takes to complete the puzzle
    print(number_of_lines)
    print(range(number_of_lines))
    for i in range(number_of_lines):
        data_i = data[i, :]
        #print("======================")
        #print("NEW LINE")
        #print("======================")
        extrapolated_value = process_extrapolation(data_i, i)
        total_extrapolated_values = np.append(total_extrapolated_values, extrapolated_value)
    print(total_extrapolated_values)
    print(np.max(total_extrapolated_values), np.min(total_extrapolated_values))
    #print(len(total_extrapolated_values))
    print("The total for the extrapolated values for the puzzle is:", np.sum(total_extrapolated_values))
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()