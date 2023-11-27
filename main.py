from engine import cordinates, print_puzzle, movement, copy_puzzle
from game import load_game

puzzle = load_game.load_game()

puzzle_update = copy_puzzle.list_copy(puzzle)

zero_position = cordinates.locate_element(puzzle_update, 0)

print_puzzle.puzzle_print(puzzle_update)
movement.move_piece(puzzle_update, zero_position, 0)
