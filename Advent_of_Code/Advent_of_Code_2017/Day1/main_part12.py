import numpy as np
import time

def read_input_data(filename):
    with open(filename, 'r') as f:
        input_sequence = list(f.readline().strip())
    return input_sequence

def find_digit_sum(input_sequence, shift):
    sequence = input_sequence.copy()
    digit_sum = 0
    number_of_digits = len(sequence)
    # Wrap ends of input sequence
    sequence.append(sequence[0])
    for index, digit in enumerate(sequence[:-1]):
        check_index = (index + shift) % number_of_digits
        if digit == sequence[check_index]:
            digit_sum += int(digit)
    return digit_sum

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2017\Day1\Puzzle_Input.txt"
    input_sequence = read_input_data(filename)
    print("The initial data is:")
    print(input_sequence)
    part1_digit_sum = find_digit_sum(input_sequence, 1)
    print(" ")
    print("==============================================================")
    print("The required digit sum for part 1 is:", part1_digit_sum)
    print("==============================================================")
    print(" ")
    part2_digit_sum = find_digit_sum(input_sequence, len(input_sequence)//2)
    print("==============================================================")
    print("The required digit sum for part 1 is:", part2_digit_sum)
    print("==============================================================")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()