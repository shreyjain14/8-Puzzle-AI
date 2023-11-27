from engine import neighbours, calculate_distance, print_puzzle, copy_puzzle

puzzle_solution = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]


def move_piece(puzzle_input, last_code_move, move_counts):
    current_h_distance = calculate_distance.h_distance(puzzle_input)
    if current_h_distance == 0:
        print("WE HAVE SOLUTION!\n"
              "Solved in", move_counts, "moves!")
    else:
        nearest_4, zero_cords = neighbours.find_neighbours(puzzle_input)
        x0, y0 = zero_cords
        move_distance = {}

        for i in nearest_4:
            if i == last_code_move:
                print("")
            else:
                temp = copy_puzzle.list_copy(puzzle_input)
                xn, yn = i
                temp[x0][y0] = temp[xn][yn]
                temp[xn][yn] = 0
                move_distance[calculate_distance.h_distance(temp)] = i

        final_move = min(move_distance)

        move_counts += 1
        move_cord = move_distance[final_move]
        x1, y1 = move_cord

        puzzle_input[x0][y0] = puzzle_input[x1][y1]
        puzzle_input[x1][y1] = 0
        last_code_move = zero_cords

        print("Move Count ==", move_counts)
        print_puzzle.puzzle_print(puzzle_input)

        if puzzle_input != puzzle_solution:
            move_piece(puzzle_input, last_code_move, move_counts)
        else:
            print("WE HAVE SOLUTION!\n"
                  "Solved in", move_counts, "moves!")
