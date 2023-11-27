from game import save_game


def load_from_file(file_location):
    puzzle = [[0, 1, 2],
              [4, 5, 3],
              [7, 8, 6]]

    file = open(file_location, "r")
    loaded = file.readlines()
    file.close()

    load_num = 0

    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            in_num = int(loaded[load_num].strip("\n"))
            puzzle[i][j] = in_num
            load_num += 1

    return puzzle


def load_game():
    print("-----------------------------------\n"
          "1. Load Solved\n"
          "2. Load Saved\n"
          "3. Save a New Game\n"
          "-----------------------------------\n")

    user_input = input("Enter an Option: ")
    match user_input:
        case '1':
            loaded_puzzle = load_from_file("game/solved_game.txt")
        case '2':
            loaded_puzzle = load_from_file("game/saved_game.txt")
        case '3':
            save_game.save_to_file()
            loaded_puzzle = load_from_file("game/saved_game.txt")
    return loaded_puzzle