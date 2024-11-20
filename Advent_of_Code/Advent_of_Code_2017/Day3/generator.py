import numpy as np
import time

def generate_ulam_spiral(size, handedness):
    if handedness in ["Left", "left", "l", "L"]:
        # For processing left turns
        changing_direction = {"R" : "U", "U" : "L", "L" : "D", "D" : "R"}
        # Set initial direction
        direction = "D"
    elif handedness in ["Right", "right", "R", "r"]:
        # For processing right turns
        changing_direction = {"R": "D", "U": "R", "L": "U", "D": "L"}
        # Set initial direction
        direction = "U"
    # Make sure that size of spiral has odd length sides so it is centered
    if size % 2 == 0:
        size += 1
    ulam_spiral = np.zeros(shape=[size, size], dtype=np.int16)
    # Set the center where it starts
    location = ((size - 1)//2, (size - 1)//2)
    current_number = 1
    ulam_spiral[location] = current_number
    side_length = 0
    while True:
        side_length += 1 # The side length increases by 1 every two cycles
        for i in range(2): # Each side length occurs twice
            direction = changing_direction[direction] # There is a direction changes after each side lenght
            for j in range(1,side_length+1):
                current_number += 1
                if direction == "R":
                    location = (location[0], location[1] + 1)
                elif direction == "U":
                    location = (location[0] - 1, location[1])
                elif direction == "L":
                    location = (location[0], location[1] - 1)
                elif direction == "D":
                    location = (location[0] + 1, location[1])
                ulam_spiral[location] = current_number
                if current_number == size ** 2:
                    return ulam_spiral
    return ulam_spiral

def main():
    size = 15
    ulam_spiral = generate_ulam_spiral(size, "R")

    print(" ")
    print(ulam_spiral)
    print("==============================================================")
    print("The checksum in part 1 is:", 0)
    print("==============================================================")
    print(" ")

    print(" ")
    print("==============================================================")
    print("The divisible sum in part 2 is:", 0)
    print("==============================================================")
    print(" ")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()