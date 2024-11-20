import numpy as np
import hashlib
import time

def read_input_data(filename):
    with open(filename, 'r') as f:
        initial_data = f.readline().strip()
    return initial_data

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2015\Day4\Puzzle_Input.txt"
    initial_data = read_input_data(filename)
    print("The hash key is:",initial_data)
    index = 0
    do_once = True
    while True:
        string = initial_data+str(index)
        MD5_hash = hashlib.md5(string.encode("utf-8")).hexdigest()
        if MD5_hash[0:5] == "00000" and do_once == True:
            do_once = False
            print(" ")
            print("==============================================================")
            print("For hash with 5 preceding zeros...")
            print("==============================================================")
            print("Answer found on cycle:",index)
            print("The MD5 hash is:",MD5_hash)
            print("==============================================================")
        if MD5_hash[0:6] == "000000":
            print(" ")
            print("==============================================================")
            print("For hash with 6 preceding zeros...")
            print("==============================================================")
            print("Answer found on cycle:", index)
            print("The MD5 hash is:", MD5_hash)
            print("==============================================================")
            break
        index += 1
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()