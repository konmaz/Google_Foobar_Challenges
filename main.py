# Don't Get Volunteered https://foobar.withgoogle.com/
def get_value(A, i, j):
    if 0 > i < 8 or 0 > j < 8:
        return None
    try:
        return A[i][j]
    except IndexError:
        return None


def main():
    # Generate the chessboard 2D list stars from 1 and continues 2,3...64
    A = [[0 for i in range(8)] for j in range(8)]
    counter = 1
    for i in range(0, 8):
        for j in range(8):
            A[i][j] = counter
            counter += 1

    # Generate the acceptable moves dictionary
    acceptable_moves = {1: (-2, -1),  # Go 2 UP, 1 LEFT
                        2: (-2, 1),  # GO 2 UP , 1 RIGHT
                        3: (-1, 2),  # GO 1 UP, 2 RIGHT
                        4: (1, 2),  # GO 1 DOWN, 2 RIGHT
                        5: (2, 1),  # GO 2 DOWN, 1 RIGHT
                        6: (2, -1),  # GO 2 DOWN, 1 LEFT
                        7: (1, -2),  # GO 1 DOWN, 2 LEFT
                        8: (-1, -2)}  # GO 1 UP, 2 LEFT
    # Generate the Adjacency "Dictionary". Key : node, Value : Tuple containing neighbors
    adjacency_dict = {}
    for i in range(len(A)):  # For every row in the chessboard 2D
        for j in range(len(A[i])):  # For every collum in the chessboard 2D
            temp = []
            for item in acceptable_moves:  # For every acceptable move in the chessboard 2D
                x = i + acceptable_moves[item][0]
                y = j + acceptable_moves[item][1]
                if get_value(A, x, y):
                    temp.append(A[x][y])
                    adjacency_dict[get_value(A, i, j)] = tuple(temp)
    print(adjacency_dict)
    # Convert the Adjacency "Dictionary" to the Adjacency Matrix
    



if __name__ == '__main__':
    main()
