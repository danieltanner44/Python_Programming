def main():
    filename = r"D:\Python_Programming\Advent_of_Code\Advent_of_Code_2021\Day1\Puzzle_Input.txt"
    with open(filename, 'r') as f:
        data = [int(line.strip()) for line in f]
    print("Initial measurement data is: ", data)
    averaged_data = []
    for data_point in enumerate(data[:-2]):
        averaged_data.append(sum(data[data_point[0]:data_point[0]+3]))
    print("Averaged measurement data is: ",averaged_data)
    counter = 0
    for point in enumerate(averaged_data[1:],start=1):
        if averaged_data[point[0]] - averaged_data[point[0]-1] > 0:
            counter += 1
    print("The total number of measurements with depth increasing is: ",counter)


if __name__ == "__main__":
    main()