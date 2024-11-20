def format_number(number):
    number = str(number)
    result = ""
    for each_character in enumerate(number[::-1], start=1):
        result += each_character[1]
        if each_character[0]%3 == 0 and each_character[0] != len(number):
            result += ","
    return result[::-1]

def main():
    number = 100000
    result = format_number(number)
    print("The reformatted number is: ")
    print(result)

if __name__ == "__main__":
    main()