def main():
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2021\Day1\Puzzle_Input.txt"
    with open(filename, 'r') as f:
        data = [int(line.strip()) for line in f]
    print("Initial measurement data is: ",data)
    depth_difference = [data[a] - data[a-1] for a in range(1,len(data))]
    print("The depth differences are: ",depth_difference)
    counter = 0
    for differences in depth_difference:
        if differences > 0:
            counter += 1
    print("The total number of measurements with depth increasing is: ",counter)


if __name__ == "__main__":
    main()