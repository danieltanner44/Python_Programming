import numpy as np
import time
import itertools

def reading_input_data(f):
    print("Reading input data...", end = "")
    data = np.array([],dtype=np.int64)
    for each_line in f:
        data = np.append(data,each_line.replace(" @", ",").replace(" ", "").strip("\n").split(","))
    data = np.array(np.reshape(data,[len(data)//6,6]),dtype=np.int64)
    print("[complete]", end="\n")
    print("#########################################")
    print("The hailstone trajectory details are:")
    print(data)
    print("#########################################")
    print("There are", np.shape(data)[0],"hailstones to track!")
    print("#########################################")
    print(" ")
    return data
def create_equations_of_lines(data):
    equations_of_lines = []
    for hailstones in data:
        # y = mx + c, where m = y_dot/x_dot and c = y - mx
        equations_of_lines.append((hailstones[4]/hailstones[3], hailstones[1] - ((hailstones[4]/hailstones[3])*hailstones[0]), hailstones[3], hailstones[0]))
    print(equations_of_lines)
    return equations_of_lines

def search_for_intersections(equations_of_lines, search_range):
    number_valid_intersections = 0
    for hailstone in itertools.combinations(equations_of_lines, 2):
        if hailstone[0][0] != hailstone[1][0]: # not parallel
            x = (hailstone[1][1] - hailstone[0][1])/(hailstone[0][0] - hailstone[1][0])
            y = (hailstone[0][0])*x + hailstone[0][1]
            if search_range[0] <= x <= search_range[1] and search_range[0] <= y <= search_range[1]:
                if (x - hailstone[0][3])/hailstone[0][2] <= 0 or (x - hailstone[1][3])/hailstone[1][2] <= 0:
                    if (x - hailstone[0][3]) / hailstone[0][2] <= 0 and (x - hailstone[1][3])/hailstone[1][2] <= 0:
                        print("Intersection in the past for both hailstones")
                    elif (x - hailstone[0][3]) / hailstone[0][2] <= 0:
                        print("Intersection in the past for hailstone A")
                    else:
                        print("Intersection in the past for hailstone B")
                else:
                    number_valid_intersections += 1
                    print("found one!", x, y, number_valid_intersections)
            else:
                print("outside search area!", x, y)
        else:
            print("hailstone trajectories are parallel!")
    return number_valid_intersections

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    fI = open(r'D:\Advent_of_Code\Advent_of_Code_2023\Day24\Puzzle_Input_d.txt', 'r')
    # Read all of the input data from Puzzle Input and organise it
    data = reading_input_data(fI)
    # Let's work out the equations of the lines
    equations_of_lines = create_equations_of_lines(data)
    # Now lets search for intersections
    search_range = [200000000000000, 400000000000000]
    #search_range = [7, 27]
    number_valid_intersections = search_for_intersections(equations_of_lines, search_range)
    print(" ")
    print("#########################################################")
    print(" ")
    print("#########################################################")
    print("The number of valid hailstone intersections is:", number_valid_intersections) # 17235 too high!
    print("#########################################################")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()