import time
import numpy as np
from my_modules.development import fstring
from my_modules.development import print_array

def read_input_data(filename):
    word_search = []
    with open(filename, 'r') as f:
        for line in f:
            word_search.append(list(line.strip()))
    word_search = np.array(word_search, dtype=np.str_)
    return word_search

def find_keyword(keyword, word_search):
    num_found = 0
    word_search_shape = np.shape(word_search)
    keyword_reversed = keyword[::-1]

    # Search rows forwards and backwards
    for row in range(word_search_shape[0]):   # Loop over each row
        for j in range(word_search_shape[1] - len(keyword) + 1):
            if (np.array_equal(word_search[row,j:j+4], keyword) or
                    np.array_equal(word_search[row,j:j+4], keyword_reversed)):
                print(f"Match found: Row: {row}, Word: {word_search[row,j:j+4]}")
                num_found += 1

    # Search columns up and down
    for col in range(word_search_shape[1]):  # Loop over each column
        for j in range(word_search_shape[0] - len(keyword) + 1):
            if (np.array_equal(word_search[j:j + 4,col], keyword) or
                    np.array_equal(word_search[j:j + 4,col], keyword_reversed)):
                print(f"Match found: Col: {col}, Word: {word_search[j:j + 4,col]}")
                num_found += 1

    # Search diagonals!
    for axis in [0,1]:
        done_once = False
        for offset_direction in [-1, 1]:
            index = 0
            while True:
                offset = offset_direction * index
                if offset == 0 and done_once == False:
                    done_once = True
                    index += 1
                    continue
                else:
                    if axis == 1:
                        diagonal = word_search.diagonal(offset, axis1=0)
                    else:
                        diagonal = np.fliplr(word_search).diagonal(offset, axis1=0)

                    if len(diagonal) >= len(keyword):
                        for j in range(len(diagonal) - len(keyword) + 1):
                            if (np.array_equal(diagonal[j:j + 4], keyword) or
                                    np.array_equal(diagonal[j:j + 4], keyword_reversed)):
                                print(f"Match found: Diagonal -> Offset: {offset}, axis: {axis}, Word: {diagonal[j:j+4]}")
                                num_found += 1
                    else:
                        break   # As offset increases diagonal will get shorter so if too short just stop

                index += 1
    return num_found

def find_xmas(patterns, word_search):
    num_found = 0
    word_search_shape = np.shape(word_search)
    # Create mask so we can remove irrelevant characters for comparison of X structure elements only
    mask = np.array([["#", ".", "#"], [".", "#", "."], ["#", ".", "#"]], dtype=np.str_)

    # Scan puzzle for a match with any of the patterns
    for col in range(word_search_shape[1] - 3 + 1):
        for row in range(word_search_shape[0] - 3 + 1):
            # Grab a copy of the 3x3 section of the puzzle we are interested in
            word_search_segment = word_search[row:row + 3, col: col + 3].copy()
            # Set the elements we are not interested in to "."
            word_search_segment[np.where(mask == ".")] = "."
            # Assess if it is a match for any of the four patterns
            for pattern in range(4):
                if np.array_equal(word_search_segment, patterns[:,:,pattern]):
                    print(f"Match found: Pattern: {pattern} at location ({row},{col})")
                    num_found += 1

    return num_found


def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2024\Day4\Puzzle_Input.txt"
    word_search = read_input_data(filename)

    print(" ")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"The wordsearch has size {np.shape(word_search)}, and is:", "bk", "wt"))
    print_array(word_search)
    print(fstring(f"==============================================================", "bk", "bl"))
    print(" ")

    keyword = np.array(list("XMAS"), dtype=np.str_)
    num_found = find_keyword(keyword, word_search)
    part_one_ans = str(num_found)

    print(" ")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(f'{fstring("Part One:", "bk", "wt")}')
    print(f'The number matches is: {fstring(part_one_ans, "wt", "bk")}')
    print(fstring(f"==============================================================", "bk", "bl"))
    print(" ")

    print("Part One Complete, starting Part 2 in ...", end="")
    delay = 5
    for i in range(delay, 0, -1):
        print(str(i), end="")
        time.sleep(1)
    print()

    patterns = np.full((3, 3, 4), ".", dtype=np.str_)
    patterns[:, :, 0] = np.array([["M", ".", "S"], [".", "A", "."], ["M", ".", "S"]], dtype=np.str_)
    patterns[:, :, 1] = np.array([["M", ".", "M"], [".", "A", "."], ["S", ".", "S"]], dtype=np.str_)
    patterns[:, :, 2] = np.array([["S", ".", "M"], [".", "A", "."], ["S", ".", "M"]], dtype=np.str_)
    patterns[:, :, 3] = np.array([["S", ".", "S"], [".", "A", "."], ["M", ".", "M"]], dtype=np.str_)

    num_found = find_xmas(patterns, word_search)
    part_two_ans = str(num_found)

    print(" ")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(f'{fstring("Part Two:", "bk", "wt")}')
    print(f'The number of matches is: {fstring(part_two_ans, "wt", "bk")}')
    print(fstring(f"==============================================================", "bk", "bl"))
    print(" ")

    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()