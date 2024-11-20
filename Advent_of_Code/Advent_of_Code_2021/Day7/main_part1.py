import numpy as np
import time
import sys

def read_input_data(filename):
    with open(filename, 'r') as f:
        initial_data = f.readline().strip().split(",")
        initial_data = np.array(initial_data, dtype=np.int16)
    return initial_data

def calculate_aligned_position(initial_data):
    # progress_bar(days, days_to_model)
    minimising_function = []
    for i in range(min(initial_data), max(initial_data)+1):
        index_sum = np.int64(0)
        index_rms = initial_data - i
        for each_index_rms in index_rms:
            index_sum += abs(each_index_rms)
        minimising_function.append(index_sum)
    minimising_fuel_cost = int(np.min(minimising_function))
    minimising_function_location = int(np.where(minimising_function == np.min(minimising_function))[0])
    return minimising_function, minimising_fuel_cost, minimising_function_location

def progress_bar(iteration, total, length=40):
    percent = (iteration / total)
    arrow = '█' * int(length * percent)
    spaces = ' ' * (length - len(arrow))
    sys.stdout.write(f'\r|{arrow}{spaces}| {percent:.2%} Complete')
    sys.stdout.flush()

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2021\Day7\Puzzle_Input.txt"
    initial_data = read_input_data(filename)
    print("The initial data is:",initial_data)
    minimising_function, minimising_fuel_cost, minimising_function_location = calculate_aligned_position(initial_data)
    print("The minimising function is:", minimising_function)
    print("The fuel cost for minimising alignment is", minimising_fuel_cost)
    print("The minimising location for alignment is x =", minimising_function_location)

    print(" ")
    print("==============================================================")
    #print("The number of lanternfish after",days_to_model,"days is:",number_of_lanternfish)
    print("==============================================================")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()