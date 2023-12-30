import numpy as np
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

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
    print("The input data is:", "\n", "", data)
    print("Starting point is:", "\n", starting_point)
    print("The number of puzzle lines is:", "\n", number_of_lines)
    print("The puzzle has shape:",np.shape(data),"... so ...",np.shape(data)[0]*np.shape(data)[1],"elements to process...")
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
                data[i, j] = 0
    data = np.array(data, dtype=int)
    del(counter)
    return data, characters

def step_through_maze(data, starting_point, characters):
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
                return overall_map_steps, starting_character
            if step_counter == 1 and i == 1:
                # Figure what type of starting point we have as needed for later
                movement = next_position - starting_point
                # ref characters = {"|": (1,7), "-": (3,5), "L": (1,5), "J": (1,3), "7": (3,7), "F": (5,7)}
                if (np.array_equal(movement[0], [-1, 0]) and np.array_equal(movement[1],[0 ,1])) or (np.array_equal(movement[0], [0, 1]) and np.array_equal(movement[1], [-1 ,0])):
                    starting_character = 3 # L
                elif (np.array_equal(movement[0], [1, 0]) and np.array_equal(movement[1], [-1 ,0])) or (np.array_equal(movement[0],[1, 0]) and np.array_equal(movement[1], [1 ,0])):
                    starting_character = 1 # |
                elif (np.array_equal(movement[0], [0, -1]) and np.array_equal(movement[1], [1, 0])) or (np.array_equal(movement[0], [1, 0]) and np.array_equal(movement[1], [0, -1])):
                    starting_character = 4  # j
                elif (np.array_equal(movement[0], [0, 1]) and np.array_equal(movement[1], [0, -1])) or (np.array_equal(movement[0], [0, -1]) and np.array_equal(movement[1], [0, 1])):
                    starting_character = 2  # -
                elif (np.array_equal(movement[0], [0, 1]) and np.array_equal(movement[1], [1, 0])) or (np.array_equal(movement[0], [1, 0]) and np.array_equal(movement[1], [0, 1])):
                    starting_character = 6  # F
                elif (np.array_equal(movement[0], [0, -1]) and np.array_equal(movement[1], [-1, 0])) or (np.array_equal(movement[0], [-1, 0]) and np.array_equal(movement[1], [0, -1])):
                    starting_character = 5  # 7
                key = [k for k, v in characters.items() if v == starting_character]
                print("The starting character is an:",starting_character,"a.k.a", key[0])
            step_counter += i

