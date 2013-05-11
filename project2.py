# Authors:
# Benjamin Holbrook, 20761758
# George Gooden, 20772597

import turtle

def initialiseBoard():
    defaultBoard = [[-1, -1, -1, -1], \
                    [-1, -1, -1, -1], \
                    [-1, -1, -1, -1], \
                    [0, 0, 0, 0], \
                    [0, 0, 0, 0], \
                    [1, 1, 1, 1], \
                    [1, 1, 1, 1], \
                    [1, 1, 1, 1]]
    
    # Invalid files will result in a default board being used
    filename = str(input("Enter your board file: "))

    try:
        with open(filename)as file:
            board = []
            for line in file:
                line = [int(x) for x in line.strip().split()]
                board.append(line)
            return board
    except IOError:
        return defaultBoard

def drawBoard(b):
    #rows = len(b)
    #cols = len(b[0])

    rows = len(b)
    cols = len(b[0])
    
    drawGrid(rows, cols * 2)

    for r in range(rows):
        for c in range(cols):
            piece = b[r][c]
            c = c * 2 - 2
            if r % 2 != 0:
                c += 1

            if piece == -2:
                drawPiece(rows, cols, r, c, "white", True)
            elif piece == -1:
                drawPiece(rows, cols, r, c, "white", False)
            elif piece == 1:
                drawPiece(rows, cols, r, c, "black", False)
            elif piece == 2:
                drawPiece(rows, cols, r, c, "black", True)
            elif piece == 0:
                continue
            else:
                print("Should never reach here")

def drawRectangle(x, y, w, h, color, fill):
    t = turtle.Turtle()
    t.speed("fastest")
    t.hideturtle()
    t.color(color)

    # Move to x, y cord
    t.penup()
    t.setposition(x, y)
    t.pendown()
    t.left(90)

    # Draw square
    if fill:
        t.begin_fill()
    
    for i in range(2):        
        t.forward(h)
        t.right(90)
        t.forward(w)
        t.right(90)
        
    t.end_fill()

def drawCircle(x, y, r, color,  fill):
    t = turtle.Turtle()
    t.speed("fastest")
    t.hideturtle()
    t.color(color)

    # Move to x, y cord
    t.penup()
    t.setposition(x, y)
    t.pendown()

    if fill:
        t.begin_fill()

    t.circle(r)
    
    t.end_fill()

def drawGrid(rows, cols):
    squareWidth = 60
    startX = 0 - (cols * squareWidth) / 2
    startY = 0 - (rows * squareWidth) / 2
    
    for r in range(rows):
        for c in range(cols):
            x = startX +c * squareWidth
            y = startY + r * squareWidth
            if (r + c) % 2 == 0:
                drawRectangle(x, y, squareWidth, squareWidth, "black", False)
            else:
                drawRectangle(x, y, squareWidth, squareWidth, "black", True)
                
def drawPiece(rows, cols, r, c, color, king):
    squareWidth = 60
    startX = 0 - (cols * squareWidth) / 2
    startY = 0 - (rows * squareWidth) / 2
    
    radius = 20
    innerRadius = 10
    innerColor = "red"

    x = startX + c * squareWidth + squareWidth / 2
    y = startY + r * squareWidth + radius / 2
    if color == "white":
        drawCircle(x, y, radius, "white", True)
        drawCircle(x, y, radius, "black", False)
    else:
        drawCircle(x, y, radius, "black", True)

    if king:
        drawCircle(x, y + radius / 2, innerRadius, innerColor, True)

# In progress
def moves(b, c):
    moves = []
    

def move(b, m):
    print("Not finished")

def captures(b, c):
    print("Not finished")

def move(b, m):
    print("Not finished")

# TODO In progress
def main():
    b = initialiseBoard()
    print(b)
    drawBoard(b)    

# Advanced, general functions below
#def recursiveCaptures(b, c):

#def capture(b, ms):

#def main():

main()
