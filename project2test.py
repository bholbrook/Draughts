"""
Short test file for Project 2, playing Draughts. 

We do not claim that this file is a complete testing scheme: 
its primary purpose is to check the spelling of the function names. 
You should supplement the tests in this file with your own tests. 
The correctness of your program is your responsibility. 

Author: Lyndon While 
Date: 19/5/13 
Version 1.10 
"""


import project2


def eq(x, y):
    return x == y

def stripWhitespace(s):
    return s.replace("\n", "").replace(" ", "")


def startingBoard():
    return [[ 1,  1,  1,  1]
           ,[ 1,  1,  1,  1]
           ,[ 1,  1,  1,  1]
           ,[ 0,  0,  0,  0]
           ,[ 0,  0,  0,  0]
           ,[-1, -1, -1, -1]
           ,[-1, -1, -1, -1]
           ,[-1, -1, -1, -1]]

def sBb():
    return [[ 1,  1,  1,  1]
           ,[ 1,  1,  1,  1]
           ,[ 1,  1,  1,  0]
           ,[ 0,  0,  0,  1]
           ,[ 0,  0,  0,  0]
           ,[-1, -1, -1, -1]
           ,[-1, -1, -1, -1]
           ,[-1, -1, -1, -1]]

def sBw():
    return [[ 1,  1,  1,  1]
           ,[ 1,  1,  1,  1]
           ,[ 1,  1,  1,  1]
           ,[ 0,  0,  0,  0]
           ,[ 0,  0,  0, -1]
           ,[-1, -1, -1,  0]
           ,[-1, -1, -1, -1]
           ,[-1, -1, -1, -1]]

def board4_1():
    return [[-2,  0]
           ,[ 1, -1]
           ,[ 0,  1]
           ,[ 2, -1]]

def board8_1():
    return [[ 1, -2,  0,  0]
           ,[ 1,  0, -1,  0]
           ,[ 0, -1,  0,  1]
           ,[ 2,  0,  1,  1]
           ,[-2, -1, -1,  0]
           ,[ 0,  0,  0,  0]
           ,[ 1,  2, -1, -1]
           ,[ 0,  0, -1,  0]]

def b8_1bm():
    return [[ 1, -2,  0,  0]
           ,[ 1,  0, -1,  0]
           ,[ 0, -1,  0,  1]
           ,[ 2,  0,  1,  1]
           ,[-2, -1, -1,  0]
           ,[ 0,  2,  0,  0]
           ,[ 1,  0, -1, -1]
           ,[ 0,  0, -1,  0]]

def b8_1wm():
    return [[ 1, -2,  0, -2]
           ,[ 1,  0,  0,  0]
           ,[ 0, -1,  0,  1]
           ,[ 2,  0,  1,  1]
           ,[-2, -1, -1,  0]
           ,[ 0,  0,  0,  0]
           ,[ 1,  2, -1, -1]
           ,[ 0,  0, -1,  0]]

def b8_1bc():
    return [[ 1, -2,  0,  0]
           ,[ 1,  0, -1,  0]
           ,[ 0, -1,  0,  1]
           ,[ 2,  0,  0,  1]
           ,[-2, -1,  0,  0]
           ,[ 0,  1,  0,  0]
           ,[ 1,  2, -1, -1]
           ,[ 0,  0, -1,  0]]

def b8_1wc():
    return [[ 1,  0,  0,  0]
           ,[ 0,  0, -1,  0]
           ,[-2, -1,  0,  1]
           ,[ 2,  0,  1,  1]
           ,[-2, -1, -1,  0]
           ,[ 0,  0,  0,  0]
           ,[ 1,  2, -1, -1]
           ,[ 0,  0, -1,  0]]

def b8_1bcs():
    return [[ 1, -2,  0,  0]
           ,[ 0,  0, -1,  0]
           ,[ 0,  0,  0,  1]
           ,[ 2,  0,  1,  1]
           ,[-2, -1,  0,  0]
           ,[ 0,  0,  0,  0]
           ,[ 1,  2,  0, -1]
           ,[ 0,  2, -1,  0]]

def test_initialiseBoard():
    print("Just hit Enter")
    x = project2.initialiseBoard()
    print("Give me board8_1.txt")
    y = project2.initialiseBoard()
    print("Give me board4_1.txt")
    z = project2.initialiseBoard()
    return ([x, y, z], [startingBoard(), board8_1(), board4_1()])

def test_drawBoard():
    return ([], [])

