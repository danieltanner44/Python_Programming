import numpy as np
import time

def read_input_data(filename):
    passport_records = []
    with open(filename, 'r') as f:
        for line in f:
            passport_records.append(line.strip().replace("-", " ").replace(":", " ").replace("  ", " ").split(" "))
    return passport_records
def assess_passport_validity(passport_records):
    num_valid_passports_p1 = 0
    num_valid_passports_p2 = 0
    for record in passport_records:
        # PART 1
        # Assess number of duplicates
        duplicate_counter = 0
        for character in record[3]:
            if record[2] == character:
                duplicate_counter += 1
        if int(record[0]) <= duplicate_counter <= int(record[1]):
            num_valid_passports_p1 += 1
        # PART 2
        if (record[3][int(record[0]) - 1] == record[2] or record[3][int(record[1]) - 1] == record[2]) and (record[3][int(record[0]) - 1] != record[3][int(record[1]) - 1]):
            num_valid_passports_p2 += 1
    return num_valid_passports_p1, num_valid_passports_p2

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2020\Day2\Puzzle_Input.txt"
    passport_records = read_input_data(filename)
    print("The passport data is:")
    print(passport_records)
    num_valid_passports_p1, num_valid_passports_p2 = assess_passport_validity(passport_records)
    print(" ")
    print("==============================================================")
    print("PART 1: The number of valid passports is:", num_valid_passports_p1)
    print("==============================================================")
    print(" ")
    print(" ")
    print("==============================================================")
    print("PART 2: The number of valid passports is:", num_valid_passports_p2)
    print("==============================================================")
    print(" ")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()