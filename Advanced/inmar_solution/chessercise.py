#!/usr/bin/python
import argparse
from pprint import pprint

"""
Chess Board Game 
"""

# constants
ROWS_ALPHABETS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
ROWS = [97, 98, 99, 100, 101, 102, 103, 104]
COLUMNS = xrange(1, 9)


class ChessField(object):
    def __init__(self):
        self.chess_board = [[(r, c) for r in ROWS] for c in COLUMNS]
        self.chess_board_display = [[r + str(c) for r in ROWS_ALPHABETS] for c in COLUMNS]

        self.all_fields = reduce(lambda r, c: r + c, self.chess_board)
        self.all_fields_display = reduce(lambda r, c: r + c, self.chess_board_display)
        self.fields_map = dict(zip(self.all_fields_display, self.all_fields))
        self.fields_map_reverse = dict(zip(self.all_fields, self.all_fields_display))
        self.x = 97
        self.y = 1

    def current_position(self, pos):
        self.x = pos[0]
        self.y = pos[1]

    def display_current_position(self):
        return chr(self.x) + str(self.y)

    def knightMoves(self):  # Horse
        legal_moves = []
        for pos in [(self.x - 2, self.y + 1), (self.x - 1, self.y + 2),
                    (self.x + 2, self.y + 1), (self.x + 1, self.y + 2),
                    (self.x - 2, self.y - 1), (self.x - 1, self.y - 2),
                    (self.x + 2, self.y - 1), (self.x + 1, self.y - 2)]:
            if pos in self.all_fields:
                legal_moves.append(pos)
        return legal_moves

    def rookMoves(self):  # Elephant
        legal_moves = []
        for i in range(-8, 8):
            if (self.x + i, self.y) in self.all_fields:
                legal_moves.append((self.x + i, self.y))

        if (self.x, self.y) in legal_moves:
            legal_moves.remove((self.x, self.y))  # remove current position


        for j in range(-8, 8):
            if (self.x, self.y + j) in self.all_fields:
                legal_moves.append((self.x, self.y + j))

        if (self.x, self.y) in legal_moves:
            legal_moves.remove((self.x, self.y))  # remove current position

        return legal_moves

    def queenMoves(self):  # Mantri
        legal_moves = []
        legal_moves.extend(self.rookMoves())
        for i, j in zip(range(-8, 8), range(-8, 8)):  # principal diagonal
            if (self.x + i, self.y + j) in self.all_fields:
                legal_moves.append((self.x + i, self.y + j))

        if (self.x, self.y) in legal_moves:
            legal_moves.remove((self.x, self.y))  # remove current position

        for i, j in zip(range(8, -8, -1), range(-8, 8)):  # reverse principal diagonal
            if (self.x + i, self.y + j) in self.all_fields:
                legal_moves.append((self.x + i, self.y + j))

        if (self.x, self.y) in legal_moves:
            legal_moves.remove((self.x, self.y))  # remove current position

        return legal_moves


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script to learn basic argparse')
    parser.add_argument('-pi', '--piece',
                        help='chess piece name: knight, rook or queen',
                        required='True',
                        choices=['KNIGHT', 'QUEEN', 'ROOK'],
                        default='KNIGHT')
    parser.add_argument('-pos', '--position',
                        help='current position name in chess board',
                        required='True',
                        choices=['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6',
                                 'b7', 'b8', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'd1', 'd2', 'd3', 'd4',
                                 'd5', 'd6', 'd7', 'd8', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'f1', 'f2',
                                 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8',
                                 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8'],
                        default='d2')
    parser.add_argument('-t', '--target',
                        action='store_true', # to take argument without value
                        help='target mode')
    parser.add_argument('-c', '--collector',
                        action='store_true',
                        help='collector mode')
    args = parser.parse_args()
    print args

    # field creation
    field = ChessField()

    print '-' * 80
    print 'CHESS BOARD'.center(80)
    print '-' * 80

    for each in field.chess_board_display:
        print each

    print '-' * 80

    # print field.all_fields
    # pprint(field.fields_map)

    field.current_position(field.fields_map[args.position])

    print 'Current position is ', field.display_current_position()

    if args.piece == 'KNIGHT':
        print 'Legal positions to move for KNIGHT:'
        for fld in field.knightMoves():
            print field.fields_map_reverse[fld],
    elif args.piece == 'QUEEN':
        print 'Legal positions to move for QUEEN:'
        for fld in field.queenMoves():
            print field.fields_map_reverse[fld],
        print '\n', len(field.queenMoves())
    elif args.piece == 'ROOK':
        print 'Legal positions to move for ROOK:'
        for fld in field.rookMoves():
            print field.fields_map_reverse[fld],
        print '\n', len(field.rookMoves())
    else:
        pass
