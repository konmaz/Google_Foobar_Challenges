# Don't Get Volunteered https://foobar.withgoogle.com/
def get_value(A, i, j):
    if 0 > i < 8 or 0 > j < 8:
        return None
    try:
        return A[i][j]
    except IndexError:
        return None


def main():
    # Generate the chessboard 2D list
    A = [[0 for i in range(8)] for j in range(8)]
    counter = 0
    for i in range(0, 8):
        for j in range(8):
            A[i][j] = counter
            counter += 1

    # Generate the acceptable moves dictionary
    acceptable_moves = {1: (-2, -1),
                        2: (-2, 1),
                        3: (-1, 2),
                        4: (1, 2),
                        5: (2, 1),
                        6: (2, -1),
                        7: (1, -2),
                        8: (-1, -2)}
    # Generate the Adjacency "List" (Actually Dictionary). key: node, values: nodes that are connected to the key-node
    adjacency = {}

    for i in range(len(A)):  # For every row in the chessboard 2D
        for j in range(len(A[i])):  # For every collum in the chessboard 2D
            temp = []
            for item in acceptable_moves:  # For every acceptable move in the chessboard 2D
                x = i + acceptable_moves[item][0]
                y = j + acceptable_moves[item][1]
                if get_value(A, x, y):
                    temp.append(A[x][y])
                    adjacency[get_value(A, i, j)] = tuple(temp)
    print(adjacency)
    '''
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j]:
                print(i + 1, ':', j + 1)
    '''


if __name__ == '__main__':
    main()
