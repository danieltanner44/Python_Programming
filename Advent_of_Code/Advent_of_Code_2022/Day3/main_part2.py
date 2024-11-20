import string

rucksacks = []
fI = open(r'D:\Advent_of_Code\Advent_of_Code_2022\Day3\Puzzle_Input.txt', 'r')
for each_line in fI:
    rucksacks.append(list(each_line.rstrip("\n")))
print(" ")
print("############################################################################")
print("There are "+ str(len(rucksacks)) + " rucksacks!")
print("############################################################################")

# Set priorities
priorities = dict(zip(list(string.ascii_lowercase), range(1,27)))
priorities.update(dict(zip(list(string.ascii_uppercase), range(27,53))))

score = 0
for i in range(len(rucksacks)//3): # Loop over each set of three rucksacks
    found_one = False
    for items_a in rucksacks[3*i]: # Loop over items in first compartment
        if found_one == True:
            break
        for items_b in rucksacks[3*i + 1]: # Loop over items in second compartment
            if found_one == True:
                break
            if items_a == items_b:
                for items_c in rucksacks[3*i + 2]:
                    if items_a == items_c:
                        print("Found matching item: " + str(items_a) + ", with priority: " + str(priorities[items_a]))
                        score += priorities[items_b]
                        found_one = True # Only looking for 1 item so break out once found
                        break

print("#########################################")
print("The total score is: " + str(score))
print("#########################################")
fI.close()