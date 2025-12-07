import time
import numpy as np
from my_modules.development import fstring

def read_input_data(filename):
    # Read input file to get the problems and operations to be applied
    # For Part One the spaces in the data do not matter
    # For Part Two the spaces must be preserved
    problems = []
    problems_with_spaces = [] # For Part_Two
    operations = []
    with open(filename, 'r') as f:
        for line in f:
            temp = line.replace("\n", "")
            # Here a space is added to the end of each line
            # This helps later to the code completes the last calculation
            temp = temp[::-1]
            # For the problems - Part Two
            problems_with_spaces.extend([temp])
            temp = line.strip().split(" ")
            try:
                # For the problems - Part One
                temp = [int(i) for i in temp if len(i) != 0]
                problems.append(temp)
            except:
                # For the operations - Part One and Two
                temp = [i for i in temp if len(i) != 0]
                operations.extend(temp)
    # Reform as np array so can slice in problem direction
    problems = np.array(problems, dtype=int)
    return problems, operations, problems_with_spaces

def evaluate_problems(problems, operations):
    sum_problem_answers = 0
    size = np.shape(problems)
    for column in range(0,size[1]):
        evaluation_str = ""
        for number in problems[:,column]:
            # Create a string with all numbers separated by operators
            evaluation_str += f"{str(number)} {operations[column]} "
        # Truncate the final operator as not needed
        evaluation_str = evaluation_str[:-2]
        # Evaluate the answers to each problem and accumulate the sum
        sum_problem_answers += int(eval(evaluation_str))
    return sum_problem_answers

def evaluate_problems_cephalopods(problems_with_spaces, operations):
    sum_problem_answers = 0
    evaluation_str = ""
    # Track which column is used to have the appropriate operator
    column_number = 0
    # Reverse directions so can read from left-right
    problems_with_spaces = problems_with_spaces[:-1]
    operations = operations[::-1]
    for index, character_index in enumerate(range(0, len(problems_with_spaces[0]))):
        # Read the characters from each problem line from left-right
        temp_evaluation_str = ""
        for problem_line in problems_with_spaces:
            # Read the character in the same position on each problem line and add to string
            temp_evaluation_str += f"{problem_line[character_index]}"
        # Check the string that was just read
        temp = [character for character in temp_evaluation_str]
        temp = list(set(temp))
        # If it is only spaces then reading the numbers is complete
        # Then add it to the running total and reset the string
        if temp[0] == " " and len(temp) == 1:
            # Evaluate the current problem and add answer to total
            sum_problem_answers += int(eval(evaluation_str[:-3]))
            # Reset the string and move index to next problem
            evaluation_str = ""
            column_number += 1
        else:
            # If last loop read numbers then add operator and continue to read the next number in problem
            evaluation_str += temp_evaluation_str + f" {operations[column_number]} "
            continue
    # Evaluate the last problem and add answer to total
    sum_problem_answers += int(eval(evaluation_str[:-3]))
    return sum_problem_answers

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = (r"D:\Python_Projects\Python_Programming\Advent_of_Code\Advent_of_Code_2025\Day6\Puzzle_Input.txt")
    problems, operations, problems_with_spaces = read_input_data(filename)

    print(" ")
    print(fstring(f"=================================================================", "bk", "bl"))
    print(fstring(f"There are {str(len(problems))} problems to process...", "bk", "wt"))
    print(fstring(f"=================================================================", "bk", "bl"))
    print(" ")

    print(" ")
    print(fstring(f"=================================================================", "bk", "bl"))
    print(f'{fstring("Part One:", "bk", "wt")}')
    sum_problem_answers = evaluate_problems(problems, operations)
    part_one_ans = sum_problem_answers
    print(f'The grand total of summing the problem answers is: {fstring(str(part_one_ans), "wt", "bk")}')
    print(fstring(f"=================================================================", "bk", "bl"))
    print(" ")

    print(" ")
    print(fstring(f"=================================================================", "bk", "bl"))
    print(f'{fstring("Part Two:", "bk", "wt")}')
    sum_problem_answers = evaluate_problems_cephalopods(problems_with_spaces, operations)
    part_two_ans = sum_problem_answers
    print(f'The grand total of summing the problem answers is: {fstring(str(part_two_ans), "wt", "bk")}')
    print(fstring(f"=================================================================", "bk", "bl"))
    print(" ")

    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()