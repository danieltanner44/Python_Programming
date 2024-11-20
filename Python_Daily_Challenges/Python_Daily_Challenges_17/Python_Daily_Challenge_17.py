def triple_and(a,b,c):
    input_data = [a,b,c]
    if len(set(input_data)) == 1 and input_data[0] == True:
        return True
    return False

def main():
    input_data = [True, True, True]
    result = triple_and(input_data[0],input_data[1],input_data[2])
    print("The result is: ")
    print(result)

if __name__ == "__main__":
    main()