import time
import numpy as np
from my_modules.development import fstring
from my_modules.development import print_array

def read_input_data(filename):
    # Read input file to get the diagram of the tachyon manifold
    diagram_of_tachyon_manifold = []
    with open(filename, 'r') as f:
        for line in f:
            temp = [character for character in line.strip()]
            diagram_of_tachyon_manifold.append(temp)
    # Reform as np array so can index through more easily
    diagram_of_tachyon_manifold = np.array(diagram_of_tachyon_manifold, dtype=str)
    return diagram_of_tachyon_manifold

def map_beam_splitting(beam_starting_point, diagram_of_tachyon_manifold):
    beam_splitters_counter = 0
    manifold_shape = np.shape(diagram_of_tachyon_manifold)
    # Start a tracker of coordinates to process that we add and pop from
    beam_tracker = [beam_starting_point]
    # Create a map to track progress
    beam_tracker_map = np.full(manifold_shape, dtype=str, fill_value=".")
    # Create a nice tracker map with the original starting point and splitters
    beam_tracker_map[tuple(beam_starting_point)] = "S"
    beam_tracker_map[diagram_of_tachyon_manifold == "^"] = "^"
    while len(beam_tracker) != 0:
        # Pop first element (current beam) on tracker list to process
        current_beam = beam_tracker.pop(0)
        # Assess what is below current beam in the manifold
        next_step = [current_beam[0] + 1, current_beam[1] + 0]
        if next_step[0] > manifold_shape[0] - 1:
            # Go to next beam on the list if present one is at bottom of manifold
            continue
        if diagram_of_tachyon_manifold[tuple(next_step)] == ".":
            # If it is already done (due to other beam) don't do again
            if beam_tracker_map[tuple(next_step)] == ".":
                # The beam progresses downward to the next row
                # Mark on tracker map and add new point to tracker list
                beam_tracker_map[tuple(next_step)] = "|"
                beam_tracker.append(next_step)
        if beam_tracker_map[tuple(next_step)] == "^":
            # Counter another splitter found
            beam_splitters_counter += 1
            # Need to split the beam, left and right
            right_beam = [next_step[0], next_step[1] + 1]
            left_beam = [next_step[0], next_step[1] - 1]
            # For each ensure it is not done already to avoid duplicates
            if right_beam not in beam_tracker:
                beam_tracker.append(right_beam)
                beam_tracker_map[tuple(right_beam)] = "|"
            if left_beam not in beam_tracker:
                beam_tracker.append(left_beam)
                beam_tracker_map[tuple(left_beam)] = "|"
    return beam_splitters_counter, beam_tracker_map

def determine_number_of_timelines(beam_starting_point, diagram_of_tachyon_manifold):
    # Was unsure what the question was asking so looked at a visualisation of the answer
    # For a direction to avoid wasting time - then created my own solution here
    manifold_shape = np.shape(diagram_of_tachyon_manifold)
    beam_tracker = [beam_starting_point]
    timeline_map = np.full(manifold_shape, dtype=int, fill_value=0)
    timeline_map[tuple(beam_starting_point)] = 1
    while len(beam_tracker) != 0:
        current_beam = beam_tracker.pop(0)
        # Assess what is below current beam in the manifold
        next_step = [current_beam[0] + 1, current_beam[1] + 0]
        if next_step[0] > manifold_shape[0] - 1:
            # Go to next beam on the list as this at the end of the manifold
            continue
        if diagram_of_tachyon_manifold[tuple(next_step)] == ".":
            # The beam progresses downward to the next row
            # Add beam numbers in case there are multiple
            timeline_map[tuple(next_step)] += timeline_map[tuple(current_beam)]
            # But only add one to tracker, no need for duplicates
            if next_step not in beam_tracker:
                beam_tracker.append(next_step)
        if diagram_of_tachyon_manifold[tuple(next_step)] == "^":
            # Need to split the beam, left and right
            right_beam = [next_step[0], next_step[1] + 1]
            left_beam = [next_step[0], next_step[1] - 1]
            if right_beam not in beam_tracker:
                beam_tracker.append(right_beam)
            if left_beam not in beam_tracker:
                beam_tracker.append(left_beam)
            # Add the contributions for each
            timeline_map[tuple(right_beam)] += timeline_map[tuple(current_beam)]
            timeline_map[tuple(left_beam)] += timeline_map[tuple(current_beam)]
    # Sum the final row of the beam number tracker to get the total number of timelines
    timeline_counter = np.sum(timeline_map[-1:])
    return timeline_counter, timeline_map

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = (r"D:\Python_Projects\Python_Programming\Advent_of_Code\Advent_of_Code_2025\Day7\Puzzle_Input.txt")
    diagram_of_tachyon_manifold = read_input_data(filename)
    beam_starting_point = np.where(diagram_of_tachyon_manifold == "S")
    beam_starting_point = [int(i[0]) for i in beam_starting_point]

    print(" ")
    print(fstring(f"=================================================================", "bk", "bl"))
    manifold_shape = np.shape(diagram_of_tachyon_manifold)
    print(fstring(f"The tachyon manifold has size {str(manifold_shape)} with {str(manifold_shape[0] * manifold_shape[1])} elements.", "bk", "wt"))
    print(fstring(f"The beam starting point is {tuple([int(i) for i in beam_starting_point])} and the tachyon manifold layout is:",
        "bk", "wt"))
    print_array(diagram_of_tachyon_manifold)
    print(fstring(f"=================================================================", "bk", "bl"))
    print(" ")

    print(" ")
    print(fstring(f"=================================================================", "bk", "bl"))
    print(f'{fstring("Part One:", "bk", "wt")}')
    beam_splitters_counter, beam_tracker_map = map_beam_splitting(beam_starting_point, diagram_of_tachyon_manifold)
    part_one_ans = beam_splitters_counter
    print(f'The number of times a beam splitter is encountered is: {fstring(str(part_one_ans), "wt", "bk")}')
    print(fstring(f"=================================================================", "bk", "bl"))
    print(" ")

    print(" ")
    print(fstring(f"=================================================================", "bk", "bl"))
    print(f'{fstring("Part Two:", "bk", "wt")}')
    time_line_counter, timeline_map = determine_number_of_timelines(beam_starting_point, diagram_of_tachyon_manifold)
    part_two_ans = time_line_counter
    print(f'The total number of timelines is: {fstring(str(part_two_ans), "wt", "bk")}')
    print(fstring(f"=================================================================", "bk", "bl"))
    print(" ")

    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()