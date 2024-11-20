import numpy as np
import time

def read_input_data(filename):
    with open(filename, 'r') as f:
        initial_data = f.readline().strip()
    return initial_data

def build_travel_map(initial_data):
    travel_map = np.zeros(shape=[1000,1000], dtype=np.int8)
    current_location = (travel_map.shape[0] // 2, travel_map.shape[1] // 2)
    travel_map[current_location] = 1
    for direction in initial_data:
        if direction == "^":
            new_location = (current_location[0] - 1, current_location[1])
        elif direction == "v":
            new_location = (current_location[0] + 1, current_location[1])
        elif direction == ">":
            new_location = (current_location[0], current_location[1] + 1)
        elif direction == "<":
            new_location = (current_location[0], current_location[1] - 1)
        else:
            print("Error data incorrected!!!")
        # Check if the new location is within bounds
        if 0 <= new_location[0] < travel_map.shape[0] and 0 <= new_location[1] < travel_map.shape[1]:
            travel_map[new_location] += 1
            current_location = new_location  # Update current location
        else:
            print(f"Warning: Moving out of bounds to {new_location}")
    return travel_map

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2015\Day3\Puzzle_Input.txt"
    initial_data = read_input_data(filename)
    print("The initial data is:",initial_data)
    travel_map = build_travel_map(initial_data)
    print(" ")
    print("==============================================================")
    print("Santa visits "+str(len(np.where(travel_map >= 1)[0]))+" houses at least once!")
    print("==============================================================")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()