#!/usr/bin/python
import argparse
"""
Chess Board Game 
"""

# rows = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
rows = [97,98,99,100,101,102,103,104]
columns = xrange(1,9)

chess_board = [[(x,y) for x in rows] for y in columns]
all_fields = reduce(lambda x,y:x+y, chess_board)


def knightMoves(x,y):  # Horse
    legal_moves = []
    for pos in [(x-2,y-2), (x-2,y+2), (x+2,y-2), (x+2,y+2)]:
        if pos in all_fields:
            legal_moves.append(pos)
    return legal_moves

def rookMoves(x,y): #Elephant
    legal_moves = []
    for i in range(-8, 8):
        if (x + i, y) in all_fields:
            legal_moves.append((x + i, y))
    for j in range(-8, 8):
        if (x, y + j) in all_fields:
            legal_moves.append((x, y + j))
    return legal_moves

def queenMoves(x,y): #Mantri
    legal_moves = []
    for i,j in zip(range(-8, 8),range(-8,8)):  # principal diagonal
        if (x + i, y+j) in all_fields:
            legal_moves.append((x + i, y+j))

    for i,j in zip(range(8, -8, -1),range(-8,8)): # reverse principal diagonal
        if (x + i, y+j) in all_fields:
            legal_moves.append((x + i, y+j))
    return legal_moves


print '-'*80
print 'CHESS BOARD GAME'.center(80)
print '-'*80

for m in chess_board:
    print m

print '-'*80
print 'KNIGHT MOVES'
print 'center             :(100, 5)     :', knightMoves(100, 5)
print 'left top-corner    :(97, 1)      :', knightMoves(97, 1)
print 'right top-corner   :(104, 1)     :', knightMoves(104, 1)
print 'left bottom-corner :(97, 8)      :', knightMoves(97, 8)
print 'right bottom-corner:(104, 8)     :', knightMoves(104, 8)
print
print 'top middle         :(100, 1)     :', knightMoves(100, 1)
print 'left middle        :(97, 4)      :', knightMoves(97, 4)
print 'right middle       :(104, 4)     :', knightMoves(104, 4)
print 'bottom middle      :(100, 8)     :', knightMoves(100, 8)

print '-'*80
print 'ROCK MOVES'
print 'center             :(100, 5)     :', rookMoves(100, 5)
print 'left top-corner    :(97, 1)      :', rookMoves(97, 1)
print 'right top-corner   :(104, 1)     :', rookMoves(104, 1)
print 'left bottom-corner :(97, 8)      :', rookMoves(97, 8)
print 'right bottom-corner:(104, 8)     :', rookMoves(104, 8)
print
print 'top middle         :(100, 1)     :', rookMoves(100, 1)
print 'left middle        :(97, 4)      :', rookMoves(97, 4)
print 'right middle       :(104, 4)     :', rookMoves(104, 4)
print 'bottom middle      :(100, 8)     :', rookMoves(100, 8)

print '-'*80
print 'QUEEN MOVES'
print 'center             :(100, 5)     :', queenMoves(100, 5)
print 'left top-corner    :(97, 1)      :', queenMoves(97, 1)
print 'right top-corner   :(104, 1)     :', queenMoves(104, 1)
print 'left bottom-corner :(97, 8)      :', queenMoves(97, 8)
print 'right bottom-corner:(104, 8)     :', queenMoves(104, 8)

print 'top middle         :(100, 1)     :', queenMoves(100, 1)
print 'left middle        :(97, 4)      :', queenMoves(97, 4)
print 'right middle       :(104, 4)     :', queenMoves(104, 4)
print 'bottom middle      :(100, 8)     :', queenMoves(100, 8)
