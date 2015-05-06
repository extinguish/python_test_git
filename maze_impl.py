# solve the maze puzzle using the A* algorothm and
# in recursive way.
# the first way to implement this by using the recursive way
# first, we store the maze map : one 6 X 6 matrix
# in this matrix, the 1 represents the wall, and 0 indicates path
# that we can walk through directly, and the finally 2 indicate
# the terminal point.
grid = [[0, 0, 0, 0, 0, 1],
		[1, 1, 0, 0, 0, 1],
		[0, 0, 0, 1, 0, 0],
		[0, 1, 1, 0, 0, 1],
		[0, 1, 0, 0, 1, 0],
		[0, 1, 0, 0, 0, 2]
		]

# the following implementation are the recursive implementation.
# the search function accepts the coordinates of a cell to explore.
# If it is the end cell, it returns True. If it is a wall or an already
# visited cell, it returns false. 
# we mark the path that we have visited as 3(of which different than 0 and 1)
def search(x, y):
	if grid[x][y] == 2:
		print "found at %d, %d : " % (x, y)
		return True # the terminal situation
	elif grid[x][y] == 1:
		print "wall at %d, %d : " % (x, y)
	elif grid[x][y] == 3:
		print "we have visited here at %d, %d : " % (x, y)
		return False # we have not found the way to get off the maze, so we are fail at last

	print "we are current visiting at %d, %d : " % (x, y)

	# mark as visited
	# If we have walked through the previous steps, then mark the grid
	# we have walked as 3, to tag it we need'n to walk through it again.
	grid[x][y] = 3 

	# explore neighbors clockwise starting by the one on the right
	# we search in four direction
	if((x < len(grid) - 1 and search(x + 1, y)) 
		or (y > 0 and search(x, y - 1)) 
		or (x > 0 and search(x - 1, y)) 
		or (y < len(grid) - 1 and search(x, y + 1))):
		return True

	return False



# test the function
if search(0, 0):
	print "we have finally found the way to get off here!!!"
else:
	print "Fuck!!! This maze are dead lock, we cannot get off here~~~~~"

# and now, we will re-implement the maze algorithm by using the A* algorithm
# def searchAStar(x, y):
# It is too hard for me now 
# TODO: implement the A* algorithm



























































