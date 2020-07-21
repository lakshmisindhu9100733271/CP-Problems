# Without using the builtin method s.replace(), 
# write its equivalent. Specifically, write the function 
# replace(s1, s2, s3) that returns a string equal to 
# s1.replace(s2, s3), but again without calling s.replace().


def fun_replace(s1, s2, s3):
	try:
		l=s1.index(s2)
		s=s1[:l]
		s+=s3
		s+=s1[l+len(s2):]

		return s
	except:
	    return s1

