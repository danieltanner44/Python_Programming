import numpy as np
import time
import my_modules.development as mmd

def read_input_data(filename):
    input_data = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            input_data.append(line)
    return input_data

def find_row(boarding_pass):
    current_row_min = 0
    current_row_max = 127
    row_encryption = list(boarding_pass[:-3])
    for element in row_encryption:
        half_range = (current_row_max + current_row_min) / 2
        if element == "F":
            current_row_max = int(half_range)
        elif element == "B":
            current_row_min = round(half_range)
        else:
            print("ERROR: Input incorrect in row data")
    if current_row_max - current_row_min == 1:
        if element == "F":
            current_row_max = current_row_min
        elif element == "B":
            current_row_min = current_row_max
    return current_row_min

def find_column(boarding_pass):
    current_column_min = 0
    current_column_max = 7
    column_encryption = list(boarding_pass[-3:])
    for element in column_encryption:
        half_range = (current_column_max + current_column_min) / 2
        if element == "R":
            current_column_min = round(half_range)
        elif element == "L":
            current_column_max = int(half_range)
        else:
            print("ERROR: Input incorrect in row data")
    if current_column_max - current_column_min == 1:
        if element == "R":
            current_column_min = current_column_max
        elif element == "L":
            current_column_max = current_column_min
    return current_column_min

def find_seat(plan_seating_map):
    for row_index, row in enumerate(plan_seating_map):
        if len(np.where(row == ".")[0]) == 1 :
            required_seat_location = [row_index, int(np.where(row == ".")[0][0])]
    return required_seat_location

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2020\Day5\Puzzle_Input.txt"
    input_data = read_input_data(filename)
    print("The initial passport data is:")
    print(input_data)
    plan_seating_map = np.full([128, 8], ".")
    seat_ids = []
    for boarding_pass in input_data:
        row = find_row(boarding_pass)
        column = find_column(boarding_pass)
        seat_id = (row * 8) + column
        plan_seating_map[row, column] = "#"
        seat_ids.append(seat_id)

    mmd.print_array(plan_seating_map)
    required_seat_location = find_seat(plan_seating_map)
    required_seat_id = (required_seat_location[0] * 8) + required_seat_location[1]
    print(" ")
    print("==============================================================")
    print("PART 1: The highest seat id is:", max(seat_ids))
    print("==============================================================")
    print(" ")
    print(" ")
    print("==============================================================")
    print("PART 2: Our seat id is:", required_seat_id)
    print("==============================================================")
    print(" ")

    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()