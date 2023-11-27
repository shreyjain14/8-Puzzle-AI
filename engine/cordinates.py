def calculate_cords(puzzle):
    current = {}
    for i in puzzle:
        for j in i:
            current[j] = (puzzle.index(i), i.index(j))
    return current


def locate_element(puzzle, number):
    current = calculate_cords(puzzle)
    return current[number]
