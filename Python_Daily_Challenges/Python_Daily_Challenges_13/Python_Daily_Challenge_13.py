def get_row_col(input_data):
    location = [0,0]
    if input_data[0] == "A":
        location[1] = 0
    elif input_data[0] == "B":
        location[1] = 1
    elif input_data[0] == "C":
        location[1] = 2
    else:
        print("Input error!")
        return (0,0)
    location[0] = int(input_data[1]) - 1

    return tuple(location)

def main():
    input_data = "A3"
    location = get_row_col(input_data)
    print("The row and column locations are:")
    print(location)

if __name__ == "__main__":
    main()