# Write the function nearestOdd(n) that takes an float n, 
# and returns as an int value the nearest odd number to n. 
# In the case of a tie, return the smaller odd value. 
# Note that the result must be an int, so nearestOdd(13.0) is the int 13, and not the float 13.0.



def fun_nearestodd(n):
	nu=int(n)
	if nu%2==0:
		s=nu-1
		b=nu+1
		if n-s<b-n:
			return s
		elif n-s>b-n:
			return b
		elif n-s==b-n:
			return s
	else:
		return nu


