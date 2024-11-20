import numpy as np
import time
import sys

def read_input_data(filename):
    input_data = []
    with open(filename, 'r') as f:
        for each_line in f:
            input_data.append(list(each_line.strip()))
        input_data = np.array(input_data,dtype=int)
        input_data_shape = np.shape(input_data)
        input_data = np.reshape(input_data,input_data_shape)
    return input_data

def find_low_points(input_data):
    temp_input_data = np.pad(input_data, pad_width=1, mode='constant', constant_values=9)
    low_point_masks = (0*temp_input_data)-1
    low_points = []
    shape_temp_input_data = np.shape(temp_input_data)
    # Check internals
    for rows in range(1,shape_temp_input_data[0]-1):
        for columns in range(1,shape_temp_input_data[1]-1):
            if (temp_input_data[rows + 1][columns] > temp_input_data[rows][columns] and
                    temp_input_data[rows - 1][columns] > temp_input_data[rows][columns] and
                    temp_input_data[rows][columns + 1] > temp_input_data[rows][columns] and
                    temp_input_data[rows][columns - 1] > temp_input_data[rows][columns]):
                low_point_masks[rows][columns] = temp_input_data[rows][columns]
                low_points.append(temp_input_data[rows][columns])
    return low_points

def main():
    # progress_bar(days, days_to_model)
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = f"D:\Python_Programming\Advent_of_Code\Advent_of_Code_2021\Day9\Puzzle_Input.txt"
    input_data = read_input_data(filename)
    print(" ")
    print("The input data is: ")
    print(input_data)
    low_points = find_low_points(input_data)
    print(" ")
    print("The low points are:", [point for point in low_points])
    risk_points = sum([(point + 1) for point in low_points])
    print(" ")
    print("The total risk is:", risk_points)


    print(" ")
    print("==============================================================")
    #print("The number of lanternfish after",days_to_model,"days is:",number_of_lanternfish)
    print("==============================================================")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()