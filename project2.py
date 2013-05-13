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
    gridCols = cols * 2
    
    drawGrid(rows, gridCols)

    print("Drawing pieces")
    print("DrawBoard() %d, %d" % (rows, cols))
    
    for r in range(rows):
        for c in range(cols):
            piece = b[r][c]
            c = c * 2
            if r % 2 != 0:
                c += 1

            if piece == -2:
                drawPiece(rows, gridCols, r, c, "white", True)
            elif piece == -1:
                drawPiece(rows, gridCols, r, c, "white", False)
            elif piece == 1:
                drawPiece(rows, gridCols, r, c, "black", False)
            elif piece == 2:
                drawPiece(rows, gridCols, r, c, "black", True)
            elif piece == 0:
                continue
            else:
                print("Should never reach here")

def drawRectangle(x, y, w, h, innerColor, fill, borderColor):
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.color(borderColor)
    t.fillcolor(innerColor)

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

# Draw a single cell
# Note: Rows and cols are the grid dimenions, not the board dimensions
def drawCell(rows, cols, r, c, color):
    #print("DrawCell() %d, %d" % (rows, cols))
    
    squareWidth = 60
    startX = 0 - (cols * squareWidth) / 2
    startY = 0 - (rows * squareWidth) / 2

    x = startX + c * squareWidth
    y = startY + r * squareWidth

    drawRectangle(x, y, squareWidth, squareWidth, color, True, "black")

# Draws the checkerboard grid
# Note: Rows and cols are the grid dimenions, not the board dimensions
def drawGrid(rows, cols):
    #print("DrawGrid() %d, %d" % (rows, cols))
    
    squareWidth = 60
    startX = 0 - (cols * squareWidth) / 2
    startY = 0 - (rows * squareWidth) / 2
    
    for r in range(rows):
        for c in range(cols):
            x = startX + c * squareWidth
            y = startY + r * squareWidth
            if (r + c) % 2 == 0:
                #drawRectangle(x, y, squareWidth, squareWidth, "black", False)
                drawCell(rows, cols, r, c, "white")
            else:
                #drawRectangle(x, y, squareWidth, squareWidth, "black", True)
                drawCell(rows, cols, r, c, "black")
                
def drawCircle(x, y, r, innerColor, fill, borderColor):
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.color(borderColor)
    t.fillcolor(innerColor)

    # Move to x, y cord
    t.penup()
    t.setposition(x, y)
    t.pendown()

    if fill:
        t.begin_fill()

    t.circle(r)
    
    t.end_fill()
    
def drawPiece(rows, cols, r, c, color, king):
    print("DrawPiece() %d, %d, %d, %d" % (rows, cols, r, c))
    
    squareWidth = 60
    startX = 0 - (cols * squareWidth) / 2
    startY = 0 - (rows * squareWidth) / 2
    
    radius = 20
    innerRadius = 10
    innerColor = "red"

    x = startX + c * squareWidth + squareWidth / 2
    y = startY + r * squareWidth + radius / 2
    
    print("DrawPiece() drawing: x: %d, y: %d" % (x, y))
    
    if color == "white":
        drawCircle(x, y, radius, "white", True, "black")
    else:
        drawCircle(x, y, radius, "black", True, "black")

    if king:
        drawCircle(x, y + radius / 2, innerRadius, innerColor, True, innerColor)

# In progress
def moves(b, c): 
    moves = []
    
    rows = len(b)
    cols = len(b[0])

    for row in range(rows):
        for col in range(cols): 
            if c == 1: # if black player
                if b[row][col] == 1 or b[row][col] == 2: ## detemining moves forward for normal or king pieces
                    if row != rows-1: # if end row (so can't move down any more)
                        if b[row+1][col] == 0: # if the destination is empty
                            moves.append((row, col, row+1, col))
                        if row % 2 != 0: # if the current row is odd numbered
                            if col != cols-1: # if not at the edge of the board
                                if b[row+1][col+1] == 0: # then check if destination is empty
                                    moves.append((row, col, row+1, col+1))
                        else: # if the current row is even numbered
                            if col != 0: # if not at the edge of the board
                                if b[row+1][col-1] == 0: # checking if the destination is empty
                                    moves.append((row, col, row+1, col-1))
                if b[row][col] == 2: # determining moves back for king piece
                    if row != 0: # if not at the edge of the board
                        if b[row-1][col] == 0: # check if move back destination is empty
                            moves.append((row, col, row-1, col))
                        if row % 2 != 0: # if odd numbered row
                            if col != cols-1: # check if at the edge of the board
                                if b[row-1][col+1] == 0: # check if destination is empty
                                    moves.append((row, col, row-1, col+1))
                        else: # if even numbered row
                            if col != 0: # check for edge of board
                                if b[row-1][col-1] == 0: # check if destination is empty
                                    moves.append((row, col, row-1, col-1))
            elif c == -1: # same below, but for white player moving up
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
    gridCols = cols * 2

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
    print("Redrawing new moves")
    drawCell(rows, gridCols, m[1], m[0], "white")
    drawPiece(rows, gridCols, m[3], m[2], color, king)

    if isCapture:
        drawCell(rows, gridCols, captured[1], captured[0], "white")

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

    drawCircle(0, 0, 10, "blue", True, "blue")

# Advanced, general functions below
#def recursiveCaptures(b, c):

#def capture(b, ms):

#def main():

main()
