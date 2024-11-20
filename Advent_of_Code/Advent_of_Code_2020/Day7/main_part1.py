import time

def read_input_data(filename):
    input_data = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            temp = line.replace(" contain" , ",").replace(" bags", "").replace(" bag","").replace(".","").split(", ")
            input_data.append(temp)
    # Convert regulations to dictionary for ease of processing
    luggage_regulations = {}
    for luggage_layout in input_data:
        temp_ins = []
        for element in luggage_layout[1:]:
            if element == "no other":
                temp = (0, "no other")
            else:
                temp_num, temp_string_1, temp_string_2  = element.split(" ")
                temp = (int(temp_num), temp_string_1+" "+temp_string_2)
            temp_ins.append(temp)
        luggage_regulations[luggage_layout[0]] = temp_ins
    return luggage_regulations

def process_each_bag(luggage_regulations, key):
    gold_bag_counter = 0
    shiny_bag_tracker = 0
    backlog_list_bags_to_process = list(luggage_regulations[key])
    while backlog_list_bags_to_process:
        current_bag = backlog_list_bags_to_process.pop(0)
        if key == "shiny gold":
            shiny_bag_tracker += current_bag[0]
        if current_bag[1] == "shiny gold":
            gold_bag_counter += current_bag[0]
        next_bags = luggage_regulations[current_bag[1]]
        if next_bags[0][1] != "no other":
            new_bags = []
            for bag in next_bags:
                new_bags += [(bag[0] * current_bag[0], bag[1])]
            backlog_list_bags_to_process = backlog_list_bags_to_process + new_bags
    return gold_bag_counter, shiny_bag_tracker
def process_luggage_combinations(luggage_regulations):
    counter = 0
    for key in luggage_regulations:
        # Skip if the bag as not other bags inside
        if luggage_regulations[key][0][1] == "no other":
            continue
        # For each bag work through all the internal bags
        gold_bag_counter, shiny_bag_tracker = process_each_bag(luggage_regulations, key)
        # Part 1
        if gold_bag_counter >= 1:
            counter += 1
        # Part 2
        if key == "shiny gold":
            num_bags_in_shiny_gold_bag = shiny_bag_tracker
    return counter, num_bags_in_shiny_gold_bag

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2020\Day7\Puzzle_Input.txt"
    luggage_regulations = read_input_data(filename)
    print("The initial data provides " + str(len(luggage_regulations)) + " rule sets for luggage regulation:")
    print(luggage_regulations)

    counter, num_bags_in_shiny_gold_bag = process_luggage_combinations(luggage_regulations)

    print(" ")
    print("====================================================================")
    print("PART 1: The number of bags with at least on Shiny Gold bag is:", counter)
    print("====================================================================")
    print(" ")
    print(" ")
    print("====================================================================")
    print("PART 2: The number of bags in a Shiny Gold bag is:", num_bags_in_shiny_gold_bag)
    print("====================================================================")
    print(" ")

    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()