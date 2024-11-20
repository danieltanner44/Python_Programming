def zap(input_data_a, input_data_b):
    return [(element_a[1], input_data_b[element_a[0]]) for element_a in enumerate(input_data_a)]

def main():
    input_data_a = [0, 1, 2, 3]
    input_data_b = [5, 6, 7, 8]
    result = zap(input_data_a, input_data_b)
    print("The result is: ")
    print(result)

if __name__ == "__main__":
    main()