import time
import numpy as np

def read_input_data(filename):
    fabric_cut_proposals = []
    with (open(filename, 'r') as f):
        for line in f:
            line = line.strip().replace(" @", "").replace("#", "").replace(":", "").split(" ")
            line = [line[0]] + line[1].split(",") + line[2].split("x")
            fabric_cut_proposals.append(line)
    fabric_cut_proposals = np.array(fabric_cut_proposals, dtype=np.int16)
    return fabric_cut_proposals

def process_fabric(fabric_cut_proposals):
    fabric_layout = np.zeros(shape=[1000,1000], dtype=np.int16)
    # Map all proposed cuts to the layout
    for id, x, y, w, h in fabric_cut_proposals:
        fabric_layout[x:x+w, y:y+h] += 1
    # Check if each area overlapped or not
    for id, x, y, w, h in fabric_cut_proposals:
        if len(np.where(fabric_layout[x:x+w, y:y+h] <= 1)[0]) == w*h:
            claim_no_overlap = id
    return fabric_layout, claim_no_overlap

def calculate_overlap(fabric_layout):
    overlap_m2 = np.where(fabric_layout > 1)
    overlap = len(overlap_m2[0])
    return overlap

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2018\Day3\Puzzle_Input.txt"
    fabric_cut_proposals = read_input_data(filename)
    print(" ")
    print("The input proposed cuts are:")
    print(fabric_cut_proposals)

    fabric_layout, claim_no_overlap = process_fabric(fabric_cut_proposals)
    print(" ")
    print("The fabric layout is:")
    print(fabric_layout)
    overlap = calculate_overlap(fabric_layout)

    print(" ")
    print("=======================================================================================")
    print("The calculated overlap in m**2 is:", overlap)
    print("=======================================================================================")
    print(" ")

    print(" ")
    print("=======================================================================================")
    print("The only proposal that does not overlap others is from ID:", claim_no_overlap)
    print("=======================================================================================")
    print(" ")

    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())



if __name__ == "__main__":
    main()