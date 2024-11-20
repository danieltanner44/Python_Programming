import time
import numpy as np
import matplotlib.pyplot as plt

def read_input_data(filename, number_of_steps):
    insertion_rules = {}
    with open(filename, 'r') as f:
        for each_line in f:
            if each_line.find("->") > 0:
                temp = each_line.strip().replace("-> ","").split(" ")
                insertion_rules[temp[0]] = temp[0][0]+temp[1]+temp[0][1]
            elif each_line.strip() != "":
                p_template = each_line.strip()
    print("STEP", 1)
    print(insertion_rules)
    ss_insertion_rules = insertion_rules.copy()
    # Now lets cycle our rules by the number of process steps to take
    for step in range(2,5 + 1):
        print("STEP", step)
        for key in insertion_rules:
            # key and insertion_rules[key]
            temp = ""
            for index in range(0, len(insertion_rules[key]) - 1):
                temp += ss_insertion_rules[insertion_rules[key][index:index + 2]][:-1]
            temp += insertion_rules[key][-1]
            insertion_rules[key] = temp
    return insertion_rules, p_template

def process_insertion_cycle(insertion_rules, p_template):
    updated_p_template = p_template[0]
    for index in range(0,len(p_template)-1):
        updated_p_template += insertion_rules[p_template[index:index+2]][1:]
    p_template = updated_p_template
    return p_template

def find_common_difference(p_template):
    elements = set([character for character in p_template])
    element_numbers = {element : 0 for element in elements}
    p_template = np.array(list(p_template))
    for element in elements:
        element_numbers[element] = len(np.where(p_template == element)[0])
    common_difference = max(element_numbers.values()) - min(element_numbers.values())
    return common_difference

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    number_of_steps = 8
    filename = f"D:\Python_Programming\Advent_of_Code\Advent_of_Code_2021\Day14\Puzzle_Input_d.txt"
    insertion_rules, p_template = read_input_data(filename, number_of_steps)
    print("==============================================================")
    print("The polymer template is:")
    print(p_template)
    print(" ")
    print("The insertion rules are:")
    print(insertion_rules)
    print("==============================================================")
    print(" ")
    for i in range(number_of_steps):
        print(" ")
        print("==============================================================")
        print("Processing step "+str(i+1)+":")
        p_template = process_insertion_cycle(insertion_rules, p_template)
        print("Polymer template now",str(len(p_template)),"long!")
        #print("New polymer template:",p_template)
        print("==============================================================")
        print(" ")
    common_difference = find_common_difference(p_template)
    print(" ")
    print("==============================================================")
    print("==============================================================")
    print("The common difference is:", common_difference)
    print("Polymer template now", str(len(p_template)), "long!")
    print("==============================================================")
    print("==============================================================")
    print(" ")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()