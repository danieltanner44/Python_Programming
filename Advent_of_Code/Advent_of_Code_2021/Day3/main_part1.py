import numpy as np

def read_input_data(filename):
    readings = []
    with open(filename, 'r') as f:
        for each_line in f:
            readings.append((each_line.strip("\n")))
    for reading in enumerate(readings):
        readings[reading[0]] = [int(each_bit) for each_bit in reading[1]]
    readings = np.array(readings)
    return readings

def determine_rates(readings):
    gamma_totals = np.sum(readings,axis=0)
    epsilon_totals = np.sum(readings,axis=0)
    for value in enumerate(gamma_totals):
        if value[1] >= np.size(readings, axis=0)/2:
            gamma_totals[value[0]] = 1
            epsilon_totals[value[0]] = 0
        else:
            gamma_totals[value[0]] = 0
            epsilon_totals[value[0]] = 1
    gamma_rate = ""
    epsilon_rate = ""
    for element in gamma_totals:
        gamma_rate += str(element)
    for element in epsilon_totals:
        epsilon_rate += str(element)
    gamma_rate = int(gamma_rate, 2)
    epsilon_rate = int(epsilon_rate, 2)
    print("Gamma rate is: ",gamma_rate)
    print("Epsilon rate is: ",epsilon_rate)

    return gamma_rate * epsilon_rate

def main():
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2021\Day3\Puzzle_Input.txt"
    readings = read_input_data(filename)
    power_consumption = determine_rates(readings)
    print("Power consumption is: ",power_consumption)

if __name__ == "__main__":
    main()