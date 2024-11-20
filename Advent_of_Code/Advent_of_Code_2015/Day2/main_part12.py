import numpy as np
import time

def read_input_data(filename):
    initial_data = []
    with open(filename, 'r') as f:
        for line in f:
            temp = line.strip().split("x")
            initial_data.append(temp)
    initial_data = np.array(initial_data, dtype=np.int64)
    return initial_data

def estimating_wrapping_paper_amount(initial_data):
    paper_order_size = 0
    ribbon_order_size = 0
    for each_present in initial_data:
        each_present = sorted(each_present)
        area_per_package = ((2 * each_present[0] * each_present[1] +
                2 * each_present[1] * each_present[2] +
                2 * each_present[0] * each_present[2]) + each_present[0] * each_present[1])
        ribbon_length_per_package = ((2 * each_present[0]) + (2 * each_present[1])) + (each_present[0]*each_present[1]*each_present[2])
        # Accumulate order over presents
        paper_order_size += area_per_package
        ribbon_order_size += ribbon_length_per_package
    return paper_order_size, ribbon_order_size

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2015\Day2\Puzzle_Input.txt"
    initial_data = read_input_data(filename)
    print("The initial data is:",initial_data)
    paper_order_size, ribbon_order_size = estimating_wrapping_paper_amount(initial_data)
    print(" ")
    print("==============================================================")
    print("Order this amount of wrapping paper:", paper_order_size)
    print("Order this amount of ribbon:", ribbon_order_size)
    print("==============================================================")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()