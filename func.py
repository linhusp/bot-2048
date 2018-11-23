def merge(matrix):
    move = False
    for i in range(len(matrix)):
        for j in range(len(matrix[0]) - 1):
            if matrix[i][j] != 0 and matrix[i][j] == matrix[i][j + 1]:
                matrix[i][j] *= 2
                matrix[i][j + 1] = 0
                move = True
    return move


def reverse(matrix):
    new = []
    for i in range(len(matrix)):
        new.append([])
        for j in range(len(matrix[0])):
            new[i].append(matrix[i][len(matrix[0]) - 1 - j])
    return new


def swipe_left(matrix):
    new = []
    for i in range(len(matrix)):
        new.append([0] * len(matrix[0]))

    for i in range(len(matrix)):
        c = 0
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                new[i][c] = matrix[i][j]
                c += 1
    return new


def transpose(matrix):
    new = []
    for j in range(len(matrix[0])):
        new.append([])
        for i in range(len(matrix)):
            new[j].append(matrix[i][j])
    return new
