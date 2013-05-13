# Authors:
# Benjamin Holbrook, 20761758
# George Gooden, 20772597

import turtle

def initialiseBoard():
    defaultBoard = [[1, 1, 1, 1], \
                    [1, 1, 1, 1], \
                    [1, 1, 1, 1], \
                    [0, 0, 0, 0], \
                    [0, 0, 0, 0], \
                    [-1, -1, -1, -1], \
                    [-1, -1, -1, -1], \
                    [-1, -1, -1, -1]]
    
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
    t.speed(0)
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

# This is to used to redraw single cells when making moves
def drawCell(rows, cols, r, c, color):
    squareWidth = 60
    startX = 0 - (cols * squareWidth) / 2
    startY = 0 - (rows * squareWidth) / 2

    x = startX + c * squareWidth
    y = startY + r * squareWidth
    drawRectangle(x, y, squareWidth, squareWidth, color, True)

def drawCircle(x, y, r, color,  fill):
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.color("black")
    t.fillcolor(color)

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
    else:
        drawCircle(x, y, radius, "black", True)

    if king:
        drawCircle(x, y + radius / 2, innerRadius, innerColor, True)

# In progress
def moves(b, c): 
    moves = []
    
    rows = len(b)
    cols = len(b[0])

    for row in range(rows):
        for col in range(cols): 
            if c == 1: 
                if b[row][col] == 1 or b[row][col] == 2:
                    if row != rows-1: 
                        if b[row+1][col] == 0: 
                            moves.append((row, col, row+1, col))
                        if row % 2 != 0:
                            if col != cols-1:
                                if b[row+1][col+1] == 0:
                                    moves.append((row, col, row+1, col+1))
                        else:
                            if col != 0:
                                if b[row+1][col-1] == 0:
                                    moves.append((row, col, row+1, col-1))
                if b[row][col] == 2:
                    if row != 0:
                        if b[row-1][col] == 0:
                            moves.append((row, col, row-1, col))
                        if row % 2 != 0:
                            if col != cols-1:
                                if b[row-1][col+1] == 0:
                                    moves.append((row, col, row-1, col+1))
                        else:
                            if col != 0:
                                if b[row-1][col-1] == 0:
                                    moves.append((row, col, row-1, col-1))
            elif c == -1:
                if b[row][col] == -1 or b[row][col] == -2:
                    if row != 0:
                        if b[row-1][col] == 0:
                            moves.append((row, col, row-1, col))
                        if row % 2 != 0:
                            if col != cols-1:
                                if b[row-1][col+1] == 0:
                                    moves.append((row, col, row-1, col+1))
                        else:
                            if col != 0:
                                if b[row-1][col-1] == 0:
                                    moves.append((row, col, row-1, col-1))
                if b[row][col] == -2:
                    if row != rows-1:
                        if b[row+1][col] == 0:
                            moves.append((row, col, row+1, col))
                        if row % 2 != 0:
                            if col != cols-1:
                                if b[row+1][col+1] == 0:
                                    moves.append((row, col, row+1, col+1))
                        else:
                            if col != 0:
                                if b[row+1][col-1] == 0:
                                    moves.append((row, col, row+1, col-1))
    return moves
    
    
# In  progress
# This will probably take in x,y values using the 0-3 rather than the 0-7 range
# If using 0-3 will need to double it
def move(b, m):
    rows = len(b)
    cols = len(b[0])

    # Check if capture
    isCapture = False
    if len(m) == 6:
        isCapture = True
        captured = (m[2], m[3])
        m = (m[0], m[1], m[4], m[5])

    # Set moving pieces type
    if b[m[1]][m[0]] == -2:
        color = "white"
        king = True
    elif b[m[1]][m[0]] == -1:
        color = "white"
        king = False
    elif b[m[1]][m[0]] == 1:
        color = "black"
        king = False
    else:
        color = "black"
        king = True

    # Check for piece promotion
    if m[3] == 0 or m[3] == cols - 1:
        if color == "white":
            b[m[1]][m[0]] = -2
        else:
            b[m[1]][m[0]] = 2

    # Update board
    if isCapture:
        b[captured[1]][captured[0]] = 0
        
    b[m[3]][m[2]] = b[m[1]][m[0]]
    b[m[1]][m[0]] = 0

    # Redraw new moves
    drawCell(rows, cols, m[1], m[0], "white")
    drawPiece(rows, cols, m[3], m[2], color, king)

    if isCapture:
        drawCell(rows, cols, captured[1], captured[0], "white")

    return b

def captures(b, c):
    print("Not finished")

# TODO In progress
def main():
    b = initialiseBoard()
    print(b)
    drawBoard(b)

    #t = (0, 2, 1, 3)
    t = (0, 0, 1, 1, 2, 2)
    b = move(b, t)
    print(b)

# Advanced, general functions below
#def recursiveCaptures(b, c):

#def capture(b, ms):

#def main():

main()
