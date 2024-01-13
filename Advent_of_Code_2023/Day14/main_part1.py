import numpy as np
import time

def reading_input_data(fI):
    print("Reading block of input data...")
    only_once = False
    for each_line in fI:
        each_line = (each_line.strip("\n")).split()[0]
        temp = np.array(list(each_line), dtype=str)
        if only_once == True:
            data = np.vstack((data, temp)) # Build each block
        else:
            data = np.array(temp, dtype=str)
            only_once = True
    return data

def tilting_level(data, size):
    R_indices = np.array(np.where(data == "#"))
    R_indices = np.array(list(zip(R_indices[0], R_indices[1])))
    R_indices = R_indices[R_indices[:, 1].argsort(kind="mergesort")]
    # Now we know where everything is lets start sorting
    for i in range(size[1]): # one column at a time
        starting_point = 0
        while data[starting_point, i] == "#":
            starting_point += 1
        found_one = False
        for R in R_indices:
            temp = np.array([], dtype=str)
            if R[1] == i:
                found_one = True
                temp = data[starting_point:R[0],i]
                temp = np.array(list(temp[temp[:].argsort(kind="mergesort")]))[::-1]
                data[starting_point:R[0],i] = temp
                starting_point = R[0]
                while data[starting_point, i] == "#" and starting_point != size[0]-1:
                    starting_point += 1
            elif found_one == True: # reached end of R rocks but had found an R rock previously
                temp = data[starting_point:size[0], i]
                temp = np.array(list(temp[temp[:].argsort(kind="mergesort")]))[::-1]
                data[starting_point:size[0], i] = temp
        if found_one == False: # Never found one then there are no R rocks in column
            temp = data[starting_point:size[0], i]
            temp = np.array(list(temp[temp[:].argsort(kind="mergesort")]))[::-1]
            data[starting_point:size[0], i] = temp
    return data

def score_calculation(data, size):
    total_score = 0
    O_indices = np.array(np.where(data == "O"))
    O_indices = np.array(list(zip(O_indices[0], O_indices[1])))
    for O in O_indices:
        total_score += size[0] - O[0]
    return total_score

def main():
    ts0 = time.time()
    total_score = 0
    print("Starting time:", ts0)
    print(" ")
    fI = open(r'D:\Advent_of_Code\Advent_of_Code_2023\Day14\Puzzle_Input.txt', 'r')
    # Read all of the input data from Puzzle Input and organise it
    data = reading_input_data(fI)
    size = np.shape(data)
    # Apply the tilting level process
    data = tilting_level(data, size)
    # Calculate Score
    total_score = score_calculation(data, size)
    print("The total score is:", total_score)
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()