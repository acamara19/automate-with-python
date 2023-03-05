# Conway's Game of Life
import random
import time
import copy

WIDTH = 60
HEIGHT = 20

# Create a list of lists for the cells:
nextCells = []
for x in range(WIDTH):
    column = [] # Create a new column
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#') # add a living cell
        else:
            column.append(' ') # add a dead cell.
        nextCells.append(column) # next cell is a list of column list

while True: # Main program loop.
    print('\n\n\n\n\n') # separate each steps with a new line.
    currentCells = copy.deepcopy(nextCells)

    # Print currentCells on the screen.
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='') # Print # or space
        print() # Print a new line at the end of the row.

    # Calculate the next step's cells based on the current cells.
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # get neighboring coordinates.
            # '% WIDTH' ensures leftCoord is always between 0 and WIDTH - 1. 
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            # Count number of living neighbor.
            numNeighbor = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbor += 1 # Top left neighbor is alive.
            if currentCells[x][aboveCoord] == '#':
                numNeighbor += 1 # Tob neighbor is alive;
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbor += 1 # Top right neighbor is alive.
            if currentCells[leftCoord][y] == '#':
                numNeighbor += 1 # Left neighbor is alive.
            if currentCells[rightCoord][y] == '#':
                numNeighbor += 1 # Right neighbor is alive.
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbor += 1 # Bottom left neighbor is alive.
            if currentCells[x][belowCoord] == '#':
                numNeighbor += 1 # Bottom neighbor is alive.
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbor += 1 # Bottom right neighbor is alive.

            # Set cells based on Conway's game of life:
            if currentCells[x][y] == '#' and (numNeighbor == 2 or numNeighbor == 3): # Living cells with 2 or 3 neighbors stay alive.
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and (numNeighbor == 3): # Dead cells with 3 neighbors stay alive.
                nextCells[x][y] = '#'
            else: # Everything else dies or stay dead.
                nextCells[x][y] = ' '
    time.sleep(1) # add a 1 second pause to avoid flickering effect.