import numpy as np
import time

def read_input_data(filename):
    initial_data = []
    with open(filename, 'r') as f:
        for line in f:
            temp = line.strip()
            initial_data.append(temp)
    initial_data = np.array(initial_data, dtype=np.str_)
    return initial_data

def process_input_strings(initial_data):
    number_nice_strings = 0
    for line in initial_data:

        # Check for repeated letter with one letter in middle
        contains_repeat_letter = False
        for index, character in enumerate(line[:-2]):
            if character == line[index + 2]:
                contains_repeat_letter = True
                break

        # Check for repeated pairs of letters
        contains_repeat_pair = False
        pairs = [line[index:index+2] for index in range(len(line)-1)]
        for pair in pairs:
            if line.rfind(pair) - line.find(pair) > 1: # Found repeats
                contains_repeat_pair = True
                break

        # Check for nice strings
        if contains_repeat_letter is True and contains_repeat_pair is True:
            number_nice_strings += 1
            print(line, " GOOD")
        else:
            print(line, " BAD")

    return number_nice_strings

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2015\Day5\Puzzle_Input.txt"
    initial_data = read_input_data(filename)
    print("The initial data is:")
    print(initial_data)
    number_of_nice_strings = process_input_strings(initial_data)
    print(" ")
    print("==============================================================")
    print("The number of nice strings is:",number_of_nice_strings)
    print("==============================================================")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()