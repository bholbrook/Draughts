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
    
    for r in range(rows):
        for c in range(cols):
            x = startX + c * squareWidth
            y = startY + r * squareWidth
            if (r + c) % 2 == 0:
                #drawRectangle(x, y, squareWidth, squareWidth, "black", False)
                drawCell(rows, cols, c, r, "white")
            else:
                #drawRectangle(x, y, squareWidth, squareWidth, "black", True)
                drawCell(rows, cols, c, r, "black")
                
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

def moves(b, c):
    rows = len(b)
    cols = len(b[0])

    moves = []

    for row in range(rows):
        for col in range(cols):
            piece = b[row][col]
            #print("Colour: %d - Piece: %s - (%d, %d)" % (c, piece, col, row))

            # Found a white piece
            if c == -1 and (piece == -1 or piece == -2):
               # print("White piece at (%d, %d)" % (col, row))
                # Height boundary check
                if row - 1 >= 0:
                    #Check board row shift
                    if row % 2 == 0:
                        # Left move position check
                        if col - 1 >= 0 and b[row-1][col-1] == 0:
                            moves.append((col, row, col-1, row-1))
                        # Right move position check
                        if col < cols and b[row-1][col] == 0:
                            moves.append((col, row, col, row-1))
                    else:
                        # Left move position check
                        #print("Col: %d, Row: %d, b[][]: %d, newb[][]: %d" % (col, row, b[row][col], b[row-1][col]))
                        if col >= 0 and b[row-1][col] == 0:
                            moves.append((col, row, col, row-1))
                        # Right move position check
                        if col + 1 < cols and b[row-1][col+1] == 0:
                            moves.append((col, row, col+1, row-1))
    
                # King piece. Check moves below current position
                if piece == -2:
                    # Height boundary check
                    if row + 1 < rows:
                        #Check board row shift
                        if row % 2 == 0:
                            # Left move position check
                            if col - 1 >= 0 and b[row+1][col-1] == 0:
                                moves.append((col, row, col-1, row+1))
                            # Right move position check
                            if col < cols and b[row+1][col] == 0:
                                moves.append((col, row, col, row+1))
                        else:
                            # Left move position check
                            if col >= 0 and b[row+1][col] == 0:
                                moves.append((col, row, col, row+1))
                            # Right move position check
                            if col + 1 < cols and b[row+1][col+1] == 0:
                                moves.append((col, row, col+1, row+1))

            # Found a black piece
            if c == 1 and (piece == 1 or piece == 2):
                #print("Black piece at (%d, %d)" % (col, row))
                # Height boundary check
                if row + 1 < rows:
                    #Check board row shift
                    if row % 2 == 0:
                        # Left move position check
                        if col - 1 >= 0 and b[row+1][col-1] == 0:
                            moves.append((col, row, col-1, row+1))
                        # Right move position check
                        if col < cols and b[row+1][col] == 0:
                            moves.append((col, row, col, row+1))
                    else:
                        # Left move position check
                        if col >= 0 and b[row+1][col] == 0:
                            moves.append((col, row, col, row+1))
                        # Right move position check
                        if col + 1 < cols and b[row+1][col+1] == 0:
                            moves.append((col, row, col+1, row+1))

                # King piece. Check moves below current position
                if piece == 2:
                    # Height boundary check
                    if row - 1 >= 0:
                        #Check board row shift
                        if row % 2 == 0:
                            # Left move position check
                            if col - 1 >= 0 and b[row-1][col-1] == 0:
                                moves.append((col, row, col-1, row-1))
                            # Right move position check
                            if col < cols and b[row-1][col] == 0:
                                moves.append((col, row, col, row-1))
                        else:
                            # Left move position check
                            if col >= 0 and b[row-1][col] == 0:
                                moves.append((col, row, col, row-1))
                            # Right move position check
                            if col + 1 < cols and b[row-1][col+1] == 0:
                                moves.append((col, row, col+1, row-1))
                                
    return moves

# Makes a move or a capture and redraws the board
def move(b, m):
    rows = len(b)
    cols = len(b[0])
    gridCols = cols * 2

    isCapture = False
    if len(m) == 6:
        isCapture = True
        captureCoord = (m[2], m[3])
        m = (m[0], m[1], m[4], m[5])

    print("Move(): %s, Capture: %r" % ((m,), isCapture))

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