def test_moves():
    xs = [project2.moves(b, c) for b in [startingBoard(), board8_1(), board4_1()] for c in [1, -1]]
    for ys in xs: ys.sort()
    return (xs, [[(2, 0, 3, 0), (2, 1, 3, 0), (2, 1, 3, 1), (2, 2, 3, 1), (2, 2, 3, 2), (2, 3, 3, 2), (2, 3, 3, 3)]
                ,[(5, 0, 4, 0), (5, 0, 4, 1), (5, 1, 4, 1), (5, 1, 4, 2), (5, 2, 4, 2), (5, 2, 4, 3), (5, 3, 4, 3)]
                ,[(1, 0, 2, 0), (3, 0, 2, 0), (3, 2, 4, 3), (3, 3, 4, 3), (6, 0, 7, 0), (6, 1, 5, 0), (6, 1, 5, 1), (6, 1, 7, 0), (6, 1, 7, 1)]
                ,[(0, 1, 1, 1), (1, 2, 0, 2), (1, 2, 0, 3), (2, 1, 1, 1), (4, 0, 5, 0), (4, 1, 3, 1), (4, 2, 3, 1), (6, 2, 5, 1), (6, 2, 5, 2), (6, 3, 5, 2), (6, 3, 5, 3)]
                ,[(1, 0, 2, 0), (3, 0, 2, 0)]
                ,[(1, 1, 0, 1)]])

def test_move():
    return ([project2.move(b, m) for (b, m) in [(startingBoard(), (2, 3, 3, 3)), (startingBoard(), (5, 3, 4, 3)),
                                                (board8_1(),      (6, 1, 5, 1)), (board8_1(),      (1, 2, 0, 3)),
                                                (board8_1(),(3, 2, 4, 2, 5, 1)), (board8_1(),(0, 1, 1, 0, 2, 0))]]
           ,[sBb(), sBw(), b8_1bm(), b8_1wm(), b8_1bc(), b8_1wc()])

def test_captures():
    xs = [project2.captures(b, c) for b in [startingBoard(), board8_1(), board4_1()] for c in [1, -1]]
    for ys in xs: ys.sort()
    return (xs, [[]
                ,[]
                ,[(1, 0, 2, 1, 3, 1), (3, 0, 2, 1, 1, 1), (3, 0, 4, 1, 5, 1), (3, 2, 4, 2, 5, 1)]
                ,[(0, 1, 1, 0, 2, 0), (4, 1, 3, 0, 2, 0)]
                ,[]
                ,[]])

def test_recursiveCaptures():
    xs = [project2.recursiveCaptures(b, c) for b in [startingBoard(), board8_1(), board4_1()] for c in [1, -1]]
    for ys in xs: ys.sort()
    return (xs, [[]
                ,[]
                ,[[(1, 0, 2, 1, 3, 1), (3, 1, 4, 1, 5, 0)]
                 ,[(1, 0, 2, 1, 3, 1), (3, 1, 4, 2, 5, 2), (5, 2, 6, 2, 7, 1)]
                 ,[(1, 0, 2, 1, 3, 1), (3, 1, 4, 2, 5, 2), (5, 2, 6, 3, 7, 3)]
                 ,[(3, 0, 2, 1, 1, 1)]
                 ,[(3, 0, 4, 1, 5, 1)]
                 ,[(3, 2, 4, 2, 5, 1)]]
                ,[[(0, 1, 1, 0, 2, 0)]
                 ,[(4, 1, 3, 0, 2, 0)]]
                ,[]
                ,[]])

def test_capture():
    return ([project2.capture(b, m) for (b, m) in [(board8_1(), [(1, 0, 2, 1, 3, 1), (3, 1, 4, 2, 5, 2), (5, 2, 6, 2, 7, 1)]),
                                                   (board8_1(), [(0, 1, 1, 0, 2, 0)])]]
           ,[b8_1bcs(), b8_1wc()])

def test_main():
    return ([], [])


def msg(f, z):
    (xs, ys) = z
    bs = list(map(eq, xs, ys))
    if bs == []:
        s = "untested"
    elif all(bs):
        s = "all " + str(len(bs)) + " test(s) correct"
    else:
        zs = []
        for k in range(len(bs)):
            if not bs[k]:
                zs.append(k)
        s = "These tests incorrect: " + str(zs)[1:-1]
    print("%20s" % (f + ":"), s)

msg("initialiseBoard",    test_initialiseBoard())
msg("drawBoard",          test_drawBoard())
msg("moves",              test_moves())
msg("move",               test_move())
msg("captures",           test_captures())
msg("recursiveCaptures",  test_recursiveCaptures())
msg("capture",            test_capture())
msg("main",               test_main())
print()
input("Hit Enter to finish")
