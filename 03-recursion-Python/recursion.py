"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(position):
    fib=0
    c=1
    if position==0:
        return fib
    elif position==1:
        return c
    else:
        for i in range (2,position+1):
            t=fib+c
            fib=c
            c=t
        return c
    return -1