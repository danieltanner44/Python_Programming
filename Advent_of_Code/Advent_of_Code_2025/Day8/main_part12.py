import math
import time
import numpy as np
import copy
from my_modules.development import fstring
from my_modules.development import print_array

def read_input_data(filename):
    # Read input file to get the junction box locations
    junction_box_locations = []
    with open(filename, 'r') as f:
        for line in f:
            temp = line.strip().split(",")
            junction_box_locations.append(temp)
    # Reform as np array so can index through more easily
    junction_box_locations = np.array(junction_box_locations, dtype=np.int64)
    return junction_box_locations

def find_distance_between_junction_box_pairs(junction_box_locations):
    # Should create once an array of the closest distance and just use those
    distance_between_junction_box_pairs = []
    avoid_duplicates = []
    for index1, junction_box_location1 in enumerate(junction_box_locations):
        avoid_duplicates.append(index1)
        for index2, junction_box_location2 in enumerate(junction_box_locations):
            if index2 not in avoid_duplicates:
                distance = math.sqrt((junction_box_location1[0] - junction_box_location2[0])**2 +
                                     (junction_box_location1[1] - junction_box_location2[1])**2 +
                                     (junction_box_location1[2] - junction_box_location2[2])**2)
                distance_between_junction_box_pairs.append([distance, index1, index2])
    # closest_junction_box_pair structure: [distance, Junction Box ID1, Junction Box ID2]
    distance_between_junction_box_pairs = np.array(distance_between_junction_box_pairs, dtype=np.object_)
    return distance_between_junction_box_pairs

def process_junction_boxes(number_circuits, junction_box_locations, distance_between_junction_box_pairs):
    shape = np.shape(junction_box_locations)
    circuit_tracker = []
    # Sort junction box distances to start with shortest
    distance_between_junction_box_pairs = distance_between_junction_box_pairs[distance_between_junction_box_pairs[:,0].argsort()]
    counter = 0

    while True:
        # For the first loop just add the first pair of junction boxes as a new circuit
        if counter == 0:
            circuit_tracker.append([distance_between_junction_box_pairs[counter, 1], distance_between_junction_box_pairs[counter, 2]])

        # Check if either junction is in an existing circuit and if so what circuit they affect
        circuit_indexes = [None, None]
        for index, circuit in enumerate(circuit_tracker):
            if distance_between_junction_box_pairs[counter, 1] in circuit:
                circuit_indexes[0] = index
            if distance_between_junction_box_pairs[counter, 2] in circuit:
                circuit_indexes[1] = index

        if circuit_indexes[0] is None and circuit_indexes[1] is None:
            # Neither of the junction boxes are in an existing circuit then just add both as new circuit
            circuit_tracker.append([distance_between_junction_box_pairs[counter, 1], distance_between_junction_box_pairs[counter, 2]])

        elif circuit_indexes[0] is None or circuit_indexes[1] is None:
            # One of the junction boxes is in an existing circuit
            # Check if only one is in an existing circuit
            if circuit_indexes[0] is not None:
                circuit_tracker[circuit_indexes[0]] += [distance_between_junction_box_pairs[counter, 2]]
            elif circuit_indexes[1] is not None:
                circuit_tracker[circuit_indexes[1]] += [distance_between_junction_box_pairs[counter, 1]]

        elif circuit_indexes[0] != circuit_indexes[1]:
            # Each junction box is in a separate circuit so need to merge them
            # Add the merged circuit, remove each of the originals
            circuit_tracker.append(circuit_tracker[circuit_indexes[0]] + circuit_tracker[circuit_indexes[1]])
            circuit_tracker.pop(max(circuit_indexes))
            circuit_tracker.pop(min(circuit_indexes))

        # PART ONE COMPLETION CHECK
        if counter == number_circuits - 1:
            # For Part 1 once the required number of connections are made store the current circuit list
            part1_circuit_tracker = copy.deepcopy(circuit_tracker)

        # PART TWO COMPLETION CHECK
        # For Part Two stop making connections when all junction boxes are connected together
        if len(circuit_tracker[0]) == shape[0]:
            # Now the circuits are fully complete/connected multiply the X coordinates of the last two junction boxes together
            last_connected_pair = distance_between_junction_box_pairs[counter, 1:]
            multiplication_x_last_junction_boxes = junction_box_locations[last_connected_pair[0]][0] * \
                                                   junction_box_locations[last_connected_pair[1]][0]
            break
        # Counter index used to move to the next shortest distance by incrementing index for each loop
        counter += 1

    return part1_circuit_tracker, multiplication_x_last_junction_boxes

def calculate_multiplication_of_three_largest_circuits(Part1_circuit_tracker):
    # Calculate junction box sizes
    circuit_lengths = []
    # Create a list of circuit lengths
    for circuit in Part1_circuit_tracker:
        circuit_lengths.extend([len(circuit)])
    # Sort the lengths
    circuit_lengths = sorted(circuit_lengths)
    # Multiply the largest three together
    multiplication_of_three_largest_circuits = circuit_lengths[-1] * circuit_lengths[-2] * circuit_lengths[-3]
    return multiplication_of_three_largest_circuits

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = (r"D:\Python_Projects\Python_Programming\Advent_of_Code\Advent_of_Code_2025\Day8\Puzzle_Input.txt")
    junction_box_locations = read_input_data(filename)

    print(" ")
    print(fstring(f"===========================================================================================================", "bk", "bl"))
    print(fstring(f"There are {np.shape(junction_box_locations)[0]} junction boxes with the following locations:", "bk", "wt"))
    print_array(junction_box_locations)
    print(fstring(f"===========================================================================================================", "bk", "bl"))
    print(" ")

    # Calculate the distances between junction box pairs
    distance_between_junction_box_pairs = find_distance_between_junction_box_pairs(junction_box_locations)
    number_circuits = 1000

    print(" ")
    print(fstring(f"===========================================================================================================", "bk", "bl"))
    print(f'{fstring("Part One:", "bk", "wt")}')
    Part1_circuit_tracker, multiplication_x_last_junction_boxes = process_junction_boxes(number_circuits,
                                                                                         junction_box_locations,
                                                                                         distance_between_junction_box_pairs)
    multiplication_of_three_largest_circuits = calculate_multiplication_of_three_largest_circuits(Part1_circuit_tracker)
    part_one_ans = multiplication_of_three_largest_circuits
    print(f'The multiplication of the lengths of the three largest circuits is: {fstring(str(part_one_ans), "wt", "bk")}')
    print(fstring(f"===========================================================================================================", "bk", "bl"))
    print(" ")

    print(" ")
    print(fstring(f"===========================================================================================================", "bk", "bl"))
    print(f'{fstring("Part Two:", "bk", "wt")}')
    part_two_ans = multiplication_x_last_junction_boxes
    print(f'The multiplication of the x coordinates of the final connected junction boxes is: {fstring(str(part_two_ans), "wt", "bk")}')
    print(fstring(f"===========================================================================================================", "bk", "bl"))
    print(" ")

    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()