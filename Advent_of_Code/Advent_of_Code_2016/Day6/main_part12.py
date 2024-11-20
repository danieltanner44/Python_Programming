import numpy as np
import time
import hashlib
from collections import Counter

def read_input_data(filename):
    input_messages = []
    with open(filename, 'r') as f:
        for line in f:
            input_messages.append(list(line.strip()))
    input_messages = np.array(input_messages, np.str_)
    input_messages = input_messages.T
    return input_messages

def find_duplicate_counts(input_messages):
    element_counters = []
    min_code = ""
    max_code = ""
    for row in input_messages:
        count = {}
        elements = list(set(row))
        for element in elements:
            count[element] = len(np.where(row == element)[0])
        element_counters.append(count)
        max_key = max(count, key = count.get)
        min_key = min(count, key = count.get)
        max_code += max_key
        min_code += min_key
    return min_code, max_code

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2016\Day6\Puzzle_Input.txt"
    input_messages = read_input_data(filename)
    print(" ")
    print("==============================================================")
    print("The input messages are:")
    print(input_messages)
    print("==============================================================")
    print(" ")
    min_code, max_code = find_duplicate_counts(input_messages)
    print(" ")
    print("==============================================================")
    print("PART 1: The decrypted message is:", max_code)
    print("==============================================================")
    print(" ")
    print(" ")
    print("==============================================================")
    print("PART 2: The decrypted message is:", min_code)
    print("==============================================================")
    print(" ")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()