import time
import numpy as np
from my_modules.development import fstring
from my_modules.development import print_array
import itertools as it

def read_input_data(filename):
    signal_map = []
    with open(filename, 'r') as f:
        for line in f:
            temp = line.strip().replace(":","").split(" ")
            calibration_equations.append([int(element) for element in temp])
    return calibration_equations


def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2024\Day7\Puzzle_Input.txt"
    calibration_equations = read_input_data(filename)

    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=======================  Puzzle Input  =======================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"There are {len(calibration_equations)} calibration equations, they are as follows:", "bk", "wt"))
    [print(equation) for equation in calibration_equations]
    print(fstring(f"====================  Puzzle Input - End =====================", "bk", "bl"))

    print(" ", end="\n\n")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=========================  PART ONE  =========================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))

    operator_list = [["+"], ["*"]]
    total_calibration_result, valid_equations = process_calibration_equations(calibration_equations, operator_list)
    part_one_ans = str(total_calibration_result)

    print(fstring(f"The valid equations are: ", "bk", "wt"))
    [print(equation[0]) for equation in valid_equations]
    print(fstring(f"======================  PART ONE - END  ======================", "bk", "bl"))

    print(" ", end="\n\n")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=========================  PART TWO  =========================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))

    operator_list = [["+"], ["*"], ["||"]]
    total_calibration_result, valid_equations = process_calibration_equations(calibration_equations, operator_list)
    print(fstring(f"The valid equations are: ", "bk", "wt"))
    [print(equation[0]) for equation in valid_equations]

    part_two_ans = str(total_calibration_result)
    print(fstring(f"======================  PART TWO - END  ======================", "bk", "bl"))

    print(" ", end="\n\n")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=========================  ANSWERS  ==========================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))
    print(f'{fstring("Part One:", "bk", "wt")}')
    print(f'The total calibration result is: {fstring(part_one_ans, "wt", "bk")}')
    print(fstring(f"==============================================================", "bk", "bl"))
    print(f'{fstring("Part Two:", "bk", "wt")}')
    print(f'The total calibration result is: {fstring(part_two_ans, "wt", "bk")}')
    print(fstring(f"==============================================================", "bk", "bl"))
    print(" ")

    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()