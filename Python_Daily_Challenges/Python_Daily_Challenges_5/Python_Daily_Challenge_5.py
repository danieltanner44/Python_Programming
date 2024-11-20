def only_ints(a, b):
    if type(a) is int and type(b) is int:
        return True
    else:
        return False

def main():
    output = only_ints(1 ,2)
    print(output)

if __name__ == "__main__":
    main()