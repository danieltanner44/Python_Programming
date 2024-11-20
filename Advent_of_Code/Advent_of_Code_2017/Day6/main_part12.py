import time
import numpy as np

def read_input_data(filename):
    with open(filename, 'r') as f:
        memory_banks = f.readline().strip().split("\t")
    memory_banks = np.array(memory_banks, dtype=np.int16)
    return memory_banks

def memory_reallocation_routine(memory_banks):
    index = 0
    memory_distribution_record = [[index, list(memory_banks)]]
    while True:     # Cycles continuously until complete
        index += 1
        # Find memory block with most memory (ties won by lowest-numbered memory bank)
        max_index = np.where(memory_banks == np.max(memory_banks))[0][0]
        max_value = memory_banks[max_index]
        # Distribute this memory to other blocks
        memory_banks[max_index] = 0     # Remove from cell to distribute
        for i in range(max_value):      # Distribution loop
            write_index = (max_index + i + 1) % np.shape(memory_banks)[0]
            memory_banks[write_index] += 1

        # Check if repeated
        for memory_record in memory_distribution_record:
            if np.array_equal(memory_record[1], memory_banks):
                return memory_distribution_record, index, memory_banks
        memory_distribution_record.append([index, list(memory_banks)])

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2017\Day6\Puzzle_Input.txt"
    memory_banks = read_input_data(filename)
    print(f"The initial memory banks are: {memory_banks}")

    memory_distribution_record, index1, memory_banks = memory_reallocation_routine(memory_banks)
    print(" ")
    print("==============================================================")
    print(f"Part One: The number of cycles to detected cycle is: {index1}")
    print("==============================================================")
    print(" ")

    memory_distribution_record, index2, memory_banks = memory_reallocation_routine(memory_banks)
    print(" ")
    print("==============================================================")
    print(f"Part Two: The cycle length is: {index2}")
    print("==============================================================")
    print(" ")

    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()