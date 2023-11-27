from engine import cordinates

solve = {1: (0, 0), 2: (0, 1), 3: (0, 2),
         4: (1, 0), 5: (1, 1), 6: (1, 2),
         7: (2, 0), 8: (2, 1), 0: (2, 2)}


def h_distance(puzzle):
    current = cordinates.calculate_cords(puzzle)
    distance = 0
    for i in puzzle:
        for j in i:
            if j == 0:
                to_add = 0
            else:
                to_add = ((solve[j][0] - current[j][0]) ** 2) ** (1 / 2) + (
                        (solve[j][1] - current[j][1]) ** 2) ** (1 / 2)
                distance = distance + to_add
    return distance
