import numpy as np
import time
import sys

def read_input_data(filename):
    with open(filename, 'r') as f:
        initial_states = f.readline().strip("\n").replace("Initial state: ", "").split(",")
        initial_states = np.array(initial_states, dtype=np.int16)
        # Convert to tally
        state_tally = [len(np.where(initial_states==i)[0]) for i in range(9)]
    return initial_states, state_tally

def simulate_lanternfish_population(state_tally, initial_states, days_to_model):
    print("Initial tally is: ", state_tally)
    for days in range(1, days_to_model + 1):
        # Decrement all by one day
        zero_store = state_tally[0]
        for i in range(0,8):
            state_tally[i] = state_tally[i+1]
        state_tally[8] = 0
        progress_bar(days, days_to_model)
        # Process zero timers
        # Reset internal timer
        state_tally[6] += zero_store
        # Spawn new fish
        state_tally[8] += zero_store
        print("\n")
        print("================")
        print("After",days,"days:",state_tally)
        print("Total number of lanternfish is:",np.sum(state_tally))
        print("================")
    return np.sum(state_tally)

def progress_bar(iteration, total, length=40):
    percent = (iteration / total)
    arrow = '█' * int(length * percent)
    spaces = ' ' * (length - len(arrow))
    sys.stdout.write(f'\r|{arrow}{spaces}| {percent:.2%} Complete')
    sys.stdout.flush()

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2021\Day6\Puzzle_Input.txt"
    days_to_model = 256
    initial_states, state_tally = read_input_data(filename)
    print("There are",np.sum(state_tally)," initial states, namely: ")
    print(initial_states)
    number_of_lanternfish = simulate_lanternfish_population(state_tally, initial_states, days_to_model)
    print(" ")
    print("==============================================================")
    print("The number of lanternfish after",days_to_model,"days is:",number_of_lanternfish)
    print("==============================================================")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()