def capital_indexes(input):
    output = []
    for each_letter in enumerate(input):
        if each_letter[1].isupper():
            output.append(each_letter[0])
    return output

def main():
    input_string = input("Please enter input string: ")
    output = capital_indexes(input_string)
    print(output)

if __name__ == "__main__":
    main()