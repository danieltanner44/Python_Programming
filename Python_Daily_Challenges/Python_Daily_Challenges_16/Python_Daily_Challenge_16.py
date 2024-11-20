def all_equal(input_data):
    print(len(set(input_data)))
    return len(set(input_data)) == 1 or len(set(input_data)) == 0

def main():
    input_data = []
    result = all_equal(input_data)
    print("The result of the check for all equal is: ")
    print(result)

if __name__ == "__main__":
    main()