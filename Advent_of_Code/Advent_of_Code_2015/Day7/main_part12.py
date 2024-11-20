import numpy as np
import time

def read_input_data(filename):
    instructions = []
    wires = []
    with open(filename, 'r') as f:
        for line in f:
            temp = line.strip().split(" ")
            if len(temp) == 5: # AND, OR, LSHIFT, RSHIFT
                temp_instruction = [temp[1], temp[0], temp[2], temp[4]]
            elif len(temp) == 3:    # Signal to wire
                temp_instruction = ["WIRE", temp[0], temp[2]]
            elif len(temp) == 4:    # NOT GATE
                temp_instruction = [temp[0], temp[1], temp [3]]
            else:
                ValueError("Unexpected data in input!")
            instructions.append(temp_instruction)
    # Create a dictionary of the wires with a preset value of uint16(0)
    for instruction in instructions:
        for element in instruction[1:]:
            try:
                int(element)
            except:
                wires.append(element)
    wires = sorted(set(wires))
    wire_values = {wire : None for wire in wires}
    return instructions, wire_values

def process_instructions(instructions, wire_values):
    # Need to continuing looping over the instructions as they are not in execution order
    while True:
        for instruction in instructions:

            # Check if the inputs for the instruction are all complete otherwise move to next instruction
            instruction_ready = True
            # Instruction is ready if all of the input wires are defined
            for element in instruction[1:-1]:
                # Check as some inputs are numeric so always ready
                try:
                    int(element)
                except:
                    if wire_values[element] is None:
                        instruction_ready = False

            if instruction_ready == True:
                inputs = instruction.copy()
                # Define all of the inputs to the function as some are numeric and some need to reference wire values
                for index, element in enumerate(instruction[:-1]):
                    if index != 0:
                        try:
                            inputs[index] = np.uint16(element)
                        except:
                            inputs[index] = wire_values[element]
                # Main logic for Bitwise operators
                match instruction[0]:
                    case "AND":     # Bitwise AND => &
                        wire_values[instruction[3]] = inputs[1] & inputs[2]
                    case "OR":      # Bitwise OR => |
                        wire_values[instruction[3]] = inputs[1] | inputs[2]
                    case "NOT":     # Bitwise NOT => ~
                        wire_values[instruction[2]] = ~inputs[1]
                    case "RSHIFT":  # Bitwise Right Shift => >>
                        wire_values[instruction[3]] = inputs[1] >> inputs[2]
                    case "LSHIFT":  # Bitwise Left Shift => <<
                        wire_values[instruction[3]] = inputs[1] << inputs[2]
                    case "WIRE":    # Direct wire
                        wire_values[instruction[2]] = inputs[1]

                # Need to check if finished. Finished when no wire values are None
                if None not in wire_values.values():
                    # Tidy up offsets for negative numbers
                    for key in wire_values:
                        if wire_values[key] < 0:
                            wire_values[key] += 65536
                    # Return dictionary of wire values
                    return wire_values

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2015\Day7\Puzzle_Input.txt"
    instructions, wire_values = read_input_data(filename)

    print(f"There are {len(instructions)} instructions, these are:")
    [print(instruction) for instruction in instructions]

    wire_values1 = wire_values.copy()
    wire_values1 = process_instructions(instructions, wire_values1)

    answer = wire_values1["a"]
    print(" ")
    print("==============================================================")
    print(f"Part One: The signal provided by wire a is: {answer}")
    print("==============================================================")

    # For Part Two we need to replaced the wire vale for "b" with the output from Part One
    wire_values2 = wire_values.copy()
    wire_values2["b"] = wire_values1["a"]
    # Now update the instructions to replace "b" with this value everywhere
    for i, instruction in enumerate(instructions):
        for j, element in enumerate(instruction):
            if element == "b":
                print(instruction)
                instructions[i][j] = str(wire_values1["a"])
                print(instructions[i])
    # Now process the instructions again with the new hardwired inputs
    wire_values2 = process_instructions(instructions, wire_values2)

    answer = wire_values2["a"]

    print(" ")
    print("==============================================================")
    print(f"Part Two: The signal provided by wire a is: {answer}")
    print("==============================================================")

    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()