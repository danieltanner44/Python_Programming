import numpy as np

def read_input_data(filename):
    boards = []
    with open(filename, 'r') as f:
        # Read bingo numbers
        bingo_numbers = [int(num) for num in f.readline().strip().split(",")]
        # Read boards
        boards_data = f.read().replace("\n\n", "\n").split("\n")
        # Split boards into 5 x 5 hands
        for entry in boards_data:
            if entry:
                temp_line = entry.replace("  ", " ").split(" ")
                if temp_line[0] == "":
                    temp_line = temp_line[1:]
                boards += [[int(a) for a in temp_line]]
    boards = np.array(boards)
    boards = np.reshape(boards, [np.size(boards)//25,5,5])
    return bingo_numbers, boards

def marking_boards(bingo_numbers, boards):
    marking_boards = boards.copy()
    boards_to_remove = []
    # Step through each bingo number
    for call_number in bingo_numbers:
        print("=====================")
        print("Number: ", call_number)
        print("=====================")
        marking_boards[marking_boards == call_number] = -1
        # For each number check all boards for completion
        for board in enumerate(marking_boards):
            check_row = np.sum(board[1], axis=1)
            check_column = np.sum(board[1], axis=0)
            # If complete board found then add to list of those to remove
            if np.min(check_row) == -5 or np.min(check_column) == -5:
                if np.size(marking_boards) > 25:
                    boards_to_remove.append(board[0])
                else:
                    return call_number, marking_boards
        # After checking all boards remove the complete boards if they exist
        if boards_to_remove:
            marking_boards = np.delete(marking_boards, np.array(boards_to_remove), axis=0)
            boards_to_remove = []
    return

def final_score(call_number, last_winning_board):
    answer = np.sum(last_winning_board[np.where(last_winning_board != -1)]) * call_number
    return answer

def main():
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2021\Day4\Puzzle_Input.txt"
    bingo_numbers, boards = read_input_data(filename)
    call_number, last_winning_board = marking_boards(bingo_numbers, boards)
    print("BINGO!")
    answer = final_score(call_number, last_winning_board)
    print("Answer: ",answer)

if __name__ == "__main__":
    main()