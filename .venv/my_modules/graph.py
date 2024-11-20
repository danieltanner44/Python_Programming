def create_adjacency_matrix(nodes, edges):
    """
    Creates an adjacency matrix from a list of nodes and edges.

    Args:
        nodes (list): A list of nodes.
        edges (list): A list of tuples representing edges,
                      where each tuple contains two nodes (e.g., [(node1, node2), (node2, node3)]).

    Returns:
        dict: A dictionary representing the adjacency matrix,
              where each node maps to a list of its connected nodes.

    Raises:
        ValueError: If nodes or edges are not of the correct type or if any edges refer to invalid nodes.

    Example:
        nodes = ['A', 'B', 'C']
        edges = [('A', 'B'), ('B', 'C'), ('A', 'C')]

        adjacency_matrix = create_adjacency_matrix(nodes, edges)
        print(adjacency_matrix)  # Output: {'A': ['B', 'C'], 'B': ['A', 'C'], 'C': ['B', 'A']}
    """
    # Input validation
    if not isinstance(nodes, list) or not all(isinstance(node, str) for node in nodes):
        raise ValueError("Nodes must be a list of strings.")

    if not isinstance(edges, list) or not all(isinstance(edge, tuple) and len(edge) == 2 for edge in edges):
        raise ValueError("Edges must be a list of tuples, each containing two nodes.")

    for node1, node2 in edges:
        if node1 not in nodes or node2 not in nodes:
            raise ValueError(f"Edge ({node1}, {node2}) refers to invalid nodes.")

    print("\n==============================================")
    print("Creating adjacency matrix ...", end="\r")
    adjacency_matrix = {node: set() for node in nodes}  # Use a set for unique neighbors
    
    # Populate the adjacency matrix
    for edge in edges:
        node1, node2 = edge
        if node1 in adjacency_matrix:
            adjacency_matrix[node1].add(node2)
        if node2 in adjacency_matrix:
            adjacency_matrix[node2].add(node1)
            
    # Convert sets back to lists and print completion
    for node in adjacency_matrix:
        adjacency_matrix[node] = list(adjacency_matrix[node])

    print("complete\n")
    print("==============================================")
    return adjacency_matrix

def create_directional_adjacency_matirx(edges):
    """
        Create a directional adjacency matrix from a list of edges.

        Args:
            edges: List of directed edges, where each edge is a tuple (source, target).

        Returns:
            A dictionary where each key is a node, and the value is a list:
            - The first element is a list of parent nodes (incoming edges).
            - The second element is a list of child nodes (outgoing edges).

        Raises:
            ValueError: If any of the following conditions are met:
                - If edges are not a list of tuples.
                - If tuples do not contain a pair of nodes (i.e., does not have exactly two elements).

        Example:
            >>> edges = [(A, B), (B, C), (C, D), (D, A)]
            >>> adjacency_matrix = create_directional_adjacency(edges)
            >>> print(adjacency_matrix)
            {
                A: [[D], [B]],  # Node A: Parent [D], Child [B]
                B: [[A], [C]],  # Node B: Parent [A], Child [C]
                2: [[B], [D]],  # Node C: Parent [B], Child [D]
                3: [[C], [A]]   # Node D: Parent [C], Child [A]
            }
        """
    # Input validation
    if not isinstance(edges, list) or not all(isinstance(edge, tuple) and len(edge) == 2 for edge in edges):
        raise ValueError("Edges must be a list of tuples, each containing two nodes.")

    # Create the directional adjacency matrix
    nodes = sorted(set([x for y in edges for x in y]))
    directional_adjacency_matrix = {node : [[],[]] for node in nodes}
    for edge in edges:
        directional_adjacency_matrix[edge[1]][0].append(edge[0])
        directional_adjacency_matrix[edge[0]][1].append(edge[1])
    return directional_adjacency_matrix

