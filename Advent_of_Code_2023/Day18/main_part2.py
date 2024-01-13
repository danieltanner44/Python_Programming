import numpy as np
import time
import math
from matplotlib import pyplot as plt


def reading_input_data(fI):
    data = []
    print("Reading block of input data...")
    for each_line in fI:
        each_line = (each_line.strip("\n")).split(" ")[:]
        each_line[2] = each_line[2].strip("(").strip(")").strip("#")
        temp = each_line[2]
        each_line[1] = int(str(temp[0:len(temp)-1]), 16)
        direction = int(temp[len(temp)-1:len(temp)])
        if direction == 0:
            each_line[0] = "R"
        elif direction == 1:
            each_line[0] = "D"
        elif direction == 2:
            each_line[0] = "L"
        elif direction == 3:
            each_line[0] = "U"
        data.append(each_line)
    data = np.array(data)
    print("################################")
    print("The data has been read and structured")
    print(" ")
    print("The input array has:", len(data), "elements!")
    print("################################")
    return data

def get_trench_coordinates(data):
    boundary_vertices = [[0,0]]
    perimeter = 0
    for i in range(np.shape(data)[0]):
        if data[i][0] == "D":
            boundary_vertices.append([boundary_vertices[i][0], boundary_vertices[i][1] - int(data[i][1])])
            perimeter += math.sqrt(((boundary_vertices[i][0] - boundary_vertices[i-1][0])**2 + (boundary_vertices[i][1] - boundary_vertices[i-1][1])**2))
        elif data[i][0] == "U":
            boundary_vertices.append([boundary_vertices[i][0], boundary_vertices[i][1] + int(data[i][1])])
            perimeter += math.sqrt(((boundary_vertices[i][0] - boundary_vertices[i - 1][0]) ** 2 + (boundary_vertices[i][1] - boundary_vertices[i - 1][1]) ** 2))
        elif data[i][0] == "R":
            boundary_vertices.append([boundary_vertices[i][0] + int(data[i][1]), boundary_vertices[i][1]])
            perimeter += math.sqrt(((boundary_vertices[i][0] - boundary_vertices[i - 1][0]) ** 2 + (boundary_vertices[i][1] - boundary_vertices[i - 1][1]) ** 2))
        elif data[i][0] == "L":
            boundary_vertices.append([boundary_vertices[i][0] - int(data[i][1]), boundary_vertices[i][1]])
            perimeter += math.sqrt(((boundary_vertices[i][0] - boundary_vertices[i - 1][0]) ** 2 + (boundary_vertices[i][1] - boundary_vertices[i - 1][1]) ** 2))
    print("Perimeter:", perimeter)
    # Plot the boundary for a QC check
    only_once = False
    for vertex in boundary_vertices:
        if only_once == False:
            x, y = np.array(boundary_vertices[0][0]), np.array(boundary_vertices[0][1])
            only_once = True
        else:
            x = np.append(x, vertex[0])
            y = np.append(y, vertex[1])
    plt.plot(x, y, 'r-')
    # Inflate boundary to lasso full squares and not just their centers
    delta = 0.5
    for i in range(np.shape(data)[0]):
        # External corners
        if data[i-1][0] == "R" and data[i][0] == "D": # 7
            boundary_vertices[i] = [boundary_vertices[i][0] + delta, boundary_vertices[i][1] + delta]
        elif data[i - 1][0] == "D" and data[i][0] == "L":  # J
            boundary_vertices[i] = [boundary_vertices[i][0] + delta, boundary_vertices[i][1] - delta]
        elif data[i - 1][0] == "L" and data[i][0] == "U":  # L
            boundary_vertices[i] = [boundary_vertices[i][0] - delta, boundary_vertices[i][1] - delta]
        elif data[i - 1][0] == "U" and data[i][0] == "R":  # F
            boundary_vertices[i] = [boundary_vertices[i][0] - delta, boundary_vertices[i][1] + delta]
        # Internal corners
        elif data[i-1][0] == "U" and data[i][0] == "L": # 7
            boundary_vertices[i] = [boundary_vertices[i][0] - delta, boundary_vertices[i][1] - delta]
        elif data[i - 1][0] == "R" and data[i][0] == "U":  # J
            boundary_vertices[i] = [boundary_vertices[i][0] - delta, boundary_vertices[i][1] + delta]
        elif data[i - 1][0] == "D" and data[i][0] == "R":  # L
            boundary_vertices[i] = [boundary_vertices[i][0] + delta, boundary_vertices[i][1] + delta]
        elif data[i - 1][0] == "L" and data[i][0] == "D":  # F
            boundary_vertices[i] = [boundary_vertices[i][0] + delta, boundary_vertices[i][1] - delta]
    boundary_vertices[np.shape(data)[0]] = boundary_vertices[0]
    # plot inflated boundary too
    only_once = False
    for vertex in boundary_vertices:
        if only_once == False:
            x, y = np.array(boundary_vertices[0][0]), np.array(boundary_vertices[0][1])
            only_once = True
        else:
            x = np.append(x, vertex[0])
            y = np.append(y, vertex[1])
    plt.plot(x, y, 'r-')
    plt.axis('equal')
    plt.grid(True, which='both', linestyle='-', linewidth=1)
    plt.show()
    return boundary_vertices

def get_trench_area(boundary_vertices):
    trench_area = 0
    boundary_vertices = np.array(boundary_vertices, dtype=float)
    # Using this algorithm for area of a non-intersecting polygon - Triangle formula - https://en.wikipedia.org/wiki/Shoelace_formula
    for i in range(len(boundary_vertices) - 1):
        trench_area += ((boundary_vertices[i][0]*boundary_vertices[i+1][1]) - (boundary_vertices[i+1][0]*boundary_vertices[i][1]))/2
    trench_area = int(abs(trench_area))
    return trench_area

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    fI = open(r'D:\Advent_of_Code\Advent_of_Code_2023\Day18\Puzzle_Input.txt', 'r')
    # Read all of the input data from Puzzle Input and organise it
    data = reading_input_data(fI)
    # Now lets dig the trench
    boundary_vertices = get_trench_coordinates(data)
    # Lets calculate the area
    trench_area = get_trench_area(boundary_vertices)
    print("The total volume is:", trench_area)
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()