def number_of_elements_enclosed(overall_map_steps, data, starting_character, starting_point):
    counter, zero_padding_width, method = 0, 2, 2
    data[starting_point[0], starting_point[1]] = starting_character
    overall_map_steps[starting_point[0], starting_point[1]] = starting_character
    overall_map_steps = np.pad(overall_map_steps, pad_width=2, mode="constant", constant_values=(0))
    data = np.pad(data, pad_width=zero_padding_width, mode="constant", constant_values=(0))
    for i in range(np.shape(overall_map_steps)[0]): # rows
        for j in range(np.shape(overall_map_steps)[1]): # columns
            if overall_map_steps[i,j] != 0:
                overall_map_steps[i, j] = 1
            else:
                overall_map_steps[i, j] = 0
    if method == 1 or method == 3:
        seed_points = np.array([[1,1]])
        num_rows_limit = np.shape(overall_map_steps)[0] - 2
        num_columns_limit = np.shape(overall_map_steps)[1] - 2
        print(" ")
        overall_map_steps[1,1] = 1
        while len(seed_points) != 0:
            seed_points_00, seed_points_01 = seed_points[0][0], seed_points[0][1]
            # look in all directions and flood fill to adjacent nodes if they are 0 - then only isolated nodes remain
            if overall_map_steps[seed_points_00 - 1, seed_points_01] == 0 and seed_points_00 - 1 >= 0:
                seed_points = np.vstack((seed_points, np.array([seed_points_00 - 1, seed_points_01])))
                overall_map_steps[seed_points_00 - 1, seed_points_01] = 1
            if overall_map_steps[seed_points_00 + 1, seed_points_01] == 0 and seed_points_00 + 1 <= num_rows_limit:
                seed_points = np.vstack((seed_points, np.array([seed_points_00 + 1, seed_points_01])))
                overall_map_steps[seed_points_00 + 1, seed_points_01] = 1
            if overall_map_steps[seed_points_00, seed_points_01 - 1] == 0 and seed_points_01 - 1 >= 0:
                seed_points = np.vstack((seed_points, np.array([seed_points_00, seed_points_01 - 1])))
                overall_map_steps[seed_points_00, seed_points_01 - 1] = 1
            if overall_map_steps[seed_points_00, seed_points_01 + 1] == 0 and seed_points_01 + 1 <= num_columns_limit:
                seed_points = np.vstack((seed_points, np.array([seed_points_00, seed_points_01 + 1])))
                overall_map_steps[seed_points_00, seed_points_01 + 1] = 1
            seed_points = np.delete(seed_points, 0,axis=0)
            counter += 1
            if counter%1000==0:
                print("Updates: counter=", counter, "length of seed_points=", len(seed_points))
                fig, ax = plt.subplots()
                img = ax.imshow(overall_map_steps, cmap='hot')
                plt.colorbar(img)
                img.set_data(overall_map_steps)
                img.set_clim(vmin=overall_map_steps.min(), vmax=overall_map_steps.max())
                plt.draw()
                plt.get_current_fig_manager().full_screen_toggle()
                plt.show(block=False)
                plt.pause(0.5)
        print("Flooding/Filling Complete!")
        overall_map_steps = np.delete(overall_map_steps, np.shape(overall_map_steps)[0] - 1, 0)
        overall_map_steps = np.delete(overall_map_steps, np.shape(overall_map_steps)[1] - 1, 1)
        print(np.max(overall_map_steps), np.min(overall_map_steps))
        counter = (np.shape(overall_map_steps)[0] * np.shape(overall_map_steps)[1]) - np.sum(overall_map_steps)
    if method == 2 or method == 3:
        counter = 0
        for i in range(np.shape(overall_map_steps)[0]):
            crossings = 0
            l_found, f_found = False, False
            for j in range(np.shape(overall_map_steps)[1] - 1):
                if overall_map_steps[i, j] == 0 and crossings % 2 != 0:
                    counter += 1
                    overall_map_steps[i, j] = 2
                if data[i,j] == 1 and overall_map_steps[i,j] == 1:
                    crossings += 1
                elif (data[i, j] == 6 and overall_map_steps[i,j] == 1) or f_found == True:  # "F"
                    f_found = True
                    if data[i, j] == 5 and overall_map_steps[i,j] == 1:  # "7"
                        crossings += 0
                        f_found = False
                    elif data[i, j] == 4 and overall_map_steps[i,j] == 1:  # "J"
                        crossings += 1
                        f_found = False
                elif (data[i, j] == 3 and overall_map_steps[i,j] == 1) or l_found == True:  # "L"
                    l_found = True
                    if data[i, j] == 5 and overall_map_steps[i,j] == 1:  # "7"
                        crossings += 1
                        l_found = False
                    elif data[i, j] == 4 and overall_map_steps[i,j] == 1:  # "J"
                        crossings += 0
                        l_found = False
    plt.imshow(overall_map_steps, cmap='hot')
    plt.colorbar()
    plt.show()
    plt.imshow(data, cmap='hot')
    plt.colorbar()
    plt.show()
    return counter

def main():
    ts0 = time.time()
    print("Starting time:", ts0)
    print(" ")
    f = open(r'D:\Advent_of_Code\Advent_of_Code_2023\Day10\Puzzle_Input.txt', 'r')
    # Read all of the input data from Puzzle Input and organise it
    data, number_of_lines, starting_point = reading_input_data(f)
    # Step all of the characters and make masks to help step later
    data, characters = convert_data_to_numbers(data, starting_point)
    overall_map_steps, starting_character = step_through_maze(data, starting_point, characters)
    enclosed_elements = number_of_elements_enclosed(overall_map_steps, data, starting_character, starting_point)
    print(np.max(overall_map_steps))

    print("The total number of maze steps is:", np.max(overall_map_steps))
    print("There are", enclosed_elements,"elements enclosed!")
    print(" ")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()