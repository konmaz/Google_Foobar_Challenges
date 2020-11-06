# Don't Get Volunteered https://foobar.withgoogle.com/
from collections import defaultdict
from heapq import *


def dijkstra(edges, f, t):  # git from https://gist.github.com/kachayev/5990802
    g = defaultdict(list)
    for l, r, c in edges:
        g[l].append((c, r))

    q, seen, mins = [(0, f, ())], set(), {f: 0}
    while q:
        (cost, v1, path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 in seen: continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))

    return float("inf")


def get_value(A, i, j):
    if 0 > i < 8 or 0 > j < 8:
        return None
    try:
        return A[i][j]
    except IndexError:
        return None


def solution(start:int = 0 , end:int = 1):
    # Generate the chessboard 2D list stars from 0 and continues 1,2,3...63
    A = [[0 for i in range(8)] for j in range(8)]
    counter = 0
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

    edges = []
    for key in adjacency_dict:
        for value in adjacency_dict[key]:
            edges.append((key, value, 1))

    return dijkstra(edges, start, end)[0]
    #print(dijkstra(edges, 0, 1))


if __name__ == '__main__':
    solution()
