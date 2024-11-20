import numpy as np
import time
import sys

def read_input_data(filename):
    input_data = []
    with open(filename, 'r') as f:
        for each_line in f:
            input_line_read = each_line.strip().split(" | ")[0].split(" ")
            output_line_read = each_line.strip().split(" | ")[1].split(" ")
            input_data.append([input_line_read] + [output_line_read])
        print(" ")
        print("The input data is: ")
        print(input_data)
    return input_data

def process_data(input_data):
    counter = 0
    for outputs in input_data:
        for each_output in outputs[1]:
            if len(each_output) in [2, 3, 4, 7]:
                counter += 1
    return counter

def progress_bar(iteration, total, length=40):
    percent = (iteration / total)
    arrow = '█' * int(length * percent)
    spaces = ' ' * (length - len(arrow))
    sys.stdout.write(f'\r|{arrow}{spaces}| {percent:.2%} Complete')
    sys.stdout.flush()

def main():
    # progress_bar(days, days_to_model)
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2021\Day8\Puzzle_Input.txt"
    input_data = read_input_data(filename)
    counter = process_data(input_data)
    print(" ")
    print("The number of instances is:", counter)


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