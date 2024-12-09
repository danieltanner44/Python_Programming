import time
from my_modules.development import fstring

def read_input_data(filename):
    with open(filename, 'r') as f:
        disk_map = f.readline().strip()
    disk_map = [int(element) for element in disk_map]
    return disk_map

def identify_current_file_structure(disk_map):
    # This subroutine restructures the filesystem format from, for example: 12345 -> 0..111....22222
    current_file_structure = []
    data_id = - 1
    for index, element in enumerate(disk_map):
        for update_data_id in range(element):
            if index % 2 == 0:
                if update_data_id == 0:
                    data_id += 1
                current_file_structure.append(data_id)
            else:
                current_file_structure.append(".")
    return current_file_structure

def restructure_filesystem(current_file_structure):
    # This subroutine restructures the filesystem, allowing data blocks to be split up, for example:
    # 0..111....22222 -> 022111222......
    restructured_filesystem = current_file_structure.copy()
    while True:
        # Find index of last element
        upper_bound_index = len(restructured_filesystem)
        for i in range(upper_bound_index - 1,0,-1):
            if restructured_filesystem[i] != ".":
                index_last_element = i
                upper_bound_index = i
                break
        # Find index of first space
        index_first_space = restructured_filesystem.index(".")

        # Stop if the indices are about to crossover
        if index_last_element <= index_first_space:
            break

        # Swap element positions using multiple assignments
        restructured_filesystem[index_first_space], restructured_filesystem[index_last_element] = (
            restructured_filesystem[index_last_element], restructured_filesystem[index_first_space])

    return restructured_filesystem

def find_available_space_blocks(filesystem):
    # This subroutine scans the filesystem and identifies available spaces for data
    # The available spaces is saved as the following structure: [[start index, length], ...]
    available_space_blocks = []
    in_space_block = False
    for index in range(len(filesystem)):
        # Find space blocks
        # Find first space in block
        if filesystem[index] == "." and not in_space_block:
            temp = [index]  # Start a new space block
            space_counter = 1   # It's length starts at 1
            in_space_block = True   # Now we are in a space block
        elif filesystem[index] == "." and in_space_block:
            # If we are in a space block and the current filesystem value is a space then increase length by 1
            space_counter += 1
            if index == len(filesystem) - 1:    # If we are at the end of the filesystem we need to stop
                temp.extend([space_counter])
                available_space_blocks.append(temp)
        elif filesystem[index] != "." and in_space_block:
            # If the current data value is not a space and we were in a space block then the block is complete
            in_space_block = False
            temp.extend([space_counter])
            available_space_blocks.append(temp)
    return available_space_blocks

def find_data_blocks(filesystem):
    # This subroutine scans the filesystem and identifies blocks of data of the same type
    # The data blocks are saved in the following structure: [[start index, length, value], ...]
    data_blocks = []
    in_data_block = False
    for index in range(len(filesystem)):
        # Find data blocks
        # Find first space
        if filesystem[index] != "." and not in_data_block:
            temp = [index]  # Start a new data block
            data_counter = 1    # Its length starts at 1
            in_data_block = True    # Now we are in a new data block
        elif filesystem[index] == filesystem[temp[0]] and in_data_block:
            # If the current data value is the same as start value of the block then it is part of same block
            data_counter += 1   # Incresae length by 1
            if index == len(filesystem) - 1:    # If we are at the end of the filesystem we need to stop
                temp.extend([data_counter, filesystem[temp[0]]])
                data_blocks.append(temp)
        elif (filesystem[index] != filesystem[temp[0]] and in_data_block):
            # If the current data value is not the same as start value of the block then it is not part of same block
            temp.extend([data_counter, filesystem[temp[0]]])
            data_blocks.append(temp)
            if filesystem[index] == ".":
                in_data_block = False   # No longer in a block as reached a space "."
            else:   # If not a space then we are starting a new data block directly next to the previous one
                temp = [index]  # Start a new data block
                data_counter = 1
    return data_blocks

def restructure_filesystem_blocks(current_file_structure):
    # This subroutine restructures the filesystem format, whilst keeping data blocks together, for example:
    # 00...111...2...333.44.5555.6666.777.888899 -> 0099811188827773336446555566..............
    restructured_filesystem = current_file_structure.copy()
    # Find all contiguous data blocks
    data_blocks = find_data_blocks(restructured_filesystem)
    # Loop over blocks to move and move if possible
    index = 0
    for data_block in data_blocks[::-1]:
        index += 1
        # Find available space blocks - this is in loop, so it is updated once data is swapped
        available_space_blocks = find_available_space_blocks(restructured_filesystem)
        # data_block structure is: [[start index, length, value], ...]
        len_data_block = data_block[1]
        # Look for space of required length
        for space_block in available_space_blocks:
            if space_block[1] >= len_data_block:
                # Need to check that it would result in moving left and not right
                if space_block[0] < data_block[0]:
                    # Space to fit it to the left so swap
                    # Swap block positions using multiple assignments
                    (restructured_filesystem[space_block[0]:space_block[0] + data_block[1]],
                     restructured_filesystem[data_block[0]:data_block[0]+data_block[1]]) = (
                        restructured_filesystem[data_block[0]:data_block[0]+data_block[1]],
                        restructured_filesystem[space_block[0]:space_block[0] + data_block[1]])
                    break   # Once swapped stop looking for other spaces
                else:
                    break   # If current space available is not to the left just stop as no subsequent ones will be

    return restructured_filesystem

def calculate_filesystem_checksum(filesystem):
    # Calculate file checksum
    file_checksum = 0
    for index, entry in enumerate(filesystem):
        try:    # Try accept allows for "." in the filesystem
            file_checksum += index * entry
        except:
            pass
    return file_checksum

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2024\Day9\Puzzle_Input.txt"
    disk_map = read_input_data(filename)

    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=======================  Puzzle Input  =======================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"The disk map is {len(disk_map)} entries long and is: ", "bk", "wt"))
    print(disk_map)
    print(fstring(f"====================  Puzzle Input - End =====================", "bk", "bl"))

    print(" ", end="\n\n")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=========================  PART ONE  =========================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))

    current_file_structure = identify_current_file_structure(disk_map)
    restructured_filesystem = restructure_filesystem(current_file_structure)
    file_checksum = calculate_filesystem_checksum(restructured_filesystem)
    part_one_ans = str(file_checksum)

    print(fstring(f"The current file structure looks like this: ", "bk", "wt"))
    print(current_file_structure)
    print(fstring(f"The restructured file structure looks like this: ", "bk", "wt"))
    print(restructured_filesystem)
    print(fstring(f"The restructured file structure checksum is: {file_checksum} ", "bk", "wt"))
    print(fstring(f"======================  PART ONE - END  ======================", "bk", "bl"))

    print(" ", end="\n\n")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=========================  PART TWO  =========================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))

    restructured_filesystem_blocks = restructure_filesystem_blocks(current_file_structure)
    file_checksum = calculate_filesystem_checksum(restructured_filesystem_blocks)
    part_two_ans = str(file_checksum)

    print(fstring(f"The restructured block-like file structure looks like this: ", "bk", "wt"))
    print(restructured_filesystem_blocks)
    print(fstring(f"The restructured block-like file structure checksum is: {file_checksum} ", "bk", "wt"))
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