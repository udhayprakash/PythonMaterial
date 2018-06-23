#!/usr/bin/python
import argparse
from random import sample
from pprint import pprint

"""
Purpose: Command-line based CHESS GAME 

To  implement three pieces: Knight, Rook and Queen  

Knight - Horse 
Rook   - Elephant 
Queen - Mantri 

USAGE: 
    python chessercise.py --piece KNIGHT --position d2 --target --collector
    
"""
__author__ = 'Udhay Prakash Pethakamsetty'
__contact__ = 'uday3prakash@gmail.com'

# constants  - Memoization
ROWS_ALPHABETS = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
ROWS = (97, 98, 99, 100, 101, 102, 103, 104)
COLUMNS = (1, 2, 3, 4, 5, 6, 7, 8)

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


class Opponents(object):
    def __init__(self, piece_name, piece):
        self.available_fields = [i for i in all_fields_display if i != chr(piece.row) + str(piece.column)]
        self.opponent_positions = sample(self.available_fields, 8)

        if piece_name == 'KNIGHT':
            self.opponents = [Knight(op_pos) for op_pos in self.opponent_positions]
            print self.opponents[0].cur_pos()
            # print self.aaaaaaaa(piece, self.opponents[0].cur_pos())
            print 'piece.moves()', piece.moves()

        elif piece_name == 'ROOK':
            self.opponents = [Rook(op_pos) for op_pos in self.opponent_positions]
            self.opponents_distance = []
            min_distance = 14
            for opponent in self.opponents:
                distance, least_distant_position = self.rook_distance(piece, opponent)
                self.opponents_distance.append((opponent.cur_pos(), distance, least_distant_position))
            pprint(self.opponents_distance)


        elif piece_name == 'QUEEN':
            self.opponents = [Queen(op_pos) for op_pos in self.opponent_positions]
        else:
            pass

        self.available_fields = list(set(self.available_fields) - set(self.opponent_positions))




    def rook_distance(self, piece, target_pos):
        distance = 14
        least_distant_position = target_pos.row

        for pos in piece.moves():
            temp = abs(pos[0] - target_pos.row) + abs(pos[1] - target_pos.column)
            if distance > temp:
                distance = temp
                least_distant_position = pos
        print 'with minimum', distance, ' moves, most distant tile is at', fields_map_reverse[least_distant_position]
        return distance, least_distant_position


def most_distant_opponent(): pass




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

    print 'For "%s" with current position: "%s"' % (args.piece, args.position)
    print 'Legal Moves :',
    if args.piece == 'KNIGHT':
        kt = Knight(args.position)
        for fld in kt.moves():
            print fields_map_reverse[fld],
        print '\n', 'No. of moves:', len(kt.moves())

        if args.target:
            print '=' * 80
            print 'Entered TARGET MODE'.center(80)
            print '=' * 80

            # 8 opponent KNIGHTS positions at random positions
            opponent_knights = Opponents(args.piece, kt)
            print kt.moves()
            print [(op.row, op.column) for op in opponent_knights.opponents]

        if args.collector:
            print '=' * 80
            print 'Entered COLLECTOR MODE'.center(80)
            print '=' * 80

    elif args.piece == 'ROOK':
        rk = Rook(args.position)
        for fld in rk.moves():
            print fields_map_reverse[fld],
        print '\n', 'No. of moves:', len(rk.moves())

        if args.target:
            print '=' * 80
            print 'Entered TARGET MODE'.center(80)
            print '=' * 80

            # 8 opponent ROOK positions at random positions
            opponent_rooks = Opponents(args.piece, rk)

#            most_distant_opponent()

            # rook_distance(rk.moves(), rk.cpos)

            # print get_distance(rk.row, rk.column, r1.row,r1.column)

            # print 'rk.cur_pos()', rk.cur_pos()
            # print 'r1.cur_pos()', r1.cur_pos()
            # print len(r1.moves()), [fields_map_reverse[i] for i in r1.moves()]
            # print len(rk.moves()), [fields_map_reverse[i] for i in rk.moves()]
        if args.collector:
            print '=' * 80
            print 'Entered COLLECTOR MODE'.center(80)
            print '=' * 80

    elif args.piece == 'QUEEN':
        qn = Queen(args.position)
        for fld in qn.moves():
            print fields_map_reverse[fld],
        print '\n', 'No. of moves:', len(qn.moves())
        if args.target:
            print '=' * 80
            print 'Entered TARGET MODE'.center(80)
            print '=' * 80

            # 8 opponent QUEEN positions at random positions
            opponent_queens = Opponents(args.piece, qn)

        if args.collector:
            print '=' * 80
            print 'Entered COLLECTOR MODE'.center(80)
            print '=' * 80
    else:
        pass

print '\n' * 10
print '-' * 80
print 'GAME COMPLETED'.center(80)
print '-' * 80
