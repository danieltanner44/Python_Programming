import numpy as np
import time
import matplotlib.pyplot as plt

def reading_input_data(f):
    print("Reading input data...", end = "")
    data = np.array([],dtype=np.int32)
    for each_line in f:
        data = np.append(data,each_line.replace("~", ",").strip("\n").split(","))
    data = np.array(np.reshape(data,[len(data)//6,6]),dtype=np.int64)
    delete_indices = np.where(np.logical_or.reduce((
        np.logical_or(data[:, 2] < 16, data[:, 2] > 20),
        np.logical_or(data[:, 5] < 16, data[:, 5] > 20),
        np.logical_or(data[:, 0] < 5, data[:, 0] > 10),
        np.logical_or(data[:, 3] < 5, data[:, 3] > 10),
        np.logical_or(data[:, 1] < 0, data[:, 1] > 3),
        np.logical_or(data[:, 4] < 0, data[:, 4] > 3)
    )))
    data = np.delete(data, delete_indices, 0)
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
    brick_tracker = np.zeros([np.max(data[:, [0, 3]]) + 1, np.max(data[:, [1, 4]]) + 1, np.max(data[:, [2, 5]]) + 1], dtype=int)  # x y z
    # Lets populate bricks into the 3D tracker array, each brick gets its own number
    for brick in enumerate(data):
        brick_details = brick[1][0:3] - brick[1][3:6]
        if np.array_equal(brick_details,[0,0,0]) == True:
            direction = 0 # Brick is a single cube
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
    ax = plt.figure().add_subplot(projection='3d')
    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    touching_bricks = []
    check_if_brick_moved = np.zeros([number_of_bricks], dtype=int)
    minimum_cube_distances = np.zeros([number_of_bricks], dtype=int)
    # Find cubes closest to the ground, so we can process them in order
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
                if each_cube[2] - counter == -1:  # reached z = 0
                    check_hit_bottom = True
                    #counter += 1
                    break
                underneath_cube = brick_tracker[tuple(each_cube - np.array([0, 0, counter]))]
                if underneath_cube != current_brick:
                    temp.append(underneath_cube)
                    print(underneath_cube, "under")
            print(temp, "TEMP")
            if np.count_nonzero(temp) == 0:
                if check_hit_bottom == False: # nothing underneath and not at bottom
                    continue
            else: # Something underneath
                check_hit_bottom = True
                for element in temp:
                    if element != 0:
                        touching_bricks_temp.append(element)
        touching_bricks.append(touching_bricks_temp)
        print(touching_bricks, "Touching Bricks")

        # Move the brick and update the brick indices
        for each_cube in enumerate(brick_cube_indices[current_brick]):
            print(each_cube, "ec")
            brick_tracker[tuple(each_cube[1])] = 0 # zero values in its original position
            brick_tracker[tuple(each_cube[1] - np.array([0,0,counter - 1]))] = current_brick # move it down as far as possible
            brick_cube_indices[current_brick][each_cube[0]] = brick_cube_indices[current_brick][each_cube[0]] - np.array([0,0,counter - 1])
        plot_blocks(brick_tracker, ax, brick_cube_indices, 'none')
        plt.draw()  # plt.show()  # savefig("demo.png")
    touching_bricks = [list(dict.fromkeys(sublist)) for sublist in touching_bricks]
    return touching_bricks, ax

def identify_bricks_to_disintegrate(touching_bricks, number_of_bricks, brick_tracker, brick_cube_indices, ax):
    disintegratable_bricks = np.zeros([number_of_bricks], dtype=int)
    bricks_that_i_sit_on = [[] for _ in range(number_of_bricks)]
    bricks_that_sit_on_me = [[] for _ in range(number_of_bricks)]
    # What bricks sit on each brick
    for touches in enumerate(touching_bricks):
        print(touches)
        for indexes in enumerate(touches[1]):
            bricks_that_sit_on_me[indexes[1]].append(touches[0] + 1)
    print(touching_bricks, "bricks that I sit on")
    print(bricks_that_sit_on_me, "bricks that sit on me")

    bricks_that_i_sit_on = touching_bricks
    # Now lets check for disintegration!


    for bricks_on_top in enumerate(bricks_that_sit_on_me): # loop over all bricks
        check = []
        for each in bricks_on_top[1]: # For each brick on top of me
            print(each, bricks_on_top[0])
            for every in bricks_that_i_sit_on[each - 1]: # Look at other bricks it sits on
                print(every, "ev")
                if bricks_on_top[0] + 1 != every: # Check if it sits on other bricks
                    check.append(1)
        if check:
            print(check, "check")
            print(bricks_on_top[1])
            if sum(check) == len(check): # There may be multiple bricks on top so only disintegrate if they are all supported by another brick
                disintegratable_bricks[bricks_on_top[0]] = 1
    # for i in range(number_of_bricks):
    #     if bricks_that_sit_on_me[i] == []:
    #         disintegratable_bricks[i] = 1
    disintegratable_bricks[np.where([len(sit_on_me) == 0 for sit_on_me in bricks_that_sit_on_me])] = 1
    plot_blocks(brick_tracker, ax, brick_cube_indices, disintegratable_bricks)
    plt.draw()  # plt.show()  # savefig("demo.png")
    plt.show()
    print(disintegratable_bricks)


    return disintegratable_bricks

def plot_blocks(brick_tracker, ax, brick_cube_indices, disintegratable_bricks):
    plt.pause(3)
    ax.clear()
    n_voxels = np.zeros_like(brick_tracker, dtype=bool)
    n_voxels[np.where(brick_tracker > 0)] = True
    facecolors = np.where(n_voxels, 'temp', 'temp')
    edgecolors = np.where(n_voxels, '0', 'black')
    colors = ['b','g','r','c','m','y'] # ,'lime', 'pink', 'cyan'
    edge_colors = ['black', 'white']
    for bricks in enumerate(brick_cube_indices):
         for cube in bricks[1]:
            facecolors[tuple(cube)] = colors[bricks[0] % len(colors)]
            if type(disintegratable_bricks) == str:
                edgecolors[tuple(cube)] = 'k'
            else:
                edgecolors[tuple(cube)] = edge_colors[disintegratable_bricks[bricks[0]]]

    filled = np.zeros(n_voxels.shape)
    filled[np.where(n_voxels > 0)] = 1

    # upscale the above voxel image, leaving gaps
    filled_2 = explode(filled)
    fcolors_2 = explode(facecolors)
    ecolors_2 = explode(edgecolors)

    # Shrink the gaps
    x, y, z = np.indices(np.array(filled_2.shape) + 1).astype(float) // 2
    x[0::2, :, :] += 0.05
    y[:, 0::2, :] += 0.05
    z[:, :, 0::2] += 0.05
    x[1::2, :, :] += 0.95
    y[:, 1::2, :] += 0.95
    z[:, :, 1::2] += 0.95

    ax.voxels(x, y, z, filled_2, facecolors=fcolors_2, edgecolors=ecolors_2)
    ax.set_aspect('equal')

    plt.draw()
    plt.pause(1)

def explode(data):
    size = np.array(data.shape)*2
    data_e = np.zeros(size - 1, dtype=data.dtype)
    data_e[::2, ::2, ::2] = data
    return data_e

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
    touching_bricks, ax = create_settled_pattern(data, brick_tracker, brick_cube_indices, number_of_bricks)
    # STEP 4: Let's figure out which bricks can be safely disintegrated
    disintegratable_bricks = identify_bricks_to_disintegrate(touching_bricks, number_of_bricks, brick_tracker, brick_cube_indices, ax)

    print(" ")
    print("#########################################################")
    print(" ")
    print("#########################################################")
    print("The number of disintegratable bricks is:", np.sum(disintegratable_bricks), len(disintegratable_bricks)) # 618 is too high & 111 too low & 368 too low & wrong 487, 497 wrong
    print("#########################################################")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()