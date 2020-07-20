# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 



def fun_set_kth_digit(n, k, d):
	 n=list(str(n)[::-1])
	 try:
		 if n[k] in "0123456789":
			 n[k]=str(d)
		 elif(n[k] in "-"):
			 n[k]=str(d)
			 n.append("-")
		 return int(''.join(n[::-1]))
	 except:
		 n.append(str(d))
		 return int(''.join(n[::-1]))


