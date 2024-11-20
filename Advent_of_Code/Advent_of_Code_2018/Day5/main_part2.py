import time
import numpy as np

def read_input_data(filename):
    with (open(filename, 'r') as f):
        for line in f:
            input_data = line.strip()
    input_data = list(input_data)
    return input_data

def find_prevention_element(input_data):
    shortest_sequence_length = 0
    elements_to_check = sorted(list(set(input_data)))
    while len(elements_to_check) > 0:
        current_element = elements_to_check[0]
        print(" ")
        print("============================================================")
        print("Currently assessing input sequence with redacted: " + str(current_element) + " and " + str(current_element.swapcase()))

        # Remove elements we are looking at from the list of those to check
        # Using ,remove as these are sets
        elements_to_check.remove(current_element)
        elements_to_check.remove(current_element.swapcase())

        # Check sequence is the input sequence with current elements removed
        check_sequence = [element for element in input_data if element not in [current_element, current_element.swapcase()]]

        # Update to keep track of shortest length
        length_of_updated_sequence = process_sequence(check_sequence)
        if length_of_updated_sequence < shortest_sequence_length or shortest_sequence_length == 0:
            shortest_sequence_length = length_of_updated_sequence
        print(" Redacted sequence reduces to length: ", length_of_updated_sequence)
        print(" Current shortest sequence is: ", shortest_sequence_length)
        print("============================================================")
    return shortest_sequence_length

def process_sequence(input_data):
    while True:
        check_convergence = input_data.copy()
        for i, character in enumerate(input_data):
            try:
                if character == input_data[i + 1].swapcase():
                    input_data = input_data[:i] + input_data[i+2:]
                    break
            except:
                break
        # If no changes made in last cycle then stop
        if check_convergence == input_data:
            return len(input_data)

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2018\Day5\Puzzle_Input.txt"
    input_data = read_input_data(filename)
    print(" ")
    print("The input sequence is:")
    print(input_data)

    shortest_sequence_length = find_prevention_element(input_data)


    print(" ")
    print("=======================================================================================")
    print("The length of the residual sequence is:", shortest_sequence_length)
    print("=======================================================================================")
    print(" ")


    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())



if __name__ == "__main__":
    main()