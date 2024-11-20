import numpy as np
import time
import my_modules.development as md

def read_input_data(filename):
    with open(filename, 'r') as f:
        input_number = f.readline().strip()
    return int(input_number)

def process_accumulation(size, input_number):
    # Ensure size is odd for centering
    if size % 2 == 0:
        size += 1

    accumulation_spiral = np.zeros((size, size), dtype=np.int32)

    # Counterclockwise (left turn after each side)
    changing_direction = {"R": "U", "U": "L", "L": "D", "D": "R"}
    direction = "D"  # Start moving to the right

    # Initialize spiral array and starting values
    location = (size // 2, size // 2)
    accumulation_spiral[location] = 1 # Start at 1 in middle of accumulation spiral
    current_number = 1
    current_accumulation_number = 0

    # Begin spiral generation
    side_length = 0
    while current_number < size ** 2:
        side_length += 1
        for _ in range(2):  # Each side length occurs twice
            direction = changing_direction[direction]  # Update direction
            for _ in range(side_length):
                current_number += 1
                print(accumulation_spiral)
                if current_accumulation_number > input_number:
                    return current_accumulation_number, accumulation_spiral, "Number threshold reached"

                # Update location based on direction
                if direction == "R":
                    location = (location[0], location[1] + 1)
                elif direction == "U":
                    location = (location[0] - 1, location[1])
                elif direction == "L":
                    location = (location[0], location[1] - 1)
                elif direction == "D":
                    location = (location[0] + 1, location[1])

                # Add surrounding elements to current entry on spiral
                current_accumulation_number = np.sum(accumulation_spiral[location[0] - 1 : location[0] + 2,location[1] - 1 : location[1] + 2])
                accumulation_spiral[location] = current_accumulation_number

    return current_accumulation_number, accumulation_spiral, "Spiral filled but number threshold not reached"

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2017\Day3\Puzzle_Input.txt"
    input_number = read_input_data(filename)
    print("The initial number is:")
    print(input_number)
    size = 13 # Set side length for ulam spiral
    current_accumulation_number, accumulation_spiral, message = process_accumulation(size, input_number)

    print(" ")
    print("==============================================================")
    print("The accumulated Ulam spiral is:")
    print(accumulation_spiral)
    print("==============================================================")
    print(" ")

    print(" ")
    print("==============================================================")
    print("The first value written that is larger than", input_number, "is:", current_accumulation_number)
    print("Note: "+message)
    print("==============================================================")
    print(" ")

    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()