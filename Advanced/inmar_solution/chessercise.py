#!/usr/bin/python
import argparse
# from pprint import pprint
from random import choice

"""
Chess Board Game 
"""

# constants  - Memoization
ROWS_ALPHABETS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
ROWS = [97, 98, 99, 100, 101, 102, 103, 104]
COLUMNS = [1, 2, 3, 4, 5, 6, 7, 8]

chess_board = [[(r, c) for r in ROWS] for c in COLUMNS]
chess_board_display = [[r + str(c) for r in ROWS_ALPHABETS] for c in COLUMNS]
all_fields = reduce(lambda r, c: r + c, chess_board)
all_fields_display = reduce(lambda r, c: r + c, chess_board_display)

fields_map = dict(zip(all_fields_display, all_fields))
fields_map_reverse = dict(zip(all_fields, all_fields_display))


# def current_position(self, pos):
#     self.row = pos[0]
#     self.column = pos[1]
#
# def display_current_position(self):
#     return chr(self.row) + str(self.column)

class Knight(object):  # Horse
    def __init__(self, current_position):
        self.row = ord(current_position[0])
        self.column = int(current_position[1])
        self.legal_moves = []

    def cur_pos(self):
        return chr(self.row)+str(self.column)

    def moves(self):
        self.legal_moves = []
        for pos in [(self.row - 2, self.column + 1), (self.row - 1, self.column + 2),
                    (self.row + 2, self.column + 1), (self.row + 1, self.column + 2),
                    (self.row - 2, self.column - 1), (self.row - 1, self.column - 2),
                    (self.row + 2, self.column - 1), (self.row + 1, self.column - 2)]:
            if pos in all_fields and pos != (self.row, self.column):
                self.legal_moves.append(pos)
        return self.legal_moves


class Rook(object):  # Elephant
    def __init__(self, current_position):
        self.row = ord(current_position[0])
        self.column = int(current_position[1])
        self.legal_moves = []

    def cur_pos(self):
        return chr(self.row) + str(self.column)

    def moves(self):
        self.legal_moves = []
        for i in xrange(-8, 8):
            if (self.row + i, self.column) in all_fields:
                self.legal_moves.append((self.row + i, self.column))

        for j in xrange(-8, 8):
            if (self.row, self.column + j) in all_fields:
                self.legal_moves.append((self.row, self.column + j))

        # avoid current position
        for _ in xrange(0, self.legal_moves.count((self.row, self.column))):
            self.legal_moves.remove((self.row, self.column))

        return self.legal_moves


class Queen(Rook):  # Mantri
    def __init__(self, current_position):
        self.row = ord(current_position[0])
        self.column = int(current_position[1])
        self.legal_moves = []
        super(Queen, self).__init__(current_position)

    def cur_pos(self):
        return chr(self.row) + str(self.column)

    def moves(self):
        self.legal_moves = []
        self.legal_moves.extend(super(Queen, self).moves())
        for i, j in zip(xrange(-8, 8), xrange(-8, 8)):  # principal diagonal
            if (self.row + i, self.column + j) in all_fields:
                self.legal_moves.append((self.row + i, self.column + j))

        for i, j in zip(xrange(8, -8, -1), xrange(-8, 8)):  # reverse principal diagonal
            if (self.row + i, self.column + j) in all_fields:
                self.legal_moves.append((self.row + i, self.column + j))

        # avoid current position
        for _ in xrange(0, self.legal_moves.count((self.row, self.column))):
            self.legal_moves.remove((self.row, self.column))

        return self.legal_moves


def get_rook_distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Chess board game')
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
                        action='store_true',  # to take argument without value
                        help='target mode')
    parser.add_argument('-c', '--collector',
                        action='store_true',
                        help='collector mode')
    args = parser.parse_args()
    # print args

    # display chess board
    print '-' * 80
    print 'CHESS BOARD'.center(80)
    print '-' * 80

    for each in chess_board_display:
        print each

    print '-' * 80

    print 'LEGAL Moves for', args.piece
    print 'current position:', args.position
    if args.piece == 'KNIGHT':
        kt = Knight(args.position)
        for fld in kt.moves():
            print fields_map_reverse[fld],
        print '\n', 'No. of legal moves available:', len(kt.moves())

    elif args.piece == 'ROOK':
        rk = Rook(args.position)
        for fld in rk.moves():
            print fields_map_reverse[fld],
        print '\n', 'No. of legal moves available:', len(rk.moves())

        if args.target:
            r1 = Rook(choice(all_fields_display))  # Mersenne Twister algorithm
            print r1.cur_pos()
            print rk.cur_pos()
            print len(r1.moves()), [fields_map_reverse[i] for i in r1.moves()]
            print len(rk.moves()), [fields_map_reverse[i] for i in rk.moves()]
            # r2 = Rook(choice(all_fields_display))
            # r3 = Rook(choice(all_fields_display))
            # r4 = Rook(choice(all_fields_display))
            # r5 = Rook(choice(all_fields_display))
            # r6 = Rook(choice(all_fields_display))
            # r7 = Rook(choice(all_fields_display))
            # r8 = Rook(choice(all_fields_display))
            #
            # for i in [r1, r2, r3, r4, r5, r6, r7, r8]:
            #     print chr(i.row) + str(i.column)
            #     # print get_distance(rk.row, rk.column, i.row, i.column)
    elif args.piece == 'QUEEN':
        qn = Queen(args.position)
        for fld in qn.moves():
            print fields_map_reverse[fld],
        print '\n', 'No. of legal moves available:', len(qn.moves())
    else:
        pass
