import time

def read_input_data(filename):
    input_passphrases = []
    with open(filename, 'r') as f:
        for line in f:
            input_passphrases.append(line.strip().split(" "))
    return input_passphrases

def assess_passphrases(input_passphrases):
    part1_valid_passphrase_count = 0
    part2_valid_passphrase_count = 0
    # Step through each passphrase
    for passphrase in input_passphrases:
        # Create list comprehension for direct duplicates (part 1)
        max_duplicate_words = max([passphrase.count(string) for string in passphrase if string in passphrase])
        # If the max duplicate count is 1 then all is fine (the word in passphrase found itself)
        if max_duplicate_words == 1:
            part1_valid_passphrase_count += 1
        # Create a list of 1s where anagrams are found, if this is the len of the passphrase no anagrams present
        number_anagrams_found = sum([1 for string1 in passphrase for string2 in passphrase if sorted(list(string1)) == sorted(list(string2))]) - len(list(passphrase))
        if number_anagrams_found == 0:
            part2_valid_passphrase_count += 1
    return part1_valid_passphrase_count, part2_valid_passphrase_count

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2017\Day4\Puzzle_Input.txt"
    input_passphrases = read_input_data(filename)
    print("The initial passphrases to assess are:")
    print(input_passphrases)
    part1_valid_passphrase_count, part2_valid_passphrase_count = assess_passphrases(input_passphrases)
    print(" ")
    print("==============================================================")
    print("PART1: The number of valid passphrases is:", part1_valid_passphrase_count)
    print("==============================================================")
    print(" ")

    print(" ")
    print("==============================================================")
    print("PART2: The number of valid passphrases is:", part2_valid_passphrase_count)
    print("==============================================================")
    print(" ")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()