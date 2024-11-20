import time

def read_input_data(filename):
    input_masses = []
    with open(filename, 'r') as f:
        for line in f:
            input_masses.append(int(line.strip()))
    return input_masses

def process_masses(input_masses):
    module_mass_fuel_requirement = 0
    total_fuel_requirement = 0
    for index, mass in enumerate(input_masses):
        module_mass_fuel_requirement += int((mass / 3)) - 2
        while mass > 0:
            mass = int((mass / 3)) - 2
            if mass <= 0:
                continue
            elif mass > 0:
                total_fuel_requirement += mass
    return module_mass_fuel_requirement, total_fuel_requirement

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2019\Day1\Puzzle_Input.txt"
    input_masses = read_input_data(filename)
    print("The input masses are:")
    print(input_masses)
    module_mass_fuel_requirement, total_fuel_requirement = process_masses(input_masses)
    print(" ")
    print("==============================================================")
    print("PART 1: The fuel requirement for module mass only is:", module_mass_fuel_requirement)
    print("==============================================================")
    print(" ")
    print(" ")
    print("==============================================================")
    print("PART 2: The total fuel requirement is:", total_fuel_requirement)
    print("==============================================================")
    print(" ")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()