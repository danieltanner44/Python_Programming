def list_xor(n, list1, list2):
    print(list1.count(n))
    if list1.count(n) == 0 and list2.count(n) == 0: # In neither list
        return False
    elif list1.count(n) != 0 and list2.count(n) != 0: # In both lists
        return False
    return True

def main():
    n = 1
    list1 = [1, 2, 3]
    list2 = [1, 5, 6]
    result = list_xor(n, list1, list2)
    print("The check returned: ")
    print(result)

if __name__ == "__main__":
    main()