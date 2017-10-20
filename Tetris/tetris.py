import curses, random
from random import randrange

curses.initscr()
curses.curs_set(0)

board = curses.newwin(30,32,0,0)
board.keypad(1)
board.nodelay(1)

shape = [ [0x315,0x4cd,0x13f,0xc47],[0x31d,0x4cf,0x137,0xc45],[0x374,0x374,0x374,0x374],[0x741,0x51c,0xdc3,0xf34],
    [0xfc1,0x73c,0x543,0xd14],[0x311,0x4cc,0x133,0xc44],[0xc34,0x341,0x41c,0x1c3]]

class Gameplay:

    def __init__(self):
        board = curses.newwin(30,32,0,0)
        board.keypad(1)
        board.nodelay(1)

    def selectAndPlace(figPos,s):
        c = lambda el,n: -1 if (n >> el & 3) == 3 else 1 if (n >> el & 3) == 1 else 0
        pos = [ c(i ,shape[ figPos[3] ][ figPos[2] ] ) for i in range(0,15,2)[::-1]]
        return checkPiecePos([map(lambda x,y: x+y, figPos[0:2]*4,pos)[i-2:i] for i in range(2,9,2)],s)

    def checkRowUpdateScore(score):
        for i in range(29):
            if all([chr(board.inch(i,x)) == 'X' for x in range(1,29)]):
                board.deleteln()
                board.move(1,1)
                board.insertln()
                score = score + 1

class Board(Gameplay):

    def checkPiecePos(tnot,s):
        check = all([board.inch(c[1],c[0]) & 255 == 32 for c in tnot])
        for c in tnot: board.addch(c[1],c[0],'X' if s==1 else 32) if ((check and s == 1) or s == 0) else None
        return True if s == 0 else check

class Block(Gameplay):

    def move(figPos,value,d):
        figPos[0] = figPos[0] - d if value == ord('a') else figPos[0] + d if value == ord('d') else figPos[0]
        figPos[1] = figPos[1] + d if value in [ord('s'), -1] else figPos[1]
        if value == ord('w'): figPos[2] = 0 if figPos[2] + d > 3 else 3 if figPos[2] + d < 0 else figPos[2] + d

def speedOfBlocks(score):
    board.timeout(300)
    if score % 10 == 0: board.timeout(300-(score*2))

def checkPiecePos(tnot,s):
    check = all([board.inch(c[1],c[0]) & 255 == 32 for c in tnot])
    for c in tnot: board.addch(c[1],c[0],'X' if s==1 else 32) if ((check and s == 1) or s == 0) else None
    return True if s == 0 else check

def selectAndPlace(figPos,s):
    c = lambda el,n: -1 if (n >> el & 3) == 3 else 1 if (n >> el & 3) == 1 else 0
    pos = [ c(i ,shape[ figPos[3] ][ figPos[2] ] ) for i in range(0,15,2)[::-1]]
    return checkPiecePos([map(lambda x,y: x+y, figPos[0:2]*4,pos)[i-2:i] for i in range(2,9,2)],s)

def move(figPos,value,d):
    figPos[0] = figPos[0] - d if value == ord('a') else figPos[0] + d if value == ord('d') else figPos[0]
    figPos[1] = figPos[1] + d if value in [ord('s'), -1] else figPos[1]
    if value == ord('w'): figPos[2] = 0 if figPos[2] + d > 3 else 3 if figPos[2] + d < 0 else figPos[2] + d

def checkRowUpdateScore(score):
    for i in range(29):
        if all([chr(board.inch(i,x)) == 'X' for x in range(1,29)]):
            board.deleteln()
            board.move(1,1)
            board.insertln()
            score = score + 1
            speedOfBlocks(score)

    return score

position = [15,3,0,randrange(0,6,1)] # x,y,rotation,figure

score = selectAndPlace(position,1) ^ 1

board.timeout(300)

while 1:
    board.border('|','|','-','-','+','+','+','+')
    board.addstr(0,2,' Score: '+str(score)+' ')
    value = board.getch()
    if value == 27:
        break
    selectAndPlace(position,0)
    move(position,value,1)
    if not selectAndPlace(position,1):
        move(position,value, -1)
        selectAndPlace(position,1)
        if position[1]==3:
            break
        if value in [ord('s'),-1]:
            score = checkRowUpdateScore(score)
            position = [15,3,0,randrange(0,6,1)]
            selectAndPlace(position,1)