# Makes a move or a capture without redrawing the board
def moveNoDraw(b, m):
    rows = len(b)
    cols = len(b[0])
    gridCols = cols * 2

    isCapture = False
    if len(m) == 6:
        isCapture = True
        captureCoord = (m[2], m[3])
        m = (m[0], m[1], m[4], m[5])

    print("Move(): %s, Capture: %r" % ((m,), isCapture))

    # Set moving pieces type
    cellValue = b[m[1]][m[0]]
    if cellValue == -1 or cellValue == -2:
        if m[3] == 0 or cellValue == -2:
            b[m[1]][m[0]] = -2
    else:
        if m[3] == rows - 1 or cellValue == 2:
            b[m[1]][m[0]] = 2

    # Update board
    b[m[3]][m[2]] = b[m[1]][m[0]]
    b[m[1]][m[0]] = 0
    if isCapture:
        b[captureCoord[1]][captureCoord[0]] = 0

    return b

def captures(b, c):
    rows = len(b)
    cols = len(b[0])

    captures = []

    for row in range(rows):
        for col in range(cols):
            piece = b[row][col]
            #print("Colour: %d - Piece: %s - (%d, %d)" % (c, piece, col, row))

            # Found a white piece
            if c == -1 and (piece == -1 or piece == -2):
                #print("White piece at (%d, %d)" % (col, row))
                # Height boundary check
                if row - 2 >= 0:
                    #Check board row shift
                    if row % 2 == 0:
                        # Left move position check
                        if col - 1 >= 0 and b[row-2][col-1] == 0:
                            # Jumped piece check
                            if b[row-1][col-1] == 1 or b[row-1][col-1] == 2:
                                captures.append((col, row, col-1, row-1, col-1, row-2))
                        # Right move position check
                        if col + 1 < cols and b[row-2][col+1] == 0:
                            # Jumped piece check
                            if b[row-1][col] == 1 or b[row-1][col] == 2:
                                captures.append((col, row, col, row-1, col+1, row-2))
                    else:
                        # Left move position check
                        if col - 1 >= 0 and b[row-2][col-1] == 0:
                            # Jumped piece check
                            if b[row-1][col] == 1 or b[row-1][col] == 2:
                                captures.append((col, row, col, row-1, col-1, row-2))
                        # Right move position check
                        if col + 1 < cols and b[row-2][col+1] == 0:
                            # Jumped piece check
                            if b[row-1][col+1] == 1 or b[row-1][col+1] == 2:
                                captures.append((col, row, col+1, row-1, col+1, row-2))

                # King piece. Check moves below current position
                if piece == -2:
                    # Height boundary check
                    if row + 2 < rows:
                        #Check board row shift
                        if row % 2 == 0:
                            # Left move position check
                            if col - 1 >= 0 and b[row+2][col-1] == 0:
                                # Jumped piece check
                                if b[row+1][col-1] == 1 or b[row+1][col-1] == 2:
                                    captures.append((col, row, col-1, row+1, col-1, row+2))
                            # Right move position check
                            if col + 1 < cols and b[row+2][col+1] == 0:
                                # Jumped piece check
                                if b[row+1][col] == 1 or b[row+1][col] == 2:
                                    captures.append((col, row, col, row+1, col+1, row+2))
                        else:
                            # Left move position check
                            if col - 1 >= 0 and b[row+2][col-1] == 0:
                                # Jumped piece check
                                if b[row+1][col] == 1 or b[row+1][col] == 2:
                                    captures.append((col, row, col, row+1, col-1, row+2))
                            # Right move position check
                            if col + 1 < cols and b[row+2][col+1] == 0:
                                # Jumped piece check
                                if b[row+1][col+1] == 1 or b[row+1][col+1] == 2:
                                    captures.append((col, row, col+1, row+1, col+1, row+2))

            # Found a black piece
            elif c == 1 and (piece == 1 or piece == 2):
                #print("Black piece at (%d, %d)" % (col, row))
                # Height boundary check
                if row + 2 < rows:
                    #Check board row shift
                    if row % 2 == 0:
                        # Left move position check
                        if col - 1 >= 0 and b[row+2][col-1] == 0:
                            # Jumped piece check
                            if b[row+1][col-1] == -1 or b[row+1][col-1] == -2:
                                captures.append((col, row, col-1, row+1, col-1, row+2))
                        # Right move position check
                        if col + 1 < cols and b[row+2][col+1] == 0:
                            # Jumped piece check
                            if b[row+1][col] == -1 or b[row+1][col] == -2:
                                captures.append((col, row, col, row+1, col+1, row+2))
                    else:
                        # Left move position check
                        if col - 1 >= 0 and b[row+2][col-1] == 0:
                            # Jumped piece check
                            if b[row+1][col] == -1 or b[row+1][col] == -2:
                                captures.append((col, row, col, row+1, col-1, row+2))
                        # Right move position check
                        if col + 1 < cols and b[row+2][col+1] == 0:
                            # Jumped piece check
                            if b[row+1][col+1] == -1 or b[row+1][col+1] == -2:
                                captures.append((col, row, col+1, row+1, col+1, row+2))

                # King piece. Check moves below current position
                if piece == 2:
                    # Height boundary check
                    if row - 2 < rows:
                        #Check board row shift
                        if row % 2 == 0:
                            # Left move position check
                            if col - 1 >= 0 and b[row-2][col-1] == 0:
                                # Jumped piece check
                                if b[row-1][col-1] == -1 or b[row-1][col-1] == -2:
                                    captures.append((col, row, col-1, row-1, col-1, row-2))
                            # Right move position check
                            if col + 1 < cols and b[row-2][col+1] == 0:
                                # Jumped piece check
                                if b[row-1][col] == -1 or b[row-1][col] == -2:
                                    captures.append((col, row, col, row-1, col+1, row-2))
                        else:
                            # Left move position check
                            if col - 1 >= 0 and b[row-2][col-1] == 0:
                                # Jumped piece check
                                if b[row-1][col] == -1 or b[row-1][col] == -2:
                                    captures.append((col, row, col, row-1, col-1, row-2))
                            # Right move position check
                            if col + 1 < cols and b[row-2][col+1] == 0:
                                # Jumped piece check
                                if b[row-1][col+1] == -1 or b[row-1][col+1] == -2:
                                    captures.append((col, row, col+1, row-1, col+1, row-2))
                                
    return captures

