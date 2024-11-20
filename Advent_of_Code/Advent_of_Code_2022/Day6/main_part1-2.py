fI = open(r'D:\Advent_of_Code\Advent_of_Code_2022\Day6\Puzzle_Input.txt', 'r')
signal = list(fI.readline())
print(" ")
print("############################################################################")
print("There are " + str(len(signal)) + " characters in the signal!")
print("The signal is:")
print(signal)
print("############################################################################")

detection_lengths = [4, 14]
answer = [0,0]
for i in [0,1]:
    detection_length = detection_lengths[i]
    for element in enumerate(signal):
        if len(set(signal[element[0]:element[0] + detection_length])) == detection_length:
            answer[i] = element[0] + detection_length
            break
print("#########################################")
print("The answers are: ")
print("\t", str(answer[0]), "for Part I - detection of " + str(detection_lengths[0]) + " consecutive and unique elements")
print("\t", str(answer[1]), "for Part II - detection of " + str(detection_lengths[1]) + " consecutive and unique elements")
print("#########################################")
fI.close()