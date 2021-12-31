# this is the program to perform fibonacci series 
# also the example of recursion program 
def fibo(n):
    if n <= 1:
         return n
    else:
        # this is called recursive function when it call its function 
        return (fibo(n-1) + fibo(n-2))
    
nth = 10
if nth <= 0:
    print("Please Enter positive integers only!")
else:
    print("Fibonacci Series are: ")
    # I have used for loop to iterate through nth number 
    # to calculate its sequence recursively
    for i in range(nth):
        print(fibo(i))