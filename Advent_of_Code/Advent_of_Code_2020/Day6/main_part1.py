import numpy as np
import time
import my_modules.development as mmd

def read_input_data(filename):
    input_data = []
    temp = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                temp.append(line)
            else:
                input_data.append(temp)
                temp = []
        input_data.append(temp)
    return input_data

def process_questions(input_data):
    unique_answer_counts = []
    everyone_answered_counter = 0
    for group in input_data:
        group_size = len(group)
        temp = ""

        # Part 1 Logic
        for responses in group:
            temp += responses
        unique_answer_counts.append(len(set(list(temp))))

        # Part 2 Logic
        duplicate_dict = count_list_duplicates(temp)
        everyone_answered_counter += len([key for key, value in duplicate_dict.items() if value == group_size])

    sum_of_counts = sum(unique_answer_counts)
    return sum_of_counts, everyone_answered_counter

def count_list_duplicates(string):
    elements = np.array(sorted(list(string)))
    unique_elements = list(set(elements))
    duplicate_dict = {element : 0 for element in unique_elements}
    for element in unique_elements:
        duplicate_dict[element] = len(np.where(elements == element)[0])
    return duplicate_dict

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2020\Day6\Puzzle_Input.txt"
    input_data = read_input_data(filename)
    print("The initial data covers answers from " + str(len(input_data)) + " groups:")
    print(input_data)
    sum_of_counts, everyone_answered_counter = process_questions(input_data)


    print(" ")
    print("==============================================================")
    print("PART 1: The sum of anyone counts is:", sum_of_counts)
    print("==============================================================")
    print(" ")
    print(" ")
    print("==============================================================")
    print("PART 2: The sum of everyone counts is:", everyone_answered_counter)
    print("==============================================================")
    print(" ")

    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()