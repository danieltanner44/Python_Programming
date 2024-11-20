import time
import numpy as np


def read_input_data(filename):
    with open(filename, 'r') as f:
        for line in f:
            instructions = line.strip().split(",")
    instructions = np.array(instructions, dtype=np.int64)
    return instructions

def intercode_computer(instructions, user_input):
    diagnostic_output = []
    relative_base_offset = 0    # Needed for relative mode
    # This function manages the intercode computer logic
    update_sequence = np.pad(instructions.copy(), (0,1000000), mode='constant', constant_values=0)
    print(update_sequence)
    index = 0
    while True:
        # Check what the next opcode is
        check_modes = update_sequence[index]
        if check_modes == 99:
            # If opcode is 99 then program is finished and should halt
            return update_sequence, diagnostic_output
        elif check_modes > 99:  # Has opcode and parameter modes
            # An opcode > 99 also includes data on the parameter modes for each parameter
            opcode = int(str(check_modes)[-2:])     # Opcode is last two digits
            parameter_mode_list = list(str(check_modes))
            parameter_modes = list(reversed(parameter_mode_list[:-2]))  # Parameters are reverse ordered remainder of check_modes
            if len(parameter_modes) == 1:
                parameter_modes = parameter_modes + [0, 0]  # Pad out parameter_modes if needed
            elif len(parameter_modes) == 2:
                parameter_modes = parameter_modes + [0]     # Pad out parameter_modes if needed
            parameter_modes = [int(parameter) for parameter in parameter_modes]     # Convert all back to ints
        else:
            # An opcode <= 99 includes the opcode only and position parameter mode is to be used for all parameters
            # Note 99 itself cannot be accessed as it was checked first and would cause a return
            opcode = check_modes
            parameter_modes = [0, 0, 0]     # Allow for at least three parameters (may be less)

        # Now read in the length of the current instruction
        if opcode in [1,2,7,8]:     # These opcodes have 3 parameters, e.g., [1,10,20,30]
            num_parameters = 3
        elif opcode in [5, 6]:      # These opcodes have 2 parameters, e.g., [5,1,50]
            num_parameters = 2
        elif opcode in [3,4,9]:     # These opcodes have 1 parameter, e.g., [3,50]
            num_parameters = 1

        # Define the current instruction and parameters based on determined opcode
        current_instruction = update_sequence[index:index + num_parameters + 1]
        parameter_modes = parameter_modes[:num_parameters]

        # Determine the parameters based on whether position, immediate or relative mode are selected for each
        values = []
        for i, parameter_mode in enumerate(parameter_modes, start=1):
            if parameter_mode == 0:     # Position Mode
                values.append(update_sequence[current_instruction[i]])
            elif parameter_mode == 1:   # Immediate Mode
                values.append(current_instruction[i])
            elif parameter_mode == 2:   # Relative Mode
                values.append(update_sequence[relative_base_offset + current_instruction[i]])

        # If the relative parameter is used to write data then adjust write index here
        if opcode in [1,2,3,7,8]:
            if parameter_modes[-1] == 2:    # The index -1 gives the mode of the last parameter (the write parameter)
                write_index = current_instruction[-1] + relative_base_offset
            else:
                write_index = current_instruction[-1]

        # Now step through all the logic for the opcodes
        if opcode == 1:     # If opcode is 1 then program uses addition logic
            update_sequence[write_index] = values[0] + values[1]

        elif opcode == 2:     # If opcode is 2 then program uses multiplication logic
            update_sequence[write_index] = values[0] * values[1]

        elif opcode == 3:     # If opcode is 3 then read an input value and store to a position, e.g., [3, 50]
            update_sequence[write_index] = user_input

        elif opcode == 4:   # If opcode is 4 then output a value stored at a position, e.g., [4, 50]
            diagnostic_output.append(values[0])
            print(f"OUTPUT: {values[0]}")

        elif opcode in [5,6]:
            if opcode == 5 and values[0] != 0:  # If opcode is 5 and the first parameter is non-zero then jump to second parameter position
                index = values[1]
                print(
                    f"Pointer Index {index}: opcode = {opcode}, instruction = {current_instruction}, parameter modes are = {parameter_modes}")
                continue
            elif opcode == 6 and values[0] == 0:   # If opcode is 6 and the first parameter is zero then jump to second parameter position
                index = values[1]
                print(
                        f"Pointer Index {index}: opcode = {opcode}, instruction = {current_instruction}, parameter modes are = {parameter_modes}")
                continue

        elif opcode == 7:     # If opcode is 7 and the first parameter is less than the second it stores 1 in third parameter position, else 0
            if values[0] < values[1]:
                update_sequence[write_index] = 1
            else:
                update_sequence[write_index] = 0

        elif opcode == 8:     # If opcode is 8 and the first parameter equals the second it stores 1 in third parameter position, else 0
            if values[0] == values[1]:
                update_sequence[write_index] = 1
            else:
                update_sequence[write_index] = 0

        elif opcode == 9:  # If opcode is 9 adjust the relative base by the value of its only parameter
            relative_base_offset += values[0]

        # Now move the index forward to the next opcode for the next instruction (opcode)
        if opcode in [1,2,7,8]:
            index += 4  # After each iteration move forward 4 indexes to the next opcode
        elif opcode in [5, 6]:
            index += 3  # If jump conditions are not met need to advance to next opcode
        elif opcode in [3,4,9]:
            index += 2  # After each iteration move forward 2 indexes to the next opcode
        else:
            ValueError("Opcode value not recognised!")

        print(f"Pointer Index {index}: opcode = {opcode}, instruction = {current_instruction}, parameter modes are = {parameter_modes}")

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2019\Day9\Puzzle_Input.txt"
    instructions = read_input_data(filename)

    print(" ")
    print("==============================================================")
    print("The input code instructions are:")
    print(instructions)
    print("==============================================================")
    print(" ")

    user_inputs = {"Part One":1, "Part Two":2}
    for index, key in enumerate(user_inputs):
        if index != 0:
            print(f"Commencing {key} in:   ", end="")
            for i in range(10, 0, -1):
                print(f"{i}...", end="")
                time.sleep(1)
            print(" ")

        user_input = user_inputs[key]
        update_sequence, diagnostic_output = intercode_computer(instructions, user_input)

        print(" ")
        print("==============================================================")
        print(f"This is {key}")
        print(f"The diagnostic output is: {[int(element) for element in diagnostic_output]}")
        print(f"The diagnostic output code is: {np.max(diagnostic_output)}")
        print("==============================================================")
        print(" ")


    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()