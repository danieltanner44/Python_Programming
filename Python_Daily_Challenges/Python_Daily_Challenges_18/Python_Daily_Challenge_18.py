def convert(input_data):
    return [str(each_element) for each_element in input_data]

def main():
    input_data = [0, 1, 2]
    result = convert(input_data)
    print("The result is: ")
    print(result)

if __name__ == "__main__":
    main()