import time
from my_modules.development import fstring

def read_input_data(filename):
    computer_memory = []
    with open(filename, 'r') as f:
        for line in f:
            computer_memory.extend(list(line.strip()))

    # Find and convert any integers
    for index, element in enumerate(computer_memory):
        try:
            computer_memory[index] = int(computer_memory[index])
        except:
            pass

    # Merge/concatenate any adjacent integers, i.e., that are digits of the same number
    # Keep merging until no adjacent integers found
    found_digits_to_merge = True
    while found_digits_to_merge:
        found_digits_to_merge = False
        index = 0
        while index < len(computer_memory) - 1:
            if isinstance(computer_memory[index], int):
                if isinstance(computer_memory[index + 1], int):
                    integer = int(str(computer_memory[index]) + str(computer_memory[index+1]))
                    computer_memory = computer_memory[:index] + [integer] + computer_memory[index + 2:]
                    found_digits_to_merge = True
            index += 1
    return computer_memory

def find_valid_commands(computer_memory):
    sum_of_multiplications = 0
    for index, character in enumerate(computer_memory):
        # Scan for required structure "m","u","l","(", integer, "," , integer, ")"
        if (computer_memory[index : index + 4] == ["m", "u", "l", "("] and
                isinstance(computer_memory[index + 4], int) and
                computer_memory[index + 5] == "," and
                isinstance(computer_memory[index + 6], int) and
                computer_memory[index + 7] == ")"):
            sum_of_multiplications += computer_memory[index + 4] * computer_memory[index + 6]
            # print(f"Found: {computer_memory[index: index + 8]}, cumulative sum: {sum_of_multiplications}")

    return sum_of_multiplications

def find_enabled_segments(computer_memory):
    # Run through computer memory and splice together segments of memory that are enabled
    # Enabled segments are after a do() and before a don't() they are enabled at the start
    enable_indices = []
    enabled = False
    for index, character in enumerate(computer_memory):
        if (computer_memory[index:index + 4] == ["d", "o", "(",")"] and not enabled) or index == 0:
            enabled_index = index
            enabled = True
        elif computer_memory[index:index + 7] == ["d", "o", "n", "'", "t", "(",")"] and enabled:
            enable_indices.append((enabled_index,index))
            enabled = False
    # Now create the enabled memory segments
    enabled_computer_memory = []
    for segment in enable_indices:
        enabled_computer_memory.extend(computer_memory[segment[0]:segment[1]])
    return enabled_computer_memory

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2024\Day3\Puzzle_Input.txt"
    computer_memory = read_input_data(filename)

    print(" ")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"There are {len(computer_memory)} characters to process in computer memory, they are:", "bk", "wt"))
    print(computer_memory)
    print(fstring(f"==============================================================", "bk", "bl"))
    print(" ")

    sum_of_multiplications = find_valid_commands(computer_memory)

    part_one_ans = str(sum_of_multiplications)

    print(" ")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(f'{fstring("Part One:", "bk", "wt")}')
    print(f'The number of safe reports is: {fstring(part_one_ans, "wt", "bk")}')
    print(fstring(f"==============================================================", "bk", "bl"))
    print(" ")

    enabled_computer_memory = find_enabled_segments(computer_memory)
    sum_of_multiplications = find_valid_commands(enabled_computer_memory)

    part_two_ans = str(sum_of_multiplications)

    print(" ")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(f'{fstring("Part Two:", "bk", "wt")}')
    print(f'The overall max register value is: {fstring(part_two_ans, "wt", "bk")}')
    print(fstring(f"==============================================================", "bk", "bl"))
    print(" ")

    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()