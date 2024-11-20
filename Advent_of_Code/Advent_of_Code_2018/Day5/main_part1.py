import time
import numpy as np

def read_input_data(filename):
    with (open(filename, 'r') as f):
        for line in f:
            input_data = line.strip()
    input_data = list(input_data)
    return input_data

def process_sequence(input_data):

    while True:
        check_convergence = input_data.copy()
        for i, character in enumerate(input_data):
            try:
                if character == input_data[i + 1].swapcase():
                    input_data = input_data[:i] + input_data[i+2:]
                    break
            except:
                break
        # If no changes made in last cycle then stop
        if check_convergence == input_data:
            return len(input_data)

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2018\Day5\Puzzle_Input.txt"
    input_data = read_input_data(filename)
    print(" ")
    print("The input sequence is:")
    print(input_data)

    length_of_residual_sequence = process_sequence(input_data)


    print(" ")
    print("=======================================================================================")
    print("The length of the residual sequence is:", length_of_residual_sequence)
    print("=======================================================================================")
    print(" ")


    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())



if __name__ == "__main__":
    main()