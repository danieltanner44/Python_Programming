import numpy as np
import time

def read_input_data(filename):
    triangles = []
    with open(filename, 'r') as f:
        for line in f:
            triangles.append(line.strip().split())
    triangles = np.array(triangles, dtype=np.int16)
    return triangles

def assess_triangles(triangles):
    count_good_triangles = 0
    for triangle in triangles:
        triangle_to_check = sorted(triangle)
        if sum(triangle_to_check[:2]) > triangle_to_check[2]:
            count_good_triangles += 1
    return count_good_triangles

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2016\Day3\Puzzle_Input.txt"
    triangles = read_input_data(filename)
    print(" ")
    print("==============================================================")
    print("The input triangles are:")
    print(triangles)
    print("==============================================================")
    print(" ")
    count_good_triangles = assess_triangles(triangles)
    print("==============================================================")
    print("The number of good triangles is:", count_good_triangles)
    print("==============================================================")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()