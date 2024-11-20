def online_count(statuses):
    counter = 0
    for each_person in statuses:
        if statuses[each_person] == "online":
            counter += 1
    return counter

def main():
    statuses = {
        "Alice": "online",
        "Bob": "offline",
        "Eve": "online",
    }
    counter = online_count(statuses)
    print(counter)

if __name__ == "__main__":
    main()