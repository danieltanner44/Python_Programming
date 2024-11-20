import numpy as np

def read_input_data(filename):
    input_data = []
    with open(filename, 'r') as f:
        for lines in f:
            input_data.append(lines.strip("\n").replace(" -> ", ",").split(","))
            # Consider only horizontal lines
            if input_data[-1][0] != input_data[-1][2] and input_data[-1][1] != input_data[-1][3]:
                input_data.remove(input_data[-1])
        input_data = np.array(input_data,dtype=int)
    return input_data

def calculate_cloud_locations(input_data):
    max_x = max(np.max(input_data[:,0]),np.max(input_data[:,2]))
    max_y = max(np.max(input_data[:,1]), np.max(input_data[:,3]))
    cloud_map = np.zeros([max_x+1,max_y+1], dtype=int)
    for lines in input_data:
        x1,y1,x2,y2 = lines
        steps_x = x2 - x1
        steps_y = y2 - y1
        cloud_map[x1, y1] += 1
        for i in range(max(abs(steps_x),abs(steps_y))):
            x1 += steps_x//max(abs(steps_x),abs(steps_y))
            y1 += steps_y//max(abs(steps_x),abs(steps_y))
            cloud_map[x1,y1] += 1
    return cloud_map

def find_peak_locations(cloud_map):
    return len(cloud_map[cloud_map >= 2])

def main():
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2021\Day5\Puzzle_Input.txt"
    input_data = read_input_data(filename)
    print("The input data is",len(input_data),"lines long and contains: ")
    print(input_data)
    cloud_map = calculate_cloud_locations(input_data)
    answer = find_peak_locations(cloud_map)
    print("The answer is: ",answer)

if __name__ == "__main__":
    main()