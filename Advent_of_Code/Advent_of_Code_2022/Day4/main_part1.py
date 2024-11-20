elf_assignments = []
fI = open(r'D:\Advent_of_Code\Advent_of_Code_2022\Day4\Puzzle_Input.txt', 'r')
for each_line in fI:
    elf_assignments.append((list(each_line.rstrip("\n").replace("-",",").split(","))))
# They are read as strings so lets convert to integers
elf_assignments = [[int(assignment) for assignment in assignments] for assignments in elf_assignments]
print(" ")
print("############################################################################")
print("There are "+ str(len(elf_assignments)) + " assignments!")
print(elf_assignments)
print("############################################################################")

# If one is contained in the other can just check the endpoints
counter = 0
for assignments in elf_assignments: # Loop over each pair of assignments
    if assignments[0] <= assignments[2] and assignments[1] >= assignments[3]:  # 2nd contained in 1st
        counter += 1
    elif assignments[2] <= assignments[0] and assignments[3] >= assignments[1]:  # 1st contained in 2nd
        counter += 1

print("#########################################")
print("The total score is: " + str(counter)) # 872 too high, 501 TOO HIGH
print("#########################################")
fI.close()