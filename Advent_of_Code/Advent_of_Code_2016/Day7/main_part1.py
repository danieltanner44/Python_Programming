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
        # Assume these to support later logic
        ip_valid_even, ip_valid_odd = False, True
        abba_check = []
        for index, string in enumerate(ip_address):
            abba = check_for_abba(string)
            abba_check.append(abba)
        # Logic to check if this is a valid ip address
        # abba_check must be False for all odd values (in brackets) and True in at lease one even
        for index, check in enumerate(abba_check):
            if index % 2 == 0: # Even - Need one True to update to ip_valid_even True
                if abba_check[index] == True:
                    ip_valid_even = True
            else:               # Odd - If none are True then remains ip_valid_odd True
                if abba_check[index] == True:
                    ip_valid_odd = False

        # If there is a abba sequence outside the brackets but none in the brackets then it is a valid ip address
        if ip_valid_odd == True and ip_valid_even == True:
            valid_ip_counter += 1
    return valid_ip_counter

def check_for_abba(string):
    # Look for the require repeating characters abba or similar
    string = list(string)
    for index, character in enumerate(string[:-3]):
        # Assess in blocks of 4 if first and last equal and middle two equal and outer not equal to inner
        if character == string[index + 3] and string[index + 1] == string[index + 2] and string[index + 3] != string[index + 2]:
            return True
    return False

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2016\Day7\Puzzle_Input.txt"
    ip_addresses = read_input_data(filename)

    print(" ")
    print("==============================================================")
    print(f"There are {len(ip_addresses)} input ip addresses to assess, they are:")
    [print(ip_address) for ip_address in ip_addresses]
    print("==============================================================")
    print(" ")

    # Now count the number of valid ip addresses
    valid_ip_counter = process_ip_addresses(ip_addresses)

    print(" ")
    print("==============================================================")
    print(f"PART 1: The number of valid ip addresses is: {valid_ip_counter}")
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