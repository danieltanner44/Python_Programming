def readfile(filename):
    data = []
    f = open(filename)
    for each_line in f:
        data.append(float(each_line))
    return data

def analyse_data(data):
    counter = 0
    for element in data:
        if counter == 0:
            max_value = element
            min_value = element
            counter += 1
        if element >= max_value:
            max_value = element
        if element <= min_value:
            min_value = element
    return min_value, max_value

def main():
    filename = "Python_Nerds_Challenge_1.txt"
    data = readfile(filename)
    min_value, max_value = analyse_data(data)
    print("The maximum value in the data is: "+str(max_value))
    print("The minimum value in the data is: "+str(min_value))

if __name__ == "__main__":
    main()