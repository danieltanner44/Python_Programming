import time
from my_modules.development import fstring
import sympy as sp

def read_input_data(filename):
    # Read data into a structure like this: [[['A', 46, 72], ['B', 49, 18], [5353, 4446]], ...]
    machine_configs, temp_config = [], []
    with (open(filename, 'r') as f):
        for line in f:
            temp = line.strip().replace(":","").replace(",","").split()
            if len(temp) == 0:
                # Skip blank lines
                continue
            elif temp[0] == "Button":
                temp_config.append([temp[1]] + [int(temp[2][2:]), int(temp[3][2:])])
            elif temp[0] == "Prize":
                temp_config.append([int(temp[1][2:]), int(temp[2][2:])])
                machine_configs.append(temp_config)
                temp_config = []
    return machine_configs

def process_machines(machine_configs, offset):
    winning_approaches = []
    for index, machine_config in enumerate(machine_configs):
        # Create the matrix equation AX = B and solve for X (the presses required)
        # Set up matrix A - The button movements on press
        A = sp.Matrix(([machine_config[0][1], machine_config[1][1]], [machine_config[0][2], machine_config[1][2]]))
        # Set up matrix B - The corresponding final target locations
        B = sp.Matrix(([machine_config[2][0] + offset], [machine_config[2][1] + offset]))
        # Invert A and multiply by B to get X - the number of button presses required
        A_inv = A.inv()
        presses_required = A_inv*B
        print(f"# {index}: Presses Required: {[press for press in presses_required]}", end="")

        # If the number of button presses are integers then that is the answer
        if isinstance(presses_required[0], sp.core.numbers.Integer) and isinstance(presses_required[1], sp.core.numbers.Integer):
            print(f" -> Prize Won!")
            token_cost = int(presses_required[0]) * 3 + int(presses_required[1]) * 1
            winning_approaches.append([(int(presses_required[0]),int(presses_required[1])), token_cost])
        else:
            # If not the prize is not reachable
            print(f" -> Cannot win prize!")
    return winning_approaches

def total_cost_tokens(winning_approaches):
    final_token_cost = 0
    # Loop over each of the winning approaches and add the token costs
    # Winning_approach has the structure: [(A presses, B presses), token_cost]
    for winning_approach in winning_approaches:
        final_token_cost += winning_approach[1]
    return final_token_cost

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")

    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=======================  Puzzle Input  =======================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2024\Day13\Puzzle_Input.txt"
    machine_configs = read_input_data(filename)
    print(fstring(f"There are {len(machine_configs)} machine configurations, they are: ", "bk", "wt"))
    [print(machine_config) for machine_config in machine_configs]
    print(fstring(f"====================  Puzzle Input - End =====================", "bk", "bl"))

    print(" ", end="\n\n")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=========================  PART ONE  =========================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))

    offset = 0
    winning_approaches = process_machines(machine_configs, offset)
    final_token_cost = total_cost_tokens(winning_approaches)
    part_one_ans = str(final_token_cost)

    print(fstring(f"There are {len(winning_approaches)} possible prizes to be won!", "bk", "wt"))
    print(fstring(f"Winning all of these would require {part_one_ans} tokens!", "bk", "wt"))
    print(fstring(f"======================  PART ONE - END  ======================", "bk", "bl"))

    print(" ", end="\n\n")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=========================  PART TWO  =========================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))

    offset = 10000000000000
    winning_approaches = process_machines(machine_configs, offset)
    final_token_cost = total_cost_tokens(winning_approaches)
    part_two_ans = str(final_token_cost)

    print(fstring(f"There are {len(winning_approaches)} possible prizes to be won!", "bk", "wt"))
    print(fstring(f"Winning all of these would require {part_one_ans} tokens!", "bk", "wt"))
    print(fstring(f"======================  PART TWO - END  ======================", "bk", "bl"))

    print(" ", end="\n\n")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=========================  ANSWERS  ==========================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))
    print(f'{fstring("Part One:", "bk", "wt")}')
    print(f'The total token cost is: {fstring(part_one_ans, "wt", "bk")}')
    print(fstring(f"==============================================================", "bk", "bl"))
    print(f'{fstring("Part Two:", "bk", "wt")}')
    print(f'The total token cost is: {fstring(part_two_ans, "wt", "bk")}')
    print(fstring(f"==============================================================", "bk", "bl"))
    print(" ")

    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()