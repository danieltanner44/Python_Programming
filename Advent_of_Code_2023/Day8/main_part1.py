import numpy as np
import time

def reading_input_data(f):
    print("Reading input data...", end = "")
    print("[complete]", end="\n")
    print(" ")
    # Lets read all of the input data
    symbol_list = {"\n","(",")",","}
    directions = []
    data = np.array([])
    number_of_maps = 0
    only_once = False
    for each_line in f:
        # Lets read in all the key information
        if number_of_maps >= 2:
            each_line = each_line.split()
            for symbol in symbol_list:
                each_line = [element.replace(symbol, "") for element in each_line]
            if only_once == False:
                data = each_line
                only_once = True
            else:
                data = np.vstack((data, each_line))
            number_of_maps += 1
        elif number_of_maps == 0:
            temp = each_line.strip("\n")
            number_of_maps += 1
            continue
        elif number_of_maps == 1:
            number_of_maps += 1
            continue
    # Tidy up input data
    [directions.append(letter) for letter in temp]
    data = np.delete(data, 1, 1)
    data = data[data[:, 0].argsort()]
    side = {"L" : 1, "R" : 2}
    directions_int = np.array([], dtype=int)
    for i in range(0,len(directions)):
        directions_int = np.append(directions_int, side.get(directions[i]))
    my_list = dict(zip(data[:,0],range(np.shape(data)[0])))
    del (temp, symbol_list, directions, only_once, number_of_maps, each_line, side)
    return data, my_list, directions_int

def stepping(data, my_list, directions_int):
    number_of_steps, current_row, next_row, done = 0, 0, "AAA", False
    while done == False:
        for i in range(len(directions_int)):
            if done == False and next_row != "ZZZ":
                next_row = data[current_row, directions_int[round(i%len(directions_int))]]
                current_row = my_list.get(next_row)
                number_of_steps += 1
            else:
                done = True
                break
    del(current_row, next_row)
    return done, number_of_steps

def main():
    ts0 = time.time()
    print("Starting time:", ts0)
    print(" ")
    f = open(r'D:\Advent_of_Code\Advent_of_Code_2023\Day8\Puzzle_Input.txt', 'r')
    # Read all of the input data from Puzzle Input and organise it
    data, my_list, directions_int = reading_input_data(f)
    # Step through the data and see how many steps it takes to complete the puzzle
    done, number_of_steps = stepping(data, my_list, directions_int)
    print("The number of steps required to complete the puzzle are:", number_of_steps)
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()