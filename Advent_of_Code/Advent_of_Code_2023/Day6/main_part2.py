import numpy as np
import time

extra_wins = np.array([], dtype=np.int64)
distance = np.array([], dtype=np.int64)
counter, ts0 = 0, time.time()
print("Starting time:", time.ctime())
# Lets read all of the input data
f = open(r'D:\Advent_of_Code\Advent_of_Code_2023\Day6\Puzzle_Input_P2.txt', 'r')
data = np.array([], dtype=np.int64)
for each_line in f:
    # Lets read in all the key information
    temp = "".join(each_line.rstrip("/n").split()[1:len(each_line)])
    print(temp)
    data = np.append(data, temp)
    print(data.dtype)
data = data.astype("int64")
# Step through each race
for i in range(0, len(data)//2):
    counter = 0
    # Step through each hold time
    for hold_time in range(0, data[i]):
        if hold_time % 100000 == 0:
            print(hold_time)
        if (data[i] - hold_time) * hold_time > data[i + len(data)//2]:
            counter += 1
    extra_wins = np.append(extra_wins, counter)
    print("For race", i, "of", len(data)//2, "races there were", counter, "extra wins!")
print("Result is:", np.prod(extra_wins))
print(" ")
print("Elapsed time:", round((time.time() - ts0)/3600,2), "hours or", round((time.time() - ts0),1),"seconds!")
print(" ")
print("Finishing time:", time.ctime())