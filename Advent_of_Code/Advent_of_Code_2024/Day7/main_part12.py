import time
import numpy as np
from my_modules.development import fstring
from my_modules.development import print_array
import itertools as it

def read_input_data(filename):
    calibration_equations = []
    with open(filename, 'r') as f:
        for line in f:
            temp = line.strip().replace(":","").split(" ")
            calibration_equations.append([int(element) for element in temp])
    return calibration_equations

def operator_permutations_calculator(num_operators, operator_list):
    # This subroutine generates all possible sets of operators from the list of available operators
    # This can be significant as the number of operator set permutations is n**k
    # Where n is the number of operators that can be used
    # and k is the number of operators missing from the equation
    # So if we are missing 10 operators and for each can choose from a list of three there are
    # 3**10 = 59,049 possible sets of 5 operators that are created by this subroutine!
    for index in range(num_operators):
        temp1 = []
        if index == 0:
            # Start off with the operator set, say ["+", "*", "||"]
            operator_permutations = operator_list
            continue
        # Now loop over all operator lists in the set and add each operator
        # So ["+"] -> [["+", "+"],["+", "*"],["+", "||"]] etc.
        for i, permutation in enumerate(operator_permutations):
            temp2 = []
            # Need to loop over all operators
            # For each create a new sub list which has each original sublist with each operator appended
            for i in range(len(operator_list)):
                temp3 = []
                if i == 0:
                    temp3.append(permutation + ["+"])
                elif i == 1:
                    temp3.append(permutation + ["*"])
                elif i == 2:
                    # Note for Part One the operator list only has two element so this is never reached
                    # For Part Two there are three operators in the list so this is used as required
                    temp3.append(permutation + ["||"])
                temp2.extend(temp3)
            temp1.extend(temp2)
        operator_permutations = temp1
    return operator_permutations

def process_calibration_equations(calibration_equations, operator_list):
    total_calibration_result = 0
    # Each equation is the test value followed by the values
    # Need to find if operators can produce the test value
    # Loop over each equation to check it
    valid_equations = []
    for index, equation in enumerate(calibration_equations):
        # Determine the number of operators missing (number of values - 1)
        num_operators = len(equation[1:]) - 1   # Skip the first index (as test output not value) and one value
        # Determine all the possible permutations of operators needed for equation (brute force - try all)
        operator_permutations = operator_permutations_calculator(num_operators, operator_list)
        # Now check if any permutation of operators provides the test output
        for operator_permutation in operator_permutations:
            for i, value in enumerate(equation[1:-1]):
                # Operators are always evaluated left to right so do one calculation at a time left to right
                if i == 0:
                    calculation_string = str(value) + " " + operator_permutation[i] + " " + str(equation[i + 2])
                    calculation_string = calculation_string.replace(" || ", "")
                    calculation = eval(calculation_string)
                else:
                    calculation_string = str(calculation) + " " + operator_permutation[i] + " " + str(equation[i + 2])
                    calculation_string = calculation_string.replace(" || ", "")
                    calculation = eval(calculation_string)
            # Check if the calculation is equal to the test if it is log and break
            # If not try next permutation of operators, if any are left
            if equation[0] == calculation:
                valid_equations.append([f"#{index}: Equation: {equation}, Operators: {operator_permutation}"])
                total_calibration_result += calculation
                break   # Only need to find first set of operators that work - this could save a lot of time

    return total_calibration_result, valid_equations

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