def find_all_paths(start_point, end_point, allowable_visits, nodes, adjacency_matrix):
    """
        Find all paths from start_point to end_point in a graph represented by an adjacency matrix.

        Parameters:
        - start_point: The node where the search starts.
        - end_point: The node where the search should end.
        - allowable_visits: A dictionary specifying the maximum number of times each node can be visited.
        - nodes: A list of all nodes in the graph.
        - adjacency_matrix: A dictionary mapping each node to a list of its neighbors.

        Returns:
        - A list of paths, where each path is represented as a list of nodes.

        Raises:
            ValueError: If any of the following conditions are met:
                - start_point is not a string.
                - end_point is not a string.
                - allowable_visits is not a dictionary.
                - nodes is not a list of strings or is empty.
                - adjacency_matrix is not a dictionary.
                - start_point or end_point is not in the nodes list.
                - any node in nodes is missing in allowable_visits or adjacency_matrix.
                - any entry in adjacency_matrix is not a list of neighbors for the corresponding node.

        Example:
            nodes = ['A', 'B', 'C', 'D', 'end']
            allowable_visits = {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'end': 1}
            adjacency_matrix = {
                'A': ['B', 'C'],
                'B': ['A', 'D'],
                'C': ['A', 'D'],
                'D': ['B', 'C', 'end'],
                'end': []
            }

            all_paths = find_all_paths('A', 'end', allowable_visits, nodes, adjacency_matrix)
            print("All paths found:", all_paths)
        """

    # Input checks
    if not isinstance(start_point, str):
        raise ValueError("start_point must be a string representing a node.")
    if not isinstance(end_point, str):
        raise ValueError("end_point must be a string representing a node.")
    if not isinstance(allowable_visits, dict):
        raise ValueError("allowable_visits must be a dictionary.")
    if not isinstance(nodes, list):
        raise ValueError("nodes must be a list.")
    if not isinstance(adjacency_matrix, dict):
        raise ValueError("adjacency_matrix must be a dictionary.")

    if not nodes:
        raise ValueError("The nodes list cannot be empty.")
    if start_point not in nodes:
        raise ValueError(f"The start_point '{start_point}' must be in the nodes list.")
    if end_point not in nodes:
        raise ValueError(f"The end_point '{end_point}' must be in the nodes list.")

    for node in nodes:
        if node not in allowable_visits:
            raise ValueError(f"Each node must have an entry in allowable_visits. Missing: {node}")
        if node not in adjacency_matrix:
            raise ValueError(f"Each node must have an entry in the adjacency_matrix. Missing: {node}")
        if not isinstance(adjacency_matrix[node], list):
            raise ValueError(f"Each entry in the adjacency_matrix must be a list of neighbors for node '{node}'.")

    print("\n==============================================")
    print("Finding all paths between", start_point, "and", end_point, "...", "\r")

    all_paths = []
    queued_paths = [[start_point]]  # Initialize with the starting node
    visited_nodes = [{node: 0 for node in nodes}]  # Track visited nodes as a dictionary
    while queued_paths:
        queue = queued_paths.pop(0)  # Get and remove the first path
        current_visited_nodes = visited_nodes[0]  # Get the visited nodes
        # If the last node in the current path is not the end point
        if queue[-1] != end_point:
            current_node = queue[-1]
            current_visited_nodes[current_node] += 1 # Mark the current node as visited once

            # Explore neighbours
            for neighbour in adjacency_matrix[current_node]:
                # Check if the neighbour can be visited
                if ((current_visited_nodes[neighbour] < allowable_visits[neighbour]) or
                        allowable_visits[neighbour] < 0):  # If neighbour is not visited or revisitable
                    temp_queue = queue + [neighbour]  # Create a new path that includes neighbour
                    queued_paths.append(temp_queue)  # Add new path to the queue
                    visited_nodes.append(current_visited_nodes.copy())  # Copy visited state
        else:
            # Found a path that ends at the endpoint
            all_paths.append(queue)
        # Remove the current visited node state (if needed)
        visited_nodes.pop(0)
    print("complete\n")
    print("==============================================")
    return all_paths