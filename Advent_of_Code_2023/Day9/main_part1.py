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
        temp[counter, 0:len(data_i) - counter] = temp1 # fill row with difference output, will leave trailing zeros
        counter += 1
    temp = np.hstack((temp, np.zeros((counter, 1)))) # Add zeros to the end of the array
    temp = np.array(temp, dtype=int) # make integer array
    if np.sum(np.abs(temp1)) == 0:
        # Lets reconstruct
        for j in range(counter - 1): # Must not wrap over to top of array
            temp[counter - j - 2, len(temp1) + j + 1] = temp[counter - j - 2, len(temp1) + j] + temp[counter - j - 1, len(temp1) + j]
            extrapolated_value = temp[counter - j - 2, len(temp1) + j + 1]
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
    if "Plot Results" == "Plot Results!!!":
        x_values = np.array(range(np.shape(data)[1]))
        plt.figure(figsize=(20, 10))
        plt.grid(True)
        lines, = plt.plot(x_values, data[0, :], marker='o')
        plt.show(block=False)
        #for i in range(100,np.shape(data)[0]): # first 100 fine - 109.144.
        for i in range(1,np.shape(data)[0]):  # first 100 fine - 109.144.
            spline = CubicSpline(x_values, data[i, :])
            x_interp_data = np.linspace(min(x_values), max(x_values), 21)  # Generate more points for a smoother curve
            print(x_interp_data)
            print(np.shape(x_interp_data))
            y_interp_data = spline(x_interp_data)
            print(y_interp_data)
            print(np.shape(y_interp_data))
            ymin, ymax = np.min(data[i, :]), np.max(data[i, :])
            plt.ylim(ymin, ymax)
            plt.title("This is iteration:" + str(i))
            lines.set_ydata(y_interp_data)  # Update the y-data for the line
            plt.pause(0.5)  # Pause for 1 second to view the updated plot
            plt.draw()  # Draw the updated plot

        plt.show()

if __name__ == "__main__":
    main()