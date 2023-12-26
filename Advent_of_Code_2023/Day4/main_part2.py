f = open(r'D:\Advent_of_Code\Advent_of_Code_2023\Day4\Puzzle_Input.txt', 'r')
winners_list = []
counter = 0
for each_line in f:
    number_of_winners = len(each_line.rstrip("\n").split()) - (len(list(set(each_line.rstrip("\n").split()))))
    try:
        winners_list[counter] += 1
    except:
        winners_list.append(1)
        pass
    for i in range(1, number_of_winners + 1):
        try:
            winners_list[counter + i] += winners_list[counter]
        except:
            winners_list.append(1)
            winners_list[counter + i] = winners_list[counter]
            pass
    print("Card ", counter + 1, "had ", number_of_winners, " matches and the winners list is: ", winners_list)
    counter += 1
f.close()
print("The number of total scratchcards is: ", sum(winners_list))