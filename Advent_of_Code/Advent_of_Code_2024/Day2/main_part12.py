import time
from my_modules.development import fstring
from my_modules.development import determine_num_duplicates_in_list

def read_input_data(filename):
    input_data = []
    with open(filename, 'r') as f:
        for line in f:
            temp = line.strip().split(" ")
            temp = [int(element) for element in temp]
            input_data.append(temp)
    return input_data

def assess_report(report):
    levels_increasing, levels_decreasing = False, False  # Assume false and check
    adjacent_levels_in_range = True  # Assume true and check

    if sorted(report) == report:  # Check if increasing
        levels_increasing = True
    elif sorted(report, reverse=True) == report:  # Check if decreasing
        levels_decreasing = True
    for i in range(len(report) - 1):  # Check if step to adjacent levels in range
        if abs(report[i] - report[i + 1]) < 1 or abs(report[i] - report[i + 1]) > 3:  # Check reports out of range
            adjacent_levels_in_range = False

    # Now check if one condition is met
    if (levels_increasing or levels_decreasing) and adjacent_levels_in_range:
        outcome = "Safe"
    else:
        outcome = "Unsafe"
    return outcome

def check_safety_of_reports(input_data):
    part1_num_safe_reports, part2_num_safe_reports = 0, 0  # Count safe reports
    for report in input_data:
        outcome = assess_report(report)
        # Part 1: Logic
        if outcome == "Safe":
            part1_num_safe_reports += 1
        else:
            # Part 2: Logic
            # If not safe try removing one value at a time and trying again (brute force)
            # If one safe configuration is found stop looking and move to next report
            for index in range(len(report)):
                temp_report = report.copy()
                temp_report.pop(index)
                outcome = assess_report(temp_report)
                if outcome == "Safe":
                    part2_num_safe_reports += 1
                    break

    return part1_num_safe_reports, part2_num_safe_reports

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2024\Day2\Puzzle_Input.txt"
    input_data = read_input_data(filename)



    print(" ")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"There are {str(len(input_data))} reports to process, they are:", "bk", "wt"))
    [print(input_list) for input_list in input_data]
    print(fstring(f"==============================================================", "bk", "bl"))
    print(" ")

    part1_num_safe_reports, part2_num_safe_reports = check_safety_of_reports(input_data)

    part_one_ans = str(part1_num_safe_reports)

    part_two_ans = str(part1_num_safe_reports + part2_num_safe_reports)


    print(" ")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(f'{fstring("Part One:", "bk", "wt")}')
    print(f'The number of safe reports is: {fstring(part_one_ans, "wt", "bk")}')
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