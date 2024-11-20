import time
import numpy as np

def read_input_data(filename):
    input_sequence = []
    with open(filename, 'r') as f:
        for line in f:
            input_sequence = line.strip().split(",")
    input_sequence = np.array(input_sequence, dtype=np.int64)
    return input_sequence

def process_sequence(input_sequence):
    # This function manages the intercode computer logic
    update_sequence = input_sequence.copy()
    index = 0
    while True:
        # If opcode is 99 then program is finished and should halt
        # This opcode has no parameters so check for it first as may be last in input sequence
        if update_sequence[index] == 99:
            # Once halt is called break loop with and return the updated sequence
            return update_sequence

        # If opcode is not 99 then look at the opcode and its three parameters
        current_sequence = input_sequence[index:index+4]

        # This is the logic for the non 99 opcodes
        if current_sequence[0] == 1:
            # If opcode is 1 then program uses addition logic
            update_sequence[current_sequence[3]] = update_sequence[current_sequence[1]] + update_sequence[current_sequence[2]]
        elif current_sequence[0] == 2:
            # If opcode is 2 then program uses multiplication logic
            update_sequence[current_sequence[3]] = update_sequence[current_sequence[1]] * update_sequence[current_sequence[2]]

        # After each iteration move forward 4 indexes to the next opcode
        index += 4

def find_inputs_for_output(input_sequence, target_output):
    # Logic to find what inputs provide required output
    while True:
        for input1 in range(100):
            for input2 in range(100):
                input_sequence_copy = input_sequence.copy()
                input_sequence_copy[1] = input1
                input_sequence_copy[2] = input2
                update_sequence = process_sequence(input_sequence_copy)
                if update_sequence[0] == target_output:
                    return input1, input2

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2019\Day2\Puzzle_Input.txt"
    input_sequence = read_input_data(filename)
    print("The input sequence is:")
    print(input_sequence)
    target_output = 19690720
    input1, input2 = find_inputs_for_output(input_sequence, target_output)

    print(" ")
    print("==============================================================")
    print(f"The input values {input1} and {input2} produce an output value of: {target_output}")
    print("==============================================================")
    print(" ")

    print(" ")
    print("==============================================================")
    print(f"These input values produce the required answer: {(100*input1)+input2}")
    print("==============================================================")
    print(" ")

    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()