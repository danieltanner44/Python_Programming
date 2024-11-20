import numpy as np
import time

def read_input_data(filename):
    with open(filename, 'r') as f:
        input_number = f.readline().strip()
    return int(input_number)

def find_location(input_number):
    estimated_range = round(input_number**0.5)
    for n in range(1,estimated_range): # Moving along the diagonals
        for a in range(estimated_range): # Moving to adjacent diagonals
            for i in [1,-1]: # Do positive and negative directions
                a = a*i
                if a >= 0:
                    j = 4*n**2 + (8*a - 8)*n + (4*a**2 - 10*a + 5)
                else:
                    j = 4*n**2 - (8*a + 8)*n + (4*a**2 + 6*a + 5)
                if a > 0:
                    k = 4*n**2 + (8*a - 12)*n + (4*a**2 - 10*a + 9)
                else:
                    k = 4*n**2 - (8*a + 4)*n + (4*a**2 + 6*a + 1)
                if input_number == j or input_number == k:
                    return a, n - 1
    return print("OHOH")
def calculate_manhattan_distance(input_number):
    if input_number % 2 == 0:
        a1, n1 = find_location(input_number + 1)
        MD1 = abs(a1 + n1) + abs(a1 - n1)
        a2, n2 = find_location(input_number -1)
        MD2 = abs(a2 + n2) + abs(a2 - n2)
        manhattan_distance = (MD1 + MD2)//2
    else:
        a, n = find_location(input_number)
        manhattan_distance = abs(a + n) + abs(a - n)
    return manhattan_distance

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2017\Day3\Puzzle_Input.txt"
    input_number = read_input_data(filename)
    print("The initial number is:")
    print(input_number)
    manhattan_distance = calculate_manhattan_distance(input_number)
    print("The Manhattan distance is: " + str(manhattan_distance))


    print(" ")
    print("==============================================================")
    print("The checksum in part 1 is:", 0)
    print("==============================================================")
    print(" ")

    print(" ")
    print("==============================================================")
    print("The divisible sum in part 2 is:", 0)
    print("==============================================================")
    print(" ")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()