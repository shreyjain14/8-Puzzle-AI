from engine import calculate_distance


def puzzle_print(puzzle):
    for i in puzzle:
        print(i)
    print("End Distance is", calculate_distance.h_distance(puzzle))
    print("\n")
