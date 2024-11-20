# There is a bug as dictionary[0] != np.sum(total_file_sizes), which it should


import numpy as np
data = []
fI = open(r'D:\Advent_of_Code\Advent_of_Code_2022\Day7\Puzzle_Input.txt', 'r')
for each_line in fI:
    data.append(each_line.strip("\n"))

print(" ")
print("############################################################################")
print("The data has shape: " + str(len(data)))
print("The data is:")
print(data)
print("############################################################################")
structure = [["/"]]
directories = [["/", 0]]
current_directory = 0
for line in data:
    if line[0] == "$":
        reading_directory = False
        if line[2:4] == "cd":
            argument = line[5:]
            if argument == "..":
                # Go back up a directory
                current_directory -= 1
            elif argument == "/":
                # Go to top directory
                current_directory = 0
            else:
                # Go to new directory
                structure.append(["dir " + str(argument)])
                current_directory = len(structure) - 1
                directories.append(["dir " + str(argument), len(structure) - 1])
        elif line[2:4] == "ls":
            reading_directory = True
    elif reading_directory == True:
        structure[current_directory].append(line)
print(" ")
print("#########################################")
print("The determined structure is: ")
print("#########################################")
print(" ")
print(structure)
print(" ")
print("#########################################")
print("The directories and their indices are: ")
print("#########################################")
print(" ")
print(directories)
directories = np.array(directories)

directory_sizes = np.zeros((len(structure), 1), dtype=int)
total_file_sizes = []
for each_directory in reversed(list(directories)):
    file_size = []
    file_name = []
    for element in structure[int(each_directory[1])]:
        if element[0:3] != "dir" and element != "/" and element != "cd ..":
            file_size.append(int(element.split(" ")[0]))
            total_file_sizes.append(int(element.split(" ")[0]))
            file_name.append(element.split(" ")[1])
            directory_sizes[int(each_directory[1])] += file_size[-1]
# Need to propagate subdirectory sizes through
check = np.ones_like(directory_sizes)
while np.max(check) == 1: # Keep going until all directories have been totalled
    for each_directory in reversed(list(directories)):
        if check[int(each_directory[1])] == 1: # So not processed yet
            subdirectory_total = 0
            skip_first = True
            all_subdirectories_complete = True
            for element in structure[int(each_directory[1])]:
                if skip_first == True: # The first element of each sublist is the name of the directory
                    skip_first = False
                    continue
                if element[0:3] == "dir": # For each subdirectory add its total on if it has previously been processed
                    # Walk froward from current index to find the subdirectory of same name
                    index = int(each_directory[1])
                    while 1 == 1:
                        index += 1
                        index = index % len(directories)
                        if element == directories[index, 0]:
                            break
                    if check[index] == 0:  # Subdirectory was processed already
                        subdirectory_total += directory_sizes[index]
                    else:
                        all_subdirectories_complete = False  # If current directory was processed skip it and go to next
            if all_subdirectories_complete == True: # Only add the total if all subdirectories completely processed
                directory_sizes[int(each_directory[1])] += subdirectory_total
                check[int(each_directory[1])] = 0
print(" ")
print("#########################################")
print("The directories and their sizes are: ")
print("#########################################")
print(" ")
print(list(directory_sizes[:,0]))
print(" ")
# Part I: Lets work out how many directories have size less than the required value
answer = np.zeros([2,1], int)
for each_directory in enumerate(directory_sizes):
    if each_directory[1] <= 100000:
        answer[0] += int(each_directory[1][0])

# Part II: Lets work out the smallest directory that would provide the required space
total_disc_space = 70000000
space_needed = 30000000
unused_space = total_disc_space - np.sum(total_file_sizes)
space_to_create = space_needed - unused_space
for elements in np.sort(directory_sizes, 0):
    if elements[0] >= space_to_create:
        answer[1] = elements[0]
        break # Stop when first smallest directory is large enough
print("##############################################################################")
print("The total size of all directories with of size <= 100000 is: " + str(answer[0][0]))
print("##############################################################################")
print("##############################################################################")
print("The smallest directory that can be removed to free space has size: " + str(answer[1][0]))
print("##############################################################################")
fI.close()