from datetime import datetime, date
import time
import numpy as np
import my_modules.development as mmd

def read_input_data(filename):
    guards_rota = []
    with (open(filename, 'r') as f):
        for line in f:
            line = line.strip().replace("[", "").replace("]","").replace("#", "")
            temp = [line[:16]]+line[17:].split(" ")
            guards_rota.append(temp)
    return guards_rota

def reorder_guards_rota(guards_rota):
    guard_ids = []
    # Sort guard entries chronologically
    sorted_guards_rota = sorted(guards_rota, key=lambda x: datetime.strptime(x[0], '%Y-%m-%d %H:%M'))
    # Determine number of guards
    for entries in sorted_guards_rota:
        if entries[1] == "Guard":
            guard_ids.append(int(entries[2]))
    # Produce list of sorted and unique guard ids
    guard_ids = sorted(list(set(guard_ids)))
    number_of_guards = len(guard_ids)
    guard_ids = dict(zip(guard_ids, range(number_of_guards)))
    print(guard_ids)

    # Now create and complete sleep tracker for each guard
    sleep_tracker = np.full([1, 62], ".", dtype="U10") # Up to 10-character strings
    mmd.print_array(sleep_tracker)

    # Now read entries and write to tracker
    guard_entry_index = -1
    for index, entry in enumerate(sorted_guards_rota):
        print(entry, entry[0])
        if entry[1] == "Guard":
            guard_entry_index += 1
            new_row = np.full([1, 62], ".", dtype="U10")
            sleep_tracker = np.append(sleep_tracker, new_row, axis=0)
            sleep_tracker[guard_entry_index, 0] = entry[0][5:11]
            sleep_tracker[guard_entry_index, 1] = entry[2]
        elif entry[1] == "falls":
            time_falls_asleep = datetime.strptime(entry[0], "%Y-%m-%d %H:%M")
            time_wakes_up = datetime.strptime(sorted_guards_rota[index+1][0], "%Y-%m-%d %H:%M")
            start_sleep_index = int(time_falls_asleep.minute) + 2
            end_sleep_index = int(time_wakes_up.minute) + 2
            if end_sleep_index > 59:
                end_sleep_index = 59
            sleep_tracker[guard_entry_index, start_sleep_index:end_sleep_index] = "#"
    print(" ")
    mmd.print_array(sleep_tracker)

    # Find longest sleeper
    longest_sleep = 0
    for day_entry in sleep_tracker:
        length_of_sleep = len(np.where(day_entry == "#")[0])
        if length_of_sleep >= longest_sleep:
            longest_sleep = length_of_sleep
            longest_sleeper = day_entry[1]

    print(" ")
    print(longest_sleeper, longest_sleep)



    return

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2018\Day4\Puzzle_Input_d.txt"
    guards_rota = read_input_data(filename)
    print(" ")
    print("The input guard rotas are:")
    print(guards_rota)
    ordered_guards_rota = reorder_guards_rota(guards_rota)

    print(" ")

    print(" ")
    print("=======================================================================================")
    print("The calculated overlap in m**2 is:", 0)
    print("=======================================================================================")
    print(" ")

    print(" ")
    print("=======================================================================================")
    print("The only proposal that does not overlap others is from ID:", 0)
    print("=======================================================================================")
    print(" ")

    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())



if __name__ == "__main__":
    main()