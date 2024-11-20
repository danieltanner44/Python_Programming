import time
import numpy as np
import my_modules.development as mmd

def read_input_data(filename):
    input_sequence = []
    with open(filename, 'r') as f:
        for index, line in enumerate(f):
            input_sequence.append(line.strip().split(","))
    return input_sequence

def process_movement(input_sequence):
    starting_location = (0,0)
    total_distance = [[0],[0]]
    coordinates = []
    for n in range(2):
        temp_coordinates = [starting_location]
        for direction in input_sequence[n]:
            if direction[0] == "R":
                location = (temp_coordinates[-1][0], temp_coordinates[-1][1] + int(direction[1:]))
            elif direction[0] == "L":
                location = (temp_coordinates[-1][0], temp_coordinates[-1][1] - int(direction[1:]))
            elif direction[0] == "U":
                location = (temp_coordinates[-1][0] - int(direction[1:]), temp_coordinates[-1][1])
            elif direction[0] == "D":
                location = (temp_coordinates[-1][0] + int(direction[1:]), temp_coordinates[-1][1])
            # Record the accumulating track length for both journeys
            total_distance[n].append(total_distance[n][-1] + int(direction[1:]))
            temp_coordinates.append(location)
        coordinates.append(temp_coordinates)
    return coordinates, total_distance

def check_for_intersection(coordinates, total_distance):
    print(total_distance)
    min_manhattan_distance = 0
    min_track_length = 0
    for i, coord_a in enumerate(coordinates[0][:-1]): #
        xa1, ya1 = coord_a
        xa2, ya2 = coordinates[0][i + 1]
        for j, coord_b in enumerate(coordinates[1][:-1]):
            xb1, yb1 = coord_b
            xb2, yb2 = coordinates[1][j + 1]
            # Crossing type 1: line 1 vertical line 2 horizontal
            if xa1 == xa2 and yb1 == yb2 and (xb1 <= xa1 <= xb2 or xb1 >= xa1 >= xb2) and (ya1 <= yb1 <= ya2 or ya1 >= yb1 >= ya2):
                print(" ")
                print("Intersection found:", (xa1, yb1))
                manhattan_distance = abs(xa1) + abs(yb1)
                # Track length of both paths plus the extension of each to the intersection
                track_length = total_distance[0][i] + total_distance[1][j] + abs(xa1 - xb1) + abs(ya1 - yb1)
                print("Manhattan distance is: ", manhattan_distance)
                print("Min track length is: ", track_length)
                if manhattan_distance < min_manhattan_distance or min_manhattan_distance == 0:
                    min_manhattan_distance = manhattan_distance
                if track_length < min_track_length or min_track_length == 0:
                    min_track_length = track_length


            # Crossing type 2: line 1 horizontal line 2 vertical
            if ya1 == ya2 and xb1 == xb2 and (yb1 <= ya1 <= yb2 or yb1 >= ya1 >= yb2) and (xa1 <= xb1 <= xa2 or xa1 >= xb1 >= xa2):
                print(" ")
                print("Intersection found:", (xb1, ya1))
                manhattan_distance = abs(xb1) + abs(ya1)
                # Track length of both paths plus the extension of each to the intersection
                track_length = total_distance[0][i] + total_distance[1][j] + abs(xa1 - xb1) + abs(ya1 - yb1)
                print("Manhattan distance is: ", manhattan_distance)
                print("Min track length is: ", track_length)
                if manhattan_distance < min_manhattan_distance or min_manhattan_distance == 0:
                    min_manhattan_distance = manhattan_distance
                if track_length < min_track_length or min_track_length == 0:
                    min_track_length = track_length
    return min_manhattan_distance, min_track_length

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2019\Day3\Puzzle_Input.txt"
    input_sequence = read_input_data(filename)

    print(" ")
    print("==============================================================")
    print("The updated sequence is:")
    print(input_sequence)
    print("==============================================================")
    print(" ")

    coordinates, total_distance = process_movement(input_sequence)
    print("==============================================================")
    print("The coordinates sequences are:")
    print(coordinates[0])
    print(coordinates[1])
    print("==============================================================")
    print(" ")

    min_manhattan_distance, min_track_length = check_for_intersection(coordinates, total_distance)

    print(" ")
    print("==============================================================")
    print("PART 1: The minimum manhattan distance is:", min_manhattan_distance)
    print("==============================================================")
    print(" ")
    print(" ")
    print("==============================================================")
    print("PART 2: The minimum track length is:", min_track_length)
    print("==============================================================")
    print(" ")

    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()