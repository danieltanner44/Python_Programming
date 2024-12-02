import time
from my_modules.development import fstring
from my_modules.development import determine_num_duplicates_in_list

def read_input_data(filename):
    input_numbers0, input_numbers1  = [], []
    with open(filename, 'r') as f:
        for line in f:
            temp = line.strip().split("   ")
            input_numbers0.append(int(temp[0]))
            input_numbers1.append(int(temp[1]))
        input_numbers = [sorted(input_numbers0)] + [sorted(input_numbers1)]
    return input_numbers

def process_number_differences(input_numbers):
    total_difference = 0
    for i in range(len(input_numbers[0])):
        total_difference += abs(input_numbers[0][i] - input_numbers[1][i])
    return total_difference

def process_duplication_counts(input_numbers):
    total_similarity_score = 0
    for number in input_numbers[0]:
        list_1_duplicates = determine_num_duplicates_in_list(input_numbers[1])
        try:
            total_similarity_score += number * list_1_duplicates[number]
        except:
            pass
    return total_similarity_score

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2024\Day1\Puzzle_Input.txt"
    input_numbers = read_input_data(filename)

    print(" ")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"There are {str(len(input_numbers[0]))} input numbers to process, they are:", "bk", "wt"))
    [print(input_list) for input_list in input_numbers]
    print(fstring(f"==============================================================", "bk", "bl"))
    print(" ")

    total_difference = process_number_differences(input_numbers)
    part_one_ans = str(total_difference)

    total_similarity_score = process_duplication_counts(input_numbers)
    part_two_ans = str(total_similarity_score)


    print(" ")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(f'{fstring("Part One:", "bk", "wt")}')
    print(f'The number of lit elements is: {fstring(part_one_ans, "wt", "bk")}')
    print(fstring(f"==============================================================", "bk", "bl"))
    print(" ")

    print(" ")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(f'{fstring("Part Two:", "bk", "wt")}')
    print(f'The overall max register value is: {fstring(part_two_ans, "wt", "bk")}')
    print(fstring(f"==============================================================", "bk", "bl"))
    print(" ")

    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()