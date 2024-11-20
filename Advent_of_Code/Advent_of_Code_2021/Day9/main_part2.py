import numpy as np
import time
import matplotlib.pyplot as plt

def read_input_data(filename):
    input_data = []
    with open(filename, 'r') as f:
        for each_line in f:
            input_data.append(list(each_line.strip()))
        input_data = np.array(input_data,dtype=int)
        input_data_shape = np.shape(input_data)
        input_data = np.reshape(input_data,input_data_shape)
        print(np.shape(input_data))
    return input_data

def find_low_points(input_data):
    temp_input_data = np.pad(input_data, pad_width=1, mode='constant', constant_values=9)
    low_point_masks = (0*temp_input_data)-1
    low_points = []
    low_point_locations = []
    shape_temp_input_data = np.shape(temp_input_data)
    # Check internals
    for rows in range(1,shape_temp_input_data[0]-1):
        for columns in range(1,shape_temp_input_data[1]-1):
            if (temp_input_data[rows + 1][columns] > temp_input_data[rows][columns] and
                    temp_input_data[rows - 1][columns] > temp_input_data[rows][columns] and
                    temp_input_data[rows][columns + 1] > temp_input_data[rows][columns] and
                    temp_input_data[rows][columns - 1] > temp_input_data[rows][columns]):
                low_point_masks[rows][columns] = temp_input_data[rows][columns]
                low_point_locations.append([rows - 1,columns - 1])
                low_points.append(temp_input_data[rows][columns])
    return low_point_locations

def find_basins(low_point_locations, input_data):
    temp_input_data = np.pad(input_data, pad_width=1, mode='constant', constant_values=9)
    basin_masks = (0 * temp_input_data.copy())
    for index, points in enumerate(low_point_locations, start=1):
        points[0] += 1
        points[1] += 1
        print(" ")
        print("Starting low location...", points)
        print(" ")
        points_to_check = [points]
        basin_masks[points_to_check[0][0]][points_to_check[0][1]] = index
        while points_to_check:
            print("Growing...", points)
            if temp_input_data[points[0] + 1][points[1]] >= temp_input_data[points[0]][points[1]] and temp_input_data[points[0] + 1][points[1]] != 9:
                if basin_masks[points[0] + 1][points[1]] == 0 and points[0] not in [0,np.shape(basin_masks)[0]]:
                    points_to_check.append([points[0] + 1, points[1]])
                    basin_masks[points[0] + 1][points[1]] = index
            if temp_input_data[points[0] - 1][points[1]] >= temp_input_data[points[0]][points[1]] and temp_input_data[points[0] - 1][points[1]] != 9:
                if basin_masks[points[0] - 1][points[1]] == 0 and points[0] not in [0,np.shape(basin_masks)[0]]:
                    points_to_check.append([points[0] - 1, points[1]])
                    basin_masks[points[0] - 1][points[1]] = index
            if temp_input_data[points[0]][points[1] + 1] >= temp_input_data[points[0]][points[1]] and temp_input_data[points[0]][points[1] + 1] != 9:
                if basin_masks[points[0]][points[1] + 1] == 0 and points[1] not in [0,np.shape(basin_masks)[1]]:
                    points_to_check.append([points[0], points[1] + 1])
                    basin_masks[points[0]][points[1] + 1] = index
            if temp_input_data[points[0]][points[1] - 1] >= temp_input_data[points[0]][points[1]] and temp_input_data[points[0]][points[1] - 1] != 9:
                if basin_masks[points[0]][points[1] - 1] == 0 and points[1] not in [0,np.shape(basin_masks)[1]]:
                    points_to_check.append([points[0], points[1] - 1])
                    basin_masks[points[0]][points[1] - 1] = index
            points_to_check.remove(points)
            # Next point to check
            if points_to_check:
                points = points_to_check[0]
            else:
                break # Go to next lowest point to start growing basin again
    return basin_masks

def plot_heatmap(basin_masks):
    plt.imshow(basin_masks, cmap='viridis', interpolation='nearest')
    plt.colorbar()  # Show color scale
    plt.title('Heatmap using Matplotlib')
    plt.show()
    return None
def find_basin_sizes(basin_masks):
    basin_sizes = np.zeros((1,np.max(basin_masks)+1), dtype=int)
    for i in range(1, np.max(basin_masks) + 1):
        basin_sizes[0][i] = len(np.where(basin_masks == i)[0])
    basin_sizes = np.sort(basin_sizes[0], kind = "quicksort", axis=-1)
    basin_sizes = basin_sizes[::-1]
    return basin_sizes

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
    low_point_locations = find_low_points(input_data)
    basin_masks = find_basins(low_point_locations, input_data)
    plot_heatmap(basin_masks)
    basin_sizes = find_basin_sizes(basin_masks)
    print(basin_sizes)
    size_multiplication = basin_sizes[0]*basin_sizes[1]*basin_sizes[2] # Too low 950400
    print(" ")
    print("==============================================================")
    print("The multiplication answer is:",size_multiplication)
    print("==============================================================")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()