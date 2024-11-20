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
    if what_beats_hand[hand[0]] == hand[1]: # You win
        score += values_winning_hands[hand[1]] + 6 # Six point bonus for winning
        # print("Win")
    elif values_winning_hands[hand[0]] == values_winning_hands[hand[1]]: # Draw
        score += values_winning_hands[hand[1]] + 3  # Three point bonus for draw
        # print("Draw")
    else: # They win
        score += values_winning_hands[hand[1]]  # No bonus for losing
        # print("Loss")
print("The total score is: " + str(score)) # 11936 too low, too low 109
f.close()