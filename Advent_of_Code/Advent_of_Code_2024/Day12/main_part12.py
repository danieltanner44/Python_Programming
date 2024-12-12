import time
import numpy as np
from my_modules.development import fstring
from my_modules.development import print_array

def read_input_data(filename):
    garden_plot_map = []
    with open(filename, 'r') as f:
        for line in f:
            garden_plot_map.append(list(line.strip()))
    plot_types = sorted(set([plot for line in garden_plot_map for plot in line]))
    garden_plot_map = np.array(garden_plot_map, dtype=np.str_)
    return garden_plot_map, plot_types

def calculate_area_of_regions(regions, garden_region_map):
    region_areas = {}
    for region_id in regions:
        region_areas[region_id] = len(np.where(garden_region_map == region_id)[0])
    return region_areas

def calculate_perimeter_of_regions(regions, garden_region_map):
    # This is the Part One logic
    # Loop over all plots and check the neighbours in the cardinal directions
    # If they are a different plot type in any direction a fence is needed
    plot_perimeters = {region_id : 0 for region_id in regions}
    garden_shape = np.shape(garden_region_map)
    # Loop over every plot in the garden and check its neighbours to see if a fence is needed
    for row in range(garden_shape[0]):
        for col in range(garden_shape[1]):
            region_id = garden_region_map[row, col]
            # The main check for the fence is performed in this subroutine
            perimeter = check_perimeter_with_neighbour_plots(garden_region_map, (row, col), region_id, garden_shape)
            # Add the perimeter to the associated region
            plot_perimeters[region_id] += perimeter
    return plot_perimeters

def check_perimeter_with_neighbour_plots(garden_region_map, index, region_id, garden_shape):
    # For each input plot check the four cardinal neighbours
    # If they are off the garden map or a different type add one to the perimeter (as a fence is needed)
    # Check for non-matching neighbouring plot type in cardinal directions
    cardinal_directions = [(1,0),(-1,0),(0,1),(0,-1)]
    perimeter = 0
    for cardinal_direction in cardinal_directions:
        neighbour = (index[0] + cardinal_direction[0], index[1] + cardinal_direction[1])
        # Check if neighbour still in plot
        if neighbour[0] >= 0 and neighbour[1] >= 0 and neighbour[0] < garden_shape[0] and neighbour[1] < garden_shape[1]:
            if garden_region_map[neighbour] != region_id:
                perimeter += 1
        else:
            perimeter += 1
    return perimeter

def calculate_fencing_price(region_areas, region_perimeters):
    # The fence pricing is the region area times the region perimeter
    # Same logic applied to both Part One and Part Two
    fencing_cost = 0
    for region_id in region_areas:
        fencing_cost += region_areas[region_id] * region_perimeters[region_id]
    return fencing_cost

def create_unique_region_id(starting_plot_type, regions):
    index = 0
    while True:
        index += 1
        region_id = starting_plot_type + str(index)
        if region_id in regions:
            continue
        else:
            return region_id

def find_neighbours_in_region(garden_plot_map, next_neighbour_to_check, region_plot_type, garden_shape, region_id):
    # This subroutine finds the neighbours of input plots and determines if they
    # are the same type and therefore belong to the same region
    # Additionally, his subroutine gathers additional neighbour data to support Part Two
    # For each plot a record is stored of what sides are fenced
    neighbours_in_region = []
    neighbours_in_region_details = {}
    fence_sides = {"id": region_id, 1: 0, 2: 0, 3: 0, 4: 0}
    # Check for non-matching neighbouring plot type in cardinal directions
    cardinal_directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for index, cardinal_direction in enumerate(cardinal_directions, start=1):
        neighbour = (next_neighbour_to_check[0] + cardinal_direction[0],
                     next_neighbour_to_check[1] + cardinal_direction[1])
        # Check if neighbour still in garden
        if 0 <= neighbour[0] < garden_shape[0] and 0 <= neighbour[1] < garden_shape[1]:
            # If in garden and of the same type then it is part of the same region
            if garden_plot_map[neighbour] == region_plot_type:
                neighbours_in_region.extend([neighbour])
            else:
                fence_sides[index] = 1
        else:
            fence_sides[index] = 1
        neighbours_in_region_details[next_neighbour_to_check] = fence_sides
    return neighbours_in_region, neighbours_in_region_details

