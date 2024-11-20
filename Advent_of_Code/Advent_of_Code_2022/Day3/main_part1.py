import string

first_compartment, second_compartment = [], []
fI = open(r'D:\Advent_of_Code\Advent_of_Code_2022\Day3\Puzzle_Input.txt', 'r')
for each_line in fI:
    first_compartment.append(list(each_line.rstrip("\n"))[:len(each_line)//2])
    second_compartment.append(list(each_line.rstrip("\n"))[len(each_line)//2:])
print(" ")
print("############################################################################")
print("There are "+ str(len(first_compartment)) + " rucksacks!")
print("############################################################################")

# Set priorities
priorities = dict(zip(list(string.ascii_lowercase), range(1,27)))
priorities.update(dict(zip(list(string.ascii_uppercase), range(27,53))))

score = 0
for i in range(len(first_compartment)): # Loop over each rucksack
    found_one = False
    for items_a in first_compartment[i]: # Loop over items in first compartment
        if found_one == True: # Only looking for 1 item so break out once found
            break
        for items_b in second_compartment[i]: # Loop over items in second compartment
            if items_a == items_b and found_one == False:
                print("Found matching item: " + str(items_a) + ", with priority: " + str(priorities[items_a]))
                score += priorities[items_b]
                found_one = True # Only looking for 1 item so break out once found
                break

print("#########################################")
print("The total score is: " + str(score))
print("#########################################")
fI.close()