import time
import numpy as np
from my_modules.development import fstring

def read_input_data(filename):
    # Read input file to get ingredient ID ranges and ingredient IDs
    reading_ingredient_ranges = True
    ingredient_ID_ranges = []
    ingredient_IDs = []
    with open(filename, 'r') as f:
        for line in f:
            if len(line.strip()) == 0:
                # This is the blank line in the input file format changes to ingredient IDs
                reading_ingredient_ranges = False
                continue
            elif reading_ingredient_ranges:
                # For ingredient ranges
                temp = [int(i) for i in line.strip().split("-")]
                ingredient_ID_ranges.append(temp)
            elif not reading_ingredient_ranges:
                # For ingredient IDs
                ingredient_IDs.append(int(line.strip()))
            else:
                print("Error")
                break
    return ingredient_ID_ranges, ingredient_IDs

def determine_number_of_fresh_ingredients(ingredient_ID_ranges, ingredient_IDs):
    # This module determines the number of fresh ingredients
    number_of_fresh_ingredients = 0
    for ingredient_ID in ingredient_IDs:
        for ingredient_ID_range in ingredient_ID_ranges:
            # Check if it is in a fresh range if it is add to counter to track
            if ingredient_ID >= ingredient_ID_range[0] and ingredient_ID <= ingredient_ID_range[1]:
                # Break so fresh ingredient is not recounted for another matching range
                number_of_fresh_ingredients += 1
                break
    return number_of_fresh_ingredients

def determine_fresh_ingredient_ranges(ingredient_ID_ranges):
    # Need to merge ingredient ranges that overlap
    # If 1-4 and 3-5 => 1-5
    # Loop over each range and check if it overlaps any other range
    # If it does then merge it to form one new broader range
    while True:
        merged_fresh_ranges = []
        tracker = np.zeros(len(ingredient_ID_ranges), dtype=int)
        # Loop over each range in turn
        for i, id_range1 in enumerate(ingredient_ID_ranges):
            # Ensure the current range was not already processed
            if tracker[i] == 0:
                # If a merge is not found then add that range directly in as is
                found = False
                for j, id_range2 in enumerate(ingredient_ID_ranges):
                    # Loop over to check each range with each other range (but not itself)
                    if i != j and tracker[j] == 0:
                        if (id_range1[0] <= id_range2[0] <= id_range1[1]) or (
                                id_range1[0] <= id_range2[1] <= id_range1[1]) or (
                                id_range2[0] <= id_range1[0] <= id_range2[1]) or (
                                id_range2[0] <= id_range1[1] <= id_range2[1]):
                            # If they overlap then merge them
                            min_range = min(id_range1[0], id_range2[0])
                            max_range = max(id_range1[1], id_range2[1])
                            merged_fresh_ranges.append([min_range,max_range])
                            tracker[i], tracker[j] = 1, 1
                            # Mark as merged/found so the original is not added back in
                            found = True
                            break
                if not found:
                    # If there are no overlapped ranges add the existing range back in
                    merged_fresh_ranges.append(id_range1)
            else:
                # If the range was already used in this main loop just skip to next one
                continue
        if sum(tracker) == 0:
            # Keep looping to merge ranges until a loop where no range merging occurs
            # If there are no change then break the main loop here
            break
        else:
            # If ranges were merged in the last loop then update to the new range list and go again
            ingredient_ID_ranges = merged_fresh_ranges

    # Calculate number of ranges
    number_of_fresh_ingredient_IDs = 0
    for range_ID in merged_fresh_ranges:
        # The number of intermediate vales for range [a, b] is (a - b + 1)
        # So [3, 5] = (5 - 3 + 1) = 3 or 3, 4 and 5
        number_of_fresh_ingredient_IDs += range_ID[1] - range_ID[0] + 1
    return number_of_fresh_ingredient_IDs

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = (r"D:\Python_Projects\Python_Programming\Advent_of_Code\Advent_of_Code_2025\Day5\Puzzle_Input.txt")
    ingredient_ID_ranges, ingredient_IDs = read_input_data(filename)

    print(" ")
    print(fstring(f"=================================================================", "bk", "bl"))
    print(fstring(f"There are {str(len(ingredient_ID_ranges))} ingredient ranges to process, they are:", "bk", "wt"))
    [print(ingredient_ID_range) for ingredient_ID_range in ingredient_ID_ranges]
    print(fstring(f"There are {str(len(ingredient_IDs))} ingredient IDs to process, they are:", "bk", "wt"))
    [print(ingredient_ID) for ingredient_ID in ingredient_IDs]
    print(fstring(f"=================================================================", "bk", "bl"))
    print(" ")

    print(" ")
    print(fstring(f"=================================================================", "bk", "bl"))
    print(f'{fstring("Part One:", "bk", "wt")}')
    number_of_fresh_ingredients = determine_number_of_fresh_ingredients(
        ingredient_ID_ranges, ingredient_IDs)
    part_one_ans = number_of_fresh_ingredients
    print(f'The total number fresh ingredient IDs is: {fstring(str(part_one_ans), "wt", "bk")}')
    print(fstring(f"=================================================================", "bk", "bl"))
    print(" ")

    print(" ")
    print(fstring(f"=================================================================", "bk", "bl"))
    print(f'{fstring("Part Two:", "bk", "wt")}')
    number_of_fresh_ingredient_IDs = determine_fresh_ingredient_ranges(ingredient_ID_ranges)
    part_two_ans = number_of_fresh_ingredient_IDs
    print(f'The total number of fresh ingredient IDs is: {fstring(str(part_two_ans), "wt", "bk")}')
    print(fstring(f"=================================================================", "bk", "bl"))
    print(" ")

    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()