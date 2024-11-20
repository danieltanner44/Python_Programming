import numpy as np
import hashlib
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
        line_array = np.array(list(line),dtype=np.str_)
        # Find the number of vowels
        number_vowels = len(np.where( (line_array == "a") |
                                      (line_array == "e") |
                                      (line_array == "i") |
                                      (line_array == "o") |
                                      (line_array == "u"))[0])

        # Check for repeated letter
        contains_repeat_letter = False
        for index, character in enumerate(line[:-1]):
            if character == line[index+1]:
                contains_repeat_letter = True
                break

        # Find the number of vowels
        bad_strings = ["ab","cd","pq","xy"]
        contains_bad_substring = any(bad in line for bad in bad_strings)

        # Check for nice strings
        if number_vowels >= 3 and contains_repeat_letter > 0 and contains_bad_substring == False:
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
    print("The initial data is:",initial_data)
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