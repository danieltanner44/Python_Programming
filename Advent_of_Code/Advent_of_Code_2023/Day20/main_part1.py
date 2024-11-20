import time
import numpy as np

def reading_input_data(fI):
    print("Reading input data...", end = "")
    data = []
    for each_line in fI:
        print(each_line)
        each_line = each_line.replace(" -> ", " ").replace(",","").strip("\n").split(" ")
        data.append(each_line)
    print("[complete]", end="\n")
    print("#########################################")
    print("The initial data is:")
    print(data)
    print("#########################################")
    print("The data has length:", len(data))
    print("#########################################")
    print(" ")
    return data

def create_dictionary(data):
    module_dict = {} # Create a dictionary to return an modules index based on its name
    module_dict_letter = {}  # Create a dictionary to return an modules index based on its name
    for line in enumerate(data):
        for element in line[1]:
            if element == "broadcaster":
                broadcaster_index = line[0]
                break
            elif element[0] == "%" or element[0] == "&":
                module_dict[element] = line[0]
                module_dict_letter[element[1:]] = element
    return module_dict, module_dict_letter, broadcaster_index

def process_signals(data, module_dict, module_dict_letter, broadcaster_index):
    temp = []
    module_input_state = np.ones([len(module_dict), 1], dtype=int) * 8
    module_previous_state = np.ones([len(module_dict), 1], dtype=int) * 8
    module_current_state = np.ones([len(module_dict), 1], dtype=int) * 8
    # Button pressed sends low signal to broadcaster
    print("Button low -> broadcaster")
    for element in enumerate(data[broadcaster_index][1:]):
        index = module_dict[module_dict_letter[element[1]]]
        module_previous_state[index] = 0 # Set connected modules to low
        for key, value in module_dict.items():
            if value == index:
                temp.append([key, 0]) # Downstream module and output signal that module receives
                break
    # Initialise States - could probable just use np.zeros as all initialised to 0
    for module in enumerate(data):
        if module[0] != broadcaster_index:
            if module[0] == "&":
                module_previous_state[module[0]] = 0 # Set to low initially
            elif module[0] == "%":
                module_previous_state[module[0]] = 0  # Set to low initially
        else:
            continue # Skip the broadcaster state

    # Start sending out the signals from module to module
    while len(temp) != 0:
        # Step through all currently stored downstream modules
        for module in temp:
            if module[0][0] == "&":

                print("")
            elif module[0][0] == "%":
                if module[1] == 0: # Switch state
                    module_current_state[module_dict[module[0]]] = (module_previous_state[module_dict[module[0]]] + 1) % 2  # Flip state
                    print(module[0], "->", module_current_state[module_dict[module[0]]][0])
                else:
                    module_current_state[module_dict[module[0]]] = module_previous_state[module_dict[module[0]]]  # Maintain existing state
                    print(module[0], "->", module_current_state[module_dict[module[0]]][0])
                # For each of these lets add the next downstream modules to temp
                for items in data[module_dict[module[0]]][1:]:
                    for element in enumerate(data[module_dict[module[0]]][1:]):
                        temp.append([module_dict_letter[element[1]], module_current_state[module_dict[module[0]]]])
            del temp[0]






    return

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    fI = open(r'D:\Advent_of_Code\Advent_of_Code_2023\Day20\Puzzle_Input_d.txt', 'r')
    # STEP 1: Read all of the input data from Puzzle Input and organise it
    data = reading_input_data(fI)
    # STEP 2: Create a dictionary to convert connection names with unique indices
    module_dict, module_dict_letter, broadcaster_index = create_dictionary(data)

    # STEP 3: Process the signals on button press
    answer = process_signals(data, module_dict, module_dict_letter, broadcaster_index)

    print(" ")
    print("#########################################################")
    print(" ")
    print("#########################################################")
    print("The number of disintegratable bricks is:", 0)
    print("#########################################################")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()