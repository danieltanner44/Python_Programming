import random
def random_number():
    output = random.randint(0, 100)
    return output

def main():
    output = random_number()
    print(output)

if __name__ == "__main__":
    main()