import time

def read_input_data(filename):
    input_directions = []
    with open(filename, 'r') as f:
        for line in f:
            input_directions.append(int(line.strip().split(" ")[0]))
    return input_directions

def process_steps(input_directions):
    next_index = input_directions[0]
    number_steps = 0
    while True:
        try:
            index = next_index
            next_index = input_directions[index] + index
            input_directions[index] += 1
        except:
            return number_steps
        number_steps += 1
    return number_steps

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2017\Day5\Puzzle_Input.txt"
    input_directions = read_input_data(filename)
    print("The initial passphrases to assess are:")
    print(input_directions)
    number_steps = process_steps(input_directions)
    print(" ")
    print("==============================================================")
    print("The number of steps to exit is:", number_steps)
    print("==============================================================")
    print(" ")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()