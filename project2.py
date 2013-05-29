# Authors:
# Benjamin Holbrook, 20761758
# George Gooden, 20772597

import turtle
import random
import copy

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

# Draw a single cell
# Note: Rows and cols are the grid dimensions, not the board dimensions
def drawCell(rows, cols, c, r, color):
    #print("DrawCell() %d, %d, %d, %d" % (cols, rows, c, r))
    
    squareWidth = 60
    startX = 0 - (cols * squareWidth) / 2
    startY = 0 - (rows * squareWidth) / 2

    x = startX + c * squareWidth
    y = startY + r * squareWidth

    drawRectangle(x, y, squareWidth, squareWidth, color, True, "black")

# Draws the checkerboard grid
# Note: Rows and cols are the grid dimensions, not the board dimensions
def drawGrid(cols, rows):
    #print("DrawGrid() %d, %d" % (rows, cols))
    
    squareWidth = 60
    startX = 0 - (cols * squareWidth) / 2
    startY = 0 - (rows * squareWidth) / 2
    boardHeight = rows * squareWidth
    boardWidth = cols * squareWidth

    drawRectangle(startX, startY, boardWidth, boardHeight, "white", False, "black")
    
    for r in range(rows):
        for c in range(cols):
            if (r + c) % 2 != 0:
                drawCell(rows, cols, c, r, "black")
                
# Draw a single piece
# Note: Rows and cols are the grid dimensions, not the board dimensions
def drawPiece(cols, rows, c, r, color, king):
    #print("DrawPiece() %d, %d, %d, %d" % (cols, rows, c, r))
    
    squareWidth = 60
    startX = 0 - (cols * squareWidth) / 2
    startY = 0 - (rows * squareWidth) / 2
    
    radius = 20
    innerRadius = 10
    innerColor = "red"

    x = startX + c * squareWidth + squareWidth / 2
    y = startY + r * squareWidth + radius / 2
    
    #print("DrawPiece() drawing: x: %d, y: %d" % (x, y))
    
    if color == "white":
        drawCircle(x, y, radius, "white", True, "black")
    else:
        drawCircle(x, y, radius, "black", True, "black")

    if king:
        drawCircle(x, y + radius / 2, innerRadius, innerColor, True, innerColor)

def drawString(x, y, string):
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.penup()
    t.setposition(x, y)
    t.pendown()
    t.write(string, font=("Arial", 16, "normal"));


def drawScore(b, color):
    cellWidth = 60

    rows = len(b)
    cols = len(b[0])

    nKings = 0;
    nPieces = 0;

    for r in range(rows):
        for c in range(cols):
            piece = b[r][c]
            if piece == color:
                nPieces += 1
            elif piece == color * 2:
                nKings += 1
    
    x = (-((cols - 1) * cellWidth) / 2)            
    y = (-color * (rows + 1) * cellWidth) / 2 - 10

    drawRectangle(x, y, 5 * cellWidth, 25, "white", "white", "white")

    colorString = ""
    if color == 1:
        colorString = "Black"
    else:
        colorString = "White"

    drawString(x, y, colorString + " - " + "Pieces: " + str(nPieces) + ", Kings: " + str(nKings))

def drawBoard(b):
    rows = len(b)
    cols = len(b[0])
    gridCols = cols * 2
    
    drawGrid(gridCols, rows)

    #print("Drawing pieces")

    #print("DrawBoard() %d, %d" % (cols, rows))
    
    for r in range(rows):
        for c in range(cols):
            piece = b[r][c]
            c = c * 2
            if r % 2 != 0:
                c += 1

            if piece == -2:
                drawPiece(rows, gridCols, c, r, "white", True)
            elif piece == -1:
                drawPiece(rows, gridCols, c, r, "white", False)
            elif piece == 1:
                drawPiece(rows, gridCols, c, r, "black", False)
            elif piece == 2:
                drawPiece(rows, gridCols, c, r, "black", True)
            elif piece == 0:
                continue
            else:
                raise SystemExit("Invalid piece value")

