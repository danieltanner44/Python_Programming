def is_anagram(a, b):
    if sorted(a) == sorted(b):
        return True
    return False

def main():
    output = is_anagram("typhoon", "opython")
    print("The input strings anagram check was "+str(output)+"!")

if __name__ == "__main__":
    main()