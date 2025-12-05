import time
import numpy as np
from my_modules.development import fstring
from my_modules.development import print_array

def read_input_data(filename):
    # Read input file
    map_of_rolls = []
    with open(filename, 'r') as f:
        for line in f:
            temp = [character for character in line.strip()]
            map_of_rolls.append(temp)
    map_of_rolls = np.array(map_of_rolls)
    return map_of_rolls

def check_adjacent_cells(map_of_rolls):
    map_of_rolls = np.pad(map_of_rolls, ((1,1), (1,1)), mode="constant", constant_values=".")
    map_size = np.shape(map_of_rolls)
    updated_map_of_accessible_rolls = np.copy(map_of_rolls)
    roll_accessible_counter = 0
    for row in range(1,map_size[0]-1):
        for col in range(1, map_size[1]-1):
            blocking_roll_counter = 8
            if map_of_rolls[row,col] == "@":
                blocking_roll_counter = 0
                # Top Row
                if map_of_rolls[row - 1, col - 1] == "@":
                    blocking_roll_counter += 1
                if map_of_rolls[row - 1, col] == "@":
                    blocking_roll_counter += 1
                if map_of_rolls[row - 1, col + 1] == "@":
                    blocking_roll_counter += 1
                # Bottom Row
                if map_of_rolls[row + 1, col - 1] == "@":
                    blocking_roll_counter += 1
                if map_of_rolls[row + 1, col] == "@":
                    blocking_roll_counter += 1
                if map_of_rolls[row + 1, col + 1] == "@":
                    blocking_roll_counter += 1
                # Middle Row
                if map_of_rolls[row, col - 1] == "@":
                    blocking_roll_counter += 1
                if map_of_rolls[row, col + 1] == "@":
                    blocking_roll_counter += 1
            if blocking_roll_counter < 4:
                roll_accessible_counter += 1
                updated_map_of_accessible_rolls[row,col] = "."
    return roll_accessible_counter, updated_map_of_accessible_rolls

def total_number_of_rolls_to_remove(map_of_rolls):
    roll_accessible_counter = None
    total_number_of_rolls_removed_counter = 0
    while roll_accessible_counter != 0:
        roll_accessible_counter, map_of_rolls = check_adjacent_cells(map_of_rolls)
        total_number_of_rolls_removed_counter += roll_accessible_counter
    updated_map_of_accessible_rolls = map_of_rolls
    return total_number_of_rolls_removed_counter, updated_map_of_accessible_rolls

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = r"D:\Python_Programming\Advent_of_Code\Advent_of_Code_2025\Day4\Puzzle_Input.txt"
    map_of_rolls = read_input_data(filename)

    print(" ")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"There are {str(len(map_of_rolls))} rows to process, they are:", "bk", "wt"))
    [print(row) for row in map_of_rolls]
    print(fstring(f"==============================================================", "bk", "bl"))
    print(" ")

    print(" ")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(f'{fstring("Part One:", "bk", "wt")}')
    roll_accessible_counter, updated_map_of_accessible_rolls = check_adjacent_cells(map_of_rolls)
    part_one_ans = roll_accessible_counter
    print("The final map of the rolls is:")
    print_array(updated_map_of_accessible_rolls)
    print(f'The number of accessible rolls are: {fstring(str(part_one_ans), "wt", "bk")}')
    print(fstring(f"==============================================================", "bk", "bl"))
    print(" ")

    print(" ")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(f'{fstring("Part Two:", "bk", "wt")}')
    total_number_of_rolls_removed_counter, updated_map_of_accessible_rolls = total_number_of_rolls_to_remove(map_of_rolls)
    part_two_ans = total_number_of_rolls_removed_counter
    print("The final map of the rolls is:")
    print_array(updated_map_of_accessible_rolls)
    print(f'The total number of rolls that can be removed is: {fstring(str(part_two_ans), "wt", "bk")}')
    print(fstring(f"==============================================================", "bk", "bl"))
    print(" ")

    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()