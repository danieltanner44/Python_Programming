import time
import numpy as np
import matplotlib.pyplot as plt

def read_input_data(filename):
    input_numbers = []
    folds = []
    with open(filename, 'r') as f:
        for each_line in f:
            if each_line.find("=") > 0:
                temp = each_line.strip().split(" ")
                folds.append(temp[2].split("="))
            elif each_line.find(",") > 0:
                input_numbers.append(each_line.strip().split(","))
    input_numbers = np.array(input_numbers, dtype=np.int16)
    return input_numbers, folds

def plot_paper_dots(input_numbers):
    x_max = np.max(input_numbers[:, 0]) + 1
    y_max = np.max(input_numbers[:, 1]) + 1
    plot_array = np.full([y_max,x_max], ".", dtype=np.str_)
    print(plot_array)
    print(" ")
    for dot in input_numbers:
        plot_array[dot[1],dot[0]] = "#"
    print(plot_array)
    return plot_array

def process_folds(plot_array, folds):
    print(" ")
    print("Initial array no folds, shape "+ str(np.shape(plot_array)))
    print("Number of dots found:", len(np.where(plot_array == "#")[0]))  # 742 too high
    for index, instruction in enumerate(folds, start = 1):
        if instruction[0] == "y":
            first_array = plot_array[0:int(instruction[1]), :]
            second_array = plot_array[int(instruction[1]) + 1:, :][::-1,:]
            if np.shape(first_array) != np.shape(second_array):
                # If the paper is not folded in the centre then we need to pad one of the arrays to add them
                difference = np.shape(first_array)[0] - np.shape(second_array)[0]
                second_array = np.pad(second_array, pad_width=((difference,0),(0,0)), mode="constant", constant_values=".")
                plot_array = first_array + second_array
            else:
                plot_array = plot_array[0:int(instruction[1]), :] + plot_array[int(instruction[1]) + 1:, :][::-1,:]
        elif instruction[0] == "x":
            first_array = plot_array[:,0:int(instruction[1])]
            second_array = plot_array[:, int(instruction[1])+1:][:,::-1]
            if np.shape(first_array) != np.shape(second_array):
                # If the paper is not folded in the centre then we need to pad one of the arrays to add them
                difference = np.shape(first_array)[1] - np.shape(second_array)[1]
                second_array = np.pad(second_array, pad_width=((0, 0), (difference, 0)), mode="constant", constant_values=".")
                plot_array = first_array + second_array
            else:
                plot_array = plot_array[:,0:int(instruction[1])] + plot_array[:, int(instruction[1])+1:][:,::-1]
        # Merge the element components to be either # or .
        plot_array = np.where(np.char.find(plot_array, '#') != -1, "#", plot_array)
        plot_array = np.where(np.char.find(plot_array, '.') != -1, ".", plot_array)
        print(" ")
        print("Following fold " + str(index), "with instruction "+str(folds[index - 1]),"and shape "+ str(np.shape(plot_array)))
        print("Number of dots found:", len(np.where(plot_array == "#")[0])) # 742 too high
        print(plot_array)
        plot_image_of_array(plot_array)
        print(" ")
    return plot_array

def plot_image_of_array(plot_array):
    image_of_array = np.zeros(shape=np.shape(plot_array), dtype=np.int8)
    image_of_array = np.where(np.char.find(plot_array, '.') != -1, 0, image_of_array)
    image_of_array = np.where(np.char.find(plot_array, '#') != -1, 1, image_of_array)

    # Plot the array as an image
    plt.imshow(image_of_array, cmap='gray')  # You can change the colormap
    plt.colorbar()  # Optional: add a colorbar
    plt.title('Current fold')
    plt.axis('off')  # Optional: turn off axis
    plt.show()

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = f"D:\Python_Programming\Advent_of_Code\Advent_of_Code_2021\Day13\Puzzle_Input.txt"
    input_numbers, folds = read_input_data(filename)
    print("The input numbers are:")
    print(input_numbers)
    print("The fold instructions are:")
    print(folds)
    plot_array = plot_paper_dots(input_numbers)
    plot_array = process_folds(plot_array, folds)

    print("==============================================================")
    print("The final image from the thermal camera is:")
    print(" ")
    print(plot_array)
    print(" ")
    print("==============================================================")
    print(" ")
    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()