def div_3(input_data):
    return input_data%3 == 0

def main():
    input_data = 9
    print("The input data is:")
    print(input_data)
    output = div_3(input_data)
    print("The check for divisibility by 3 is:")
    print(output)

if __name__ == "__main__":
    main()