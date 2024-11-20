import os
limits = {"red" : 12, "green" : 13, "blue" : 14}
power_total = 0
f = open(r'D:\Advent_of_Code\Advent_of_Code_2023\Day2\Puzzle_Input.txt', 'r')
counter = 0
for each_line in f:
    each_line = each_line.rstrip("\n")
    # Let's preprocess the line to tidy up the input data and find separators for each draw from the bag
    draw_indexes = []
    for i in range(0,len(each_line)):
        if each_line[i] == ":":
            start_index = i
        elif each_line[i] == ";":
            draw_indexes.append(i)
        # Add start and end indexes
    draw_indexes.insert(0,start_index)
    draw_indexes.append(len(each_line))
    game_number = int(each_line.split()[1].rstrip(":"))
    print("Game Number: ",game_number)
    print("There are: ", str(len(draw_indexes) - 1), "draws on this line...")
    print("Processing line: ",each_line[start_index:len(each_line)])
    print("Identified indices: ",draw_indexes)
    # Now lets process the data for each game
    temp = []
    for i in range(0,(len(draw_indexes)-1)):
        temp = each_line[draw_indexes[i] + 2:draw_indexes[i+1]].rsplit()
        #print(temp, "temp")
        blue_counter = red_counter = green_counter = 0
        for j in range(0,len(temp)):
            #print(j, "j", temp[len(temp) - 1 - j])
            check = temp[len(temp) - 1 - j].rstrip(",")
            if check == "red":
                red_counter = red_counter + int(temp[len(temp) - j - 2])
                # print("found red", red_counter)
            elif check == "green":
                green_counter = green_counter + int(temp[len(temp) - j - 2])
                # print("found green", green_counter)
            elif check == "blue":
                blue_counter = blue_counter + int(temp[len(temp) - j - 2])
                #print("found blue", blue_counter)
        print("For Draw ", i, "found: ",blue_counter, " blue ",green_counter, "green and ", red_counter, "red elf cubes")
        if i == 0:
            max_red = red_counter
            max_green = green_counter
            max_blue = blue_counter
        if max_red  < red_counter:
            max_red = red_counter
        if max_green < green_counter:
            max_green = green_counter
        if max_blue < blue_counter:
            max_blue = blue_counter
    print(max_red, max_green, max_blue)
    print(max_red*max_green*max_blue, "edgerg")
    power_total = power_total + (max_red*max_green*max_blue)
print("The summation of all possible game ids is: ",power_total)
f.close()