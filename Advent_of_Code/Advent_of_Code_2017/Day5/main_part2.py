import time

def read_input_data(filename):
    input_frequency_changes = []
    with open(filename, 'r') as f:
        for line in f:
            input_frequency_changes.append(int(line.strip().split(" ")[0]))
    return input_frequency_changes

def process_frequencies(input_directions):
    next_index = input_directions[0]
    number_steps_exit = 0
    while True:
        try:
            index = next_index
            next_index = input_directions[index] + index
            if input_directions[index] >= 3:
                input_directions[index] -= 1
            else:
                input_directions[index] += 1
        except IndexError:  # Catch out-of-bounds explicitly
            return number_steps_exit
        number_steps_exit += 1

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2017\Day5\Puzzle_Input.txt"
    input_frequency_changes = read_input_data(filename)
    print("The input frequency changes are:")
    print(input_frequency_changes)
    number_steps_exit = process_frequencies(input_frequency_changes)
    print(" ")
    print("==============================================================")
    print("The number of steps to exit is:", number_steps_exit)
    print("==============================================================")
    print(" ")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()