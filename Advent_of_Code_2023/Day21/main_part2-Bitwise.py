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
    starting_point = [starting_point[0][0], starting_point[1][0]]
    print("[complete]", end="\n")
    print("################################")
    print("The map is", np.shape(mask))
    print("################################")
    print(" ")
    return mask, starting_point

def map_steps(mask, starting_point, backtracking, max_steps):
    search_mask = np.array([[0,1,0], [1,0,1], [0,1,0]], dtype=int)
    search_mask = np.reshape(search_mask, (3,3))
    mask = np.array(mask, dtype=int)
    # Convert to binary matrix
    seed_points = [starting_point]
    mask[seed_points[0][0], seed_points[0][1]] = 0
    for i in range(1, max_steps + 1):
        new_seed_points = []
        for j in range(len(seed_points)):
            print(j, "j", len(seed_points))
            reset_mask = np.array(mask)
            seed_points_00, seed_points_01 = seed_points[0][0], seed_points[0][1]
            # look in all directions and flood fill to adjacent nodes if they are 0 - then only isolated nodes remain
            reset_mask[seed_points_00 - 1: seed_points_00 + 2, seed_points_01 - 1: seed_points_01 + 2] = np.add(reset_mask[seed_points_00 - 1: seed_points_00 + 2, seed_points_01 - 1: seed_points_01 + 2], search_mask)
            new_seed_points += list(zip(*np.where(reset_mask == 1)))
            print(new_seed_points)
        seed_points = list(set(list(new_seed_points)))
        print(seed_points, "egiojheihjgeiojgjeiojge")
        print(reset_mask)
        print("Step", i,"in which there were", 0, "gardens reachable!")
        if i%1 == 0 or i == max_steps:
            plt.contourf(reset_mask, cmap='viridis', interpolation='none')
            plt.title(f'Contour Plot at Step {i}')  # Add a title with the step number
            plt.colorbar(label='Values')
            #plt.show()
    print("################################")
    print("Flooding/Filling Complete!")
    return total_gardens_reachable


def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    fI = open(r'D:\Advent_of_Code\Advent_of_Code_2023\Day21\Puzzle_Input_d.txt', 'r')
    # Read all of the input data from Puzzle Input and organise it
    mask, starting_point = reading_input_data(fI)
    # Now lets walk through the gardens
    backtracking, max_steps = True, 6
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