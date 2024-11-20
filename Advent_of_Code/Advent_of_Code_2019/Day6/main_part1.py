import time
import numpy as np
import my_modules.graph as mmg
import networkx as nx
import matplotlib.pyplot as plt


def read_input_data(filename):
    input_orbits = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip().split(")")
            input_orbits.append(tuple(line))
    bodies = sorted(set([y for x in input_orbits for y in x]))
    return input_orbits, bodies

def plot_graph(bodies, input_orbits):
    adjacency_matrix = mmg.create_adjacency_matrix(bodies, input_orbits)
    G = nx.Graph(adjacency_matrix)
    nx.draw(G, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_color='black')
    plt.show()
    return

def calculate_total_paths(bodies, input_orbits):
    path_length = 0
    adjacency_matrix = mmg.create_adjacency_matrix(bodies, input_orbits)
    allowable_visits = {body: 1 for body in bodies}
    for body in bodies:
        if body != "COM":
            path = mmg.find_all_paths(start_point="COM", end_point=body, allowable_visits=allowable_visits, nodes=bodies,
                                adjacency_matrix=adjacency_matrix)
            path_length += len(path[0]) - 1
    return path_length

def calculate_orbit_transfers(bodies, input_orbits):
    adjacency_matrix = mmg.create_adjacency_matrix(bodies, input_orbits)
    allowable_visits = {body: 1 for body in bodies}
    path = mmg.find_all_paths(start_point="YOU", end_point="SAN", allowable_visits=allowable_visits, nodes=bodies,
                        adjacency_matrix=adjacency_matrix)
    print(path)
    orbit_transfers = len(path[0]) - 3
    return orbit_transfers

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2019\Day6\Puzzle_Input.txt"
    input_orbits, bodies = read_input_data(filename)

    print(" ")
    print("==============================================================")
    print("The heavenly bodies are:")
    print(bodies)
    print("==============================================================")
    print("The input orbits are:")
    print(input_orbits)
    print("==============================================================")
    print(" ")

    # Plot graph of orbit connectivity as visual reference
    plot_graph(bodies, input_orbits)

    # Part 1 - Calculate all path lengths between all bodies and "COM"
    path_length = calculate_total_paths(bodies, input_orbits)

    # Part 2 - Calculate path between "YOU" and "SAN"
    orbit_transfers = calculate_orbit_transfers(bodies, input_orbits)

    print(" ")
    print("==============================================================")
    print("PART 1: The number of direct / indirect orbits is:", path_length)
    print("==============================================================")
    print(" ")

    print(" ")
    print("==============================================================")
    print("PART 2: The number of required orbit transfers is:", orbit_transfers)
    print("==============================================================")
    print(" ")

    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()