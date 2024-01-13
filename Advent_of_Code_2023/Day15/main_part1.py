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
    ordered_boxes = np.array(np.shape([9, 256]), dtype=str)
    counter = 0
    for i in range(len(box_to_use)):
        label = data[i].replace("=", " ")
        label = label.replace("-", " ")
        print(label)
        if step_type[i] == "-":
            # Want to go to relevant box and remove the lens with the given label
            for
            temp = np.where(ordered_boxes[i][:] == label[0:2])
            print(temp, "temp")
            ordered_boxes = np.delete(ordered_boxes,temp,axis=1)


            # If no lens with required label present do nothing
            print("")

            # Then reorganise remaining lenses into the box without changing their order

        elif step_type[i] == "=":
            # Add a lens to the box with the required focal length
            print("")
            # If it is there then replace it but leave other lenses untouched

            # If it is not there then add it after other lenses in the box. Do not move other lenses


        counter += 1
    return ordered_boxes

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    fI = open(r'D:\Advent_of_Code\Advent_of_Code_2023\Day15\Puzzle_Input_d.txt', 'r')
    # Read all of the input data from Puzzle Input and organise it
    data = reading_input_data(fI)
    print("The input array has:",len(data),"elements!" )
    print(" ")
    box_to_use, step_type, focal_length = process_steps(data)
    print(box_to_use)
    print(step_type)
    print(focal_length)
    print(data)
    # Now lets process the boxes by adding, removing or ordering lenses
    output = process_boxes(box_to_use, step_type,focal_length, data)

    print("The total score is:", box_to_use)
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()