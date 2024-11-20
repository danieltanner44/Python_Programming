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
    # First loop check oxygen and second loop co2
    for i in range(2):
        readings_to_check = readings
        for current_bit in range(0,np.size(readings,axis=1)):
            if np.size(readings_to_check, axis=0) == 1:
                break
            reading_totals = np.sum(readings_to_check, axis=0)
            if reading_totals[current_bit] >= np.size(readings_to_check, axis=0)/2:
                common = [1,0] # (most, least)
                delete = [0,1]
            else:
                common = [0,1] # (most, least)
                delete = [1,0]
            readings_to_check = np.delete(readings_to_check,np.where(readings_to_check[:,current_bit] == delete[i]),axis=0)
        # Now save final numbers
        if i == 0:
            oxygen_generator_rating = ""
        else:
            CO2_scrubber_rating = ""
        for element in readings_to_check[0]:
            if i == 0:
                oxygen_generator_rating += str(element)
            else:
                CO2_scrubber_rating += str(element)
    print("CO2 scrubber rating: ", CO2_scrubber_rating, int(CO2_scrubber_rating, 2))
    print("oxygen_generator_rating: ", oxygen_generator_rating, int(oxygen_generator_rating, 2))

    return int(oxygen_generator_rating, 2) * int(CO2_scrubber_rating, 2)

def main():
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2021\Day3\Puzzle_Input.txt"
    readings = read_input_data(filename)
    power_consumption = determine_rates(readings)
    print("Power consumption is: ",power_consumption)

if __name__ == "__main__":
    main()