import numpy as np
import time

def read_input_data(filename):
    with open(filename, 'r') as f:
        directions = f.readline().strip().replace(" ","").split(",")
    return directions

def walking_the_grid(directions):
    direction = {"NR": "E","NL": "W", "SR": "W", "SL": "E", "ER": "S","EL": "N", "WR": "N", "WL": "S"}
    current_direction = "N"
    location = {"X" : 0, "Y" : 0}
    for step in directions:
        distance = int(step[1:])
        current_direction = direction[current_direction+step[:1]]
        if current_direction == "N":
            location["Y"] = location["Y"] + distance
        elif current_direction == "S":
            location["Y"] = location["Y"] - distance
        elif current_direction == "E":
            location["X"] = location["X"] + distance
        elif current_direction == "W":
            location["X"] = location["X"] - distance
        else:
            print("Error in directions!")
    blocks_away = abs(location["X"]) + abs(location["Y"])
    return blocks_away

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2016\Day1\Puzzle_Input.txt"
    directions = read_input_data(filename)
    print(" ")
    print("==============================================================")
    print("The input directions are:")
    print(directions)
    print("==============================================================")
    print(" ")
    blocks_away = walking_the_grid(directions)
    print("==============================================================")
    print("The number of blocks away is:", blocks_away)
    print("==============================================================")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()