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
        temp = np.array([], dtype=int)
        # Lets read in all the key information
        each_line = (each_line.strip("\n")).split()
        for i in range(len(each_line[0][:])):
            temp = np.append(temp, each_line[0][i])
            if each_line[0][i] == "S":
                starting_point = [number_of_lines, i]
                starting_point = np.add(starting_point, 1)
        if only_once == True:
            data = np.vstack((data, temp))
        else:
            data = temp
            only_once = True
        number_of_lines += 1
    del(each_line, only_once, temp)
    data = np.pad(data, pad_width=1, mode="constant", constant_values=(-1))
    print(data)
    print("The input data is:", "\n", "", data)
    print("Starting point is:", "\n", starting_point)
    print("The number of puzzle lines is:", "\n", number_of_lines)
    return data, number_of_lines, starting_point

def convert_data_to_numbers(data, starting_point):
    characters = {"|": (1,7), "-": (3,5), "L": (1,5), "J": (1,3), "7": (3,7), "F": (5,7)}
    counter = 1
    for i in characters:
        characters[i] = counter
        counter += 1
    for i in range(1,np.shape(data)[0] - 1):
        for j in range(1,np.shape(data)[1] - 1):
            if np.array_equal(starting_point,[i,j]) == True:
                data[i, j] = -9
            elif data[i, j] in ["|", "-", "L", "J", "7", "F"]:
                data[i, j] = characters.get(data[i,j])
            else:
                data[i, j] = -1
    data = np.array(data, dtype=int)
    del(counter)
    return data

def step_through_maze(data, starting_point):
    current_position = next_position = np.array([starting_point, starting_point], dtype=int)
    overall_map_steps = np.zeros((np.shape(data)), dtype=int)
    index = np.zeros((2,4,2), dtype=int)
    overall_map_steps[starting_point[0],starting_point[1]] = -9
    step_counter = 1
    while 0 == 0:
        current_position = next_position
        for i in range(2): # Loop over each to take a step in each direction
            index[i,0,0] = (current_position[i] - [1, 0])[0]
            index[i,0,1] = (current_position[i] - [1, 0])[1]
            index[i,1,0] = (current_position[i] + [1, 0])[0]
            index[i,1,1] = (current_position[i] + [1, 0])[1]
            index[i,2,0] = (current_position[i] - [0, 1])[0]
            index[i,2,1] = (current_position[i] - [0, 1])[1]
            index[i,3,0] = (current_position[i] + [0, 1])[0]
            index[i,3,1] = (current_position[i] + [0, 1])[1]
            if (data[index[i,0,0], index[i,0,1]] in [1, 5, 6]) and (data[current_position[i][0],current_position[i][1]] in [1, 3, 4, -9]) and overall_map_steps[index[i,0,0], index[i,0,1]] == 0: # above has 7
                next_position[i] = [index[i,0,0], index[i,0,1]]
                overall_map_steps[index[i,0,0],index[i,0,1]] = step_counter
            elif (data[index[i,1,0], index[i,1,1]] in [1, 3, 4]) and (data[current_position[i][0],current_position[i][1]] in [1, 5, 6, -9]) and overall_map_steps[index[i,1,0], index[i,1,1]] == 0: # below has 1
                next_position[i] = [index[i,1,0], index[i,1,1]]
                overall_map_steps[index[i,1,0], index[i,1,1]] = step_counter
            elif (data[index[i,2,0], index[i,2,1]] in [2, 3, 6]) and (data[current_position[i][0],current_position[i][1]] in [2, 4, 5, -9]) and overall_map_steps[index[i,2,0], index[i,2,1]] == 0:  # left has 5
                next_position[i] = [index[i,2,0], index[i,2,1]]
                overall_map_steps[index[i,2,0], index[i,2,1]] = step_counter
            elif (data[index[i,3,0], index[i,3,1]] in [2, 4, 5]) and (data[current_position[i][0],current_position[i][1]] in [2, 3, 6, -9]) and overall_map_steps[index[i,3,0], index[i,3,1]] == 0:  # right has 3
                next_position[i] = [index[i,3,0], index[i,3,1]]
                overall_map_steps[index[i,3,0], index[i,3,1]] = step_counter
            else:
                print(" ")
                print("CONVERGED")
                return overall_map_steps
            step_counter += i

def main():
    ts0 = time.time()
    print("Starting time:", ts0)
    print(" ")
    f = open(r'D:\Advent_of_Code\Advent_of_Code_2023\Day10\Puzzle_Input.txt', 'r')
    # Read all of the input data from Puzzle Input and organise it
    data, number_of_lines, starting_point = reading_input_data(f)
    # Step all of the characters and make masks to help step later
    data = convert_data_to_numbers(data, starting_point)
    overall_map_steps = step_through_maze(data, starting_point)

    print("The total number of maze steps is:", np.max(overall_map_steps))
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()