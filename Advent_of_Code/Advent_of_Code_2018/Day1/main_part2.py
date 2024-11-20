import time

def read_input_data(filename):
    input_frequency_changes = []
    with open(filename, 'r') as f:
        for line in f:
            input_frequency_changes.append(int(line.strip().split(" ")[0]))
    return input_frequency_changes

def process_frequencies(input_frequency_changes):
    frequency_tracker = set()
    current_frequency = 0
    frequency_tracker.add(current_frequency)
    while True:
        for input in input_frequency_changes:
            current_frequency += input
            if current_frequency in frequency_tracker:
                first_repeated_frequency = current_frequency
                return first_repeated_frequency
            frequency_tracker.add(current_frequency)

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2018\Day1\Puzzle_Input.txt"
    input_frequency_changes = read_input_data(filename)
    print("The input frequency changes are:")
    print(input_frequency_changes)
    first_repeated_frequency = process_frequencies(input_frequency_changes)
    print(" ")
    print("==============================================================")
    print("The first repeated frequency is:", first_repeated_frequency)
    print("==============================================================")
    print(" ")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()