from engine import cordinates


def find_neighbours(p):
    current = cordinates.calculate_cords(p)
    zero_cords = current[0]
    n4 = []

    # vertical neighbours
    if zero_cords[0] == 0:
        n4.append((1, zero_cords[1]))
    elif zero_cords[0] == 1:
        n4.append((0, zero_cords[1]))
        n4.append((2, zero_cords[1]))
    elif zero_cords[0] == 2:
        n4.append((1, zero_cords[1]))

    # horizontal neighbours
    if zero_cords[1] == 0:
        n4.append((zero_cords[0], 1))
    elif zero_cords[1] == 1:
        n4.append((zero_cords[0], 0))
        n4.append((zero_cords[0], 2))
    elif zero_cords[1] == 2:
        n4.append((zero_cords[0], 1))

    return n4, zero_cords
