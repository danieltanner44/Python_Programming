import numpy as np
import time
import matplotlib.pyplot as plt
import plotly.graph_objs as go
from mpl_toolkits.mplot3d import Axes3D

def reading_input_data(f):
    print("Reading input data...", end = "")
    data = np.array([],dtype=np.int32)
    for each_line in f:
        data = np.append(data,each_line.replace("~", ",").strip("\n").split(","))
    data = np.array(np.reshape(data,[len(data)//6,6]),dtype=np.int64)
    number_of_bricks = np.shape(data)[0]
    print("[complete]", end="\n")
    print("#########################################")
    print("The initial data is:")
    print(data)
    print("#########################################")
    print("The data has shape:", np.shape(data))
    print("#########################################")
    print(" ")
    return data, number_of_bricks

def create_initial_pattern(data):
    brick_cube_indices = []
    brick_tracker = np.zeros([np.max(data[:,[0,3]])+1, np.max(data[:,[1,4]])+1, np.max(data[:,[2,5]])+1], dtype=int) # x y z
    #Lets populate bricks into the 3D tracker array, each brick gets its own number
    for brick in enumerate(data):
        brick_details = brick[1][0:3] - brick[1][3:6]
        if np.array_equal(brick_details,[0,0,0]) == True:
            direction = 0
        else:
            direction = (np.where(brick_details != 0)[0])[0]
        length_of_brick = brick_details[direction]
        brick_cubes = range(brick[1][direction], brick[1][direction+3] + 1)
        temp_brick_indices = []
        for i in range(abs(length_of_brick) + 1):
            temp_brick_indices.append(brick[1][0:3])
        temp_brick_indices = np.reshape(temp_brick_indices,[abs(length_of_brick) + 1,3])
        temp_brick_indices[:,direction] = brick_cubes
        brick_cube_indices.append(temp_brick_indices)
        for row in temp_brick_indices:
            brick_tracker[tuple(row)] = brick[0] + 1
    return brick_tracker, brick_cube_indices


def create_settled_pattern(data, brick_tracker, brick_cube_indices, number_of_bricks):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    touching_bricks = []
    check_if_brick_moved = np.zeros([number_of_bricks], dtype=int)
    minimum_cube_distances = np.zeros([number_of_bricks], dtype=int)
    # Find cubes closest to the ground so we can process them in order
    for cube_indices in enumerate(brick_cube_indices):
        minimum_cube_distances[cube_indices[0]] = min(cube_indices[1][:,2])
    # Lets move the cubes until they all stack, starting with those closest to the ground
    for i in range(number_of_bricks):
        touching_bricks_temp = []
        # Lets find the first cube to process (closed to ground and not previously processed)
        indices = np.where(check_if_brick_moved == 0)[0]  # Get indices where check_if_brick_moved is zero
        min_index = np.argmin(minimum_cube_distances[indices])  # Get index of minimum value in selected indices
        # Get the corresponding brick index
        current_brick = indices[min_index]
        check_if_brick_moved[current_brick] = 1 # Mark it off as processed, so we do not consider again
        # Check if there is space to move it downward (one voxel at a time)
        check_hit_bottom = False
        counter = 0
        while check_hit_bottom == False:
            counter += 1
            temp = []
            for each_cube in brick_cube_indices[current_brick]:
                underneath_cube = brick_tracker[tuple(each_cube - np.array([0, 0, counter]))]
                if underneath_cube != current_brick + 1:
                    temp.append(underneath_cube)
            if sum(temp) == 0: # nothing underneath or
                if each_cube[2] - counter == 0: # reached z = 0
                    counter += 1
                    break
                else:
                    continue
            else: # Something underneath
                    check_hit_bottom = True
                    for element in temp:
                        if element != 0:
                            touching_bricks_temp.append(element)
        touching_bricks.append(touching_bricks_temp)
        plot_blocks(brick_tracker, ax, number_of_bricks)
        plt.pause(1)
        # Move the brick and update the brick indices
        for each_cube in enumerate(brick_cube_indices[current_brick]):
            brick_tracker[tuple(each_cube[1])] = 0 # zero values in its original position
            brick_tracker[tuple(each_cube[1] - np.array([0,0,counter - 1]))] = current_brick + 1 # move it down as far as possible
            brick_cube_indices[current_brick][each_cube[0]] = brick_cube_indices[current_brick][each_cube[0]] - np.array([0,0,counter - 1])
    plt.show()  # savefig("demo.png")
    return touching_bricks


def identify_bricks_to_disintegrate(touching_bricks, number_of_bricks):
    disintegratable_bricks = np.zeros([number_of_bricks], dtype=int)
    bricks_that_i_sit_on = [[] for _ in range(number_of_bricks)]
    bricks_that_sit_on_me = [[] for _ in range(number_of_bricks)]
    # What bricks sit on each brick
    for touches in enumerate(touching_bricks):
        for indexes in enumerate(touches[1]):
            bricks_that_sit_on_me[indexes[1] - 1].append(touches[0])
    bricks_that_i_sit_on = touching_bricks
    print(bricks_that_sit_on_me)
    print(bricks_that_i_sit_on)
    # Now lets check for disintegration!
    for bricks_on_top in enumerate(bricks_that_sit_on_me):
        for each in bricks_on_top[1]:
            for every in bricks_that_i_sit_on[each]:
                if bricks_on_top[0] + 1 != every:
                    disintegratable_bricks[bricks_on_top[0]] = 1
    for i in range(number_of_bricks):
        if bricks_that_sit_on_me[i] == []:
            disintegratable_bricks[i] = 1
    # disintegratable_bricks[np.where([len(sit_on_me) == 0 for sit_on_me in bricks_that_sit_on_me])] = 1
    print(disintegratable_bricks)

    return disintegratable_bricks

def plot_blocks(brick_tracker ,ax, number_of_bricks):
    ax.clear()
    z,x,y = np.where(brick_tracker != 0)
    ax.scatter(x, y, -z, zdir='z', c=range(4322), cmap="viridis", s=500)
    plt.draw()


def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    fI = open(r'D:\Advent_of_Code\Advent_of_Code_2023\Day22\Puzzle_Input.txt', 'r')
    # STEP 1: Read all of the input data from Puzzle Input and organise it
    data, number_of_bricks = reading_input_data(fI)
    # STEP 2: Let's work out the initial pattern
    brick_tracker, brick_cube_indices = create_initial_pattern(data)
    # STEP 3: Let's work out the settled pattern
    touching_bricks = create_settled_pattern(data, brick_tracker, brick_cube_indices, number_of_bricks)
    # STEP 4: Let's figure out which bricks can be safely disintegrated
    disintegratable_bricks = identify_bricks_to_disintegrate(touching_bricks, number_of_bricks)



    print(" ")
    print("#########################################################")
    print(" ")
    print("#########################################################")
    print("The number of disintegratable bricks is:", np.sum(disintegratable_bricks)) # 618 is too high
    print("#########################################################")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()