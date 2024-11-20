def consecutive_zeros(input_data):
    number_of_consecutive_zeros = 0
    zero_locations = input_data.split("1")
    for each_location in zero_locations:
        if len(each_location) > number_of_consecutive_zeros:
            number_of_consecutive_zeros = len(each_location)
    return number_of_consecutive_zeros

def main():
    input_data = "1001101000110"
    result = consecutive_zeros(input_data)
    print("The maximum number of consecutive zeros is: ")
    print(result)

if __name__ == "__main__":
    main()