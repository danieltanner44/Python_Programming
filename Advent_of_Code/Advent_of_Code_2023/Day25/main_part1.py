import time
import networkx as nx
import matplotlib.pyplot as plt

def reading_input_data(fI):
    print("Reading input data...", end = "")
    connection_details = []
    for each_line in fI:
        connection_details.append(each_line.replace(":", "").strip("\n").split(" "))
    connectors_dict = set([item for sublist in connection_details for item in sublist])
    connectors_dict = dict(zip(connectors_dict, range(len(connectors_dict))))
    print("[complete]", end="\n")
    print("#########################################")
    print("The connection details are:")
    print(connection_details)
    print("#########################################")
    print("There are", len(connection_details),"components!")
    print("#########################################")
    print(" ")
    return connection_details, connectors_dict

def form_tree(connection_details, connectors_dict):
    G = nx.Graph()
    for connectors in enumerate(connection_details):
        G.add_node(connectors[1][0])
        for connector in connectors[1][1:]:
            G.add_node(connector)
            G.add_edge(connectors[1][0], connector)
    print("Details of G: ", G)
    plot_graph(G)

    print(" ")
    print("###########################################################")
    print("You will now have to input the nodes of three edges to remove")
    for i in range(1,4):
        edge_to_trim = input(str(i)+") Please enter an edge to trim, e.g., ""jqt ilh"":")
        edge_to_trim = edge_to_trim.split(" ")
        print("\t","Edge successfully removed that connects node: ", edge_to_trim)
        G.remove_edge(edge_to_trim[0], edge_to_trim[1])
    print("###########################################################")
    plot_graph(G)
    print(" ")
    num_connected_graphs = nx.number_connected_components(G)
    connected_subgraphs = list(nx.connected_components(G))
    print("###########################################################")
    print("There are " + str(num_connected_graphs) + " connected graphs of size " + str(len(connected_subgraphs[0])) + " and " + str(len(connected_subgraphs[1])))
    print("###########################################################")

    return num_connected_graphs, connected_subgraphs

def plot_graph(G):
    options = {'node_color': 'blue', 'node_size': 6000, 'width': 3, 'font_color': 'white', 'font_size': 30}
    nx.draw(G, with_labels=True, font_weight='bold', **options)
    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    plt.show()
    return

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    fI = open(r'D:\Advent_of_Code\Advent_of_Code_2023\Day25\Puzzle_Input.txt', 'r')
    # Read all of the input data from Puzzle Input and organise it
    connection_details, connectors_dict = reading_input_data(fI)
    # Let's create a tree to see how all of the components are connected
    num_connected_graphs, connected_subgraphs = form_tree(connection_details, connectors_dict)

    print(" ")
    print("###########################################################")
    print("Multiplying the size of the groups gives: " + str(len(connected_subgraphs[0])*len(connected_subgraphs[1])))
    print("###########################################################")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()