import numpy as np
import time
import my_modules.graph as mm
import matplotlib.pyplot as plt

def read_input_data(filename):
    instruction = []
    lights_affected = []
    with open(filename, 'r') as f:
        for line in f:
            temp = line.strip().split(" ")
            if len(temp) == 5: # Turn on/off
                temp = temp[1:]
            temp.pop(2)
            lights_affected.append([temp[1].split(","),temp[2].split(",")])
            instruction.append(temp[0])
    lights_affected = np.array(lights_affected, dtype=np.int16)
    return instruction, lights_affected

def process_lights(instruction, lights_affected):
    light_map = np.zeros(shape=[1000,1000], dtype=np.int8)
    for index, action in enumerate(instruction):
        if action == "on":
            light_map[lights_affected[index][0][1]:lights_affected[index][1][1]+1,lights_affected[index][0][0]:lights_affected[index][1][0]+1] += 1
        elif action == "off":
            light_map[lights_affected[index][0][1]:lights_affected[index][1][1]+1,lights_affected[index][0][0]:lights_affected[index][1][0]+1] -= 1
            light_map[np.where(light_map == - 1)] = 0
        elif action == "toggle":
            light_map[lights_affected[index][0][1]:lights_affected[index][1][1]+1,lights_affected[index][0][0]:lights_affected[index][1][0]+1] += 2
        else:
            print("Data input error!!!")
    plot_array(light_map)
    total_light_brightness = np.sum(light_map)
    return total_light_brightness

def plot_array(array):
    # Display the matrix as an image
    plt.imshow(array, cmap='gray', interpolation='nearest')
    plt.colorbar()  # Add a color bar to indicate values
    plt.title("Matrix of Ones and Zeros")
    plt.xlabel("Column Index")
    plt.ylabel("Row Index")
    plt.show()
    return

def toggle(array):
    shape = np.shape(array)
    toggled_array = array.copy()
    print(shape)
    for i in range(shape[0]):
        for j in range(shape[1]):
            if array[i,j] == 0:
                toggled_array[i,j] = 1
            if array[i,j] == 1:
                toggled_array[i,j] = 0
    return toggled_array

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2015\Day6\Puzzle_Input.txt"
    instruction, lights_affected = read_input_data(filename)
    total_light_brightness = process_lights(instruction, lights_affected)
    print(" ")
    print("==============================================================")
    print("The total brightness of the lights is:",total_light_brightness)
    print("==============================================================")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()