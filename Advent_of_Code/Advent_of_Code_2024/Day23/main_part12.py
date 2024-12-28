import time
import numpy as np
import my_modules.development
from my_modules.development import fstring

def read_input_data(filename):
    # This subroutine reads the puzzle input and forms:
    # 1) computers: a set of computers on the network
    # 2) local_network_map: a dictionary with each computer as a key and a list of all connected computers as the value
    local_network_map = {}
    computers = set()
    with open(filename, 'r') as f:
        for line in f:
            temp = line.strip().split("-")
            # Create a set of computers on the network
            if temp[0] not in computers:
                computers.add(temp[0])
            if temp[1] not in computers:
                computers.add(temp[1])
            # Create the connectivity by looking both forward and backwards
            for index in [0, 1]:
                if index == 1:
                    temp[0], temp[1] = temp[1], temp[0]
                if temp[0] in local_network_map:
                    local_network_map[temp[0]] += [temp[1]]
                else:
                    local_network_map[temp[0]] = [temp[1]]
    # Create a sorted list of all computers
    computers = sorted(computers)
    return local_network_map, computers


def find_sets_of_three_computers(computers, local_network_map):
    # Find groups of three computers that are connected together
    three_group_computers = []

    # Loop over each computer and grow out to include neighbours
    for computer in computers:
        starting_computer = computer
        processing_list = [[starting_computer]]
        # Keep growing until a viable three group is found or abandoned
        while len(processing_list) != 0:
            current_computer_group = processing_list.pop()
            current_computer = current_computer_group[-1]

            neighbours = local_network_map[current_computer]
            for neighbour in neighbours:
                if neighbour not in current_computer_group:
                    new_path = current_computer_group + [neighbour]
                    # Check if the length is 3 and the next computer is the starting one then stop
                    # Otherwise it is abandoned as it is popped
                    if len(new_path) == 3:
                        if starting_computer in local_network_map[new_path[-1]]:
                            new_path = sorted(new_path)
                            if tuple(new_path) not in three_group_computers:
                                three_group_computers.append(tuple(sorted(new_path)))
                    else:
                        processing_list.append(new_path)
    return three_group_computers


def find_possible_historian_computer(three_group_computers):
    # Run through the list of three group computers and count if
    # they have a computer starting with a "t"
    num_possible_computers = 0
    for path in three_group_computers:
        for computer in path:
            if computer[0] == "t":
                num_possible_computers += 1
                break
    return num_possible_computers


def find_max_sets_of_connected_computers(computers, local_network_map):
    longest_set_connected_computers = []
    num_longest_set_connected_computers = 0

    # Loop over each computer
    # For each loop over all of its connected computers
    # Create a connectivity matrix between them all
    for index, computer in enumerate(computers):
        connected_list = sorted(local_network_map[computer] + [computer])
        # Find the largest group that are all connected to each other
        connectivity_matrix = []
        for computer1 in connected_list:
            computer_connectivity = []
            for computer2 in connected_list:
                if computer1 != computer2:
                    if computer1 in local_network_map[computer2]:
                        # A value of 1 indicates two computers are connected
                        computer_connectivity.extend([1])
                    else:
                        # A value of 0 indicates two computers are not connected
                        computer_connectivity.extend([0])
                else:
                    # A value of X indicates two computers are the same
                    computer_connectivity.extend(["X"])
            connectivity_matrix.append(computer_connectivity)
        # Build the final connectivity matrix
        connectivity_matrix = np.array(connectivity_matrix)

        # Now cull computers that are not connected to all other computers
        while True:
            # Find zeros where computers are not connected
            zeros = np.where(connectivity_matrix == "0")
            rows = my_modules.development.determine_num_duplicates_in_list(list(zeros[0]))
            cols = my_modules.development.determine_num_duplicates_in_list(list(zeros[1]))
            # Find the row/col indices with the largest number of 0s and remove them first
            max_row = max(rows, key=rows.get)
            max_col = max(cols, key=cols.get)
            connectivity_matrix = np.delete(connectivity_matrix, max_row, axis=0)
            connectivity_matrix = np.delete(connectivity_matrix, max_col, axis=1)
            # Also remove the associated computer name from the connected list
            connected_list.pop(max_col)
            # Check if there are more zeros, if not break loop
            num_zeros = len(np.where(connectivity_matrix == "0")[0])
            if num_zeros != 0:
                continue
            else:
                break

        print(f"Connected group found with {len(connected_list)} computers: {connected_list}")
        # Store the details of the longest sorted list of connected computers
        if len(connected_list) > num_longest_set_connected_computers:
            num_longest_set_connected_computers = len(connected_list)
            longest_set_connected_computers = connected_list

    return num_longest_set_connected_computers, longest_set_connected_computers


def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2024\Day23\Puzzle_Input.txt"
    local_network_map, computers = read_input_data(filename)

    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=======================  Puzzle Input  =======================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"There are {len(computers)} computers on the network, namely: ", "bk", "wt"))
    print(computers)
    print(fstring(f"The computer connectivity on the network is: ", "bk", "wt"))
    [print(computer, connected_computers) for computer, connected_computers in local_network_map.items()]
    print(fstring(f"====================  Puzzle Input - End =====================", "bk", "bl"))

    print(" ", end="\n\n")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=========================  PART ONE  =========================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))

    three_group_computers = find_sets_of_three_computers(computers, local_network_map)
    num_possible_computers = find_possible_historian_computer(three_group_computers)
    part_one_ans = str(num_possible_computers)

    print(fstring(f"Found {len(three_group_computers)} sub groups of three computers, namely: ", "bk", "wt"))
    [print(three_group_computer) for three_group_computer in three_group_computers]
    print(fstring(f"These have {num_possible_computers} groups that have a computer starting with a \"t\". ", "bk", "wt"))

    print(fstring(f"======================  PART ONE - END  ======================", "bk", "bl"))

    print(" ", end="\n\n")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=========================  PART TWO  =========================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"Processing connected groups... ", "bk", "wt"))

    num_longest_set_connected_computers, longest_set_connected_computers = find_max_sets_of_connected_computers(computers, local_network_map)
    string_of_computers = ",".join(longest_set_connected_computers)
    part_two_ans = str(string_of_computers)

    print(fstring(f"Largest connected group has {num_longest_set_connected_computers} computers, namely: ", "bk", "wt"))
    print(longest_set_connected_computers)
    print(fstring(f"======================  PART TWO - END  ======================", "bk", "bl"))

    print(" ", end="\n\n")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=========================  ANSWERS  ==========================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))
    print(f'{fstring("Part One:", "bk", "wt")}')
    print(f'Number of 3 connected groups with a \"t\" computer: {fstring(part_one_ans, "wt", "bk")}')
    print(fstring(f"==============================================================", "bk", "bl"))
    print(f'{fstring("Part Two:", "bk", "wt")}')
    print(f'The LAN party password is: {fstring(part_two_ans, "wt", "bk")}')
    print(fstring(f"==============================================================", "bk", "bl"))
    print(" ")

    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()