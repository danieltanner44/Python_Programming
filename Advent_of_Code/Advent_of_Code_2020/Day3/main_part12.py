import numpy as np
import time
import my_modules.development as mmd

def read_input_data(filename):
    slope_layout = []
    with open(filename, 'r') as f:
        for line in f:
            slope_layout.append(list(line.strip()))
    slope_layout = np.array(slope_layout, dtype=np.str_)
    return slope_layout

def determine_journey(slope_layout, slope):
    collision_counter = 0
    current_position = np.array([0, 0], dtype=np.int16)
    slope = np.array(slope, dtype=np.int16)
    num_steps = np.shape(slope_layout)[0]//slope[0]
    for i in range(num_steps):
        if slope_layout[tuple(current_position)] == "#":
            collision_counter += 1
        current_position = current_position + slope
        if current_position[1] > np.shape(slope_layout)[1] - 1:
            current_position[1] = current_position[1] - np.shape(slope_layout)[1]
    return collision_counter

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2020\Day3\Puzzle_Input.txt"
    slope_layout = read_input_data(filename)
    print("The initial slope layout is:")
    mmd.print_array(slope_layout)
    slope_list = [(1,1), (1,3), (1,5), (1,7), (2,1)]
    collision_counter_multiple = 1
    collision_counter = []
    for slope in slope_list:
        collision_counter.append(determine_journey(slope_layout, slope))
        collision_counter_multiple *= collision_counter[-1]


    print(" ")
    print("==============================================================")
    print("PART 1: The number of collisions is:", collision_counter[1])
    print("==============================================================")
    print(" ")
    print(" ")
    print("==============================================================")
    print("PART 2: The multiplication of the collisions is:", collision_counter_multiple)
    print("==============================================================")
    print(" ")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()