import time
import numpy as np
import re
import networkx as nx
from my_modules.graph import create_adjacency_matrix

def read_input_data(filename):
    input_data = []
    with open(filename, 'r') as f:
        for each_line in f:
            each_line = re.split("[,-]",each_line.strip())
            input_data.append(list(each_line))
        input_data = np.array(input_data, dtype=str)
    return input_data

def find_nodes(input_data):
    nodes = []
    for connection in input_data:
        for points in connection:
            if points not in ["start", "end"]:
                nodes = nodes + [points]
            else:
                nodes = nodes + ["start"] + ["end"]
    nodes = sorted(list(set(nodes)))
    visit_once = np.zeros([len(nodes)], dtype=np.int16)
    for index, node in enumerate(nodes):
        if node[0].islower():
            visit_once[index] = 1
    return nodes, visit_once

def find_edges(input_data):
    edges = []
    for connection in input_data:
        if connection[0] in ["start", "end"]:
            nodes_s = connection[0]
            nodes_e = connection[1]
        elif connection[1] in ["start", "end"]:
            nodes_e = connection[1]
            nodes_s = connection[0]
        else:
            nodes_s = connection[0]
            nodes_e = connection[1]
        edges.append((nodes_s, nodes_e))
    return edges


def find_all_paths(start_point, end_point, nodes, edges, adjacency_matrix):
    allowable_visits = {node: 0 for node in nodes}
    for node in allowable_visits:
        if node in ["start", "end"]:
            allowable_visits[node] = [1,1]
        elif node.isupper():
            allowable_visits[node] = [-1,-1]
        else:
            allowable_visits[node] = [1,2]
    all_paths = []
    queued_paths = [[start_point]]  # Initialize with the starting node
    visited_nodes = [{node: 0 for node in nodes}]  # Track visited nodes as a dictionary
    while queued_paths:
        queue = queued_paths.pop(0)  # Get and remove the first path
        current_visited_nodes = visited_nodes[0]  # Get the visited nodes
        print("=======================")
        print("Current path:", queue)
        # If the last node in the current path is not the end point
        if queue[-1] != end_point:
            # Mark the last node as visited
            current_node = queue[-1]
            current_visited_nodes[current_node] += 1
            if max(value for key, value in current_visited_nodes.items() if key.islower()) == 2:
            #if (current_visited_nodes["b"] == 2 or current_visited_nodes["c"] == 2 or current_visited_nodes["d"] == 2):
                allowable_visit_index = 0
            else:
                allowable_visit_index = 1
            # Explore neighbours
            for neighbour in adjacency_matrix[current_node]:
                if (current_visited_nodes[neighbour] < allowable_visits[neighbour][allowable_visit_index]) or allowable_visits[neighbour][allowable_visit_index] < 0:  # If neighbour is not visited or revisitable
                    temp_queue = queue + [neighbour]  # Create a new path
                    queued_paths.append(temp_queue)  # Add new path to the queue
                    visited_nodes.append(current_visited_nodes.copy())  # Copy visited state
        else:
            # Found a path that ends at the endpoint
            all_paths.append(queue)
            print("Found valid path:", queue)
        # Remove the current visited node state (if needed)
        visited_nodes.pop(0)
    return all_paths

def main():
    # progress_bar(days, days_to_model)
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = f"D:\Python_Programming\Advent_of_Code\Advent_of_Code_2021\Day12\Puzzle_Input.txt"
    input_data = read_input_data(filename)
    print("The input data is:")
    print(input_data)
    nodes, visit_once = find_nodes(input_data)
    edges = find_edges(input_data)
    adjacency_matrix = create_adjacency_matrix(nodes, edges)
    start_point = "start"
    end_point = "end"
    all_paths = find_all_paths(start_point, end_point, nodes, edges, adjacency_matrix)

    print(" ")
    print("==============================================================")
    print("The valid paths are:")
    print(all_paths)
    print("==============================================================")
    print(" ")
    print("==============================================================")
    print("Found a total of",len(all_paths),"valid paths!")
    print("==============================================================")
    print(" ")

    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()