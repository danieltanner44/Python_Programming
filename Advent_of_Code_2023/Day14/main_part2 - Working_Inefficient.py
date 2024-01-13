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

def tilting_level(data):
    r_indices = np.array(np.where(data == "#"))
    r_indices = np.array(list(zip(r_indices[0], r_indices[1])))
    r_indices = r_indices[r_indices[:, 1].argsort(kind="mergesort")]
    size = np.shape(data)
    # Now we know where everything is lets start sorting
    for i in range(size[1]): # one column at a time
        starting_point, check_counter = 0, 0
        first_r_rock = False
        # Had no R rocks then just sort them
        if not np.any(data[:,i] == "#"):
            temp = data[starting_point:size[0], i]
            temp = np.array(list(temp[temp[:].argsort(kind="mergesort")]))[::-1]
            data[starting_point:size[0], i] = temp
            continue # Skip back to next i
        for r in r_indices: # Walk through every R rock
            temp = np.array([],dtype=str)
            if r[1] == i: # R rock is in the current column
                # start to first R rock
                if first_r_rock == False:
                    if r[0] == 0: # If the first symbol is "#" just skip
                        starting_point += 1
                        first_r_rock = True
                        continue
                    else:
                        temp = data[starting_point:r[0], i]
                        temp = np.array(list(temp[temp[:].argsort(kind="mergesort")]))[::-1]
                        data[starting_point:r[0], i] = temp
                        starting_point = r[0] + 1
                        first_r_rock = True
                        continue
                # Between two R rocks
                if r[0] != size[0] - 1: # If the next R rock is not the last element of the column
                    if r[0] - starting_point <= 1: # If next one is the same space
                        starting_point = r[0] + 1
                        continue # Next R rock
                    else: # It is the last element of the current column
                        temp = data[starting_point:r[0], i]
                        temp = np.array(list(temp[temp[:].argsort(kind="mergesort")]))[::-1]
                        data[starting_point:r[0], i] = temp
                        starting_point = r[0] + 1
                        continue # Next R rock
                else: # The R Rock is at the end of the column
                    temp = data[starting_point:size[0], i]
                    temp = np.array(list(temp[temp[:].argsort(kind="mergesort")]))[::-1]
                    data[starting_point:size[0], i] = temp
        # Having step through all R rocks now consider from the last R rock to the end of the column
        if starting_point < size[0] - 1:
            temp = data[starting_point:size[0], i]
            temp = np.array(list(temp[temp[:].argsort(kind="mergesort")]))[::-1]
            data[starting_point:size[0], i] = temp
    return data

def score_calculation(data):
    total_score = 0
    size = np.shape(data)
    O_indices = np.array(np.where(data == "O"))
    O_indices = np.array(list(zip(O_indices[0], O_indices[1])))
    for O in O_indices:
        total_score += size[0] - O[0]
    return total_score

def spin_cycle(data):
    # let's undertake one cycle of North, South, West, East tilts
    # First do North
    data = tilting_level(data)
    # Mow run West - Simulate by rotating data array and rotating back after tilting
    data = np.rot90(data, -1)
    data = tilting_level(data)
    data = np.rot90(data, 1)
    # Mow run South - Simulate by inverting data array and reinverting the answer
    data = np.flipud(data)
    data = tilting_level(data)
    data = np.flipud(data)
    # Mow run East - Simulate by rotating data array and rotating back after tilting
    data = np.rot90(data,1)
    data = tilting_level(data)
    data = np.rot90(data, -1)
    return data

def main():
    ts0 = time.time()
    total_score = 0
    print("Starting time:", ts0)
    print(" ")
    fI = open(r'D:\Advent_of_Code\Advent_of_Code_2023\Day14\Puzzle_Input_d.txt', 'r')
    # Read all of the input data from Puzzle Input and organise it
    data = reading_input_data(fI)
    print(data)
    print(" ")
    # Apply a single North, South, West, East spin cycle
    for i in range(1000000000):
        data = spin_cycle(data)
        if i%100000 == 0:
            print(i, "progress")
    # Calculate Score
    total_score = score_calculation(data)
    print("The total score is:", total_score)
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()