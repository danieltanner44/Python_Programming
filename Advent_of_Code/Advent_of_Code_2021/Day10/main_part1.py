import time

def read_input_data(filename):
    input_data = []
    with open(filename, 'r') as f:
        for each_line in f:
            input_data.append(each_line.strip())
    return input_data

def remove_bracket_pairs(line):
    while True:
        length_check = len(line)
        for pairs in ["()","[]","{}","<>"]:
            line = line.replace(pairs, "")
        if len(line) == length_check:
            return line
    return None

def find_first_missing_bracket(stripped_line):
    for index, character in enumerate(stripped_line):
        if character in [")", "]", "}", ">"]:
            return character
    return ""

def score_result(found_brackets):
    dict_scorer = {")": 3, "]": 57, "}": 1197, ">": 25137}
    result = 0
    for character in dict_scorer.keys():
        result += found_brackets.count(character) * dict_scorer[character]
    return result

def main():
    # progress_bar(days, days_to_model)
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = f"D:\Python_Programming\Advent_of_Code\Advent_of_Code_2021\Day10\Puzzle_Input.txt"
    input_data = read_input_data(filename)
    print("The input data is:")
    print(input_data)
    found_brackets = []
    for line in input_data:
        stripped_line = remove_bracket_pairs(line)
        first_bracket_found = find_first_missing_bracket(stripped_line)
        found_brackets += first_bracket_found
    result = score_result(found_brackets)
    print(" ")
    print("==============================================================")
    print("The syntax score is:",result)
    print("==============================================================")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()