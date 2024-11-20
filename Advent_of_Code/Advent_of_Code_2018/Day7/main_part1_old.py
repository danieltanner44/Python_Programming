import time
import my_modules.graph as mmg
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def read_input_data(filename):
    edges = []
    with (open(filename, 'r') as f):
        for line in f:
            line = line.strip().split(" ")
            edges.append((line[1],line[7]))
    nodes = list(set([x for y in edges for x in y]))
    return edges, nodes

def create_directional_adjacency(nodes, edges):
    directional_adjacency_matrix = {node : [[],[]] for node in nodes}
    for edge in edges:
        directional_adjacency_matrix[edge[1]][0].append(edge[0])
        directional_adjacency_matrix[edge[0]][1].append(edge[1])
    return directional_adjacency_matrix

def generate_graph(edges):
    DG=nx.DiGraph()
    DG.add_edges_from(edges)
    nx.draw(DG, with_labels=True)
    plt.show()
    return

def process_nodes_in_order(nodes, directional_adjacency_matrix):
    ordered_node_list = []
    processing_list = []

    # Find a nodes to start with, if they have no backward adjacent nodes
    for node in directional_adjacency_matrix:
        if not directional_adjacency_matrix[node][0]:
            processing_list.append(node)

    # Track which nodes are processed
    nodes_processed_check = {node : 0 for node in nodes}

    # Loop over the list of nodes to process until it is empty
    while processing_list:

        # Sort processing list and choose first element in alphabetical order to start with
        # Remove it from the list, add to check that node was processed and add to final ordered list
        processing_list = sorted(list(set(processing_list)))
        current_node = processing_list.pop(0)
        nodes_processed_check[current_node] = 1
        ordered_node_list.append(current_node)

        # Now check that the associated forward nodes have backward nodes that were all processed
        for node1 in directional_adjacency_matrix[current_node][1]:
            check = True
            for node2 in directional_adjacency_matrix[node1][0]:
                if nodes_processed_check[node2] == 0:
                    check = False
            if check:
                processing_list.append(node1)

    # Concatenate string for answer
    ordered_node_list = "".join(ordered_node_list)

    return ordered_node_list

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2018\Day7\Puzzle_Input.txt"
    edges, nodes = read_input_data(filename)
    print(" ")
    print("The input pairs are:")
    print(edges)
    print(" ")
    # Let's plot graph for a look
    print("Plotting graph...", end="")
    generate_graph(edges)
    print("[COMPLETE]")

    # Let's find the forward and backward connected nodes on the graph
    directional_adjacency_matrix = create_directional_adjacency(nodes, edges)
    # Calculate the order to process nodes
    ordered_node_list = process_nodes_in_order(nodes, directional_adjacency_matrix)

    print(" ")
    print("================================================================")
    print(f"The node order for steps is: {ordered_node_list}")
    print("================================================================")
    print(" ")

    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())



if __name__ == "__main__":
    main()