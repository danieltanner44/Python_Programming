import numpy as np
import time

def reading_input_data(fI):
    workflows, part_ratings, workflow_rule_count = [], [], 0
    do_once = False
    print("Reading block of input data...")
    for each_line in fI:
        workflow_rule_count = each_line.count(":")
        if workflow_rule_count > 0:
            each_line = each_line.strip("\n").replace(",", " ").replace("{", " ").replace("}", "").replace(":", " ").split(" ")
            each_line.insert(0, workflow_rule_count)
            workflows.append(each_line)
        else:
            if do_once != False:
                each_line = each_line[3:len(each_line)-1].replace("m=", " ").replace("a=", " ").replace("s=", " ").replace(",", "").replace("}", "").split(" ")
                part_ratings.append(each_line)
            else:
                do_once = True
                continue
    part_ratings = np.array(part_ratings)
    workflow_indices =dict((zip([item[1] for item in workflows],range(len(workflows)))))
    print("################################")
    print("There were", len(workflows), "workflows detected!")
    print("There were", len(part_ratings), "part ratings detected!")
    print("################################")
    print(" ")
    return workflows, part_ratings, workflow_indices

def process_parts(workflows, part_ratings_i, workflow_indices):
    # Lets process each part through the relevant workflows
    current_workflow_index = "in"
    x, m, a, s = map(int, part_ratings_i[:4])
    while 1 == 1:
        print(current_workflow_index, "->", end="")
        if current_workflow_index == "A":
            print("Accepted")
            parts_total = x + m + a + s
            return parts_total
        elif current_workflow_index == "R":
            print("Rejected")
            return 0
        met_condition = False
        for i in range(workflows[workflow_indices[current_workflow_index]][0]): # Step through each rule
            if eval(workflows[workflow_indices[current_workflow_index]][2 + (i*2)]):
                current_workflow_index = workflows[workflow_indices[current_workflow_index]][2 + (i*2) + 1]
                met_condition = True
                break
        if met_condition == False:
            current_workflow_index = workflows[workflow_indices[current_workflow_index]][2 + (i*2) + 2]
    return parts_total

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    fI = open(r'D:\Advent_of_Code\Advent_of_Code_2023\Day19\Puzzle_Input.txt', 'r')
    # Read all of the input data from Puzzle Input and organise it
    workflows, part_ratings, workflow_indices = reading_input_data(fI)
    total_accepted_parts = 0
    # Now lets process each part
    print("################################")
    print("Mapping", len(part_ratings), "part through workflows...")
    print("################################")
    for i in range(np.shape(part_ratings)[0]):
        parts_total = process_parts(workflows, part_ratings[i], workflow_indices)
        total_accepted_parts += parts_total

    print(" ")
    print("################################")
    print("The answer is:", total_accepted_parts)
    print("################################")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()