import os
import numpy as np
f = open(r'D:\Advent_of_Code\Advent_of_Code_2023\Day3\Puzzle_Input.txt', 'r')
counter = 0
index = 1
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
                line_full_numbers_array.append(int(temp[counter1]))
        except:
            line_number_mask.append(0)
            line_full_numbers_array.append(0)
            if str(each_line[i]) == "*":
                line_symbol_mask.append(index)
                index = index + 1
            else:
                line_symbol_mask.append(0)
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
        number_mask = np.vstack((number_mask, line_number_mask))
        full_numbers_array = np.vstack((full_numbers_array, line_full_numbers_array))
    counter = counter + 1
# Expand the symbol mask by one unit in all directions
print(symbol_mask)
print(symbol_mask + number_mask)
# Combine the symbol and number masks to see where they overlap
# if the value of the assessment mask is 7 then the number is for a part of the engine. If it is 5 it is within 1 step of a valid symbol
# Now lets find the numbers
total_engine_number = 0
index = 1
tester = []
for i in range(0,np.shape(number_mask)[0]):
    for j in range(0,np.shape(number_mask)[1]):
        if symbol_mask[i,j] == index:
            index = index + 1
            for m in range(-1, 2):
                for n in range(-1, 2):
                    if full_numbers_array[i + m, j + n] != 0:
                        tester.append(full_numbers_array[i + m, j + n])
            print(tester, " tester")
            neighbouring_numbers = list(set(tester))
            tester = []
            if len(neighbouring_numbers) == 2:
                total_engine_number = total_engine_number + int(neighbouring_numbers[0]*neighbouring_numbers[1])
            elif len(neighbouring_numbers) > 2:
                print("oh oh: ", i)
                print(neighbouring_numbers)
print(symbol_mask)
print(symbol_mask + full_numbers_array)
print(total_engine_number)
f.close()