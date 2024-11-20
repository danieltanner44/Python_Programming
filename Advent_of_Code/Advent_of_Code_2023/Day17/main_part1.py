import numpy as np
import time
import matplotlib.pyplot as plt

def reading_input_data(f):
    print("Reading input data...", end = "\n")
    map_input = np.array([], dtype=int)
    for each_line in f:
        map_input = np.append(map_input, list((each_line.strip("\n"))))
    map_input = np.array(np.reshape(map_input, [len(each_line), len(map_input)//len(each_line)]), dtype=int)
    print(map_input)
    print("[complete]", end="\n")
    print("################################")
    print("The map has shape", np.shape(map_input))
    print("################################")
    print(" ")
    return map_input

def create_nodes_edges(map_input):
    connected_nodes = []
    node_index = np.array(list(range(np.shape(map_input)[0]*np.shape(map_input)[0])))
    node_index = np.reshape(node_index, np.shape(map_input))
    node_index = np.pad(node_index,1,"constant", constant_values=(-1))
    #Lets find the edges that vertices are connected to
    for i in range(1,np.shape(node_index)[0] - 1): # rows
        for j in range(1,np.shape(node_index)[1] - 1): # columns
            temp_nodes = []
            if node_index[i + 1,j] != -1:
                temp_nodes.append(node_index[i + 1,j])
            if node_index[i -1,j] != -1:
                temp_nodes.append(node_index[i - 1,j])
            if node_index[i,j + 1] != -1:
                temp_nodes.append(node_index[i,j + 1])
            if node_index[i,j - 1] != -1:
                temp_nodes.append(node_index[i,j - 1])
            connected_nodes.append(temp_nodes)
    node_index = np.delete(node_index,[0,np.shape(node_index)[0] - 1],0)
    node_index = np.delete(node_index, [0, np.shape(node_index)[1] - 1], 1)
    return connected_nodes, node_index

def dijkstras_path_finding(map_input, connected_nodes, node_index):
    # Used algorithm as described here: https://www.youtube.com/watch?v=bZkzH5x0SKU
    current_node = 0
    shortest_distance = np.ones(shape=(np.shape(node_index)), dtype=int)*100000  # infinity is distance to improve
    shortest_distance[np.where(node_index == current_node)] = map_input[np.where(node_index == current_node)]
    unvisited_nodes = np.ones(shape=(np.shape(node_index)), dtype=int) # set of nodes
    previous_node = np.zeros(shape=(np.shape(node_index)), dtype=int) # To track the shortest path
    while np.sum(unvisited_nodes) != 0:
        # Step through neighbours and assess their distances
        for node in connected_nodes[current_node]:
            temp_distance = (shortest_distance[node_index == current_node] + map_input[node_index == node])[0]
            if temp_distance < shortest_distance[node_index == node] and unvisited_nodes[node_index == node] == 1:
                shortest_distance[node_index == node] = temp_distance
                previous_node[node_index == node] = current_node
        # Set current node as now being visited
        unvisited_nodes[node_index == current_node] = 0
        if np.sum(unvisited_nodes) != 0:
            # Select new node as current node, i.e., unvisited with minimum shortest distance
            shortest_distance_to_unvisited_node = np.min(shortest_distance[unvisited_nodes == 1])
            current_node = node_index[np.where((shortest_distance == np.min(shortest_distance_to_unvisited_node)) & (unvisited_nodes == 1))][0]
        else:
            break
    print(shortest_distance)
    return shortest_distance, previous_node


def reconstruct_shortest_path(previous_node, node_index, end_node):
    path = np.zeros(shape=(np.shape(previous_node)), dtype=int) # To track final shortest path
    current_node = end_node
    while current_node !=0:
        path[node_index == current_node] = 8
        current_node = previous_node[node_index == current_node]
    path[node_index == current_node] = 8
    return path

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    fI = open(r'D:\Advent_of_Code\Advent_of_Code_2023\Day17\Puzzle_Input_d.txt', 'r')
    # Read all of the input data from Puzzle Input and organise it
    map_input = reading_input_data(fI)

    connected_nodes, node_index = create_nodes_edges(map_input)

    shortest_distance, previous_node = dijkstras_path_finding(map_input, connected_nodes, node_index)
    end_node = np.shape(previous_node)[0] * np.shape(previous_node)[1] - 1  # Start an end node

    path = reconstruct_shortest_path(previous_node, node_index, end_node)

    print(path)
    # Now lets walk through the gardens
    print(" ")
    print("###########################################")
    print("The best path provides a heat loss of:", shortest_distance[node_index == end_node][0])
    print("###########################################")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()