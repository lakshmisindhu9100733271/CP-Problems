# Without using iteration and without using strings, 
# write the recursive function onlyEvenDigits(L), 
# that takes a list L of non-negative integers 
# (you may assume that), and returns a new list of 
# the same numbers only without their odd digits 
# (if that leaves no digits, then replace the number with 0). 
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844]. 
# Also the function returns the empty list if the original list is empty. 
# Remember to not use strings. You may not use loops/iteration in this problem.

def fun_recursion_onlyevendigits(l): 
	return even(l,[],0)


def even(l,a,i):
	if i==len(l):
		return a
	else:
		li=list(str(l[i]))
		li=list(map(int,li))
		li1=[]
		for j in li:
			if j%2==0:
				li1.append(j)
		li1=list(map(str,li1))
		li1=''.join(li1)
		if len(li1)==0:
			a.append(0)
		elif int(li1)%2==0:
			a.append(int(li1))
		i+=1
		return even(l,a,i)