def flatten(input_data):
    output = []
    for each_element in input_data:
        for each_number in each_element:
            output.append(each_number)
    return output

def main():
    input_data = [[1, 2], [3, 4]]
    print("The input data is:")
    print(input_data)
    output = flatten(input_data)
    print("The flattened data is:")
    print(output)

if __name__ == "__main__":
    main()