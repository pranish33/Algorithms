# this is the program to find the fiboncci series of nth index element
# or fib memoziation 

def fib(n):
    if n <= 2:
        return 1
    else:
        return n-1 + n-2
    
print(fib(5))