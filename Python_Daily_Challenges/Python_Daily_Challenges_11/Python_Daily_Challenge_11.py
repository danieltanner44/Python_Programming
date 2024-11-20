def largest_difference(input_data):
    return max(input_data) - min(input_data)

def main():
    input_data = [1, 2, 3]
    print("The input data is:")
    print(input_data)
    output = largest_difference(input_data)
    print("The largest difference is:")
    print(output)

if __name__ == "__main__":
    main()