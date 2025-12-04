import time
from my_modules.development import fstring

def read_input_data(filename):
    input_rotations = []
    with open(filename, 'r') as f:
        for line in f:
            temp = line.strip()
            input_rotations.append([temp[0],int(temp[1:])])
    return input_rotations

def determine_code(input_rotations, starting_index):
    part_one_code, part_two_code = 0, 0
    current_index = starting_index
    for rotation in input_rotations:
        # Undertake rotation
        initial_index = current_index
        if rotation[0] == "L":
            current_index -= rotation[1]
            # Subtract the rotation from the current position
            # Consider each case of the result:
            # It is negative and did not start at zero
            # It is negative and started at zero
            # It landed on zero
            # Else (e.g., it stayed positive)
            if current_index < 0 and initial_index != 0:
                zeros_met = (abs(current_index) // 100) + 1
            elif current_index < 0:
                zeros_met = (abs(current_index) // 100)
            elif current_index == 0:
                zeros_met = 1
            else:
                zeros_met = 0
        elif rotation[0] == "R":
            current_index += rotation[1]
            # Add current position (always positive) to positive rotation
            # Integer division gives number of times zero was encountered
            zeros_met = abs(current_index) // 100
        else:
            ValueError("INPUT ERROR!")

        # Update the position to account for wraparound, must stay in range 0,99
        current_index = current_index % 100

        # For Part One count up number of zeros reached to determine part one code
        if current_index == 0:
            part_one_code += 1

        part_two_code += zeros_met
    return part_one_code, part_two_code

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2025\Day1\Puzzle_Input.txt"
    input_rotations = read_input_data(filename)

    print(" ")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"There are {str(len(input_rotations))} input rotations to process, they are:", "bk", "wt"))
    [print(input_list) for input_list in input_rotations]
    print(fstring(f"==============================================================", "bk", "bl"))
    print(" ")

    starting_index = 50
    part_one_ans, part_two_ans = determine_code(input_rotations, starting_index)

    print(" ")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(f'{fstring("Part One:", "bk", "wt")}')
    print(f'The code to unlock the safe is: {fstring(str(part_one_ans), "wt", "bk")}')
    print(fstring(f"==============================================================", "bk", "bl"))
    print(" ")

    print(" ")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(f'{fstring("Part Two:", "bk", "wt")}')
    print(f'The overall max register value is: {fstring(str(part_two_ans), "wt", "bk")}')
    print(fstring(f"==============================================================", "bk", "bl"))
    print(" ")

    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()