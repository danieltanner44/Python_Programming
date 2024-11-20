def param_count(*parameters):
    return len(parameters)

def main():
    result = param_count()
    print("The number of parameters called is: ")
    print(result)

if __name__ == "__main__":
    main()