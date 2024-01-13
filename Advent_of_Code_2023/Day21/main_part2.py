import numpy as np
import time
import matplotlib.pyplot as plt

def reading_input_data(f):
    print("Reading input data...", end = "")
    mask = np.array([], dtype=int)
    for each_line in f:
        temp = np.array([], dtype=int)
        each_line = (each_line.strip("\n")).split()
        for character in each_line[0][:]:
            if character == "#":
                temp = np.append(temp, 8)
            elif character == "S":
                temp = np.append(temp, 5)
            else:
                temp = np.append(temp, 0)
        mask = np.append(mask, temp)
    mask = np.reshape(mask, [len(mask)//len(each_line[0]), len(each_line[0])])
    starting_point = np.where(mask == 5)
    extending_multiple = 3
    starting_point = [starting_point[0][0] + (extending_multiple + 1)*np.shape(mask)[0], starting_point[1][0] + (extending_multiple + 1)*np.shape(mask)[1]]
    for i in range(extending_multiple):
        mask = np.vstack((mask,mask))
    for i in range(extending_multiple):
        mask = np.hstack((mask,mask))
    print("[complete]", end="\n")
    print("################################")
    print("The map is", np.shape(mask))
    print("################################")
    print(" ")
    return mask, starting_point

def map_steps(mask, starting_point, backtracking, max_steps):
    # Convert to binary matrix
    seed_points = [starting_point]
    num_rows_limit = np.shape(mask)[0] - 1
    num_columns_limit = np.shape(mask)[1] - 1
    mask[seed_points[0][0], seed_points[0][1]] = 0
    reset_mask = np.array(mask)
    for i in range(1, max_steps + 1):
        next_seed_points = [starting_point]
        if backtracking == True:
            reset_mask = np.array(mask)
        total_gardens_reachable = 0
        for j in range(len(seed_points)):
            seed_points_00, seed_points_01 = seed_points[0][0], seed_points[0][1]
            # look in all directions and flood fill to adjacent nodes if they are 0 - then only isolated nodes remain
            if reset_mask[seed_points_00 - 1, seed_points_01] == 0 and seed_points_00 - 1 >= 0:
                next_seed_points = np.vstack((next_seed_points, np.array([seed_points_00 - 1, seed_points_01])))
                total_gardens_reachable += 1
                reset_mask[seed_points_00 - 1, seed_points_01] = 20
            if reset_mask[seed_points_00 + 1, seed_points_01] == 0 and seed_points_00 + 1 <= num_rows_limit:
                next_seed_points = np.vstack((next_seed_points, np.array([seed_points_00 + 1, seed_points_01])))
                total_gardens_reachable += 1
                reset_mask[seed_points_00 + 1, seed_points_01] = 20
            if reset_mask[seed_points_00, seed_points_01 - 1] == 0 and seed_points_01 - 1 >= 0:
                next_seed_points = np.vstack((next_seed_points, np.array([seed_points_00, seed_points_01 - 1])))
                total_gardens_reachable += 1
                reset_mask[seed_points_00, seed_points_01 - 1] = 20
            if reset_mask[seed_points_00, seed_points_01 + 1] == 0 and seed_points_01 + 1 <= num_columns_limit:
                next_seed_points = np.vstack((next_seed_points, np.array([seed_points_00, seed_points_01 + 1])))
                total_gardens_reachable += 1
                reset_mask[seed_points_00, seed_points_01 + 1] = 20
            seed_points = np.delete(seed_points, 0,axis=0)
        next_seed_points = np.delete(next_seed_points, 0, axis=0)
        seed_points = next_seed_points
        print("Step", i,"in which there were", total_gardens_reachable, "gardens reachable!")
        if i%200 == 0 or i == max_steps:
            plt.contourf(reset_mask, cmap='viridis', interpolation='none')
            plt.title(f'Contour Plot at Step {i}')  # Add a title with the step number
            plt.colorbar(label='Values')
            plt.show()
    print("################################")
    print("Flooding/Filling Complete!")
    return total_gardens_reachable


def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    fI = open(r'D:\Advent_of_Code\Advent_of_Code_2023\Day21\Puzzle_Input.txt', 'r')
    # Read all of the input data from Puzzle Input and organise it
    mask, starting_point = reading_input_data(fI)
    # Now lets walk through the gardens
    backtracking, max_steps = True, 1000
    total_gardens_reachable = map_steps(mask, starting_point, backtracking, max_steps)
    print(" ")
    print("################################")
    print("The answer is:", total_gardens_reachable)
    print("################################")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()