def find_regions(garden_plot_map):
    # This subroutine grows out from an initial plot to encompass all adjacent plots of that type
    # Therefore it provides a regional breakdown of the garden by adjacent plot types
    regions = {}
    all_neighbour_details = {}
    garden_shape = np.shape(garden_plot_map)
    # Track which plots have been attributed to a region
    plot_processed_tracker = np.full(np.shape(garden_plot_map), fill_value=".", dtype=np.str_)
    while len(np.where(plot_processed_tracker == ".")[0]) != 0:
        plot_remaining = np.where(plot_processed_tracker == ".")
        # Take the next unprocessed plot and use it as the next region seed
        neighbour_processing_list = [(plot_remaining[0][0], plot_remaining[1][0])]
        region_plot_type = garden_plot_map[neighbour_processing_list[0]]
        region_id = create_unique_region_id(region_plot_type, regions)
        regions[region_id] = []

        # Check neighbours and add to region using this structure [(row,col), (row,col), ...]
        while len(neighbour_processing_list) != 0:
            # Keep visiting successive neighbours if they are same plot type
            # If so add to list for region and for their neighbours to be processed
            next_neighbour_to_check = neighbour_processing_list.pop(0)
            regions[region_id].extend([next_neighbour_to_check])
            plot_processed_tracker[next_neighbour_to_check] = "X"
            neighbours_in_region, neighbours_in_region_details = find_neighbours_in_region(garden_plot_map, next_neighbour_to_check, region_plot_type, garden_shape, region_id)
            all_neighbour_details.update(neighbours_in_region_details)
            # Add new neighbours to processing list for region, so their neighbours are assessed too
            for neighbour_in_region in neighbours_in_region:
                if neighbour_in_region not in neighbour_processing_list and plot_processed_tracker[neighbour_in_region] == ".":
                    neighbour_processing_list.extend([neighbour_in_region])
    return regions, all_neighbour_details

def create_garden_region_map(garden_plot_map, regions):
    # This subroutine just creates an array to show the regional breakdown of the garden
    max_id_length = max(len(region_id) for region_id in regions)
    garden_region_map = np.full(np.shape(garden_plot_map), fill_value=".", dtype=np.str_(f"U{max_id_length}"))
    for region_id in regions:
        for location in regions[region_id]:
            garden_region_map[location] = region_id
    return garden_region_map

def remove_discounted_fences(garden_region_map, neighbours_in_region_details):
    # This is pretty hacky but essentially scans first across the plots (horizontally)
    # and then down the plots (vertically). If the next cell has the same fence direction
    # then it is removed for the current plot. For instance, if the current plot is
    # checked against the plot to the right and they both have a fence at the top
    # of the plot (looking down) then remove it on the current plot. Similar for
    # other directions
    garden_shape = np.shape(garden_region_map)
    # Scan horizontally - as starting inner loop over columns
    for row in range(garden_shape[0]):
        for col in range(garden_shape[1] - 1):
            current_plot_location = (row,col)
            next_plot_location = (row, col+1)
            if neighbours_in_region_details[current_plot_location]["id"] == neighbours_in_region_details[next_plot_location]["id"]:
                # They are in the same region
                if (neighbours_in_region_details[current_plot_location][1] == 1 and
                        neighbours_in_region_details[next_plot_location][1] == 1):
                    # If they both have bottom fences then remove mine
                    neighbours_in_region_details[current_plot_location][1] = 0
                if (neighbours_in_region_details[current_plot_location][2] == 1 and
                        neighbours_in_region_details[next_plot_location][2] == 1):
                    # If they both have top fences then remove mine
                    neighbours_in_region_details[current_plot_location][2] = 0
    # Scan vertically - as starting inner loop over rows
    for col in range(garden_shape[1]):
        for row in range(garden_shape[0] - 1):
            current_plot_location = (row,col)
            next_plot_location = (row + 1, col)
            if neighbours_in_region_details[current_plot_location]["id"] == neighbours_in_region_details[next_plot_location]["id"]:
                # They are in the same region
                if (neighbours_in_region_details[current_plot_location][3] == 1 and
                        neighbours_in_region_details[next_plot_location][3] == 1):
                    # If they both have right fences then remove mine
                    neighbours_in_region_details[current_plot_location][3] = 0
                if (neighbours_in_region_details[current_plot_location][4] == 1 and
                        neighbours_in_region_details[next_plot_location][4] == 1):
                    # If they both have left fences then remove mine
                    neighbours_in_region_details[current_plot_location][4] = 0
    discounted_fence_details = neighbours_in_region_details
    return discounted_fence_details

