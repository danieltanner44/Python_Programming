def palindrome(input_data):
    print(len(input_data)//2)
    for i in range(0,len(input_data)//2):
        print(i, input_data[i], input_data[-i-1])
        if input_data[i] != input_data[-i-1]:
            return False
    return True

def main():
    input_data = "bobasbob"
    result = palindrome(input_data)
    print("The test for palindome returned a: ")
    print(result)

if __name__ == "__main__":
    main()