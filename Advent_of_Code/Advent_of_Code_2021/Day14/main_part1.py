import time
import numpy as np
import matplotlib.pyplot as plt

def read_input_data(filename):
    insertion_rules = {}
    with open(filename, 'r') as f:
        for each_line in f:
            if each_line.find("->") > 0:
                temp = each_line.strip().replace("-> ","").split(" ")
                insertion_rules[temp[0]] = temp[1]
            elif each_line.strip() != "":
                p_template = each_line.strip()
    return insertion_rules, p_template

def process_insertion_cycle(insertion_rules, p_template):
    updated_p_template = ""
    for index in range(0,len(p_template)-1):
        updated_p_template += p_template[index]
        updated_p_template += insertion_rules[p_template[index:index+2]]
    updated_p_template += p_template[-1]
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
    filename = f"D:\Python_Programming\Advent_of_Code\Advent_of_Code_2021\Day14\Puzzle_Input.txt"
    insertion_rules, p_template = read_input_data(filename)
    print("==============================================================")
    print("The polymer template is:")
    print(p_template)
    print(" ")
    print("The insertion rules are:")
    print(insertion_rules)
    print("==============================================================")
    print(" ")
    for i in range(10):
        print(" ")
        print("==============================================================")
        print("Processing step "+str(i+1)+":")
        p_template = process_insertion_cycle(insertion_rules, p_template)
        print("Polymer template now",str(len(p_template)),"long!")
        print("New polymer template:",p_template)
        print("==============================================================")
        print(" ")
    common_difference = find_common_difference(p_template)
    print(" ")
    print("==============================================================")
    print("==============================================================")
    print("The common difference is:", common_difference)
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