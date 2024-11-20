import time
import numpy as np
import my_modules.development as mmd

def read_input_data(filename):
    with open(filename, 'r') as f:
        for line in f:
            input_range = line.strip().split("-")
    return input_range

def process_combinations(input_range):
    valid_passcode_counter = 0
    # As in range must be six digit number and in require range
    for pass_candidate in range(int(input_range[0]), int(input_range[1]) + 1):
        duplicate_found = False
        monotonically_increasing = False
        monotonically_increasing_counter = 0
        pass_candidate = [int(digit) for digit in str(pass_candidate)]
        for j, digit in enumerate(pass_candidate[:-1]):
            if digit == pass_candidate[j + 1] and duplicate_found == False:
                # Duplicate adjacent digit found
                duplicate_found = True
            if digit <= pass_candidate[j + 1]:
                monotonically_increasing_counter += 1
                if monotonically_increasing_counter == 5:
                    # Candidate passcode is monotonically increasing
                    monotonically_increasing = True

        if duplicate_found == True and monotonically_increasing == True:
            # Valid passcode found
            valid_passcode_counter += 1
    return valid_passcode_counter

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2019\Day4\Puzzle_Input.txt"
    input_range = read_input_data(filename)

    print(" ")
    print("==============================================================")
    print("The input range is:")
    print(input_range)
    print("==============================================================")
    print(" ")

    number_of_valid_passcodes = process_combinations(input_range)

    print(" ")
    print("==============================================================")
    print("PART 1: The number of valid passcodes is:", number_of_valid_passcodes)
    print("==============================================================")
    print(" ")

    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()