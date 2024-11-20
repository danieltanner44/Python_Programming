import numpy as np
import time
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq, fftshift

def reading_input_data(fI):
    print("Reading block of input data...")
    only_once = False
    for each_line in fI:
        each_line = (each_line.strip("\n")).split()[0]
        temp = np.array(list(each_line), dtype=str)
        if only_once == True:
            data = np.vstack((data, temp)) # Build each block
        else:
            data = np.array(temp, dtype=str)
            only_once = True
    return data

def tilting_level(data):
    r_indices = np.array(np.where(data == "#"))
    r_indices = np.array(list(zip(r_indices[0], r_indices[1])))
    r_indices = r_indices[r_indices[:, 1].argsort(kind="mergesort")]
    size = np.shape(data)
    # Now we know where everything is lets start sorting
    for i in range(size[1]): # one column at a time
        starting_point, first_r_rock = 0, False
        # Had no R rocks then just sort them
        if not np.any(data[:,i] == "#"):
            temp = data[starting_point:size[0], i]
            data[starting_point:size[0], i] = np.sort(temp, kind='mergesort')[::-1]
            continue # Skip back to next i
        elif not np.any(data[:,i] == "O"):
            continue # Has no O rocks to sort so just skip
        for r in r_indices: # Walk through every R rock
            if r[1] == i: # R rock is in the current column
                r_indices = np.delete(r_indices, 0, axis=0)
                # start to first R rock
                if not first_r_rock:
                    if r[0] == 0: # If the first symbol is "#" just skip
                        starting_point += 1
                        first_r_rock = True
                        continue
                    else:
                        temp = data[starting_point:r[0], i]
                        data[starting_point:r[0], i] = np.sort(temp, kind='mergesort')[::-1]
                        starting_point = r[0] + 1
                        first_r_rock = True
                        continue
                # Between two R rocks
                if r[0] != size[0] - 1: # If the next R rock is not the last element of the column
                    if r[0] - starting_point <= 1: # If next one is the same space
                        starting_point = r[0] + 1
                        continue # Next R rock
                    else: # It is the last element of the current column
                        temp = data[starting_point:r[0], i]
                        data[starting_point:r[0], i] = np.sort(temp, kind='mergesort')[::-1]
                        starting_point = r[0] + 1
                        continue # Next R rock
                else: # The R Rock is at the end of the column
                    temp = data[starting_point:size[0], i]
                    data[starting_point:size[0], i] = np.sort(temp, kind='mergesort')[::-1]
            else:
                if first_r_rock == True:
                    break
                continue
        # Having step through all R rocks now consider from the last R rock to the end of the column
        if starting_point < size[0] - 1:
            temp = data[starting_point:size[0], i]
            data[starting_point:size[0], i] = np.sort(temp, kind='mergesort')[::-1]
    return data

def score_calculation(data):
    total_score = 0
    size = np.shape(data)
    O_indices = np.array(np.where(data == "O"))
    O_indices = np.array(list(zip(O_indices[0], O_indices[1])))
    for O in O_indices:
        total_score += size[0] - O[0]
    return total_score

def spin_cycle(data):
    # let's undertake one cycle of North, South, West, East tilts
    # First do North
    data = tilting_level(data)
    # Mow run West - Simulate by rotating data array and rotating back after tilting
    data = np.rot90(data, -1)
    data = tilting_level(data)
    data = np.rot90(data, 1)
    # Mow run South - Simulate by inverting data array and reinverting the answer
    data = np.flipud(data)
    data = tilting_level(data)
    data = np.flipud(data)
    # Mow run East - Simulate by rotating data array and rotating back after tilting
    data = np.rot90(data,1)
    data = tilting_level(data)
    data = np.rot90(data, -1)
    return data

def main():
    ts0 = time.time()
    total_score = 0
    print("Starting time:", time.ctime())
    print(" ")
    fI = open(r'D:\Advent_of_Code\Advent_of_Code_2023\Day14\Puzzle_Input.txt', 'r')
    # Read all of the input data from Puzzle Input and organise it
    data = reading_input_data(fI)
    print(data)
    print(" ")
    # Apply a single North, South, West, East spin cycle
    list_of_scores = np.array([],dtype=int)
    number_of_cycles = 10000
    print("Looping over the first", number_of_cycles, "cycles: ", end="")
    for i in range(number_of_cycles): # check with 3
        data = spin_cycle(data)
        list_of_scores = np.append(list_of_scores, score_calculation(data))
        if (i+1)%(number_of_cycles//10) == 0:
            print(i+1,",",end="")
    print("...[Complete]")
    print(" ")

    # Take a converged chunk of data from the end and analyse it
    test_sequence_length = 1000
    test_sequence = list_of_scores[number_of_cycles-test_sequence_length:number_of_cycles]
    average = int(np.round(np.mean(test_sequence)))
    print("Average is:", average)
    test_sequence = np.array(list_of_scores - average, dtype=int)

    # Lets visually check for convergence
    x_values = np.array(range(number_of_cycles))
    plt.figure(figsize=(20, 10))
    plt.grid(True)
    lines, = plt.plot(x_values, test_sequence, marker='o')
    plt.title("Look for convergence...it converges relatively quickly")
    plt.show()

    # Look at the frequency characteristics of the test sequence to find the periodicity
    # Compute the FFT
    fft_result = np.fft.fft(test_sequence)
    magnitude_spectrum = np.abs(fft_result)
    # Create frequency axis
    sampling_frequency = 1  # For simplicity, assuming unit sampling frequency
    frequency_axis = np.fft.fftfreq(len(test_sequence), d=1 / sampling_frequency)
    # Plot the frequency spectrum
    plt.stem(frequency_axis, magnitude_spectrum)
    plt.xlabel('Frequency')
    plt.ylabel('Magnitude')
    plt.title('Frequency plot of the integer sequence')
    plt.grid(True)
    plt.show()
    # Note peak at 0.077

    determined_frequency = float(input("What is the frequency you see (Hint: 0.077): "))
    target_number_cycles = 1000000000
    # Manually entered the
    print(int(round((target_number_cycles - number_of_cycles)%(determined_frequency*1000),0)))
    period_shift = int(round((target_number_cycles - number_of_cycles)%(determined_frequency*1000),0))
    print(period_shift)

    print(list_of_scores[len(list_of_scores) - period_shift - 4])
    print(list_of_scores[len(list_of_scores) - period_shift - 3])
    print(list_of_scores[len(list_of_scores) - period_shift - 2])
    print(list_of_scores[len(list_of_scores) - period_shift - 1])
    print(list_of_scores[len(list_of_scores) - period_shift])
    print(list_of_scores[len(list_of_scores) - period_shift + 1])
    print(list_of_scores[len(list_of_scores) - period_shift + 2])
    print(list_of_scores[len(list_of_scores) - period_shift + 3])
    print(list_of_scores[len(list_of_scores) - period_shift + 4])

    print(list_of_scores[len(list_of_scores)-40:len(list_of_scores)])

    print("The total score is: ",(list_of_scores[len(list_of_scores) - period_shift -1]))
    print("P.S. This is super messy. I plotted the frequency spectrum after the sequence appeared converged. Then worked out the modulus of the period of the n-cycle to the number of steps remaining...")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()