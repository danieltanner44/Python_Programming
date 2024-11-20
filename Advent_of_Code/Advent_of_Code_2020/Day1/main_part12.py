import numpy as np
import time

def read_input_data(filename):
    expense_report = []
    with open(filename, 'r') as f:
        for line in f:
            expense_report.append(int(line.strip()))
    return expense_report

def sum_assessment(expense_report):
    two_add = [x * y for x in expense_report for y in expense_report if x + y == 2020]
    three_add = [x * y * z for x in expense_report for y in expense_report for z in expense_report if x + y + z == 2020]
    return two_add, three_add

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2020\Day1\Puzzle_Input.txt"
    expense_report = read_input_data(filename)
    print("The initial expense data is:")
    print(expense_report)
    two_add, three_add = sum_assessment(expense_report)
    print(" ")
    print("==============================================================")
    print("PART 1: The multiple required is:", two_add[0])
    print("==============================================================")
    print(" ")
    print("==============================================================")
    print("PART 2: The multiple required is:", three_add[0])
    print("==============================================================")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()