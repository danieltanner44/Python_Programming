import os
import numpy as np
f = open(r'D:\Advent_of_Code\Advent_of_Code_2023\Day3\Puzzle_Input.txt', 'r')
counter = 0
for each_line in f:
    line_symbol_mask = []
    line_number_mask = []
    line_full_numbers_array = []
    each_line = each_line.rstrip("\n")
    # Let's find the numbers
    temp = each_line
    for r in ((".", " "), ("*", " "), ("+", " "), ("$", " "), ("#", " "), ("=", " "), ("/", " "), ("&", " "), ("%", " "), ("-", " "), ("@", " ")):
        temp = temp.replace(*r)
    temp = temp.rsplit()
    # Let's preprocess to form a numbers and synbols mask
    counter1 = 0
    print(each_line)
    for i in range(0,len(each_line)):
        try:
            if int(each_line[i]) >= -1:
                line_number_mask.append(1)
                line_symbol_mask.append(0)
                print("check 1")
                line_full_numbers_array.append(int(temp[counter1]))
                print("check 2")
        except:
            line_number_mask.append(0)
            line_full_numbers_array.append(0)
            if str(each_line[i]) == ".":
                line_symbol_mask.append(0)
            else:
                line_symbol_mask.append(3)
            if line_number_mask[i-1] == 1:
                counter1 = counter1 + 1
            pass
    if counter == 0:
        symbol_mask = line_symbol_mask
        print(len(symbol_mask))
        number_mask = line_number_mask
        full_numbers_array = line_full_numbers_array
    else:
        print(len(line_symbol_mask))
        symbol_mask = np.vstack((symbol_mask, line_symbol_mask))
        print(symbol_mask)
        number_mask = np.vstack((number_mask, line_number_mask))
        full_numbers_array = np.vstack((full_numbers_array, line_full_numbers_array))
    counter = counter + 1
# Expand the symbol mask by one unit in all directions
for i in range(1,np.shape(symbol_mask)[0]):
    for j in range(1,np.shape(symbol_mask)[1]):
        if symbol_mask[i,j] == 3:
           for m in range(-1,2):
               for n in range(-1,2):
                    symbol_mask[i + m, j + n] = 5
# Combine the symbol and number masks to see where they overlap
# if the value of the assessment mask is 7 then the number is for a part of the engine. If it is 5 it is within 1 step of a valid symbol
# Now lets find the numbers
total_engine_number = 0
for i in range(0,np.shape(number_mask)[0]):
    tester = []
    for j in range(0,np.shape(number_mask)[1]):
        if symbol_mask[i,j] == 5 and number_mask[i,j] == 1:
            tester.append(1)
            if tester[j-1] == 0:
                total_engine_number = total_engine_number + int(full_numbers_array[i, j])
        else:
            tester.append(0)
print(total_engine_number)
f.close()