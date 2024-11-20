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
    for call_number in bingo_numbers:
        print("=====================")
        print("Number: ", call_number)
        print("=====================")
        marking_boards[marking_boards == call_number] = -1
        for board in enumerate(marking_boards):
            check_row = np.sum(board[1], axis=1)
            check_column = np.sum(board[1], axis=0)
            if np.min(check_row) == -5 or np.min(check_column) == -5:
                return board[0], call_number, marking_boards[board[0], :, :]
    return

def final_score(boards, call_number, winning_board,winning_board_number):
    boards = boards[winning_board_number, :, :]
    answer = np.sum(boards[np.where(winning_board != -1)]) * call_number
    return answer

def main():
    filename = "D:\Python_Programming\Advent_of_Code\Advent_of_Code_2021\Day4\Puzzle_Input.txt"
    bingo_numbers, boards = read_input_data(filename)
    winning_board_number, call_number, winning_board = marking_boards(bingo_numbers, boards)
    print("BINGO!")
    answer = final_score(boards, call_number, winning_board, winning_board_number)
    print("Answer: ",answer)

if __name__ == "__main__":
    main()