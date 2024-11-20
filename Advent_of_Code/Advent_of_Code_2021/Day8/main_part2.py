import numpy as np
import time
import sys

def read_input_data(filename):
    input_data = []
    with open(filename, 'r') as f:
        for each_line in f:
            input_line_read = each_line.strip().split(" ")
            input_data.append([input_line_read[:10]] + [input_line_read[11:]])
        print(" ")
        print("The input data is: ")
        print(input_data)
    return input_data

def number_of_common_elements(each_input, number_to_input_mapping, number_to_check):
    counter = 0
    for character in each_input:
        if character in number_to_input_mapping[number_to_check]:
            counter += 1
    return counter

def determine_wiring_per_record(record_inputs):
    number_to_input_mapping = [""]*10
    # Find unambiguous number mappings [1,4,7,8]
    for index_inputs, each_input in enumerate(record_inputs[0]):
        number_record_elements = len(each_input)
        if number_record_elements in [2, 3, 4, 7]:
            if number_record_elements == 2:
                number_to_input_mapping[1] = "".join(sorted(each_input))
            elif number_record_elements == 3:
                number_to_input_mapping[7] = "".join(sorted(each_input))
            elif number_record_elements == 4:
                number_to_input_mapping[4] = "".join(sorted(each_input))
            elif number_record_elements == 7:
                number_to_input_mapping[8] = "".join(sorted(each_input))
            else:
                break # Stop when all found
    # Now work out mapping for remaining numbers [0,2,3,5,6,9]
    for index_inputs, each_input in enumerate(record_inputs[0]):
        number_record_elements = len(each_input)
        number_to_check = 1
        counter1 = number_of_common_elements(each_input, number_to_input_mapping, number_to_check)
        number_to_check = 4
        counter4 = number_of_common_elements(each_input, number_to_input_mapping, number_to_check)
        if number_record_elements == 6:
            # Find 6
            if counter1 == 1 and counter4 == 3:
                number_to_input_mapping[6] = "".join(sorted(each_input))
                continue
            # Find 9
            if counter1 == 2 and counter4 == 4:
                number_to_input_mapping[9] = "".join(sorted(each_input))
                continue
            # Find 0
            if counter1 == 2 and counter4 == 3:
                number_to_input_mapping[0] = "".join(sorted(each_input))
                continue
        if number_record_elements == 5:
            # Find 3
            if counter1 == 2 and counter4 == 3:
                number_to_input_mapping[3] = "".join(sorted(each_input))
                continue
            # Find 5
            if counter1 == 1 and counter4 == 3:
                number_to_input_mapping[5] = "".join(sorted(each_input))
                continue
            # Find 2
            if counter1 == 1 and counter4 == 2:
                number_to_input_mapping[2] = "".join(sorted(each_input))
                continue
    number_to_input_mapping_dict = dict(list(zip(number_to_input_mapping,range(10))))
    return number_to_input_mapping_dict

def determine_record_output_value(number_to_input_mapping_dict, record_inputs):
    record_output_value = 0
    for index_inputs, each_output in enumerate(record_inputs[1]):
        record_output_value += (10**(3-index_inputs))*number_to_input_mapping_dict["".join(sorted(each_output))]
    return record_output_value

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2021\Day8\Puzzle_Input.txt"
    input_data = read_input_data(filename)
    total_output_value = 0
    for record_index, record_inputs in enumerate(input_data):
        print("===================================")
        print("Record number:", record_index)
        print("===================================")
        number_to_input_mapping_dict = determine_wiring_per_record(record_inputs)
        record_output_value = determine_record_output_value(number_to_input_mapping_dict, record_inputs)
        print("Record inputs:", record_inputs)
        print("The determined record mapping is:", number_to_input_mapping_dict)
        print("Value for the record is:", record_output_value)
        print("")
        total_output_value += record_output_value
    print("============================================")
    print("The total value for all records is:", total_output_value)
    print("============================================")


    print(" ")
    print("==============================================================")
    #print("The number of lanternfish after",days_to_model,"days is:",number_of_lanternfish)
    print("==============================================================")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()