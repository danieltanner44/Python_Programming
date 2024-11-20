import numpy as np
import time
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def read_input_data(filename):
    with open(filename, 'r') as f:
        directions = f.readline().strip().replace(" ","").split(",")
    return directions

def walking_the_grid(directions):
    direction = {"NR": "E","NL": "W", "SR": "W", "SL": "E", "ER": "S","EL": "N", "WR": "N", "WL": "S"}
    current_direction = "N"
    location = {"X" : 0, "Y" : 0}
    location_history = [[0,0]]
    for step in directions:
        distance = int(step[1:])
        current_direction = direction[current_direction+step[:1]]
        if current_direction == "N":
            location["Y"] = location["Y"] + distance
        elif current_direction == "S":
            location["Y"] = location["Y"] - distance
        elif current_direction == "E":
            location["X"] = location["X"] + distance
        elif current_direction == "W":
            location["X"] = location["X"] - distance
        else:
            print("Error in directions!")
        new_location = [location["X"], location["Y"]]
        location_history.append(new_location)
    return location_history

def plot_journey(location_history, intersection):
    # Convert the list of points to a NumPy array for easier manipulation
    data_array = np.array(location_history)

    # Extract x and y coordinates
    x = data_array[:, 0]
    y = data_array[:, 1]

    # Create a color gradient based on the y values
    norm = plt.Normalize(y.min(), y.max())
    colors = plt.cm.viridis(norm(y))  # You can change 'viridis' to other colormaps

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Plot the line graph
    for i in range(len(x) - 1):
        ax.plot(x[i:i + 2], y[i:i + 2], color=colors[i])  # Plot each segment with its color

    # Add labels and title
    ax.set_title("Colored Line Graph of Points")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")

    # Create a ScalarMappable and add a colorbar
    sm = plt.cm.ScalarMappable(cmap='viridis', norm=norm)
    sm.set_array([])  # Only needed for older versions of Matplotlib
    cbar = plt.colorbar(sm, ax=ax, label='Y values')  # Add color bar

    # Create and add a circle patch
    circle = Circle(intersection, 4, color='red', fill=False, linewidth=5, label='1st intersection')
    ax.add_patch(circle)

    plt.grid()
    plt.legend()  # Add a legend to indicate the circle
    plt.axis('equal')  # Ensure equal aspect ratio
    plt.show()
    return

def find_intersection(location_history):
    for i in range(len(location_history)-1):
        x_range = (location_history[i+1][0], location_history[i][0])
        y_range = (location_history[i+1][1], location_history[i][1])
        direction = [abs(a - b) for a, b in zip(location_history[i + 1], location_history[i])]
        direction = tuple([element//max(direction) for element in direction])
        for j in range(len(location_history)-1):
            direction_for_list = [abs(a - b) for a, b in zip(location_history[j + 1], location_history[j])]
            direction_for_list = tuple([element // max(direction_for_list) for element in direction_for_list])
            if direction != direction_for_list: # Perpendicular
                x_range_for_list = (location_history[j + 1][0], location_history[j][0])
                y_range_for_list = (location_history[j + 1][1], location_history[j][1])
                # Check ranges for intersection
                if direction == (1,0):
                    if (((y_range_for_list[0] > y_range[0] > y_range_for_list[1]) or (y_range_for_list[0] < y_range[0] < y_range_for_list[1])) and ((x_range[0] > x_range_for_list[0] > x_range[1]) or (x_range[0] < x_range_for_list[0] < x_range[1]))):
                        intersection = tuple([x_range_for_list[0], y_range[0]])
                        blocks_away = abs(intersection[0]) + abs(intersection[1])
                        return intersection, blocks_away
                elif direction == (0,1):
                    if (((x_range_for_list[0] > x_range[0] > x_range_for_list[1]) or (x_range_for_list[0] < x_range[0] < x_range_for_list[1])) and ((y_range[0] > y_range_for_list[0] > y_range[1]) or (y_range[0] < y_range_for_list[0] < y_range[1]))):
                        intersection = tuple([x_range[0], y_range_for_list[0]])
                        blocks_away = abs(intersection[0]) + abs(intersection[1])
                        return intersection, blocks_away
                else:
                    print("Error - direction is not a unit vector!")
    return

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2016\Day1\Puzzle_Input.txt"
    directions = read_input_data(filename)
    print(" ")
    print("==============================================================")
    print("The input directions are:")
    print(directions)
    print("==============================================================")
    print(" ")
    location_history = walking_the_grid(directions)
    intersection, blocks_away = find_intersection(location_history)
    plot_journey(location_history, intersection)
    print("==============================================================")
    print("The number of blocks away is:", blocks_away)
    print("==============================================================")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()