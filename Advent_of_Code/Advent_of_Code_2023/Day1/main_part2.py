import os
calibration_value = 0
string_numbers = {"one" : 1,"two" : 2,"three" : 3,"four" : 4,"five" : 5,"six" : 6,"seven" : 7,"eight" : 8,"nine" : 9}
f = open(r'D:\Advent_of_Code\Advent_of_Code_2023\Day1\Puzzle_Input.txt', 'r')
for each_line in f:
    each_line = each_line.rstrip("\n")
    line_indexesf = []
    line_indexesl = []
    first_num = last_num = -1
    for k in range(0,len(string_numbers)):
        search_indexf = each_line.find(list(string_numbers.keys())[k])
        line_indexesf.append(search_indexf)
        search_indexl = each_line.rfind(list(string_numbers.keys())[k])
        line_indexesl.append(search_indexl)
    max_index = max_digit = min_digit = 0
    min_index = len(each_line)
    for k in range(0, len(string_numbers)):
        if line_indexesl[k] >= 0 and line_indexesl[k] > max_index:
            max_index = line_indexesl[k]
            max_digit = k + 1
        if line_indexesf[len(string_numbers)-k-1] >= 0 and line_indexesf[len(string_numbers)-k-1] < min_index:
            min_index = line_indexesf[len(string_numbers)-k-1]
            min_digit = len(string_numbers)-k
    for j in range(0,len(each_line)):
        try:
            if first_num == -1:
                if j < min_index or max_index < 0:
                    first_num = int(each_line[j])
                else:
                    first_num = min_digit
        except:
            pass
        try:
            if last_num == -1:
                if (len(each_line)-j) > max_index:
                    last_num = int(each_line[len(each_line)-j-1])
                else:
                    last_num = max_digit
        except:
            pass
    line_calibration_value = int("%d%d" % (first_num, last_num))
    print("Found line calibration value: " + str(line_calibration_value))
    calibration_value = calibration_value + line_calibration_value
print("Found file calibration value: " + str(calibration_value))
f.close()
