import numpy as np
import time
import sys

def read_input_data(filename):
    with open(filename, 'r') as f:
        initial_states = f.readline().strip("\n").replace("Initial state: ", "").split(",")
        initial_states = np.array(initial_states, dtype=np.int16)
    return initial_states

def simulate_lanternfish_population(initial_states, days_to_model):
    population_model = np.array([np.int16(each) for each in initial_states], dtype=np.int16)
    for days in range(1, days_to_model + 1):
        population_model -= 1
        pop_check_indices = np.where(population_model == -1)[0]
        progress_bar(days, days_to_model)
        population_model = np.concatenate((population_model, np.array([8]*len(pop_check_indices),np.int16)))
        population_model[pop_check_indices] = 6
    print("\n")
    print("There are", len(population_model), "fish!")
    return len(population_model)

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
    days_to_model = 160
    initial_states = read_input_data(filename)
    print("There are",len(initial_states)," initial states, namely: ")
    print(initial_states)
    number_of_lanternfish = simulate_lanternfish_population(initial_states, days_to_model)

    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()