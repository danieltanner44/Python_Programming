import time
import numpy as np


def read_input_data(filename):
    with open(filename, 'r') as f:
        for line in f:
            input_code_instructions = line.strip().split(",")
    input_code_instructions = np.array(input_code_instructions, dtype=np.int32)
    return input_code_instructions

def intercode_computer(instructions, computer_input):
    diagnostic_output = []
    # This function manages the intercode computer logic
    update_sequence = instructions.copy()
    index = 0
    while True:
        # Check what the next opcode is
        check_modes = update_sequence[index]
        if check_modes == 99:
            # If opcode is 99 then program is finished and should halt
            return update_sequence, diagnostic_output
        elif check_modes > 99:  # Has opcode and parameter modes
            # An opcode > 99 also includes data on the parameter modes for each parameter
            opcode = int(str(check_modes)[2:4])
            parameter_mode_list = list(str(check_modes))
            parameter_modes = list(reversed(parameter_mode_list[:-2]))
            if len(parameter_modes) == 1:
                parameter_modes = parameter_modes + [0, 0]
            elif len(parameter_modes) == 2:
                parameter_modes = parameter_modes + [0]
            parameter_modes = [int(parameter) for parameter in parameter_modes]
        else:
            # An opcode <= 99 includes the opcode only and position parameter mode is to be used for all parameters
            # Note 99 itself cannot be accessed as it was checked first and would cause a return
            opcode = check_modes
            parameter_modes = [0, 0, 0]     # Allow for at least three parameters (may be less)

        # Now read in the length of the current instruction
        if opcode in [1,2,7,8]:     # These opcodes have 3 parameters, e.g., [1,10,20,30]
            num_parameters = 3
            current_instruction = update_sequence[index:index + num_parameters + 1]
            parameter_modes = parameter_modes[:num_parameters]
        elif opcode in [3,4]:   # These opcodes have 1 parameter, e.g., [3,50]
            num_parameters = 1
            current_instruction = update_sequence[index:index + num_parameters + 1]
            parameter_modes = parameter_modes[:num_parameters]
        elif opcode in [5,6]:   # These opcodes have 2 parameters, e.g., [5,1,50]
            num_parameters = 2
            current_instruction = update_sequence[index:index + num_parameters + 1]
            parameter_modes = parameter_modes[:num_parameters]

        # Determine the parameters based on whether position or immediate mode are selected for each
        values = []
        for i, parameter_mode in enumerate(parameter_modes, start=1):
            if parameter_mode == 0:
                values.append(update_sequence[current_instruction[i]])
            elif parameter_mode == 1:
                values.append(current_instruction[i])

        # This is the logic for the non 99 opcodes
        if opcode == 1:     # If opcode is 1 then program uses addition logic
            update_sequence[current_instruction[3]] = values[0] + values[1]
            index += 4      # After each iteration move forward 4 indexes to the next opcode

        elif opcode == 2:   # If opcode is 2 then program uses multiplication logic
            update_sequence[current_instruction[3]] = values[0] * values[1]
            index += 4      # After each iteration move forward 4 indexes to the next opcode

        elif opcode == 3:   # If opcode is 3 then read an input value and store to a position, e.g., [3, 50]
            update_sequence[current_instruction[1]] = computer_input
            index += 2      # After each iteration move forward 4 indexes to the next opcode

        elif opcode == 4:   # If opcode is 4 then output a value stored at a position, e.g., [4, 50]
            diagnostic_output.append(values[0])
            index += 2      # After each iteration move forward 4 indexes to the next opcode

        elif opcode == 5:   # If opcode is 5 and the first parameter is non-zero then jump to second parameter position
            if values[0] != 0:
                index = values[1]
                # Need to break out
                print(
                    f"Pointer Index {index}: opcode = {opcode}, instruction = {current_instruction}, parameter modes are = {parameter_modes}")
                print(update_sequence)
                continue
            index += 3

        elif opcode == 6:   # If opcode is 6 and the first parameter is zero then jump to second parameter position
            if values[0] == 0:
                index = values[1]
                # Need to break out
                print(
                    f"Pointer Index {index}: opcode = {opcode}, instruction = {current_instruction}, parameter modes are = {parameter_modes}")
                print(update_sequence)
                continue
            index += 3

        elif opcode == 7:   # If opcode is 7 and the first parameter is less than the second it stores 1 in third parameter position, else 0
            if values[0] < values[1]:
                update_sequence[current_instruction[3]] = 1
            else:
                update_sequence[current_instruction[3]] = 0
            index += 4  # After each iteration move forward 4 indexes to the next opcode
        elif opcode == 8:  # If opcode is 8 and the first parameter equals the second it stores 1 in third parameter position, else 0
            if values[0] == values[1]:
                update_sequence[current_instruction[3]] = 1
            else:
                update_sequence[current_instruction[3]] = 0
            index += 4  # After each iteration move forward 4 indexes to the next opcode

        print(f"Pointer Index {index}: opcode = {opcode}, instruction = {current_instruction}, parameter modes are = {parameter_modes}")

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2019\Day5\Puzzle_Input.txt"
    instructions = read_input_data(filename)

    print(" ")
    print("==============================================================")
    print("The input code instructions are:")
    print(instructions)
    print("==============================================================")
    print(" ")

    computer_input = int(input("Please enter input:"))
    update_sequence, diagnostic_output = intercode_computer(instructions, computer_input)

    print(" ")
    print("==============================================================")
    print(f"The diagnostic output is: {[int(element) for element in diagnostic_output]}")
    print(f"The diagnostic output code is: {max(diagnostic_output)}")
    print("==============================================================")
    print(" ")

    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()