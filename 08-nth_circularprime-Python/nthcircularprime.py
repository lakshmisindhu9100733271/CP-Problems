# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth 
# Circular prime, which is a prime number that does not contain any 0's and such that all the 
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3, 
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime, 
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).
def prime(n):
	if n<=1:
		return False
	if n<=3:
		return True
	if(n%2==0 or n%3==0):
		return False
	i=5
	while(i*i<=n):
		if(n%i==0 or n%(i+2)==0):
			return False
		i=i+6
	return True

def rot(n):
	n=str(n)
	n=n[-1]+n[:len(n)-1]
	return int(n)

def nthcircularprime(n):
	# Your code goes here
	i=1
	c=1
	while(c<=n):
		if prime(i):
			cc=1
			k=i
			for j in range(len(str(i))-1):
				k=rot(k)
				if prime(k) and k!=i:
					cc+=1
			if cc==len(str(i)):
				c+=1
		i+=1
	return i-1					

	pass