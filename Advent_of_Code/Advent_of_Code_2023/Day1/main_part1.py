import os
calibration_value = 0
f = open(r'D:\Advent_of_Code\Advent_of_Code_2023\Day1\Puzzle_Input.txt', 'r')
for each_line in f:
    each_line = each_line.rstrip("\n")
    first_num = last_num = 10
    for j in range(0,len(each_line)):
        try:
            if first_num == 10:
                first_num = int(each_line[j])
        except:
            pass
        try:
            if last_num == 10:
                last_num = int(each_line[len(each_line)-j-1])
        except:
            pass
    line_calibration_value = int("%d%d" % (first_num, last_num))
    print("Found line calibration value: " + str(line_calibration_value))
    calibration_value = calibration_value + line_calibration_value
print("Found file calibration value: " + str(calibration_value))
f.close()