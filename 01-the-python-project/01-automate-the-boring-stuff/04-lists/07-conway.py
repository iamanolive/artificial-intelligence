# conway's game of life
import random
import time
import copy

WIDTH = 60
HEIGHT = 20

# create a list of list for the cells
next_cells = []
for x in range(WIDTH):
    column = [] # create a new column
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append("#") # add a living cell
        else:
            column.append(" ") # add a dead cell
    next_cells.append(column) # next_cells is a list of column lists

while True: # main program loop
    print("\n\n\n\n\n") # seperate each step with newlines
    current_cells = copy.deepcopy(next_cells)
    # print current_cells on the screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(current_cells[x][y], end = "") # print the # or space
        print() # print a newline at the end of the row
    # calculate the next step's cells based on current step's cells
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # get neighboring coordinates
            left_coordinate = (x - 1) % WIDTH
            right_coordinate = (x + 1) % WIDTH
            above_coordinate = (y - 1) % HEIGHT
            below_coordinate = (y + 1) % HEIGHT
            # count the number of living neighbors
            num_neighbors = 0
            if current_cells[left_coordinate][above_coordinate] == "#":
                num_neighbors += 1 # top-left neighbor is alive
            if current_cells[x][above_coordinate] == "#":
                num_neighbors += 1 # top neighbor is alive
            if current_cells[right_coordinate][above_coordinate] == "#":
                num_neighbors += 1 # top-right neighbor is alive
            if current_cells[left_coordinate][y] == "#":
                num_neighbors += 1 # left neighbor is alive
            if current_cells[right_coordinate][y] == "#":
                num_neighbors += 1 # right neighbor is alive
            if current_cells[left_coordinate][below_coordinate] == "#":
                num_neighbors += 1 # bottom-left neighbor is alive
            if current_cells[x][below_coordinate] == "#":
                num_neighbors += 1 # bottom neighbor is alive
            if current_cells[right_coordinate][below_coordinate] == "#":
                num_neighbors += 1 # bottom-right neighbor is alive
            # set cell based on conway's game of life rules
            if current_cells[x][y] == "#" and (num_neighbors == 2 or num_neighbors == 3):
                # living cells with 2 or 3 cells stay alive
                next_cells[x][y] = "#"
            elif current_cells[x][y] == " " and num_neighbors == 3:
                # dead cells with three neighbors become alive
                next_cells[x][y] = "#"
            else:
                # everything else dies or stays dead
                next_cells[x][y] = " "
        time.sleep(1) # add a 1 second pause to reduce flickering