def mid(input):
    if (len(input)%2) == 0:
        output = str("")
    else:
        output = input[round((len(input) - 1)/2)]
    return output

def main():
    input_string = input("Please enter input string: ")
    output = mid(input_string)
    print(output)

if __name__ == "__main__":
    main()