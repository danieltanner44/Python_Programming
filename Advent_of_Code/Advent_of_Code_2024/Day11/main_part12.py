import time

import my_modules.development
import numpy as np
from my_modules.development import fstring
from my_modules.development import print_array
import my_modules.development as mmd
import math

def read_input_data(filename):
    stone_configuration = []
    with open(filename, 'r') as f:
        for line in f:
            stone_configuration.extend([int(element) for element in list(line.strip().split())])
    stones_processing_dict = mmd.determine_num_duplicates_in_list(stone_configuration)
    return stones_processing_dict

def process_blink_cycle(stone):
    # This is the logic to process a blink cycle for a single stone
    new_stone_configuration = []
    # Loop over each stone in the list
    num_digitson_stone = len(str(stone))
    if stone == 0:
        # If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1
        new_stone_configuration.extend([1])
    elif num_digitson_stone % 2 == 0:  # Even number of digits for number carved on stone
        # If the stone is engraved with a number that has an even number of digits, it is replaced by
        # two stones. The left half of the digits are engraved on the new left stone, and the right half
        # of the digits are engraved on the new right stone
        digit_string = str(stone)
        right_stone_num, left_stone_num = (digit_string[num_digitson_stone // 2:],
                                           digit_string[:num_digitson_stone // 2])
        new_stone_configuration.extend([int(left_stone_num)])
        new_stone_configuration.extend([int(right_stone_num)])
    else:
        new_stone_configuration.extend([stone * 2024])
    return new_stone_configuration


def process_stones(stones_processing_dict, number_of_blinks):
    # This is the logic to process all stones over the required number of cycles
    for i in range(number_of_blinks):
        # Create a dictionary to track the next processing list
        # The structure is {stone: number of duplicates}
        next_stones_processing_dict = {}
        # Loop over each stone in the stones to process dictionary
        for stone, dup_counter in stones_processing_dict.items():
            # Process a blink cycle for each stone
            stone_list_after_blink = process_blink_cycle(stone)
            # Find any duplicates and create a dictionary (same as the stones_processing_dict)
            stone_dict_after_blink = mmd.determine_num_duplicates_in_list(stone_list_after_blink)
            # Loop over each stone in the output after the blink
            for each_stone, each_dup_counter in stone_dict_after_blink.items():
                # If it is already in the next_stones_processing_dict then add
                # The number of duplicates in the output times the number of duplicates in the input
                if each_stone in next_stones_processing_dict:
                    next_stones_processing_dict[each_stone] += stone_dict_after_blink[each_stone] * dup_counter
                else:
                    # Otherwise just set as the number duplicates in the output times the number of duplicates in the input
                    next_stones_processing_dict[each_stone] = stone_dict_after_blink[each_stone] * dup_counter
        # Set the next_stones_processing_dict as the new stones+processing_dict for the next blink cycle
        stones_processing_dict = next_stones_processing_dict
        print(f"Blink cycle: {i + 1}, Number of stones: {sum(stones_processing_dict.values())}")
    return stones_processing_dict

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2024\Day11\Puzzle_Input.txt"
    original_stones_processing_dict = read_input_data(filename)

    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=======================  Puzzle Input  =======================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"The starting stone duplicate configuration is: ", "bk", "wt"))
    print(original_stones_processing_dict)
    print(fstring(f"====================  Puzzle Input - End =====================", "bk", "bl"))

    print(" ", end="\n\n")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=========================  PART ONE  =========================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))

    number_of_blinks = 25
    stones_processing_dict = original_stones_processing_dict.copy()
    stones_processing_dict = process_stones(stones_processing_dict, number_of_blinks)
    part_one_ans = str(sum(stones_processing_dict.values()))
    print(fstring(f"The final configuration has {part_one_ans} stones.", "bk", "wt"))
    print(fstring(f"Of these {len(stones_processing_dict)} are uniquely numbered.", "bk", "wt"))
    print(fstring(f"======================  PART ONE - END  ======================", "bk", "bl"))

    print(" ", end="\n\n")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=========================  PART TWO  =========================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))

    number_of_blinks = 75
    stones_processing_dict = original_stones_processing_dict.copy()
    stones_processing_dict = process_stones(stones_processing_dict, number_of_blinks)
    part_two_ans = str(sum(stones_processing_dict.values()))
    print(fstring(f"The final configuration has {part_two_ans} stones.", "bk", "wt"))
    print(fstring(f"Of these {len(stones_processing_dict)} are uniquely numbered.", "bk", "wt"))
    print(fstring(f"======================  PART TWO - END  ======================", "bk", "bl"))

    print(" ", end="\n\n")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=========================  ANSWERS  ==========================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))
    print(f'{fstring("Part One:", "bk", "wt")}')
    print(f'The total calibration result is: {fstring(part_one_ans, "wt", "bk")}')
    print(fstring(f"==============================================================", "bk", "bl"))
    print(f'{fstring("Part Two:", "bk", "wt")}')
    print(f'The total calibration result is: {fstring(part_two_ans, "wt", "bk")}')
    print(fstring(f"==============================================================", "bk", "bl"))
    print(" ")

    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()