# Need to confirm on multiple situations
def recursiveCaptures(b, c):
    captureData = []
    
    for capture in captures(b, c):
        clonedBoard = copy.deepcopy(b)
        clonedBoard = moveNoDraw(clonedBoard, capture)
        # print(capture)
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
            moveNoDraw(cloneBoard, capture)
            captureData = capturePath(cloneBoard, c, clonepath, captureData)

    if count == 0:
        captureData.append(path)

    return captureData

# Takes a list of moves and makes each of them
def capture(b, ms):
    if len(ms) > 0:
        for m in ms:
            b = move(b, m)

    return b

# Given a board state returns if a player has won and which colour
# Black: 1, White, -1, No victor: 0
# Return ex. (True, 1): Black victory
def isGameOver(b):
    rows = len(b)
    cols = len(b[0])

    numBlackPieces = 0
    numWhitePieces = 0
    for r in range(rows):
        for c in range(cols):
            piece = b[r][c]
            if piece == -1 or piece == -2:
                numWhitePieces += 1
            elif piece == 1 or piece == 2:
                numBlackPieces += 1

    # Check number of pieces on board
    if numBlackPieces == 0 and numWhitePieces == 0:
        # No pieces left, no victor
        return (True, 0)
    elif numBlackPieces == 0:
        # No black pieces left, white victory
        return (True, -1)
    elif numWhitePieces == 0:
        # No white pieces left, black victory
        return (True, 1)
    else:
        # Both players have pieces
        whiteMoves = moves(b, -1)
        blackMoves = moves(b, 1)
        whiteCaptures = captures(b, -1)
        blackCaptures = captures(b, 1)
        numWhiteMoves = len(whiteMoves) + len(whiteCaptures)
        numBlackMoves = len(blackMoves) + len(blackCaptures)

        if numWhiteMoves == 0 and numBlackMoves == 0:
            # No more available moves, no victor
            return (True, 0)
        elif numWhiteMoves == 0:
            # No available white moves, black victory
            return (True, 1)
        elif numBlackMoves == 0:
            # No available black moves, white victory
            return (True, -1)
        else:
            # Move can be made, no victor
            return (False, 0)
                   
def main():
    autoGame = input("Do you want an automatic game? (y/n): ")
    if autoGame == 'y' or autoGame == 'Y':
        autoGame = True
    else:
        autoGame = False
    
    b = initialiseBoard()
    drawBoard(b)

    # Black player starts first
    currentPlayer = 1
    gameOverState = isGameOver(b)
    while not gameOverState[0]:
        #if currentPlayer == 1:
        #    print("Player black to move")
        #else:
        #    print("Player white to move")
        
        # Get captures and moves and make one if available
        captureMoves = recursiveCaptures(b, currentPlayer)
        moveMoves = moves(b, currentPlayer)
        
        if captureMoves != None and len(captureMoves) > 0:
            m = random.choice(captureMoves)
            capture(b, m)
        elif len(moveMoves) > 0:
            #moveNoDraw(b, random.choice(moveMoves))
            move(b, random.choice(moveMoves))
            
        # Switch player
        currentPlayer *= -1

        # Update game over state
        gameOverState = isGameOver(b)

        # Manual continue for each move made
        if not autoGame:
            input("Press enter to continue...")        

    if gameOverState[1] == 1:
        print("Player black wins!")
    else:
        print("Player white wins!")

def test():
    b = initialiseBoard()
    #drawBoard(b)

    c = 1
    rec = recursiveCaptures(b, c)
    print("RecursiveCaptures")
    print(rec)

main()
#test()
