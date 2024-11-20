import numpy as np
import time
import hashlib
from collections import Counter

def read_input_data(filename):
    with open(filename, 'r') as f:
        for line in f:
            door_id = line.strip()
    return door_id

def determine_password(door_id):
    found = 0
    index = 0
    password = ""
    while found < 8:
        index += 1
        string = door_id+str(index)
        MD5_hash = hashlib.md5(string.encode("utf-8")).hexdigest()
        if MD5_hash[0:5] == "00000":
            password += str(MD5_hash[5])
            found += 1
            print(" ")
            print("==============================================================")
            print("For hash with 5 preceding zeros...")
            print("==============================================================")
            print("Answer found on cycle:", index)
            print("The MD5 hash is:", MD5_hash)
            print("==============================================================")
    return password

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2016\Day5\Puzzle_Input.txt"
    door_id = read_input_data(filename)
    print(" ")
    print("==============================================================")
    print("The input data is:")
    print(door_id)
    print("==============================================================")
    print(" ")
    password = determine_password(door_id)
    print(" ")
    print("==============================================================")
    print("The decrypted password is:", password)
    print("==============================================================")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()