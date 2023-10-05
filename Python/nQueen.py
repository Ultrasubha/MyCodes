def queen_moves(size, Qposx, Qposy):
    possible_moves = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    for x1, y1 in directions:
        x, y = Qposx, Qposy
        while 0 < x <= size and 0 < y <= size:
            possible_moves.append((x, y))
            x += x1
            y += y1

    return possible_moves

size = int(input())
Qposx = int(input())
Qposy = int(input())
moves = queen_moves(size, Qposx, Qposy)
for move in set(moves):
    print(move)
