f = open(r'D:\Advent_of_Code\Advent_of_Code_2023\Day4\Puzzle_Input.txt', 'r')
total_points = 0
for each_line in f:
    each_line = each_line.rstrip("\n").split()
    if len(each_line) - len(list(set(each_line))) != 0:
        total_points += 2**(len(each_line) - len(list(set(each_line)))-1)
        print(total_points)
f.close()