# Makes a move or a capture and redraws the board
def move(b, m, draw = True):
    rows = len(b)
    cols = len(b[0])
    gridCols = cols * 2

    isCapture = False
    if len(m) == 6:
        isCapture = True
        captureCoord = (m[2], m[3])
        m = (m[0], m[1], m[4], m[5])

    if draw:
        print("Move(): %s, Capture: %r" % (m, isCapture))

    # Set moving pieces type
    cellValue = b[m[1]][m[0]]
    if cellValue == -1 or cellValue == -2:
        color = "white"

        if m[3] == 0 or cellValue == -2:
            king = True
            b[m[1]][m[0]] = -2
        else:
            king = False
    else:
        color = "black"

        if m[3] == rows - 1 or cellValue == 2:
            king = True
            b[m[1]][m[0]] = 2
        else:
            king = False

    # Update board
    b[m[3]][m[2]] = b[m[1]][m[0]]
    b[m[1]][m[0]] = 0
    if isCapture:
        b[captureCoord[1]][captureCoord[0]] = 0

    # Redraw new moves
    # Needs to be converted from half to full column width
    if draw:
        if m[1] % 2 == 0:
            drawCell(gridCols, rows, m[0] * 2, m[1], "white")
        else :
            drawCell(gridCols, rows, m[0] * 2 + 1, m[1], "white")

        # Redraw captured cell
        if isCapture and captureCoord[1] % 2 == 0:
            drawCell(gridCols, rows, captureCoord[0] * 2, captureCoord[1], "white")
        elif isCapture:
            drawCell(gridCols, rows, captureCoord[0] * 2 + 1, captureCoord[1], "white")

        if m[3] % 2 == 0:
            #print("Drawing piece - %s, %r" % (color, king))
            drawPiece(gridCols, rows, m[2] * 2, m[3], color, king)
        else:
            #print("Drawing piece - %s, %r" % (color, king))
            drawPiece(gridCols, rows, m[2] * 2 + 1, m[3], color, king)

    return b

def moves(b, c):
    rows = len(b)
    cols = len(b[0])

    moves = []

    for row in range(rows):
        for col in range(cols):
            piece = b[row][col]
            #print("Colour: %d - Piece: %s - (%d, %d)" % (c, piece, col, row))

            # Check for up positions
            if ((c == 1 and (piece == 1 or piece == 2)) or (c == -1 and piece == -2)) and row + 1 < rows:
                if row % 2 == 0 and col - 1 >= 0 and b[row + 1][col - 1] == 0:
                    moves.append((col, row, col - 1, row + 1))
                if row % 2 and col + 1 < cols and b[row + 1][col + 1] == 0:
                    moves.append((col, row, col + 1, row + 1))
                if b[row + 1][col] == 0:
                    moves.append((col, row, col, row + 1))
            # Check for down positions
            if ((c == -1 and (piece == -1 or piece == -2)) or (c == 1 and piece == 2)) and row - 1 >= 0:
                if row % 2 == 0 and col - 1 >= 0 and b[row - 1][col - 1] == 0:
                    moves.append((col, row, col - 1, row - 1))
                if row % 2 and col + 1 < cols and b[row - 1][col + 1] == 0:
                    moves.append((col, row, col + 1, row - 1))
                if b[row - 1][col] == 0:
                    moves.append((col, row, col, row - 1))
                                
    return moves

