# Authors:
# Benjamin Holbrook, 20761758
# George Gooden, 20772597


#README
# We need to make the function params for x,y values consistent so they always take in x then y rather than y then x

import turtle
import random

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

    #print("Drawing pieces")
    #print("DrawBoard() %d, %d" % (rows, cols))
    
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
# Note: Rows and cols are the grid dimensions, not the board dimensions
def drawCell(rows, cols, r, c, color):
    #print("DrawCell() %d, %d, %d, %d" % (rows, cols, r, c))
    
    squareWidth = 60
    startX = 0 - (cols * squareWidth) / 2
    startY = 0 - (rows * squareWidth) / 2

    x = startX + c * squareWidth
    y = startY + r * squareWidth

    drawRectangle(x, y, squareWidth, squareWidth, color, True, "black")

# Draws the checkerboard grid
# Note: Rows and cols are the grid dimensions, not the board dimensions
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

# Draw a single piece
# Note: Rows and cols are the grid dimensions, not the board dimensions
def drawPiece(rows, cols, r, c, color, king):
    #print("DrawPiece() %d, %d, %d, %d" % (rows, cols, r, c))
    
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
    
def move(b, m):
    rows = len(b)
    cols = len(b[0])
    gridCols = cols * 2

    print(m)

    # Set moving pieces type
    cellValue = b[m[1]][m[0]]
    if cellValue == -1 or cellValue == -2:
        color = "white"

        if m[3] == 0:
            king = True
        else:
            king = False
    else:
        color = "black"

        if m[3] == rows - 1:
            king = True
        else:
            king = False

    # Update board
    b[m[3]][m[2]] = b[m[1]][m[0]]

    # Update board if piece promoted
    if king:
        b[m[3]][m[2]] *= 2        
    b[m[1]][m[0]] = 0   

    # Redraw new moves
    # Needs to be converted from half to full column width
    if m[1] % 2 == 0:
        drawCell(rows, gridCols, m[1], m[0] * 2, "white")
    else :
        drawCell(rows, gridCols, m[1], m[0] * 2 + 1, "white")

    if m[3] % 2 == 0:
        drawPiece(rows, gridCols, m[3], m[2] * 2, color, king)
    else:
        drawPiece(rows, gridCols, m[3], m[2] * 2 + 1, color, king)

    return b

def captures(b, c):
    rows = len(b)
    cols = len(b[0])

    captures = []

    for row in range(rows):
        for col in range(cols):
            piece = b[row][col]
            #print("Colour: %d - Piece: %s - (%d, %d)" % (c, piece, row, col))

            # Found a white piece
            if c == -1 and (piece == -1 or piece == -2):
                #print("White piece at (%d, %d)" % (row, col))
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
                                captures.append((col, row, col, r+1, col-1, r+2))
                        # Right move position check
                        if col + 1 < cols and b[row+2][col+1] == 0:
                            # Jumped piece check
                            if b[row+1][col+1] == 1 or b[row+1][col+1] == 2:
                                captures.append((col, row, col+1, row+1, col+1, row+2))

                            
                # King piece. Check moves below current position
                if piece == 2:
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
                

            # Found a black piece
            elif c == 1 and (piece == 1 or piece == 2):
                #print("Black piece at (%d, %d)" % (row, col))
                # Height boundary check
                if row + 2 < rows:
                    #Check board row shift
                    if row % 2 == 0:
                        # Left move position check
                        if col - 1 >= 0 and b[row+2][col-1] == 0:
                            # Jumped piece check
                            if b[row+1][col-1] == -1 or b[row+1][col-1] == -2:
                                captures.append((col, row, col-1, row+1, ol-1, row+2))
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
                                
    return captures

# Advanced, general functions below
def recursiveCaptures(b, c):
    if len(c) == 0:
        return b

    #else:
    # TODO Write me
        #caps = captures(b, c)
        #return recursiveCaptures(b, c)

def capture(b, ms):
    rows = len(b)
    cols = len(b[0])
    gridCols = cols * 2

    # Set moving pieces type
    cellValue = b[ms[1]][ms[0]]
    if cellValue == -1 or cellValue == -2:
        color = "white"

        if ms[5] == 0:
            king = True
        else:
            king = False
    else:
        color = "black"

        if ms[5] == rows - 1:
            king = True
        else:
            king = False

    # Update board
    b[ms[5]][ms[4]] = b[ms[1]][ms[0]]
    b[ms[3]][ms[2]] = 0    
    b[ms[1]][ms[0]] = 0

    # Update board if piece promoted
    if king:
        b[ms[5]][ms[4]] *= 2   

    # Redraw new moves
    # Needs to be converted from half to full column width
    if ms[1] % 2 == 0:
        drawCell(rows, gridCols, ms[1], ms[0] * 2, "white")
    else :
        drawCell(rows, gridCols, ms[1], ms[0] * 2 + 1, "white")

    if ms[5] % 2 == 0:
        drawPiece(rows, gridCols, ms[5], ms[4] * 2, color, king)
    else:
        drawPiece(rows, gridCols, ms[5], ms[4] * 2 + 1, color, king)

    if ms[3] % 2 == 0:
        drawCell(rows, gridCols, ms[3], ms[2] * 2, "white")
    else:
        drawCell(rows, gridCols, ms[3], ms[2] * 2 + 1, "white")

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
        else:
            # Move can be made, no victor
            return (False, 0)
                                 
# TODO In progress
def main():    
    b = initialiseBoard()
    #print(b)
    drawBoard(b)

    # Black player starts first
    currentPlayer = 1
    gameOverState = isGameOver(b)
    while not gameOverState[0]:
        # Get captures and moves and make one if available
        captureMoves = captures(b, currentPlayer)
        moveMoves = moves(b, currentPlayer)
        
        if len(captureMoves) > 0:
            capture(b, random.choice(captureMoves))
        elif len(moveMoves) > 0:
            move(b, random.choice(moveMoves))
            
        # Switch player
        currentPlayer *= -1

        # Update game over state
        gameOverState = isGameOver(b)

    if gameOverState[1] == 1:
        print("Player black wins!")
    else:
        print("Player white wins!")

    # This section is purely for board "e.txt" and includes a black capture
    #print("Black captures")
    #bc = captures(b, 1)
    #print(bc)

    #capture(b, bc[0])
    # End black capture section

    #gameOverState = isGameOver(b)
    #print("GameOver: %r, Victor: %d" % (gameOverState[0], gameOverState[1]))

main()
