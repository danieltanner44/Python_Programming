def read_input_data(filename):
    direction_pairs = []
    with open(filename, 'r') as f:
        for each_line in f:
            direction_pairs.append((each_line.strip("\n").split(" ")))
    direction_pairs = [[direction, int(distance)] for direction, distance in direction_pairs]
    print(direction_pairs)
    return direction_pairs

def assess_movement(direction_pairs):
    position = [0,0] # [H,V]
    aim = 0
    print(position, aim)
    for movement in direction_pairs:
        if movement[0] == "forward":
            position[0] += movement[1]
            position[1] += aim * movement[1]
        elif movement[0] == "up":
            aim -= movement[1]
        elif movement[0] == "down":
            aim += movement[1]
        print(position, aim, movement)
    result_multiple = position[0] * position[1]
    return result_multiple

def main():
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2021\Day2\Puzzle_Input.txt"
    direction_pairs = read_input_data(filename)
    result_multiple = assess_movement(direction_pairs)
    print(result_multiple)
if __name__ == "__main__":
    main()