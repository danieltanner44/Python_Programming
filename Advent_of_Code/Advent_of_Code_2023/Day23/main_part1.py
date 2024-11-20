import numpy as np
import time

def reading_input_data(f):
    print("Reading input data...", end = "")
    maze_data = np.array([],dtype=str)
    for each_line in f:
        maze_data = np.append(maze_data,list(each_line.strip("\n")))
    maze_data = np.reshape(maze_data,[len(maze_data)//(len(each_line[:])),len(list(each_line[:]))])
    starting_point = [0, int(np.where(maze_data[0, :] == ".")[0][0])]
    ending_point = [np.shape(maze_data)[0] - 1, int(np.where(maze_data[np.shape(maze_data)[0] - 1, :] == ".")[0][0])]
    maze_data[tuple(starting_point)] = "S"
    maze_data[tuple(ending_point)] = "E"

    print("[complete]", end="\n")
    print("################################")
    print("The maze design is:")
    print(maze_data)
    print("################################")
    print(" ")
    print("Maze has starting point:", starting_point)
    print("and ending point:", ending_point)
    print(" ")
    return maze_data, starting_point, ending_point
def walking_through_maze(maze_data, starting_point, ending_point):
    overall_step_tracker = []
    branching_backlog = []
    branching_backlog.append([starting_point[0], starting_point[1], 1])
    tracking_mask = np.zeros((np.shape(maze_data)), dtype=int)
    branch_number = 0
    while branching_backlog:

        for i in range(len(branching_backlog)): # Search all branches in the same generation
            branch_number += 1
            next_position = np.array((branching_backlog[0][0], branching_backlog[0][1]))
            tracking_mask[tuple(next_position)] = branch_number
            number_of_steps = 1
            while 1 == 1:
                found_path = np.zeros((tuple([4, 1])), dtype=int)
                current_position = next_position
                if number_of_steps == 1:
                    # Make sure we are walking in the correct direction
                    found_path[branching_backlog[0][2]] = 1
                else:
                    # What directions are open
                    if (maze_data[tuple(current_position + np.array((-1, 0)))] == "." or maze_data[tuple(current_position + np.array((-1, 0)))] == "^") and (tracking_mask[tuple(current_position + np.array((-1, 0)))] == 0): # Up
                        found_path[0] = 1
                    if (maze_data[tuple(current_position + np.array((1, 0)))] == "." or maze_data[tuple(current_position + np.array((1, 0)))] == "v" or maze_data[tuple(current_position + np.array((1, 0)))] == "E") and (tracking_mask[tuple(current_position + np.array((1, 0)))] == 0): # Down
                        if (maze_data[tuple(current_position + np.array((1, 0)))] == "E"):
                            # Reached the end, try another branch
                            branching_backlog.remove(branching_backlog[0])
                            overall_step_tracker.append([number_of_steps, branch_number])
                            break
                        else:
                            found_path[1] = 1
                    if (maze_data[tuple(current_position + np.array((0, -1)))] == "." or maze_data[tuple(current_position + np.array((0, -1)))] == "<") and (tracking_mask[tuple(current_position + np.array((0, -1)))] == 0): # Left
                        found_path[2] = 1
                    if (maze_data[tuple(current_position + np.array((0, 1)))] == "." or maze_data[tuple(current_position + np.array((0, 1)))] == ">") and (tracking_mask[tuple(current_position + np.array((0, 1)))] == 0): # Right
                        found_path[3] = 1
                    # Is there more than one direction open, if so there is a branch
                    if np.sum(found_path) > 1: # There is a branch
                        for i in range(4):
                            if found_path[i] == 1:
                                branching_backlog.append([current_position[0], current_position[1], i]) # Add in newly found branches
                        branching_backlog.remove(branching_backlog[0])  # remove the original branch you were on
                        overall_step_tracker.append([number_of_steps, branch_number]) # Log where we are and how many steps were needed
                        break # Go back to backlog
                if np.sum(found_path) == 1: # There is only one step you can take, so take it
                    if found_path[0] == 1:
                        next_position = current_position + np.array((-1, 0))
                    elif found_path[1] == 1:
                        next_position = current_position + np.array((1, 0))
                    elif found_path[2] == 1:
                        next_position = current_position + np.array((0, -1))
                    elif found_path[3] == 1:
                        next_position = current_position + np.array((0, 1))
                    tracking_mask[tuple(next_position)] = branch_number # Mark the step so we do not revisit
                    number_of_steps += 1
                    continue # Take next step
                elif np.sum(found_path) == 0: # Dead End, go to next branch
                    branching_backlog.remove(branching_backlog[0])  # remove the original branch you were on
                    break # No help if it goes nowhere
                number_of_steps += 1
    print(tracking_mask)
    print(overall_step_tracker)
    return

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    fI = open(r'D:\Advent_of_Code\Advent_of_Code_2023\Day23\Puzzle_Input_d.txt', 'r')
    # Read all of the input data from Puzzle Input and organise it
    maze_data, starting_point, ending_point = reading_input_data(fI)
    # Let's start walking!
    path_length = walking_through_maze(maze_data, starting_point, ending_point)
    print(" ")
    print("########################################")
    print(" ")
    print("###############################################")
    print("The maximum number of energised cells is:", 0)
    print("###############################################")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()