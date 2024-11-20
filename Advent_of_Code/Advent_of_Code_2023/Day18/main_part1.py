import numpy as np
import time
import matplotlib.colors
from matplotlib import pyplot as plt


def reading_input_data(fI):
    data = []
    print("Reading block of input data...")
    for each_line in fI:
        each_line = (each_line.strip("\n")).split(" ")[:]
        each_line[2] = each_line[2].strip("(").strip(")")
        temp = matplotlib.colors.to_rgb(each_line[2])
        for i in range(3):
            each_line.append(temp[i])
        data.append(each_line)
    data = np.array(data)
    print("################################")
    print("The data is:")
    print(data)
    print(" ")
    print("The input array has:", len(data), "elements!")
    print("################################")
    return data

def dig_the_trench(data):
    max_array_size = 0
    for i in range(np.shape(data)[0]):
        max_array_size += int(data[i][1])
    print("max_array size is:", max_array_size)
    map_array = np.zeros((max_array_size,max_array_size)) # Need to determine map_array size
    current_position = [int(max_array_size//2),int(max_array_size//2)]
    print(current_position)
    map_array = np.reshape(map_array, (max_array_size, max_array_size))
    map_array[current_position[1], current_position[0]] = 1
    for i in range(np.shape(data)[0]):
        if data[i][0] == "D":
            map_array[current_position[0] + 1:current_position[0] + int(data[i][1]) + 1,current_position[1]] = 1
            current_position[0] += int(data[i][1])
        elif data[i][0] == "U":
            map_array[current_position[0] - int(data[i][1]):current_position[0], current_position[1]] = 1
            current_position[0] -= int(data[i][1])
        elif data[i][0] == "R":
            map_array[current_position[0], current_position[1] + 1:current_position[1] + int(data[i][1]) + 1] = 1
            current_position[1] += int(data[i][1])
        elif data[i][0] == "L":
            map_array[current_position[0], current_position[1] - int(data[i][1]):current_position[1]] = 1
            current_position[1] -= int(data[i][1])
    print(map_array)
    return map_array, max_array_size

def dig_out_full_area(map_array, max_array_size, x_clicked, y_clicked):
    counter = 0
    seed_points = np.array([[int(x_clicked*max_array_size), int(y_clicked*max_array_size)]])
    num_rows_limit = np.shape(map_array)[0] - 2
    num_columns_limit = np.shape(map_array)[1] - 2
    map_array = np.array(map_array, dtype=int)
    print(" ")
    while len(seed_points) != 0:
        seed_points_00, seed_points_01 = seed_points[0][0], seed_points[0][1]
        # look in all directions and flood fill to adjacent nodes if they are 0 - then only isolated nodes remain
        if map_array[seed_points_00 - 1, seed_points_01] == 0 and seed_points_00 - 1 >= 0:
            seed_points = np.vstack((seed_points, np.array([seed_points_00 - 1, seed_points_01])))
            map_array[seed_points_00 - 1, seed_points_01] = 1
        if map_array[seed_points_00 + 1, seed_points_01] == 0 and seed_points_00 + 1 <= num_rows_limit:
            seed_points = np.vstack((seed_points, np.array([seed_points_00 + 1, seed_points_01])))
            map_array[seed_points_00 + 1, seed_points_01] = 1
        if map_array[seed_points_00, seed_points_01 - 1] == 0 and seed_points_01 - 1 >= 0:
            seed_points = np.vstack((seed_points, np.array([seed_points_00, seed_points_01 - 1])))
            map_array[seed_points_00, seed_points_01 - 1] = 1
        if map_array[seed_points_00, seed_points_01 + 1] == 0 and seed_points_01 + 1 <= num_columns_limit:
            seed_points = np.vstack((seed_points, np.array([seed_points_00, seed_points_01 + 1])))
            map_array[seed_points_00, seed_points_01 + 1] = 1
        seed_points = np.delete(seed_points, 0, axis=0)
        counter += 1
    return map_array

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    fI = open(r'D:\Advent_of_Code\Advent_of_Code_2023\Day18\Puzzle_Input.txt', 'r')
    # Read all of the input data from Puzzle Input and organise it
    data = reading_input_data(fI)
    # Now lets dig the trench
    map_array, max_array_size = dig_the_trench(data)
    x_dim = max_array_size
    y_dim = max_array_size
    x = np.linspace(0, 1, x_dim)
    y = np.linspace(0, 1, y_dim)
    X, Y = np.meshgrid(x, y)
    plt.contourf(X, Y, map_array)
    plt.colorbar()
    print("Please click inside the trench!")
    clicked_point = plt.ginput(1)  # Allowing only one click
    plt.close()  # Close the plot after the click
    # Extract x and y coordinates of the clicked point
    x_clicked, y_clicked = clicked_point[0]
    # Use the clicked coordinates as variables
    print(f"Selected point: x = {x_clicked}, y = {y_clicked}")
    plt.show()
    # Now lets fill the trench
    map_array = dig_out_full_area(map_array, max_array_size, x_clicked, y_clicked)
    plt.contourf(X, Y, map_array)
    plt.colorbar()
    plt.show()
    print("The total score is:", np.sum(map_array))
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()