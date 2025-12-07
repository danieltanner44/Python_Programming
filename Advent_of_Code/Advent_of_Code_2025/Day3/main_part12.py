import time
from my_modules.development import fstring

def read_input_data(filename):
    # Read input file
    bank_joltages = []
    with open(filename, 'r') as f:
        for line in f:
            bank_joltages.append(line.strip())
    return bank_joltages

def calculate_max_joltages(bank_joltages, output_length):
    max_joltages = []
    for bank in bank_joltages:
        # Create all of the digits for each bank
        digits = [int(i) for i in bank]
        bank_length = len(digits)
        # Work out how much freedom we have (window to look for maxs)
        option_digits = bank_length - output_length + 1
        # The first digit is the largest in the window from zero to option_digits
        search_start = 0
        search_end = option_digits
        digit_output = []
        # Scan our window of option digits selecting the maximum from each, reducing the options
        # And moving to the next place from left to right
        while len(digit_output) < output_length:
            # Find the maximum in the current options window
            max_location = search_start + digits[search_start:search_end].index(max(digits[search_start:search_end]))
            # Store the maximum value
            digit_output.append(str(digits[max_location]))
            # Reduce the number of options (window size) by the number used to find maximum
            option_digits = option_digits - (max_location - search_start)
            # Set a new start in the location next to the maximum and extend window by the number of option digits remaining
            search_start = max_location + 1
            search_end = search_start + option_digits
        temp = int("".join(digit_output))
        max_joltages.append(temp)
    return max_joltages

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2025\Day3\Puzzle_Input.txt"
    bank_joltages = read_input_data(filename)

    print(" ")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"There are {str(len(bank_joltages))} banks to process, they are:", "bk", "wt"))
    [print(bank) for bank in bank_joltages]
    print(fstring(f"==============================================================", "bk", "bl"))
    print(" ")

    print(" ")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(f'{fstring("Part One:", "bk", "wt")}')
    output_length = 2
    max_joltages = calculate_max_joltages(bank_joltages, output_length)
    part_one_ans = sum(max_joltages)
    print(f'The total output joltage is: {fstring(str(part_one_ans), "wt", "bk")}')
    print(fstring(f"==============================================================", "bk", "bl"))
    print(" ")

    print(" ")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(f'{fstring("Part Two:", "bk", "wt")}')
    output_length = 12
    max_joltages = calculate_max_joltages(bank_joltages, output_length)
    part_two_ans = sum(max_joltages)
    print(f'The new total output joltage is: {fstring(str(part_two_ans), "wt", "bk")}')
    print(fstring(f"==============================================================", "bk", "bl"))
    print(" ")

    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()