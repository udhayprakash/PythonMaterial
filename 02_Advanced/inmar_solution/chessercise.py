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


class Knight(object):  # Horse
    def __init__(self, current_position):
        self.row = ord(current_position[0])
        self.column = int(current_position[1])
        self.legal_moves = []
        self.cpos = current_position

    def cur_pos(self):
        return chr(self.row) + str(self.column)

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
        self.cpos = current_position

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
        self.cpos = current_position
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


def rook_distance(my_pos, target_pos):
    print 'my_pos', my_pos
    print 'target_pos', target_pos
    distance = 14
    least_distant_position = target_pos[0]

    for pos in my_pos:
        temp = abs(pos[0] - target_pos[0]) + abs(pos[1] - target_pos[1])
        if distance > temp:
            distance = temp
            least_distant_position = pos
    # return distance, least_distant_position
    print 'with minimum', distance, ' moves, most distant tile is at', fields_map_reverse[least_distant_position]


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
                        choices=all_fields_display,
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
        print 'Legal moves for this r'
        for fld in rk.moves():
            print fields_map_reverse[fld],
        print '\n', 'No. of legal moves available:', len(rk.moves())

        if args.target:
            available_fields = [i for i in all_fields_display if i != (rk.row, rk.column)]
            r1 = Rook(choice(available_fields))  # Mersenne Twister algorithm
            r2 = Rook(choice(available_fields))
            r3 = Rook(choice(available_fields))
            r4 = Rook(choice(available_fields))
            r5 = Rook(choice(available_fields))
            r6 = Rook(choice(available_fields))
            r7 = Rook(choice(available_fields))
            r8 = Rook(choice(available_fields))

            rook_distance(rk.moves(), rk.cpos)

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

            # print 'rk.cur_pos()', rk.cur_pos()
            # print 'r1.cur_pos()', r1.cur_pos()
            # print len(r1.moves()), [fields_map_reverse[i] for i in r1.moves()]
            # print len(rk.moves()), [fields_map_reverse[i] for i in rk.moves()]
    elif args.piece == 'QUEEN':
        qn = Queen(args.position)
        for fld in qn.moves():
            print fields_map_reverse[fld],
        print '\n', 'No. of legal moves available:', len(qn.moves())
    else:
        pass

        # print all_fields_display
