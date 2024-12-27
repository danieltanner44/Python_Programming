import time
import numpy as np
from my_modules.development import fstring
from my_modules.development import print_array
from my_modules.development import determine_num_duplicates_in_list
import math

def read_input_data(filename):
    all_schematics = []
    temp_key_lock_schematics = []
    with open(filename, 'r') as f:
        for line in f:
            temp = list(line.strip())
            if temp == []:
                all_schematics.append(temp_key_lock_schematics)
                temp_key_lock_schematics = []
            else:
                temp_key_lock_schematics.append(temp)
    all_schematics.append(temp_key_lock_schematics)
    all_schematics = np.array(all_schematics, dtype=np.str_)
    return all_schematics


def separate_locks_keys(all_schematics, all_schematics_shape):
    lock_schematics, key_schematics = None, None
    for schematic in all_schematics:
        # Lock
        if (np.array_equal(schematic[0][:], ["#","#","#","#","#"]) and
                np.array_equal(schematic[all_schematics_shape[1] - 1][:], [".",".",".",".","."])):
            if lock_schematics is None:
                lock_schematics = schematic[np.newaxis,1:all_schematics_shape[1],:]
            else:
                lock_schematics = np.concatenate((lock_schematics, schematic[np.newaxis,1:all_schematics_shape[1],:]), axis=0)
        # Key
        if (np.array_equal(schematic[0][:], [".", ".", ".", ".", "."]) and
                np.array_equal(schematic[all_schematics_shape[1] - 1][:], ["#", "#", "#", "#", "#"])):
            if key_schematics is None:
                key_schematics = schematic[np.newaxis,:all_schematics_shape[1] - 1,:]
            else:
                key_schematics = np.concatenate((key_schematics, schematic[np.newaxis,:all_schematics_shape[1] - 1,:]), axis=0)
    return lock_schematics, key_schematics

def check_lock_key_fit(lock_schematics, key_schematics):
    lock_key_pairs = 0
    lock_schematics_shape = np.shape(lock_schematics)
    key_schematics_shape = np.shape(key_schematics)
    lock_codes = []
    for lock_schematic in lock_schematics:
        temp_list = []
        for index in range(lock_schematics_shape[2]):
            temp_list.append(len(np.where(lock_schematic[:,index] == "#")[0]))
        lock_codes.append(temp_list)

    key_codes = []
    for key_schematic in key_schematics:
        temp_list = []
        for index in range(key_schematics_shape[2]):
            temp_list.append(len(np.where(key_schematic[:, index] == "#")[0]))
        key_codes.append(temp_list)

    # Check if they fit
    for lock_index, lock_code in enumerate(lock_codes):
        for key_index, key_code in enumerate(key_codes):
            check = np.add(lock_code, key_code)
            if max(check) <= 5:
                lock_key_pairs += 1
                # Create array of lock and key
                print(f"Found {lock_key_pairs} pairs so far! Lock {lock_index} with code {lock_code} fits Key {key_index} with code {key_code}")
    return lock_key_pairs


def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")


    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=======================  Puzzle Input  =======================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))

    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2024\Day25\Puzzle_Input.txt"
    all_schematics = read_input_data(filename)
    all_schematics_shape = np.shape(all_schematics)  # row, col, z

    print(fstring(f"There are {all_schematics_shape[0]} lock and key schematics, namely: ", "bk", "wt"))
    [(print_array(schematic), print()) for schematic in all_schematics]
    print(fstring(f"====================  Puzzle Input - End =====================", "bk", "bl"))

    print(" ", end="\n\n")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=========================  PART ONE  =========================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))

    lock_schematics, key_schematics = separate_locks_keys(all_schematics, all_schematics_shape)
    lock_key_pairs = check_lock_key_fit(lock_schematics, key_schematics)
    part_one_ans = str(lock_key_pairs)
    print(fstring(f"======================  PART ONE - END  ======================", "bk", "bl"))

    print(" ", end="\n\n")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=========================  ANSWERS  ==========================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))
    print(f'{fstring("Part One:", "bk", "wt")}')
    print(f'There are {fstring(part_one_ans, "wt", "bk")} compatible key/lock pairs!')
    print(fstring(f"==============================================================", "bk", "bl"))
    print(" ")

    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()