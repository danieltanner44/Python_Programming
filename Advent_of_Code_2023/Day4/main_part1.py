import numpy as np
f = open(r'D:\Advent_of_Code\Advent_of_Code_2023\Day4\Puzzle_Input.txt', 'r')
counter = 0
for each_line in f:
    each_line = each_line.rstrip("\n").split()
    if counter == 0:
        game_data = each_line
        counter = counter + 1
    else:
        game_data = np.vstack((game_data, each_line))
vertical_bar = np.where(np.char.find(game_data[1,:],"|") == 0)[0]
game_data = np.delete(game_data,[0, 1, int(vertical_bar)],1)
total_points = 0
for i in range(0,np.shape(game_data)[0]):
    points = np.shape(game_data)[1] - len(list(set(game_data[i,:])))
    if points > 1:
        points = 1 * 2**(points-1)
    total_points = total_points + points
print(total_points)
f.close()