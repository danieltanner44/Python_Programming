import numpy as np
import time
import pandas as pd
from io import StringIO

def read_input_data(filename):
    # Read the file and split by blank lines (records are separated by blank lines)
    with open(filename, "r") as file:
        data = file.read().strip().split("\n\n")  # Splits on double newline

    # Parse each record into a dictionary
    records = []
    for record in data:
        # Replace newline with space and split by space for key-value pairs
        fields = record.replace("\n", " ").split(" ")
        record_dict = dict(field.split(":") for field in fields)
        records.append(record_dict)
    # Create a DataFrame from the list of dictionaries
    pd_data = pd.DataFrame(records)
    return pd_data

def find_valid_passports(pd_data):
    part1_valid_passport_counter = 0
    part2_valid_passport_counter = 0
    for index, row in pd_data.iterrows():
        part1_valid_entry = True
        part2_valid_entry = True
        for title in pd_data:
            # Part 1 Logic
            if title != "cid" and pd.isna(row[title]):
                part1_valid_entry = False
            # Part 2 Logic
            if validate_passport_data(title, row[title]) == False:
                part2_valid_entry = False
        # Now check entry if one False flag raised not valid passport entry
        if part1_valid_entry == True:
            part1_valid_passport_counter += 1
        if part2_valid_entry == True:
            part2_valid_passport_counter += 1
    return part1_valid_passport_counter, part2_valid_passport_counter

def validate_passport_data(title, value):
    if title in ["byr", "iyr", "eyr"]:
        try:
            value = int(value)
        except:
            return False
        if title == "byr" and (1920 <= value <= 2002):
            validity_assessment = True
        elif title == "iyr" and (2010 <= int(value) <= 2020):
            validity_assessment = True
        elif title == "eyr" and (2020 <= int(value) <= 2030):
            validity_assessment = True
        else:
            validity_assessment = False

    elif title == "pid":
        try:
            temp = int(value)
        except:
            return False
        if len(value) == 9:
            validity_assessment = True
        else:
            validity_assessment = False

    elif title == "cid":
        return True

    elif title == "hgt":
        try:
            temp = int(value[:-2])
        except:
            return False
        if value[-2:] == "cm" and (150 <= temp <= 193):
            validity_assessment = True
        elif value[-2:] == "in" and (59 <= temp <= 76):
            validity_assessment = True
        else:
            validity_assessment = False

    elif title == "hcl":
        validity_assessment = True
        if pd.isna(value):
            return False
        elif value[0] == "#" and len(value[1:]) == 6:
            temp = list(value[1:])
            valid_characters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
            for element in temp:
                if element not in valid_characters:
                    validity_assessment = False
        else:
            validity_assessment = False

    elif title == "ecl":
        valid_entries = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        if value not in valid_entries:
            validity_assessment = False
        else:
            validity_assessment = True
    return validity_assessment

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2020\Day4\Puzzle_Input.txt"
    pd_data = read_input_data(filename)
    print("The initial passport data is:")
    print(pd_data)
    part1_valid_passport_counter, part2_valid_passport_counter = find_valid_passports(pd_data)

    print(" ")
    print("==============================================================")
    print("PART 1: The number of valid passport entries is:", part1_valid_passport_counter)
    print("==============================================================")
    print(" ")
    print(" ")
    print("==============================================================")
    print("PART 2: The number of valid passport entries is:", part2_valid_passport_counter)
    print("==============================================================")
    print(" ")

    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()