import numpy as np
import time
import hashlib
from collections import Counter

def read_input_data(filename):
    ip_addresses = []
    with open(filename, 'r') as f:
        for line in f:
            ip_addresses.append(line.strip().replace("[","]").split("]"))
    return ip_addresses

def process_ip_addresses(ip_addresses):
    valid_ip_counter = 0
    for ip_address in ip_addresses:
        abba_check = []
        for index, string in enumerate(ip_address):
            abba = check_for_abba(string)
            abba_check.append(abba)
        if (abba_check[0] == True or abba_check[2] == True) and abba_check[1] != True:
            valid_ip_counter += 1
    return valid_ip_counter

def check_for_abba(string):
    string = list(string)
    for index, character in enumerate(string[:-3]):
        if character == string[index + 3] and string[index + 1] == string[index + 2] and string[index + 3] != string[index + 2]:
            print("found", string)
            return True
    return False

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2016\Day7\Puzzle_Input.txt"
    ip_addresses = read_input_data(filename)

    valid_ip_counter = process_ip_addresses(ip_addresses)
    print(" ")
    print("==============================================================")
    print("The input messages are:")
    print(ip_addresses)
    print("==============================================================")
    print(" ")

    print(" ")
    print("==============================================================")
    print("PART 1: The decrypted message is:", valid_ip_counter)
    print("==============================================================")
    print(" ")
    print(" ")
    print("==============================================================")
    print("PART 2: The decrypted message is:", 0)
    print("==============================================================")
    print(" ")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()