import time
import numpy as np
from my_modules.development import fstring
from my_modules.development import print_array

def read_input_data(filename):
    robot_configurations = []
    with open(filename, 'r') as f:
        for line in f:
            temp = line.strip().replace("="," ").replace(",", " ").split(" ")
            robot_configurations.append([(int(temp[2]),int(temp[1])),(int(temp[5]),int(temp[4]))])
    return robot_configurations

def create_initial_robot_map(robot_configurations, space):
    # Create a quick tracker to allow the initial robot positions to be plotted
    initial_robot_map = np.full(space, fill_value=".", dtype=np.str_("U100"))
    for index, robot_configuration in enumerate(robot_configurations, start = 1):
        if initial_robot_map[robot_configuration[0]] == ".":
            initial_robot_map[robot_configuration[0]] = str(index)
        else:
            initial_robot_map[robot_configuration[0]] += f" {str(index)}"
    return initial_robot_map

def process_all_robot_movements(robot_configurations, num_time_steps, space_shape):
    # Create a numeric tracker to assess how many robots in each quadrant
    num_tracker_map = np.full(space_shape, fill_value=0, dtype=np.int16)
    # Create a string tracker to help find our Christmas tree easter egg
    str_tracker_map = np.full(space_shape, fill_value=".", dtype=np.str_("U10"))
    # Process movements for all robots for the required number of cycles
    for i in range(num_time_steps):
        # Don't need these for all cycles, just the final one
        # However, they were useful for finding the Christmas Tree
        current_num_step_tracker_map = num_tracker_map.copy()
        current_str_step_tracker_map = str_tracker_map.copy()
        # Loop over each robot and update it's position and trackers
        for index, robot_configuration in enumerate(robot_configurations):
            # Get the robot current position and velocity
            current_position = robot_configuration[0]
            velocity = robot_configuration[1]
            # Use the modulo operator to handle robot wrapping around array
            next_position = ((current_position[0] + velocity[0]) % (space_shape[0]),
                             (current_position[1] + velocity[1]) % (space_shape[1]))
            # Update the robot position in robot configurations
            # This will then be used as the input for the next step
            robot_configurations[index] = [next_position, velocity]
            current_str_step_tracker_map[next_position] = "X"
            current_num_step_tracker_map[next_position] += 1
    # return the trackers with the final robot positions
    return current_num_step_tracker_map, current_str_step_tracker_map


def calculate_quadrant_values(final_position_tracker_map, space_shape):
    quadrant_values = []
    # Find the main row and col dividers for the quadrants
    center_row_index = (space_shape[0] // 2)
    center_col_index = (space_shape[1] // 2)
    # Slice each quadrant and add up the number of robots in each quadrant
    quadrant_values.extend([np.sum(final_position_tracker_map[0:center_row_index, 0:center_col_index])])
    quadrant_values.extend([np.sum(final_position_tracker_map[center_row_index + 1:, 0:center_col_index])])
    quadrant_values.extend([np.sum(final_position_tracker_map[0:center_row_index, center_col_index + 1:])])
    quadrant_values.extend([np.sum(final_position_tracker_map[center_row_index + 1:, center_col_index + 1:])])

    # Loop over each quadrant and multiply the robot values together to get the safety factor
    safety_factor = 1
    for quadrant_value in quadrant_values:
        safety_factor = safety_factor * quadrant_value

    return quadrant_values, safety_factor

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2024\Day14\Puzzle_Input.txt"
    original_robot_configurations = read_input_data(filename)

    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=======================  Puzzle Input  =======================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))

    space_shape = [103,101]
    robot_configurations = original_robot_configurations.copy()
    initial_robot_map = create_initial_robot_map(robot_configurations, space_shape)
    print(fstring(f"There are a total of {len(robot_configurations)} robots, with initial conditions: ", "bk", "wt"))
    print(f"Robot #ID: Robot Configuration: [(row_pos, col_pos), (row_vel, col_vel)]")
    [print(f"Robot #{index}: Robot Configuration: {robot_configuration}") for index, robot_configuration in enumerate(robot_configurations, start = 1)]
    print()
    print(fstring(f"The initial positions of the robots are shown on the {space_shape[0]}x{space_shape[1]} map below: ", "bk", "wt"))
    print(fstring(f"(each identified by its own robot ID) ", "bk","wt"))
    print_array(initial_robot_map)
    print(fstring(f"====================  Puzzle Input - End =====================", "bk", "bl"))

    print(" ", end="\n\n")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=========================  PART ONE  =========================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))

    num_time_steps = 100
    robot_configurations = original_robot_configurations.copy()
    current_num_step_tracker_map, current_str_step_tracker_map = process_all_robot_movements(robot_configurations, num_time_steps, space_shape)
    print(fstring(f"After {num_time_steps} cycles the robots are in the following positions: ", "bk", "wt"))
    print_array(current_num_step_tracker_map)
    quadrant_values, safety_factor = calculate_quadrant_values(current_num_step_tracker_map, space_shape)
    part_one_ans = str(safety_factor)
    print(fstring(f"The quadrant values are: {[int(quadrant_value) for quadrant_value in quadrant_values]}", "bk", "wt"))
    print(fstring(f"Quadrant structure is: [top left, bottom left, top right, bottom right]", "bk", "wt"))
    print(fstring(f"======================  PART ONE - END  ======================", "bk", "bl"))

    print(" ", end="\n\n")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=========================  PART TWO  =========================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))

    num_time_steps = 7623
    robot_configurations = original_robot_configurations.copy()
    current_num_step_tracker_map, current_str_step_tracker_map = process_all_robot_movements(robot_configurations, num_time_steps, space_shape)
    print(fstring(f"After {num_time_steps} cycles the robots are in the following positions: ", "bk", "wt"))
    print_array(current_str_step_tracker_map)
    part_two_ans = str(num_time_steps)

    print(fstring(f"The first Christmas tree was found on step {part_two_ans} by successively ", "bk", "wt"))
    print(fstring(f"viewing all plotted arrays of robot positions until the Christmas tree ", "bk","wt"))
    print(fstring(f"was visible. A pause on each print of 0.1 seconds helped (time.sleep(0.1)).", "bk","wt"))
    print(fstring(f"======================  PART TWO - END  ======================", "bk", "bl"))

    print(" ", end="\n\n")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=========================  ANSWERS  ==========================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))
    print(f'{fstring("Part One:", "bk", "wt")}')
    print(f'The safety factor at 100 steps is: {fstring(part_one_ans, "wt", "bk")}')
    print(fstring(f"==============================================================", "bk", "bl"))
    print(f'{fstring("Part Two:", "bk", "wt")}')
    print(f'The Christmas tree appeared on step: {fstring(part_two_ans, "wt", "bk")}')
    print(fstring(f"==============================================================", "bk", "bl"))
    print(" ")

    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()