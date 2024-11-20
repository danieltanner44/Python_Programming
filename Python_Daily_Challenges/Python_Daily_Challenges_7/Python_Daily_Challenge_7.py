def add_dots(input_string):
    output = ""
    for each_letter in input_string:
        output = output + each_letter + "."
    return output[0:-1]

def remove_dots(input_string):
    return input_string.replace('.','')

def main():
    input_string = "test"
    print(input_string, "original input text")
    string_added_dots = add_dots(input_string)
    print(string_added_dots, "added dots")
    string_removed_dots = remove_dots(string_added_dots)
    print(string_removed_dots, "removed dots")

if __name__ == "__main__":
    main()