def calculate_discounted_fence_perimeter(discounted_fence_details):
    # This subroutine loops over the dictionaries of all plot fences and adds them up for each region
    discounted_fence_perimeter = {}
    # Loop over every plot
    for plot in discounted_fence_details:
        perimeter = 0
        # Access the details dictionary
        for key, value in discounted_fence_details[plot].items():
            if key != "id":
                # Add up the perimeter/fences for each side of plot
                perimeter += value
            else:
                region_id = value
        # Add the values for each plot to the relevant region
        if region_id in discounted_fence_perimeter:
            discounted_fence_perimeter[region_id] += perimeter
        else:
            discounted_fence_perimeter[region_id] = perimeter
    return discounted_fence_perimeter

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2024\Day12\Puzzle_Input.txt"
    garden_plot_map, plot_types = read_input_data(filename)

    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=======================  Puzzle Input  =======================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"There are {len(plot_types)} plot types in the garden, namely: ", "bk", "wt"))
    print(plot_types)
    print(fstring(f"The garden plot map has shape {np.shape(garden_plot_map)} and is: ", "bk", "wt"))
    print_array(garden_plot_map)

    print(fstring(f"====================  Puzzle Input - End =====================", "bk", "bl"))

    print(" ", end="\n\n")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=========================  PART ONE  =========================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))

    regions, neighbours_in_region_details = find_regions(garden_plot_map)
    garden_region_map = create_garden_region_map(garden_plot_map, regions)
    region_areas = calculate_area_of_regions(regions, garden_region_map)
    region_perimeters = calculate_perimeter_of_regions(regions, garden_region_map)
    fencing_cost = calculate_fencing_price(region_areas, region_perimeters)
    part_one_ans = str(fencing_cost)

    print(fstring(f"There are {len(regions)} regions in the garden, namely:", "bk", "wt"))
    print([region_id for region_id in regions])
    print(fstring(f"The regional map of the garden is:", "bk", "wt"))
    print_array(garden_region_map)
    print(fstring(f"The regional areas are:", "bk", "wt"))
    print([(region_id, region_areas[region_id]) for region_id in regions])
    print(fstring(f"The regional perimeters are:", "bk", "wt"))
    print([(region_id, region_perimeters[region_id]) for region_id in regions])
    print(fstring(f"The total cost of fencing is: {part_one_ans}", "bk", "wt"))
    print(fstring(f"======================  PART ONE - END  ======================", "bk", "bl"))

    print(" ", end="\n\n")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=========================  PART TWO  =========================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))

    discounted_fence_details = remove_discounted_fences(garden_region_map, neighbours_in_region_details)
    discounted_fence_perimeter = calculate_discounted_fence_perimeter(discounted_fence_details)
    fencing_cost = calculate_fencing_price(region_areas, discounted_fence_perimeter)
    part_two_ans = str(fencing_cost)

    print(fstring(f"The regional areas remain the same and are:", "bk", "wt"))
    print([(region_id, region_areas[region_id]) for region_id in regions])
    print(fstring(f"The discounted regional perimeters are:", "bk", "wt"))
    print([(region_id, discounted_fence_perimeter[region_id]) for region_id in regions])
    print(fstring(f"The total cost of fencing is: {part_two_ans}", "bk", "wt"))
    print(fstring(f"======================  PART TWO - END  ======================", "bk", "bl"))

    print(" ", end="\n\n")
    print(fstring(f"==============================================================", "bk", "bl"))
    print(fstring(f"=========================  ANSWERS  ==========================", "bk", "bl"))
    print(fstring(f"==============================================================", "bk", "bl"))
    print(f'{fstring("Part One:", "bk", "wt")}')
    print(f'The fencing cost is: {fstring(part_one_ans, "wt", "bk")}')
    print(fstring(f"==============================================================", "bk", "bl"))
    print(f'{fstring("Part Two:", "bk", "wt")}')
    print(f'The discounted fencing cost is: {fstring(part_two_ans, "wt", "bk")}')
    print(fstring(f"==============================================================", "bk", "bl"))
    print(" ")

    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()