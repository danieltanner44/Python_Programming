import time
from my_modules.development import fstring

def read_input_data(filename):
    # Read input file as a list of index pairs, e.g., [[12, 10], [10, 15], ...]
    input_ranges = []
    with open(filename, 'r') as f:
        temp = f.readline().strip().split(",")
    for range in temp:
        range_endpoints = range.split("-")
        range = [int(range_endpoints[0]), int(range_endpoints[1])]
        input_ranges.append(range)
    return input_ranges

def process_ranges_part1(input_ranges):
    # PART ONE: For each number in each range just check if the first half of the number
    # is equal to the second. If it is then its invalid
    invalid_id_sum = 0
    # Loop over each range
    for input_range in input_ranges:
        # Loop over each number in the range
        for current_index in range(input_range[0],input_range[1]+1):
            current_index_str = str(current_index)
            # If the number is not even it length ignore it as cannot be split into halves
            if len(current_index_str) % 2 != 0:
                continue
            else:
                # Find midpoint and check if the two halves match
                midpoint = len(current_index_str) // 2
                if current_index_str[:midpoint] == current_index_str[midpoint:]:
                    # If they match then it is invalid
                    invalid_id_sum += current_index
    return invalid_id_sum

def divide_str_to_block(string, block_size):
    # Take an input string (a number from the range) and the block size
    # The block size is the number of size of each block that will be checked to see if
    # it repeats,e.g., 12 , 123, etc.
    # Function returns a list of each block divided into block sizes
    string_blocks = []
    # Check if it is equal to every other block
    num_blocks = len(string) // block_size
    for block in range(0, num_blocks):
        temp = string[block * block_size: (block * block_size) + block_size]
        string_blocks.append(temp)
    return string_blocks

def process_ranges_part2(input_ranges):
    # PART TWO: For each number in each range just create a short block at the start of the number
    # Compare this to every other block in the number if they are the same (set length == 1)
    # Then it is an invalid address.
    invalid_id_sum = 0
    for input_range in input_ranges:
        for current_index in range(input_range[0],input_range[1]+1):
            current_index_str = str(current_index)
            midpoint = len(current_index_str) // 2
            for block_size in range(1, midpoint + 1):
                # Blocks have to fit string completely
                if len(current_index_str) % block_size != 0:
                    continue
                else:
                    # Find all the blocks of the given size
                    string_blocks = divide_str_to_block(current_index_str, block_size)
                # If the length of the set is one then it was a repeating block
                string_block_set = set(string_blocks)
                if len(string_block_set) == 1:
                    print(f"Found invalid ID: {current_index_str} which repeats as: {string_block_set}")
                    invalid_id_sum += current_index
                    # Break to ensure that the same number is not found to be invalid multiple times
                    break
    return invalid_id_sum

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2025\Day2\Puzzle_Input.txt"
    input_ranges = read_input_data(filename)

    print(" ")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"There are {str(len(input_ranges))} input ranges to process, they are:", "bk", "wt"))
    [print(input_list) for input_list in input_ranges]
    print(fstring(f"==============================================================", "bk", "bl"))
    print(" ")

    print(" ")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(f'{fstring("Part One:", "bk", "wt")}')
    part_one_ans = process_ranges_part1(input_ranges)
    print(f'The sum of the invalid IDs is: {fstring(str(part_one_ans), "wt", "bk")}')
    print(fstring(f"==============================================================", "bk", "bl"))
    print(" ")

    print(" ")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(f'{fstring("Part Two:", "bk", "wt")}')
    part_two_ans = process_ranges_part2(input_ranges)
    print(f'The sum of the invalid IDs is: {fstring(str(part_two_ans), "wt", "bk")}')
    print(fstring(f"==============================================================", "bk", "bl"))
    print(" ")

    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()