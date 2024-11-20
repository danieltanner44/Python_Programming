import time
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
    scheduling_order = {}

    # Find a nodes to start with, if they have no backward adjacent nodes
    for node in directional_adjacency_matrix:
        if not directional_adjacency_matrix[node][0]:
            processing_list.append(node)

    # Track which nodes are processed
    nodes_processed_check = {node : 0 for node in nodes}

    # Loop over the list of nodes to process until it is empty
    index = 0
    while processing_list:
        index += 1
        # Sort processing list and choose first element in alphabetical order to start with
        # Remove it from the list, add to check that node was processed and add to final ordered list
        processing_list = sorted(list(set(processing_list)))
        current_node = processing_list.pop(0)
        nodes_processed_check[current_node] = 1
        ordered_node_list.append(current_node)

        # Now check that the associated forward nodes have backward nodes that were all processed
        temp = []
        for node1 in directional_adjacency_matrix[current_node][1]:
            check = True
            for node2 in directional_adjacency_matrix[node1][0]:
                if nodes_processed_check[node2] == 0:
                    check = False
            if check:
                temp.append(node1)
                processing_list.append(node1)
        scheduling_order[current_node] = temp

    # Concatenate string for answer
    ordered_node_list = "".join(ordered_node_list)

    return ordered_node_list, scheduling_order

def calculate_worker_timing(ordered_node_list, scheduling_order, num_workers, directional_adjacency_matrix):
    task_durations = {node : 60 + ord(node) - 64 for node in ordered_node_list}
    # Use worker_assignments to track what worker is working on what, in form # {[Task, Duration]}
    worker_assignments = {f"Worker {i}": [None, None] for i in range(1, num_workers + 1)}
    # Track which tasks have been fully completed
    task_completion_checker = {node : 0 for node in ordered_node_list}

    # Find intial tasks to start in parallel, these have to backward nodes
    available_tasks = []
    for task in directional_adjacency_matrix:
        if len(directional_adjacency_matrix[task][0]) == 0:
            available_tasks.append(task)
    # Need to track tasks added to available tasks but not yet complete
    in_progress_list = []
    # Start the clock and loop until all workers are idle
    timing = 0
    while True:
        # Allocate available tasks to workers (if available)
        available_tasks1 = available_tasks.copy()
        for task in available_tasks1:
            for worker_key in worker_assignments:
                if worker_assignments[worker_key][0] is None:
                    worker_assignments[worker_key][0] = task
                    worker_assignments[worker_key][1] = task_durations[task]
                    in_progress_list.append(task)
                    available_tasks.remove(task)
                    break

        # Format and print worker assignments
        for index, data in enumerate(worker_assignments.items(), start=1):
            key, value = data
            if index % num_workers == 1:
                print(f"{timing: <7}" + " ", end="")
            print(f"{value}"+" ", end="")
            if index % num_workers == 0:
                print("")

        # Now increment each current task that is being worked on
        for worker_key in worker_assignments:
            # If worker is working on it then decrement the time by 1
            if worker_assignments[worker_key][0] is not None:
                worker_assignments[worker_key][1] -= 1
            # If task decrements to 0 make worker available again and mark task as complete
            if worker_assignments[worker_key][1] == 0:
                completed_task = worker_assignments[worker_key][0]
                task_completion_checker[completed_task] = 1
                worker_assignments[worker_key] = [None, None]

                # If task finished release unblocked tasks to available_tasks list
                newly_available_tasks = []
                # Find tasks that have not been completed and are not listed already as available_tasks
                for key in directional_adjacency_matrix:
                    # If key task is incomplete then check associated backward tasks
                    if task_completion_checker[key] == 0:
                        # If all backward tasks are complete
                        backward_tasks = [task_completion_checker[element] for element in directional_adjacency_matrix[key][0]]
                        if 0 not in backward_tasks and key not in available_tasks1 and key not in in_progress_list:
                            newly_available_tasks.append(key)
                available_tasks = available_tasks + sorted(newly_available_tasks)

        # Increment the clock and check if all workers are idle and there are no available tasks
        timing += 1
        check = [element for x in worker_assignments for element in list(worker_assignments[x])]
        if not available_tasks and all(element is None for element in check):
            print("Timing is:", timing)
            break
    return timing

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
    ordered_node_list, scheduling_order = process_nodes_in_order(nodes, directional_adjacency_matrix)

    # Calculate worker timing
    num_workers = 5
    timing = calculate_worker_timing(ordered_node_list, scheduling_order, num_workers, directional_adjacency_matrix)

    print(" ")
    print("================================================================")
    print(f"Part 1: The node order for steps is: {ordered_node_list}")
    print("================================================================")
    print(" ")

    print(" ")
    print("================================================================")
    print(f"Part 2: The timing got {num_workers} workers is: {timing}")
    print("================================================================")
    print(" ")

    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()