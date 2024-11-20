import time
import numpy as np

def read_input_data(filename):
    box_ids = []
    with open(filename, 'r') as f:
        for line in f:
            box_ids.append(line.strip().split(" ")[0])
    return box_ids

def process_box_ids(box_ids):
    duplicates_found = []
    for box_id in box_ids:
        two_duplicates = 0
        three_duplicates = 0
        box_id = np.array(list(box_id), dtype=np.str_)
        character_set = np.array(list(set(box_id)), dtype=np.str_)
        for character in character_set:
            duplicity_indices = np.where(box_id == character)
            if len(duplicity_indices[0]) == 2:
                two_duplicates += 1
            elif len(duplicity_indices[0]) == 3:
                three_duplicates += 1
        duplicates_found.append((two_duplicates,three_duplicates))
    return duplicates_found

def calculate_checksum(duplicates_found):
    two_duplicate_count = 0
    three_duplicate_count = 0
    for element in duplicates_found:
        if element[0] > 0:
            two_duplicate_count += 1 # Only one counts
        if element[1] > 0:
            three_duplicate_count += 1 # Only one counts

    checksum = two_duplicate_count * three_duplicate_count
    return checksum


def find_two_boxes(box_ids):
    id_length = len(box_ids[0])
    for box_id in box_ids:
        for box_id_check in box_ids:
            check_counter = 0
            for i in range(len(box_id)):
                if box_id[i] == box_id_check[i]:
                    check_counter += 1
                else:
                    mismatch_index = i
            if check_counter == id_length - 1:
                return box_id, box_id_check, mismatch_index
    return print("ERROR: no matching BOX IDs found!")

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2018\Day2\Puzzle_Input.txt"
    box_ids = read_input_data(filename)
    print("The input Box IDs are:")
    print(box_ids)
    duplicates_found = process_box_ids(box_ids)
    checksum = calculate_checksum(duplicates_found)
    print(" ")
    print("=======================================================================================")
    print("The calculated checksum is:", checksum)
    print("=======================================================================================")
    print(" ")
    box_id, box_id_check, mismatch_index = find_two_boxes(box_ids)
    print(" ")
    print("Found the matching box IDs!")
    print(str(box_id) + ": The 1st Box ID")
    print(str(box_id_check) + ": The 2nd Box ID")
    print(" ")
    print("=======================================================================================")
    print("The common letters between the two matching Box IDs are:" + str(box_id[:mismatch_index] + box_id[mismatch_index + 1:]))
    print("=======================================================================================")
    print(" ")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())



if __name__ == "__main__":
    main()