# leastFrequentLetters(s) [20 pts]
# Write the function leastFrequentLetters(s), that takes a string s, and ignoring case (so "A" and "a" are treated 
# the same), returns a lowercase string containing the least-frequent alphabetic letters that occur in s, each 
# included only once in the result and then in alphabetic order. So:
# leastFrequentLetters("aDq efQ? FB'daf!!!") 
# returns "be". Note that digits, punctuation, and whitespace are not letters! Also note that seeing as we have not 
# yet covered lists, sets, maps, or efficiency, you are not expected to write the most efficient solution. Finally, 
# if s does not contain any alphabetic characters, the result should be the empty string ("")

def leastfrequentletters(s):
	# Your code goes here
	s=s.lower()
	a=set(s)
	di={}
	for i in a:
		if ord(i)>=65 and ord(i)<=122:
			di[i]=s.count(i)
	key=list(di.keys())
	val=list(di.values())
	li=[]
	for i in range (len(val)):
		if val[i]==min(val):
			li.append(key[i])
	li.sort()
	return ''.join(li).strip()				
	pass
