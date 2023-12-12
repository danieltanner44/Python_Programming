f = open(r'D:\Advent_of_Code\Advent_of_Code_2023\Day4\Puzzle_Input.txt', 'r')
total_points = 0
for each_line in f:
    total_points += round(2**(len(each_line.rstrip("\n").split()) - len(list(set(each_line.rstrip("\n").split())))-1))
f.close()
print(total_points)