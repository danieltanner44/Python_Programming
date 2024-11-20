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

def complete_lines(stripped_line, first_bracket_found):
    dict_bracket_pairs = {"(" : ")","[" : "]","{" : "}","<" : ">", ")" : "(","]" : "[","}" : "{",">" : "<"}
    completion_sequence = ""
    for character in stripped_line[::-1]:
        completion_sequence += dict_bracket_pairs[character]
    return completion_sequence

def score_result(found_brackets):
    dict_scorer = {")": 3, "]": 57, "}": 1197, ">": 25137}
    result = 0
    for character in dict_scorer.keys():
        result += found_brackets.count(character) * dict_scorer[character]
    return result

def score_completion_sequences(completion_sequences):
    dict_scorer = {")": 1, "]": 2, "}": 3, ">": 4}
    all_completion_scores = []
    for sequence in completion_sequences:
        completion_score = 0
        for character in sequence:
            if character in dict_scorer:
                completion_score = (completion_score*5) + dict_scorer[character]
            else:
                print(f"Warning: '{character}' not found in dict_scorer")  # Handle unexpected characters
        all_completion_scores.append(completion_score)
    all_completion_scores = sorted(all_completion_scores)
    completion_score = all_completion_scores[(len(all_completion_scores)//2)]
    return completion_score

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
    completion_sequences = []
    for index, line in enumerate(input_data):
        print("")
        print("==========================")
        print("Sequence", index)
        print("==========================")
        print("Input sequence:", line)
        stripped_line = remove_bracket_pairs(line)
        print("Stripped sequence:", stripped_line)
        first_bracket_found = find_first_missing_bracket(stripped_line)
        if len(first_bracket_found) == 0:
            print("Sequence is incomplete!")
            completion_sequence = complete_lines(stripped_line, first_bracket_found)
            completion_sequences.append(completion_sequence)
            print(first_bracket_found)
        else:
            print("Located incorrect bracket:", first_bracket_found)
            found_brackets += first_bracket_found

    syntax_error_score = score_result(found_brackets)
    print("Syntax error score is:", syntax_error_score)
    print(" ")
    completion_score = score_completion_sequences(completion_sequences)
    print(" ")
    print("==============================================================")
    print("The syntax error score is:",syntax_error_score)
    print("==============================================================")
    print(" ")
    print("==============================================================")
    print("The completion score is:", completion_score)
    print("==============================================================")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()