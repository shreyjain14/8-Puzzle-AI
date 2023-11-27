import sys
from dataclasses import dataclass
from engine import neighbours, copy_puzzle, print_puzzle, cordinates

sys.setrecursionlimit(10000)
puzzle_solution = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]


@dataclass
class NODE:
    puzzle: list
    next_moves: list
    last_move: tuple


head = 0


def add_elements(puzzle, queue, last_move):
    puzzle_neighbours, zero_cords = neighbours.find_neighbours(puzzle)
    queue.append(NODE(puzzle, puzzle_neighbours, last_move))


def create_queue(puzzle):
    queue = []
    head_pointer = 0
    current = cordinates.calculate_cords(puzzle)
    zero_cords = current[0]
    add_elements(puzzle, queue, zero_cords)
    add_in_queue(queue, head_pointer)


def add_in_queue(queue, head_pointer):
    p = queue[head_pointer].puzzle
    if p != puzzle_solution:
        for i in queue[head_pointer].next_moves:
            if i == queue[head_pointer].last_move:
                continue
            elif i in queue:
                continue
            else:
                temp_puzzle = copy_puzzle.list_copy(queue[head_pointer].puzzle)
                current = cordinates.calculate_cords(temp_puzzle)
                zero_cords = current[0]
                x1 = i[0]
                y1 = i[1]
                x0, y0 = zero_cords
                temp_puzzle[x0][y0] = temp_puzzle[x1][y1]
                temp_puzzle[x1][y1] = 0
                print(len(queue))
                add_elements(temp_puzzle, queue, zero_cords)
                print_puzzle.puzzle_print(temp_puzzle)
        add_in_queue(queue, head_pointer)
    else:
        print("Found Solution in", head_pointer, "searches!")
        print_puzzle.puzzle_print(queue[head_pointer].puzzle)


create_queue([[5, 4, 2], [3, 6, 1], [7, 0, 8]])
