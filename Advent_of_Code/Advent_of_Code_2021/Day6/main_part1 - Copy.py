import numpy as np
import time
import sys

def read_input_data(filename):
    with open(filename, 'r') as f:
        initial_states = f.readline().strip("\n").replace("Initial state: ", "").split(",")
    return initial_states

def simulate_lanternfish_population(initial_states, days_to_model):
    population_model = [int(each) for each in initial_states]
    for days in range(1, days_to_model + 1):
        progress_bar(days, days_to_model)
        new_fish_timers = []
        for index, timer in enumerate(population_model):
            if timer == 0:
                new_fish_timers.append(8)
                population_model[index] = 6
            else:
                population_model[index] = population_model[index] - 1
        if new_fish_timers:
            for each_new_fish in new_fish_timers:
                population_model.append(each_new_fish)
        #print("After", days,"days: ", population_model)
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
    days_to_model = 80
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