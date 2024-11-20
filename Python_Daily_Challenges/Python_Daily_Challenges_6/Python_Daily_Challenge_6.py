def double_letters(input_string):
    for index, each_letter in enumerate(input_string[1:], start=1):
        if each_letter == input_string[index-1]:
            print("The letter "+each_letter+" is duplicated!")
            return True
    print("No duplicated letters!")
    return False

def main():
    input_string = "abcda"
    output = double_letters(input_string)
    print(output)

if __name__ == "__main__":
    main()