import numpy as np
import time

def reading_input_data(f):
    print("Reading input data...", end = "")
    print("[complete]", end="\n")
    print(" ")
    # Lets read all of the input data
    data = np.array([])
    counter = 0
    only_once = False
    for each_line in f:
        # Lets read in all the key information
        temp = each_line.rstrip("\n").split()
        [temp.append(letter) for letter in str(temp[0:1])]
        if only_once == False:
            data = temp
            only_once = True
        else:
            data = np.vstack((data, temp))
        counter += 1
    # Delete unneeded columns
    data = np.delete(data, [2, 3, 9, 10], 1)
    return data, counter

def check_duplicates(characters):
    char_count = {}
    # Count occurrences of each character
    for char in characters:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    check = char_count[max(char_count, key=char_count.get)]
    return check

def sort_and_rank(j, data, number_of_hands):
    start_index = [0]
    for i in range(number_of_hands):
        if i == number_of_hands - 1:
            start_index = np.append(start_index, number_of_hands)
            break
        if j == 2:
            if (data[i+1,j] != data[i,j]):
                start_index = np.append(start_index, i + 1)
        elif (data[i+1,j] != data[i,j]) or list(data[i + 1, 2:j]) != list(data[i, 2:j]):
                start_index = np.append(start_index, i + 1)
        else:
            continue
    return start_index

def reorder_rows(start_index, j, data, card_values, number_of_hands):
    for i in range(len(start_index) - 1):
        sort_list = np.array([], dtype=int)
        for k in range(start_index[i], start_index[i + 1]):
            sort_list = np.append(sort_list, card_values.get(data[k, j + 1]))
        temp = data[start_index[i]:start_index[i+1], :]
        data[start_index[i]:start_index[i+1], :] = temp[sort_list.argsort()]
    return data

def calculate_winnings(data, number_of_hands):
    total_winnings = 0
    for i in range(number_of_hands):
        total_winnings += int(data[i])*(i + 1)
    return total_winnings

def main():
    ts0 = time.time()
    print("Starting time:", ts0)
    print(" ")
    card_values = {"A": 13, "K": 12, "Q": 11, "J": 10, "T": 9, "9": 8, "8": 7, "7": 6, "6": 5, "5": 4, "4": 3, "3": 2, "2": 1}
    f = open(r'D:\Advent_of_Code\Advent_of_Code_2023\Day7\Puzzle_Input.txt', 'r')
    data, number_of_hands = reading_input_data(f)
    hand_type = np.array([], dtype=np.int32)
    for hands in range(number_of_hands):
        # Step through each hand to determine its type
        hand_type = np.append(hand_type, len(data[hands,2:7]) - len(set(data[hands,2:7])))
        if hand_type[hands] == 0:
            # Just highest card!
            hand_type[hands] = 1
        elif hand_type[hands] == 1:
            # just one pair!
            hand_type[hands] = 2
        elif hand_type[hands] == 2:
            # two pair or three of a kind
            result = check_duplicates(characters=data[hands,2:7])
            if result == 2: #three of a kind
                hand_type[hands] = 3
            else: #two pair
                hand_type[hands] = 4
        elif hand_type[hands] == 3:
            # four of a kind or full house
            result = check_duplicates(characters=data[hands, 2:7])
            if result == 3: #full house
                hand_type[hands] = 5
            else: #four of a kind
                hand_type[hands] = 6
        elif hand_type[hands] == 4:
            # Five of a kind!
            hand_type[hands] = 7
        else:
            print("Error: hand_type not recognised!!!")
    data = np.insert(data, 2, [hand_type], axis=1)
    data = data[data[:, 2].argsort()]

    # Lets sort it all by walking down each column and seeing if adjacent rows have the same values
    #for j in range(number_of_hands):
    for j in range(2,7):
        start_index = sort_and_rank(j, data, number_of_hands)
        data = reorder_rows(start_index, j, data, card_values, number_of_hands)
    total_winnings = calculate_winnings(data[:,1], number_of_hands)
    print("Total winnings are:", total_winnings)

    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())
    file_path = "D:\Advent_of_Code\Advent_of_Code_2023\Day7\data.txt"
    # Open the file in write mode and write the array elements
    with open(file_path, 'w') as file:
        for item in data:
            file.write("%s\n" % item)

if __name__ == "__main__":
    main()