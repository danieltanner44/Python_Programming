import numpy as np
data = []
fI = open(r'D:\Advent_of_Code\Advent_of_Code_2022\Day8\Puzzle_Input.txt', 'r')
for each_line in fI:
    data.append(list(each_line.strip("\n")))
data = np.array(data, dtype=int)
print(data)
print(len(data))
data = np.reshape(data, [len(data), len(each_line)-1])
print(" ")
print("############################################################################")
print("The data has shape: " + str(np.shape(data)))
print("The data is:")
print(data)
print("############################################################################")
counter = 0
for i_row in range(1,np.shape(data)[0] - 1):
    for j_column in range(1, np.shape(data)[1] - 1):
        if np.max(data[:i_row,j_column]) < data[i_row,j_column] or np.max(data[i_row + 1:,j_column]) < data[i_row,j_column]:
            # Visible from top/bottom
            counter += 1
            continue
        elif np.max(data[i_row,:j_column]) < data[i_row,j_column] or np.max(data[i_row,j_column + 1:]) < data[i_row,j_column]:
            # Visible from right/left
            counter += 1
            continue

answer = sum(np.shape(data)*2) - 4 + counter
print("#########################################")
print("The answer is: " + str(answer))
print("#########################################")
fI.close()