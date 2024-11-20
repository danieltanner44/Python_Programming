def count(input_string):
    return input_string.count("-") + 1

def main():
    input_string = "met-a-phor"
    count_output = count(input_string)
    print("The input string has "+str(count_output)+" syllables!")

if __name__ == "__main__":
    main()