import numpy as np
import time
from collections import Counter

def read_input_data(filename):
    input_data = []
    with open(filename, 'r') as f:
        for line in f:
            temp_string = ""
            encrypted_room_names = line.strip().split("-")[:-1]
            temp = line.strip().replace("]","").split("-")
            temp1 = temp[-1].split("[")
            for element in temp[:-1]:
                temp_string += element
            input_data.append([temp_string,temp1[0], temp1[1], encrypted_room_names])
    return input_data

def assess_checksum(input_data):
    sector_id_sum = 0
    valid_rooms = []
    for index, room in enumerate(input_data):
        element_count = Counter(room[0])
        print(" ")
        print("Processing room", index,": ",room)
        checksum = ""
        for i in range(5):
            common_elements = sorted([element for element in element_count if element_count[element] == max(element_count.values())])
            checksum += common_elements[0]
            element_count.pop(common_elements[0])
        if checksum == room[2]:
            print(checksum,"=",room[2]," - this is a match!")
            sector_id_sum += int(room[1])
            valid_rooms.append(room)
        else:
            print(checksum,"!=",room[2]," - this is not a match!")
    return sector_id_sum, valid_rooms

def process_shift_cypher(valid_rooms):
    decrypted_room_names = []
    for room in valid_rooms:
        decrypted_room_name = []
        shift = int(room[1])%26
        alphabet_array = dict(zip(np.array([chr(i) for i in range(97, 123)]),range(26)))
        for element in room[3]:
            string = ""
            for character in element:
                shifted_index = (alphabet_array[character] + shift)%26
                temp = [key for key, value in alphabet_array.items() if value == shifted_index]
                string += temp[0]
            decrypted_room_name.append(string)
        if decrypted_room_name == ["northpole","object","storage"]:
            return decrypted_room_name, room[1]
        decrypted_room_names.append(decrypted_room_name)
    return

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2016\Day4\Puzzle_Input.txt"
    input_data = read_input_data(filename)
    print(" ")
    print("==============================================================")
    print("The input data is:")
    print(input_data)
    print("==============================================================")
    print(" ")
    sector_id_sum, valid_rooms = assess_checksum(input_data)
    print(" ")
    print("==============================================================")
    print("The sum of the good rooms is:", sector_id_sum)
    print("==============================================================")
    decrypted_room_name, room_id = process_shift_cypher(valid_rooms)
    print(" ")
    print("==============================================================")
    print("The rooms", decrypted_room_name,"was found to have sector ID:",room_id)
    print("==============================================================")


    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()