# Write the function pascalsTriangleValue(row, col) 
# that takes int values row and col, and returns the 
# value in the given row and column of Pascal's 
# Triangle where the triangle starts at row 0, and 
# each row starts at column 0. If either row or col 
# are not legal values, return None, instead of crashing. 




def fun_pascaltrianglevalue(row, col):
	sq=[[1],[1,1]]
	for i in range (2,row+1):
		sq2=[]
		sq2.append(sq[-1][0])
		for j in range(len(sq[-1])-1):
			sq2.append(sq[-1][j]+sq[-1][j+1])
		sq2.append(sq[-1][-1])
		sq.append(sq2)
	try:
		return sq[row][col]
	
	except:
		return 0


	# return 1