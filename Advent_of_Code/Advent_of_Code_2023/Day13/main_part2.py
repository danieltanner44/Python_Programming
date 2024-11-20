import numpy as np
import time

def reading_input_data(fI):
    only_once = finished_reading = False
    for each_line in fI:
        temp = np.array([], dtype=int)
        if len(each_line) == 1: # Means that it found an eol character only so end of an input block
            return finished_reading, data_block
        else: # This is an actual input line from a block
            each_line = (each_line.strip("\n")).split()
        for i in range(len(each_line[0][:])): # step along the line and convert to 1s and 0s
            if each_line[0][i] == ".": # operational
                temp = np.append(temp, 0)
            elif each_line[0][i] == "#": # broken
                temp = np.append(temp, 1)
        if only_once == True:
            data_block = np.vstack((data_block, temp)) # Build each block
        else:
            data_block = np.array(temp, dtype=int)
            only_once = True
    finished_reading = True # this sets the eof found and then returns
    return finished_reading, data_block

def detect_reflections(data_blocks, eval, only_once):
    reflection_index = np.array([], dtype=int)
    # Check across columns (vertical reflection axis)
    for i in range(1,np.shape(data_blocks)[1]): # Columns
        dist = min(i, np.shape(data_blocks)[1] -i)
        if np.sum(np.abs(np.subtract(data_blocks[:,i-dist:i], np.fliplr(data_blocks[:,i:i+dist])))) == 1 and only_once == False: # captures all the reflections with an axis between columns
            index = np.array(np.where(np.abs(np.subtract(data_blocks[:, i - dist:i], np.fliplr(data_blocks[:, i:i + dist]))) == 1))
            only_once = True
            if eval == "col":
                data_blocks[index[0], index[1]] = (data_blocks[index[0], index[1]] + 1)%2 # Flip its value
            else:
                data_blocks[index[0], index[1]] = (data_blocks[index[0], index[1]] + 1)%2 # Flip its value
            print("found smudge")
            reflection_index = np.append(reflection_index, i)
    if eval == "col":
        print(data_blocks)
    else:
        print(np.rot90(data_blocks, -1))
    return reflection_index, only_once

def main():
    ts0 = time.time()
    total_score, counter = 0, 1
    print("Starting time:", ts0)
    print(" ")
    fI = open(r'D:\Advent_of_Code\Advent_of_Code_2023\Day13\Puzzle_Input.txt', 'r')
    finished_reading = False
    # Read all of the input data from Puzzle Input and organise it
    while finished_reading == False:
        print("Reading data block...", counter)
        # Read a block of data
        finished_reading, data_block = reading_input_data(fI)
        for i in [0,1]:
            only_once = False
            if i == 0: # detect column mirrors
                eval = "col"
                reflection_index, only_once = detect_reflections(data_block, eval, only_once)
                total_score += np.sum(reflection_index)
                print("     Vertical symmetries found at index:", reflection_index)
            elif i == 1: # detect row mirrors
                eval = "row"
                data_block_t = np.rot90(data_block)
                reflection_index, only_once = detect_reflections(data_block_t, eval, only_once)
                print("     Horizontal symmetries found at index:", reflection_index)
                total_score += 100 * np.sum(reflection_index)
        print(" ")
        counter += 1
    print("The total score is:",total_score)
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()