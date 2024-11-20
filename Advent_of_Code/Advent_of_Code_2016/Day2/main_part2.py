import numpy as np
import time
import matplotlib.pyplot as plt

def read_input_data(filename):
    directions = []
    with open(filename, 'r') as f:
        for line in f:
            directions.append(line.strip())
    return directions

def entering_code(directions):
    keypad = np.array([["#","#","1","#","#"],["#","2","3","4","#"],["5","6","7","8","9"],["#","A","B","C","#"], ["#","#","D","#","#"]])
    keypad = np.pad(keypad, 1,mode="constant",constant_values="#")
    print("")
    print("The keypad is:")
    print(keypad)
    print("")
    code = []
    encoding = {"U" : -1, "D" : 1, "L" : - 1, "R" : 1}
    current_location = (3,1)
    for number in directions:
        for character in number:
            if character in ["U","D"]:
                current_location = (current_location[0] + encoding[character], current_location[1])
                if keypad[current_location] == "#" and character == "U":
                    current_location = (current_location[0] + 1, current_location[1])
                elif keypad[current_location] == "#" and character == "D":
                    current_location = (current_location[0] - 1, current_location[1])
            elif character in ["L","R"]:
                current_location = (current_location[0], current_location[1] + encoding[character])
                if keypad[current_location] == "#" and character == "L":
                    current_location = (current_location[0], current_location[1] + 1)
                elif keypad[current_location] == "#" and character == "R":
                    current_location = (current_location[0], current_location[1] - 1)
            else:
                print("Error in directions!")
        code.append(str(keypad[current_location]))
    code = ''.join(code)
    return code

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2016\Day2\Puzzle_Input.txt"
    directions = read_input_data(filename)
    print(" ")
    print("==============================================================")
    print("The input directions are:")
    print(directions)
    print("==============================================================")
    print(" ")
    code = entering_code(directions)
    print("==============================================================")
    print("The code to the bathroom is:", code)
    print("==============================================================")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()