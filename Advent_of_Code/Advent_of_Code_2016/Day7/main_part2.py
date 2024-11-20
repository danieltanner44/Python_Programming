import time

def read_input_data(filename):
    ip_addresses = []
    with open(filename, 'r') as f:
        for line in f:
            ip_addresses.append(line.strip().replace("[","]").split("]"))
    return ip_addresses

def process_ip_addresses(ip_addresses):
    valid_ip_counter = 0
    for index, ip_address in enumerate(ip_addresses):
        all_valid_babs = []
        all_valid_abas = []
        for index, string in enumerate(ip_address):
            if index % 2 == 0:  # Even - ABA areas outside of []
                valid_abas = check_for_aba(string, "aba")
                if valid_abas:
                    all_valid_abas += valid_abas
            else:  # Odd - BAB areas inside of []
                valid_babs = check_for_aba(string, "bab")
                if valid_babs:
                    all_valid_babs += valid_babs

        # Logic to check if this is a valid ip address
        # Must have a matching aba and bab
        if any(a == b for a in all_valid_abas for b in all_valid_babs):
            print(f"Valid IP: {ip_address}, abas: {all_valid_abas}, babs: {all_valid_babs}")
            valid_ip_counter += 1
    return valid_ip_counter

def check_for_aba(ip_segment, string):
    valid_pattern = []
    # Look for the require repeating characters abba or similar
    ip_segment = list(ip_segment)
    for index, character in enumerate(ip_segment[:-2]):
        # Assess in blocks of 3 if first and last equal and middle is different then found
        if character == ip_segment[index + 2] and character != ip_segment[index + 1]:
            if string == "aba":
                valid_pattern.append(character + ip_segment[index + 1] + character)
            elif string == "bab":
                valid_pattern.append(ip_segment[index + 1] + character + ip_segment[index + 1])
    # returns all abas and babs found
    return valid_pattern

def main():
    ts0 = time.time()
    print("Starting time:", time.ctime())
    print(" ")
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2016\Day7\Puzzle_Input.txt"
    ip_addresses = read_input_data(filename)

    print(" ")
    print("==============================================================")
    print(f"There are {len(ip_addresses)} input ip addresses to assess, they are:")
    [print(ip_address) for ip_address in ip_addresses]
    print("==============================================================")
    print(" ")

    # Now count the number of valid ip addresses
    valid_ip_counter = process_ip_addresses(ip_addresses)

    print(" ")
    print("==============================================================")
    print(f"The number of valid ip addresses is: {valid_ip_counter}")
    print("==============================================================")
    print(" ")

    ts1 = time.time()
    print(" ")
    print("Elapsed time:", round((ts1 - ts0)//3600,2), "hours or", round(ts1 - ts0,1),"seconds!")
    print(" ")
    print("Finishing time:", time.ctime())

if __name__ == "__main__":
    main()