import numpy as np
import time

def read_input_data(filename):
    input_numbers = []
    with open(filename, 'r') as f:
        for line in f:
            input_numbers.append(line.strip().split("\t"))
    return input_numbers

def find_checksum(input_numbers):
    checksum = 0
    for numbers in input_numbers:
        numbers = np.array(numbers, dtype=np.int16)
        difference = max(numbers) - min(numbers)
        checksum += difference
    return checksum

def find_divisible_sum(input_numbers):
    divisible_sum = 0
    for numbers in input_numbers:
        numbers = np.array(numbers, dtype=np.int16)
        divisible_numbers = [(element1, element2) for element1 in numbers for element2 in numbers if element1 % element2 == 0 and element1 != element2]
        divisible_numbers = np.array(divisible_numbers,dtype=np.int16)[0]
        result = max(divisible_numbers)//min(divisible_numbers)
        divisible_sum += result
    return divisible_sum

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2017\Day2\Puzzle_Input.txt"
    input_numbers = read_input_data(filename)
    print("The initial data is:")
    print(input_numbers)
    checksum = find_checksum(input_numbers)
    print(" ")
    print("==============================================================")
    print("The checksum in part 1 is:", checksum)
    print("==============================================================")
    print(" ")
    divisible_sum = find_divisible_sum(input_numbers)
    print(" ")
    print("==============================================================")
    print("The divisible sum in part 2 is:", divisible_sum)
    print("==============================================================")
    print(" ")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()