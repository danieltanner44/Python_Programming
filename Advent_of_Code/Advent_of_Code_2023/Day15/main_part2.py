import numpy as np
import time

def reading_input_data(fI):
    print("Reading block of input data...")
    data = fI.readline()
    data = (data.strip("\n")).split(",")[:]
    print("The data looks like this:",data)
    return data

def process_steps(data):
    focal_length = box_to_use = np.array([], dtype=int)
    step_type = np.array([], dtype = str)
    for step in data:
        temp_value, do_once = 0, False
        temp_type = ""
        temp_focal_length = 0
        for letter in step:
            # Hash the label to find the box to use
            if letter != "=" and letter != "-" and do_once == False:
                temp_value = ((ord(letter) + temp_value)*17)%256
            # Work out if adding or removing lenses
            elif letter == "=" or letter == "-":
                temp_type = letter
                do_once = True
            else:
                temp_focal_length = letter
        box_to_use = np.append(box_to_use, temp_value)
        step_type = np.append(step_type, temp_type)
        focal_length = np.append(focal_length, temp_focal_length)
    return box_to_use, step_type, focal_length

def process_boxes(box_to_use, step_type,focal_length, data):
    ordered_boxes = [[] for _ in range(256)] # each row is a box
    box_to_use = np.array((box_to_use),dtype=int)
    for i in range(len(box_to_use)):
        label = data[i].replace("=", " ").replace("-", " ")
        length = len(label)
        print("############################")
        if step_type[i] == "-":
            print("Processing:", label, i, step_type[i], length, label[0:length - 1])
            # Want to go to relevant box and remove the lens with the given label
            for k in range(len(ordered_boxes[box_to_use[i]])):
                if ordered_boxes[box_to_use[i]][k][0:length - 1] == label[0:length - 1]:
                    ordered_boxes[box_to_use[i]].pop(k) # remove from set - automatically shuffles others up!
                    break
        elif step_type[i] == "=":
            print("Processing:", label, i, step_type[i], length, label[0:length - 2])
            match_found = False
            for k in range(len(ordered_boxes[box_to_use[i]])):
                # If label already present in box then Replace with new lens (no order change)
                if ordered_boxes[box_to_use[i]][k][0:length - 2] == label[0:length - 2]:
                    ordered_boxes[box_to_use[i]][k] = label
                    match_found = True
                    break
            # If not present then add the lens to box with the required focal length
            if match_found == False:
                ordered_boxes[box_to_use[i]].append(label)
    return ordered_boxes

def calculate_the_score(ordered_boxes, focal_length):
    total_score = 0
    for i in range(len(ordered_boxes)): # box number
        for j in range(len(ordered_boxes[i])): # slot number
            length = len(ordered_boxes[i][j][:])
            total_score += (1 + i) * (1 + j) * int(ordered_boxes[i][j][length -1 : length])
    return total_score

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    fI = open(r'D:\Advent_of_Code\Advent_of_Code_2023\Day15\Puzzle_Input.txt', 'r')
    # Read all of the input data from Puzzle Input and organise it
    data = reading_input_data(fI)
    print("The input array has:",len(data),"elements!" )
    print(" ")

    # Lets process and structure the information a bit more helpfully
    box_to_use, step_type, focal_length = process_steps(data)

    # Lets work out what lenses end up in what boxes
    ordered_boxes = process_boxes(box_to_use, step_type,focal_length, data)

    # Lets work out the total score
    total_score = calculate_the_score(ordered_boxes, focal_length)

    print(" ")
    print("############################")
    print("The total score is:", total_score)
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()