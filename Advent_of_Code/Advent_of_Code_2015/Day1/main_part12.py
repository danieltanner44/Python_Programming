import numpy as np
import time

def read_input_data(filename):
    with open(filename, 'r') as f:
        initial_data = list(f.readline().strip())
        initial_data = np.array(initial_data, dtype=np.str_)
    return initial_data

def check_when_first_enter_basement(intial_data):
    counter = 0
    for index, instruction in enumerate(intial_data, start=1):
        if instruction == "(":
            counter += 1
        else:
            counter -= 1
        if counter < 0:
            first_enter_basement = index
            return first_enter_basement
    return None

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2015\Day1\Puzzle_Input.txt"
    initial_data = read_input_data(filename)
    print("The initial data is:",initial_data)
    floor_number = len(np.where(initial_data == "(")[0]) - len(np.where(initial_data == ")")[0])
    first_enter_basement = check_when_first_enter_basement(initial_data)
    print(" ")
    print("==============================================================")
    print("Santa needs to head to floor:", floor_number)
    print("Santa first entered the basement at position:", first_enter_basement)
    print("==============================================================")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()