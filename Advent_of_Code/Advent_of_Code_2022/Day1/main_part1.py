calorie_count = []
temp = 0
f = open(r'D:\Advent_of_Code\Advent_of_Code_2022\Day1\Puzzle_Input.txt', 'r')
for each_line in f:
    each_line = each_line.rstrip("\n")
    if len(each_line) > 0: # If there is something there read it as a number
        temp += int(each_line)
    else: # If there is nothing there you have reached the end of the elf's calorie log
        calorie_count.append(temp)
        temp = 0
calorie_count.sort(reverse=True) # Reverse sort to find greatest and top three
top_three = sum(calorie_count[0:3])
print("The highest to lowest calories being carried per elf:"+ str(calorie_count))
print(" ")

print("############################################################################")
print("The maximum number of calories carried by an elf is: " + str(max(calorie_count)))
print("The total number of calories carried by the top three elves is: " + str(top_three))
print("############################################################################")
f.close()