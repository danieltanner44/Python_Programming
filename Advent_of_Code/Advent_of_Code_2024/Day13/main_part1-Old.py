
import time
from my_modules.development import fstring
def read_input_data(filename):
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
def generate_button_permutations(max_button_presses):
    button_permutations = []
    numbers_list = list(range(max_button_presses + 1))
    for a in numbers_list:
        for b in numbers_list:
            button_permutations.extend([(a,b)])
    return button_permutations
def process_machines(machine_configs):
    winning_approaches = []
    max_button_presses = 100
    button_permutations = generate_button_permutations(max_button_presses)
    for index, machine_config in enumerate(machine_configs):
        optimal_button_presses = None
        optimal_tokens = float("inf")
        for button_permutation in button_permutations:
            x_position, y_position = 0, 0
            # Process button A presses
            x_position += button_permutation[0] * machine_config[0][1]
            y_position += button_permutation[0] * machine_config[0][2]
            # Process button B presses
            x_position += button_permutation[1] * machine_config[1][1]
            y_position += button_permutation[1] * machine_config[1][2]
            # Process number of tokens required
            tokens_used = button_permutation[0] * 3 + button_permutation[1] * 1
            if x_position == machine_config[2][0] and y_position == machine_config[2][1]:
                if tokens_used < optimal_tokens:
                    optimal_tokens = tokens_used
                    optimal_button_presses = button_permutation
        if optimal_button_presses is not None:
            winning_approaches.append([optimal_button_presses, optimal_tokens])
    return winning_approaches
def total_cost_tokens(winning_approaches):
    final_token_cost = 0
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
    winning_approaches = process_machines(machine_configs)
    final_token_cost = total_cost_tokens(winning_approaches)
    part_one_ans = str(final_token_cost)
    print(fstring(f"There are {len(winning_approaches)} possible prizes to be won!", "bk", "wt"))
    print(fstring(f"The optimally winning approaches are [(A pushes, B pushes), tokens]:", "bk", "wt"))
    [print(winning_approach) for winning_approach in winning_approaches]
    print(fstring(f"======================  PART ONE - END  ======================", "bk", "bl"))
    print(" ", end="\n\n")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=========================  ANSWERS  ==========================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))
    print(f'{fstring("Part One:", "bk", "wt")}')
    print(f'The optimal token spend to win {len(winning_approaches)} possible prizes is: {fstring(part_one_ans, "wt", "bk")}')
    print(fstring(f"==============================================================", "bk", "bl"))
    print(" ")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())
if __name__ == "__main__":
    main()