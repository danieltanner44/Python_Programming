import numpy as np

data = []
f = open(r'D:\Advent_of_Code\Advent_of_Code_2022\Day2\Puzzle_Input.txt', 'r')
for each_line in f:
    each_line = each_line.rstrip("\n").split(" ")
    data.append(each_line)
data = np.array(np.reshape(data, [len(data), 2]), dtype=str)
print(" ")
print("############################################################################")
print("There are "+ str(np.shape(data)[0]) + " hands!")
print(data)
print("############################################################################")

values_winning_hands = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
what_beats_hand = {"A" : "Y", "B": "Z", "C": "X"}

score = 0
for hand in data:
    if hand[1] == "Y": # I draw
        score += values_winning_hands[hand[0]] + 3  # Three point bonus for draw
    elif hand[1] == "Z": # I Win
        score += values_winning_hands[what_beats_hand[hand[0]]] + 6  # Six point bonus for winning
    else: # I lose
        score += (((values_winning_hands[hand[0]] -1) + 2)%3) + 1 # No bonus for losing
print("The total score is: " + str(score)) # 11936 too low, too low 109
f.close()