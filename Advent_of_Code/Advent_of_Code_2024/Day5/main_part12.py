import time
import numpy as np
from my_modules.development import fstring
from my_modules.development import print_array

def read_input_data(filename):
    ordered_pairs, pages_to_produce = {}, []
    page_pairs_complete = False
    with open(filename, 'r') as f:
        for line in f:
            if not line.strip():
                page_pairs_complete = True
            elif page_pairs_complete == True:
                pages_to_produce.append(line.strip().split(","))
            else:
                temp = line.strip().split("|")
                try:
                    ordered_pairs[temp[1]][0].append(temp[0])
                except:
                    ordered_pairs[temp[1]] = [[temp[0]],[]]
                try:
                    ordered_pairs[temp[0]][1].append(temp[1])
                except:
                    ordered_pairs[temp[0]] = [[],[temp[1]]]
    return ordered_pairs, pages_to_produce

def check_page_ordering(update, ordered_pairs, pages_to_produce):
    valid_update = True
    for index, page in enumerate(update):
        pages_before = update[:index]
        pages_after = update[index + 1:]
        for j_index, page_before_rule in enumerate(ordered_pairs[page][0]):
            if page_before_rule in pages_after:
                #print(f"Update INVALID: Broke pages before rule: {page_before_rule}")
                valid_update = False
                bad_page_index = update.index(page_before_rule)
                return valid_update, index, page_before_rule, bad_page_index, "Page Before Rule"

        for j_index, page_after_rule in enumerate(ordered_pairs[page][1]):
            if page_after_rule in pages_before:
                #print(f"Update INVALID: Broke pages after rule: {page_after_rule}")
                valid_update = False
                bad_page_index = update.index(page_after_rule)
                return valid_update, index, page_after_rule, bad_page_index, "Page After Rule"
    return valid_update, 0, 0, 0, "none"

def process_updates(ordered_pairs, pages_to_produce):
    update_valid_index = []
    print(" ")
    print(fstring(f"==============================================================", "bk", "wt"))
    print(fstring(f"=========================  PART ONE  =========================", "bk", "wt"))
    print(fstring(f"==============================================================", "bk", "wt"))
    middle_page_sum = 0
    for index, update in enumerate(pages_to_produce):
        valid_update, index, rule_page, break_page_index, rule_string = check_page_ordering(update, ordered_pairs, pages_to_produce)
        if valid_update:
            print(f"Update VALID: {update} ")
            middle_page_sum += int(update[((len(update) - 1)//2)])
            update_valid_index.append(1)
        else:
            print(f"Update INVALID: Broke pages rule: {rule_page}")
            update_valid_index.append(0)
    print(fstring(f"==============================================================", "bk", "wt"))
    print(" ")
    return middle_page_sum, update_valid_index

def process_invalid_updates(update_valid_index, ordered_pairs, pages_to_produce):
    print(" ")
    print(fstring(f"==============================================================", "bk", "wt"))
    print(fstring(f"=========================  PART TWO  =========================", "bk", "wt"))
    print(fstring(f"==============================================================", "bk", "wt"))
    middle_page_sum = 0
    for index, update in enumerate(pages_to_produce):
        if update_valid_index[index] == 1:  # Don't look at the currently valid updates
            continue
        while True:
            valid_update, index, page_rule, break_page_index, rule = check_page_ordering(update, ordered_pairs, pages_to_produce)
            if rule == "Page Before Rule":
                # Swap bad page to after rule break page
                update.insert(break_page_index, update.pop(index))
                continue
            elif rule == "Page After Rule":
                # Swap bad page to after rule break page
                update.insert(break_page_index, update.pop(index))
                continue
            # Once it is fixed then move to next invalid update
            if valid_update:
                middle_page_sum += int(update[((len(update) - 1) // 2)])
                print(f"Fixed Update: {update} ")
                break
    print(fstring(f"==============================================================", "bk", "wt"))
    print(" ")
    return middle_page_sum

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2024\Day5\Puzzle_Input.txt"
    ordered_pairs, pages_to_produce = read_input_data(filename)

    print(" ")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"The pair ordering rules are created as follows:", "bk", "wt"))
    print("Page Number [[Pages Before], [Pages After]]")
    [print(key, value) for key, value in ordered_pairs.items()]
    print(fstring(f"==============================================================", "bk", "bl"))
    print(" ")

    print(" ")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"There are {len(pages_to_produce)} updates to process, these are:", "bk", "wt"))
    [print(update) for update in pages_to_produce]
    print(fstring(f"==============================================================", "bk", "bl"))
    print(" ")

    middle_page_sum, update_valid_index = process_updates(ordered_pairs, pages_to_produce)
    part_one_ans = str(middle_page_sum)

    middle_page_sum = process_invalid_updates(update_valid_index, ordered_pairs, pages_to_produce)
    part_two_ans = str(middle_page_sum)

    print(" ")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(f'{fstring("Part One:", "bk", "wt")}')
    print(f'The middle page sum is: {fstring(part_one_ans, "wt", "bk")}')
    print(fstring(f"==============================================================", "bk", "bl"))
    print(" ")

    print(" ")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(f'{fstring("Part Two:", "bk", "wt")}')
    print(f'The middle page sum is: {fstring(part_two_ans, "wt", "bk")}')
    print(fstring(f"==============================================================", "bk", "bl"))
    print(" ")

    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()