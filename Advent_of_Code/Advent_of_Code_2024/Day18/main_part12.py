import time
import numpy as np
from my_modules.development import fstring
from my_modules.development import print_array
import networkx as nx

def read_input_data(filename):
    byte_positions = []
    with open(filename, 'r') as f:
        for line in f:
            temp = list(reversed(line.strip().split(",")))
            for i in [0,1]:
                temp[i] = int(temp[i])
            byte_positions.extend([tuple(temp)])
    return byte_positions

def process_falling_bytes(memory_map, bytes_to_process, byte_positions):
    for i in range(bytes_to_process):
        memory_map[byte_positions[i]] = "#"
    return memory_map

def create_graph_from_map(memory_map, start_point, end_point):
    processing_list = [start_point]
    memory_map_shape = np.shape(memory_map)

    # Create node numbers
    nodes = []
    node_numbers = np.full(memory_map_shape, fill_value=0, dtype=np.int16)
    node_ids = 0
    for row in range(memory_map_shape[0]):
        for col in range(memory_map_shape[1]):
            if memory_map[row, col] != "#":
                node_numbers[row, col] = str(node_ids)
                nodes.extend([str(node_ids)])
                node_ids += 1
    start_node = str(node_numbers[start_point])
    end_node = str(node_numbers[end_point])

    # Walk through map and generate edge and node lists
    edges = []
    # Track which nodes have been processed
    completion_tracker = np.full(memory_map_shape, fill_value=0, dtype=np.int16)
    while len(processing_list) != 0:
        current_location = processing_list.pop()
        completion_tracker[current_location] = 1

        # Check for neighbours
        neighbour_indices = [(current_location[0] - 1, current_location[1]),
                            (current_location[0] + 1, current_location[1]),
                            (current_location[0], current_location[1] - 1),
                            (current_location[0], current_location[1] + 1)]

        # Now process each possible neighbour
        for neighbour in neighbour_indices:
            # If the neighbour is in the map
            if 0 <= neighbour[0] < memory_map_shape[0] and 0 <= neighbour[1] < memory_map_shape[1]:
                # If the location is not a barrier (blocked by a falling byte)
                if memory_map[neighbour] != "#":
                    possible_edge1 = (str(node_numbers[current_location]), str(node_numbers[neighbour]))
                    possible_edge2 = (possible_edge1[1], possible_edge1[0])
                    if possible_edge1 not in edges and possible_edge2 not in edges:
                        # If edge does not exist then add it as an edge
                        edges.extend([possible_edge1])
                    if completion_tracker[neighbour] == 0:
                        # If the valid and unprocessed neighbour is not on the processing list then add it
                        if neighbour not in processing_list:
                            processing_list.extend([neighbour])

    return nodes, edges, start_node, end_node, node_numbers

def find_shortest_path(memory_map, start_point, end_point):
    # Create graph - edges
    nodes, edges, start_node, end_node, node_numbers = create_graph_from_map(memory_map, start_point, end_point)

    # Find shortest path
    G = nx.Graph()
    G.add_edges_from(edges)
    shortest_path = nx.shortest_path(G, source=start_node, target=end_node,method='dijkstra')

    return shortest_path, node_numbers

def print_shortest_graph(memory_map, shortest_path, node_numbers):
    tracker_map = memory_map.copy()
    for step in shortest_path:
        location = np.where(node_numbers == int(step))
        location = (location[0][0], location[1][0])
        tracker_map[location] = "O"
    print_array(tracker_map)
    return

def find_byte_that_blocks_path(initial_memory_map, byte_positions, start_point, end_point):
    # Create a list of possible times from the first bite (0) to the last
    time_values = list(range(len(byte_positions)))
    last_time = 0
    # Loop over all possible byte positions until final blocking byte is found
    # Will used bisecting method to speed up start with the middle value of time_values
    # If there is a valid path then discount all prior time_value and choose
    # the middle one of the remaining times as the next guess
    print(f"Processing byte positions...")
    while True:
        memory_map = initial_memory_map.copy()
        path_found = True
        # Choose time value - middle of possible times:
        current_time = time_values[len(time_values)//2]
        print(f"Current time: {current_time}, byte_position: {byte_positions[current_time]}")
        # Progress byte drops to selected time value
        memory_map = process_falling_bytes(memory_map, current_time, byte_positions)
        try:
            shortest_path, node_numbers = find_shortest_path(memory_map, start_point, end_point)
        except:
            # If no valid path was found then time_value is too late, try earlier as blocked
            path_found = False
        # Adjust time using a bisecting method
        if path_found == False:
            # Need to stop sooner
            time_values = time_values[:len(time_values)//2]
        else:
            # Need later time
            time_values = time_values[len(time_values)//2:]
        if current_time == last_time:
            # If we have
            break
        last_time = current_time
    return memory_map, (byte_positions[current_time][1], byte_positions[current_time][0]), current_time

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2024\Day18\Puzzle_Input.txt"
    byte_positions = read_input_data(filename)

    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=======================  Puzzle Input  =======================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"There are {len(byte_positions)} bytes falling in the memory space, namely: ", "bk", "wt"))
    print(byte_positions)

    memory_map_shape = [70 + 1, 70 + 1]
    initial_memory_map = np.full(memory_map_shape, fill_value=".", dtype=np.str_)
    print(fstring(f"The memory map has shape {memory_map_shape} with {memory_map_shape[0] * memory_map_shape[1]} spaces, and looks like this: ", "bk", "wt"))
    print_array(initial_memory_map)
    print(fstring(f"====================  Puzzle Input - End =====================", "bk", "bl"))

    print(" ", end="\n\n")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=========================  PART ONE  =========================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))

    number_bytes_to_process = 1024
    memory_map = initial_memory_map.copy()
    memory_map = process_falling_bytes(memory_map, number_bytes_to_process, byte_positions)
    print(fstring(f"After dropping {number_bytes_to_process} bytes the memory map looks like this: ", "bk", "wt"))
    print_array(memory_map)

    start_point = (0,0)
    end_point = (memory_map_shape[0] - 1, memory_map_shape[1] - 1)
    shortest_path, node_numbers = find_shortest_path(memory_map, start_point, end_point)

    part_one_ans = str(len(shortest_path) - 1)
    print(fstring(f"The shortest path has {part_one_ans} steps and looks like this: ", "bk", "wt"))
    print_shortest_graph(memory_map, shortest_path, node_numbers)

    print(fstring(f"======================  PART ONE - END  ======================", "bk", "bl"))

    print(" ", end="\n\n")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=========================  PART TWO  =========================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))

    memory_map, blocking_byte_position, current_time = find_byte_that_blocks_path(initial_memory_map, byte_positions, start_point, end_point)
    part_two_ans = f"{blocking_byte_position[0]},{blocking_byte_position[1]}"

    print(fstring(f"The byte that finally blocks a path to the exit is: {blocking_byte_position} ", "bk", "wt"))
    print(fstring(f"This is the {current_time} byte in the falling list.", "bk", "wt"))
    print(fstring(f"======================  PART TWO - END  ======================", "bk", "bl"))

    print(" ", end="\n\n")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=========================  ANSWERS  ==========================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))
    print(f'{fstring("Part One:", "bk", "wt")}')
    print(f'The total calibration result is: {fstring(part_one_ans, "wt", "bk")}')
    print(fstring(f"==============================================================", "bk", "bl"))
    print(f'{fstring("Part Two:", "bk", "wt")}')
    print(f'The total calibration result is: {fstring(part_two_ans, "wt", "bk")}')
    print(fstring(f"==============================================================", "bk", "bl"))
    print(" ")

    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()