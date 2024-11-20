import numpy as np
import time

def reading_input_data(f):
    print("Reading input data...", end = "")
    data = np.array([],dtype=str)
    for each_line in f:
        data = np.append(data,list(each_line.strip("\n")))
    data = np.reshape(data,[len(data)//(len(each_line[:]) - 1),len(list(each_line[:])) -1])
    print("[complete]", end="\n")
    print("################################")
    print("The contraption design is:")
    print(data)
    print("################################")
    print(" ")
    return data

def tracking_beams(data):
    path_tracker = np.zeros(np.shape(data), dtype=int)
    cyclic_check = np.zeros(np.shape(data), dtype=int)
    # Initialise first beam conditions
    beam_parameters = [[0,0,4]]
    # Set the resultant directions for the two types of mirror (forward slash and backslash)
    # 1, 2, 3 and 4 are up, down, left and right, respectively
    fs_directions = {1: 4, 2: 3, 3: 2, 4: 1}
    bs_directions = {1: 3, 2: 4, 3: 1, 4: 2}
    # Keep stepping until all beams have left contraption or are cycling
    while beam_parameters: # Keep going until we have no beams to follow
        # Update map to show where beam has been
        path_tracker[tuple(beam_parameters[0][0:2])] += 1
        # Update check for cycles - note this is not robust to more complex cycles
        cyclic_check[tuple(beam_parameters[0][0:2])] = beam_parameters[0][2]
        # Assess current step in contraptions to see if a direction change is needed
        if data[tuple(beam_parameters[0][0:2])] == "/":
            beam_parameters[0][2] = fs_directions[beam_parameters[0][2]]
        elif data[tuple(beam_parameters[0][0:2])] == "\\":
            beam_parameters[0][2] = bs_directions[beam_parameters[0][2]]
        # Assess current step in contraptions to see if a beam split is needed
        elif (data[tuple(beam_parameters[0][0:2])] == "|") and (beam_parameters[0][2] == 3 or beam_parameters[0][2] == 4):
            # Beam split!
            beam_parameters[0][2] = 1 # Divert the current beam and keep tracking
            beam_parameters.append([beam_parameters[0][0],beam_parameters[0][1],2]) # Queue up second diverted beam
        elif (data[tuple(beam_parameters[0][0:2])] == "-") and (beam_parameters[0][2] == 1 or beam_parameters[0][2] == 2):
            # Beam split!
            beam_parameters[0][2] = 3 # Divert the current beam and keep tracking
            beam_parameters.append([beam_parameters[0][0], beam_parameters[0][1], 4]) # Queue up second diverted beam
        # Find New Position for Next Step, which depends on updated direction from above
        if beam_parameters[0][2] == 1:
            beam_parameters[0][0] -= 1
        elif beam_parameters[0][2] == 2:
            beam_parameters[0][0] += 1
        elif beam_parameters[0][2] == 3:
            beam_parameters[0][1] -= 1
        elif beam_parameters[0][2] == 4:
            beam_parameters[0][1] += 1
        # Check if next step is outside map, if so stop by removing the current beam from the queue
        if (0 > beam_parameters[0][0] or beam_parameters[0][0] == np.shape(path_tracker)[0]) or (0 > beam_parameters[0][1] or beam_parameters[0][1] == np.shape(path_tracker)[1]):
            beam_parameters.remove(beam_parameters[0][:])
        # Need to try and find cycles and stop to avoid infinite loops
        if cyclic_check[tuple(beam_parameters[0][0:2])] == beam_parameters[0][2]:
            # Beam revisting same space moving in the same direction so stop by removing it
            beam_parameters.remove(beam_parameters[0][:])
            continue
    number_energised_cells = np.count_nonzero(path_tracker)
    return(number_energised_cells)

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    fI = open(r'D:\Advent_of_Code\Advent_of_Code_2023\Day16\Puzzle_Input.txt', 'r')
    # Read all of the input data from Puzzle Input and organise it
    data = reading_input_data(fI)
    # Now lets track the beam trajectories
    number_energised_cells = tracking_beams(data)
    print(" ")
    print("########################################")
    print("The number of energised cells is:", number_energised_cells)
    print("########################################")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()