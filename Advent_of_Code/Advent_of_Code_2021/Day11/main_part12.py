import time
import numpy as np

def read_input_data(filename):
    input_data = []
    with open(filename, 'r') as f:
        for each_line in f:
            input_data.append(list(each_line.strip()))
        input_data = np.array(input_data, dtype=np.int16)
    return input_data

def process_steps(input_data, num_steps):
    once_only = False
    flash_counter = 0
    flash_tracker_array = input_data.copy() #Main tracker for octupus energy across steps
    for step in range(1,num_steps + 1):
        flash_location_tracker = input_data.copy() * 0 # Track octupus' that flash as only allowed 1 flash per step
        flash_tracker_array = flash_tracker_array + 1 # Increment all energy levels by 1 (per step)
        print("==============")
        print("Step:", step)
        print("==============")
        flash_indexes = np.where(flash_tracker_array > 9) # Check where the octopus have energy > 9
        while len(flash_indexes[0]) != 0:
            # Increase indexes of octopuses surrounding flashes by 1
            for k in range(0, len(flash_indexes[0])):
                flash = [flash_indexes[0][k],flash_indexes[1][k]]
                if flash_location_tracker[flash_indexes[0][k],flash_indexes[1][k]] == 1: # If already flashed then ignore
                    continue
                flash_location_tracker[flash_indexes[0][k],flash_indexes[1][k]] = 1 # If not then process flash and flag as not to flash again
                flash_counter += 1
                for i in [-1,0,1]:
                    for j in [-1,0,1]:
                        if i == 0 and j == 0: # Don't change value of flashing octopus
                            continue
                        else:
                            if 0 <= flash[0]+i < flash_tracker_array.shape[0] and 0 <= flash[1]+j < flash_tracker_array.shape[1]:
                                flash_tracker_array[flash[0] + i][flash[1] + j] += 1 # Increment surrounding octopus energy levels by 1
            flash_indexes = np.where((flash_tracker_array > 9) & (flash_location_tracker == 0)) # Create new indexes to process in next loop
            # Reset energy levels for flashed octopus
        if np.min(flash_location_tracker) == 1 and once_only == False:
            synchronisation_step = step
            once_only = True
            print("================================")
            print("Synchronised at step:", step)
            print("================================")
        try:
            flash_tracker_array[flash_location_tracker == 1] = 0
        except:
            continue
        print(flash_tracker_array)
    return flash_counter, synchronisation_step

def main():
    # progress_bar(days, days_to_model)
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    num_steps = 1000
    filename = f"D:\Python_Programming\Advent_of_Code\Advent_of_Code_2021\Day11\Puzzle_Input.txt"
    input_data = read_input_data(filename)
    print("The input data is:")
    print(input_data)
    flash_counter,synchronisation_step = process_steps(input_data,num_steps)
    print(" ")
    print("==============================================================")
    print("The syntax score is:",flash_counter)
    print("==============================================================")
    print(" ")
    print("==============================================================")
    print("Flashes synchronised at step:", synchronisation_step)
    print("==============================================================")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()