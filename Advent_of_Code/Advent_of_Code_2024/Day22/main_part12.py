import time
import numpy as np
from my_modules.development import fstring

def read_input_data(filename):
    initial_secret_numbers = []
    with open(filename, 'r') as f:
        for line in f:
            initial_secret_numbers.append(int(line.strip()))
    return initial_secret_numbers

def process_all_secret_numbers(initial_secret_numbers):
    # Generate the secret number sequence from the initial secret numbers
    # Also calculate the sum  of the 2000 secret numbers generated
    # For Part Two also store the last digit sequence of the secret number sequence
    all_sequences = []
    all_last_digit_sequences = []
    number_sum_2000 = 0
    for initial_secret_number in initial_secret_numbers:
        secret_sequence, last_digit_sequence = process_secret_sequence(initial_secret_number)
        number_sum_2000 += secret_sequence[-1]
        all_sequences.append(secret_sequence)
        all_last_digit_sequences.append(last_digit_sequence)
    return number_sum_2000, all_sequences, all_last_digit_sequences

def process_secret_sequence(initial_secret_number):
    # Generate the secret number sequence from the initial secret number
    # Use the three rules to generate the sequence
    current_secret_number = initial_secret_number
    secret_sequence = [current_secret_number]
    # Store the last digit of each as a sequence
    last_digit_sequence = [current_secret_number % 10]

    # Main logic
    for i in range(1, 2000 + 1):
        # Calculate the result of multiplying the secret number by 64. Then, mix this result into the secret number.
        # Finally, prune the secret number.
        next_secret_number = ((current_secret_number * 64) ^ current_secret_number) % 16777216
        # Calculate the result of dividing the secret number by 32. Round the result down to the nearest integer.
        # Then, mix this result into the secret number. Finally, prune the secret number.
        next_secret_number = ((next_secret_number //32) ^ next_secret_number) % 16777216
        # Calculate the result of multiplying the secret number by 2048. Then, mix this result into the secret number.
        # Finally, prune the secret number.
        next_secret_number = ((next_secret_number * 2048) ^ next_secret_number) % 16777216

        secret_sequence.extend([next_secret_number])
        last_digit_sequence.extend([next_secret_number % 10])
        # Update the next secret number to the current one and cycle through again to create next one.
        current_secret_number = next_secret_number
    return secret_sequence, last_digit_sequence

def process_all_sequences(last_digit_sequence):
    # This is the part two logic
    temp_master_value_and_diff_sequence_list = []
    master_value_and_diff_sequence_dict = {}
    # Loop over each last digit sequence
    for digit in last_digit_sequence:
        # Create dictionary of price difference sequence and resultant price {( , , , ): price}
        value_and_diff_sequence_dict = find_diff_sequence_and_price(digit)
        temp_master_value_and_diff_sequence_list.append(value_and_diff_sequence_dict)
    # Loop over each output dictionary and merge all dictionaries to a single dictionary
    # For each 4 digit difference sequence (the key) store the sum of the values for each sequence
    for dictionary in temp_master_value_and_diff_sequence_list:
        for key, value in dictionary.items():
            if key in master_value_and_diff_sequence_dict:
                master_value_and_diff_sequence_dict[key] += value
            else:
                master_value_and_diff_sequence_dict[key] = value
    # The maximum value of the dictionary represents the best outcome for any single four digit difference sequence
    most_bananas_num = max(master_value_and_diff_sequence_dict.values())
    return most_bananas_num

def find_diff_sequence_and_price(sequence):
    value_and_diff_sequence_dict = {}
    # Walk along each sequence and create the difference sequence
    # Store the value associated with the sequence to a dictionary with a key that is the 4 digit sequence
    for index, number in enumerate(sequence[1:-3], start=0):
        sequence_difference = tuple(np.diff(sequence[index:index + 5]))
        if sequence_difference not in value_and_diff_sequence_dict:
            # Only need to store the first occurrence of any four digit difference sequence
            value_and_diff_sequence_dict[sequence_difference] = sequence[index + 4]
    return value_and_diff_sequence_dict

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2024\Day22\Puzzle_Input.txt"
    initial_secret_numbers = read_input_data(filename)

    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=======================  Puzzle Input  =======================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"There are {len(initial_secret_numbers)} secret numbers, namely: ", "bk", "wt"))
    print(initial_secret_numbers)
    print(fstring(f"====================  Puzzle Input - End =====================", "bk", "bl"))

    number_sum_2000, all_sequences, all_last_digit_sequences = process_all_secret_numbers(initial_secret_numbers)
    part_one_ans = str(number_sum_2000)

    most_bananas_num = process_all_sequences(all_last_digit_sequences)
    part_two_ans = str(most_bananas_num)

    print(" ", end="\n\n")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=========================  ANSWERS  ==========================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))
    print(f'{fstring("Part One:", "bk", "wt")}')
    print(f'The sum of the 2000th secret numbers is: {fstring(part_one_ans, "wt", "bk")}')
    print(fstring(f"==============================================================", "bk", "bl"))
    print(f'{fstring("Part Two:", "bk", "wt")}')
    print(f'The most bananas that can be got is: {fstring(part_two_ans, "wt", "bk")}')
    print(fstring(f"==============================================================", "bk", "bl"))
    print(" ")

    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()