def captures(b, c):
    rows = len(b)
    cols = len(b[0])

    captures = []

    for row in range(rows):
        for col in range(cols):
            piece = b[row][col]
            #print("Colour: %d - Piece: %s - (%d, %d)" % (c, piece, col, row))

            # Check for up positions
            if ((c == 1 and (piece == 1 or piece == 2)) or (c == -1 and piece == -2)) and row + 2 < rows:
                # If even row
                if row % 2 == 0:
                    # Check left
                    if col - 1 >= 0 and b[row + 2][col - 1] == 0:
                        if ((c == 1 or c == 2) and (b[row + 1][col - 1] == -1 or b[row + 1][col - 1] == -2)) or ((c == -1 or c == -2) and (b[row + 1][col - 1] == 1 or b[row + 1][col - 1] == 2)):
                            captures.append((col, row, col - 1, row + 1, col - 1, row + 2))
                    # Check right
                    if col + 1 < cols and b[row + 2][col + 1] == 0:
                        if ((c == 1 or c == 2) and (b[row + 1][col] == -1 or b[row + 1][col] == -2)) or ((c == -1 or c == -2) and (b[row + 1][col] == 1 or b[row + 1][col] == 2)):
                            captures.append((col, row, col, row + 1, col + 1, row + 2))
                else:
                    # Check left
                    if col - 1 >= 0 and b[row + 2][col - 1] == 0:
                        if ((c == 1 or c == 2) and (b[row + 1][col] == -1 or b[row + 1][col] == -2)) or ((c == -1 or c == -2) and (b[row + 1][col] == 1 or b[row + 1][col] == 2)):
                            captures.append((col, row, col, row + 1, col - 1, row + 2))
                    # Check right
                    if col + 1 < cols and b[row + 2][col + 1] == 0:
                        if ((c == 1 or c == 2) and (b[row + 1][col + 1] == -1 or b[row + 1][col + 1] == -2)) or ((c == -1 or c == -2) and (b[row + 1][col + 1] == 1 or b[row + 1][col + 1] == 2)):
                            captures.append((col, row, col + 1, row + 1, col + 1, row + 2))

            # Check for down positions
            if ((c == -1 and (piece == -1 or piece == -2)) or (c == 1 and piece == 2)) and row - 2 >= 0:
                # If even row
                if row % 2 == 0:
                    # Check left
                    if col - 1 >= 0 and b[row - 2][col - 1] == 0:
                        if ((c == 1 or c == 2) and (b[row - 1][col - 1] == -1 or b[row - 1][col - 1] == -2)) or ((c == -1 or c == -2) and (b[row - 1][col - 1] == 1 or b[row - 1][col - 1] == 2)):
                            captures.append((col, row, col - 1, row - 1, col - 1, row - 2))
                    # Check right
                    if col + 1 < cols and b[row - 2][col + 1] == 0:
                        if ((c == 1 or c == 2) and (b[row - 1][col] == -1 or b[row - 1][col] == -2)) or ((c == -1 or c == -2) and (b[row - 1][col] == 1 or b[row - 1][col] == 2)):
                            captures.append((col, row, col, row - 1, col + 1, row - 2))
                else:
                    # Check left
                    if col - 1 >= 0 and b[row - 2][col - 1] == 0:
                        if ((c == 1 or c == 2) and (b[row - 1][col] == -1 or b[row - 1][col] == -2)) or ((c == -1 or c == -2) and (b[row - 1][col] == 1 or b[row - 1][col] == 2)):
                            captures.append((col, row, col, row - 1, col - 1, row - 2))
                    # Check right
                    if col + 1 < cols and b[row - 2][col + 1] == 0:
                        if ((c == 1 or c == 2) and (b[row - 1][col + 1] == -1 or b[row - 1][col + 1] == -2)) or ((c == -1 or c == -2) and (b[row - 1][col + 1] == 1 or b[row - 1][col + 1] == 2)):
                            captures.append((col, row, col + 1, row - 1, col + 1, row - 2))
                            
    return captures

# Generate all possible sequences of captures
def recursiveCaptures(b, c):
    captureData = []
    
    for capture in captures(b, c):
        clonedBoard = copy.deepcopy(b)
        clonedBoard = move(clonedBoard, capture, False)
        captureData = capturePath(clonedBoard, c, [capture], captureData)
    return captureData

def capturePath(b, c, path, captureData):
    caps = captures(b, c)
    count = 0
    for capture in caps:
        if capture[0] == path[-1][-2] and capture[1] == path[-1][-1]:
            count += 1
            clonepath = copy.deepcopy(path)
            clonepath.append(capture)
            cloneBoard = copy.deepcopy(b)
            move(cloneBoard, capture, False)
            captureData = capturePath(cloneBoard, c, clonepath, captureData)

    if count == 0:
        captureData.append(path)

    return captureData

# Takes a list of moves and plays them
def capture(b, ms):
    if len(ms) > 0:
        for m in ms:
            b = move(b, m)

    return b
                   
def main():
    # Set to True to enable a manual playthrough of moves
    ENABLE_MANUAL = True
    # Set to True to enable displaying of player scores
    ENABLE_SCORES = True
    
    b = initialiseBoard()
    drawBoard(b)


    # Black player starts first
    currentPlayer = 1

    while True:
        if ENABLE_SCORES:
            drawScore(b, -1) 
            drawScore(b, 1)

        # Manual continue required for each move made
        if ENABLE_MANUAL:
            input("Press enter to continue...")

        # Get captures and moves and make one if available
        captureMoves = recursiveCaptures(b, currentPlayer)
        moveMoves = moves(b, currentPlayer)
        
        if captureMoves != None and len(captureMoves) > 0:
            m = random.choice(captureMoves)
            capture(b, m)
        elif len(moveMoves) > 0:
            move(b, random.choice(moveMoves))
        else:
            break
            
        # Switch player
        currentPlayer *= -1

    if currentPlayer == 1:
        print("Player white wins!")
    else:
        print("Player black wins!")

# TODO Remove this on submission
main()
