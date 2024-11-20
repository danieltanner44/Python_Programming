import numpy as np

crates = []
moves = []
fI = open(r'D:\Advent_of_Code\Advent_of_Code_2022\Day5\Puzzle_Input.txt', 'r')
moves_data = False
for each_line in fI:
    if len(each_line) == 1 or moves_data == True:
        if moves_data == False:
            moves_data = True
            continue
        else:
            moves.append(each_line.rstrip("\n").split(" "))
    else:
        crates.append((list(each_line.rstrip("\n"))))
crates = np.array(crates, dtype=str)
crates = np.delete(crates, [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34], 1)
crates = np.delete(crates, [1,3,5,7,9,11,13,15], 1)
crates = np.delete(crates, [-1], 0) # Remove last row
print(crates)
moves = np.array(moves, dtype=str)
moves = np.delete(moves, [0,2,4], 1)
moves = np.array(moves, dtype=int)
print(" ")
print("############################################################################")
print("There are " + str(len(crates)) + " crates!")
print("There are " + str(len(moves)) + " moves required!")
print("############################################################################")

crane_type_model = 9001 # for Part 2 and 9000 for Part 1
for each_move in moves:
    each_move[1] -= 1 # As columns 1 2 3 stored in columns 0 1 2
    each_move[2] -= 1 # As columns 1 2 3 stored in columns 0 1 2
    check = np.where(crates[:,each_move[2]] == " ")
    if len(check[0]) <= each_move[0]: # Need to extend array to track crates
        for i in range(each_move[0] - len(check[0]) + 1):
            crates = np.insert(crates, 0, [" "], axis=0)
    # Find indices for where crates are and where spaces are in the columns they move to
    free_crate_spaces = np.where(crates[:,each_move[2]] == " ")
    crates_to_move = np.where(crates[:, each_move[1]] == " ")
    # Copy crates to new location (note use [::-1] to reverse order of crates)
    if crane_type_model == 9000:
        crates[free_crate_spaces[0][-1] + 1 - each_move[0] : free_crate_spaces[0][-1] + 1, each_move[2]] = crates[crates_to_move[0][-1] + 1: crates_to_move[0][-1] + 1 + each_move[0], each_move[1]][::-1]
    elif crane_type_model == 9001:
        crates[free_crate_spaces[0][-1] + 1 - each_move[0] : free_crate_spaces[0][-1] + 1, each_move[2]] = crates[crates_to_move[0][-1] + 1: crates_to_move[0][-1] + 1 + each_move[0], each_move[1]]
    else:
        print("Crane type model is not valid, choose 9000 or 9001!")
    # Delete crates from old location
    crates[crates_to_move[0][-1] + 1: crates_to_move[0][-1] + 1 + each_move[0], each_move[1]] = " "
print(crates)
answer = []
for i in range(np.shape(crates)[1]):
    temp = np.where(crates[:,i] != " ")
    answer.append(crates[temp[0][0],i])
answer = "".join(answer)

print("#########################################")
print("The answer is: " + answer)
print("#########################################")
fI.close()