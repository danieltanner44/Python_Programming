import numpy as np
data = []
fI = open(r'D:\Advent_of_Code\Advent_of_Code_2022\Day8\Puzzle_Input.txt', 'r')
for each_line in fI:
    data.append(list(each_line.strip("\n")))
data = np.array(data, dtype=int)
print(data)
print(len(data))
data = np.reshape(data, [len(data), len(each_line) - 1])
print(" ")
print("############################################################################")
print("The data has shape: " + str(np.shape(data)))
print("The data is:")
print(data)
print("############################################################################")
scenic_scores = []
for i_row in range(1,np.shape(data)[0] - 1):
    for j_column in range(1, np.shape(data)[1] - 1):
        counter = [1, 1, 1, 1]
        current_index = j_column - 1
        while data[i_row,j_column] > data[i_row,current_index] and current_index != 0: # Walk left
            counter[0] += 1
            current_index -= 1
        current_index = j_column + 1
        while data[i_row,j_column] > data[i_row,current_index] and current_index != np.shape(data)[1] - 1: # Walk right
            counter[1] += 1
            current_index += 1
        current_index = i_row - 1
        while data[i_row, j_column] > data[current_index, j_column] and current_index != 0:  # Walk up
            counter[2] += 1
            current_index -= 1
        current_index = i_row + 1
        while data[i_row, j_column] > data[current_index, j_column] and current_index != np.shape(data)[0] - 1:  # Walk down
            counter[3] += 1
            current_index += 1
        scenic_scores.append(np.prod(np.array(counter)))

print("The scenic scores are: ", scenic_scores)
print("#########################################")
print("The maximum scenic score is: " + str(np.max(scenic_scores)))
print("#########################################")
fI.close()