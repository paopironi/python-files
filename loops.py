old_fib = 0
fib = 1
print("Next Fibonacci number: %d" % (old_fib))
while fib < 50:
    temp = fib
    fib = fib + old_fib  
    if fib >= 50:
        break
    old_fib = temp
    print("Next Fibonacci number: %d" % (fib))
    
n = int(input("Enter a number between 2 and 9 "))
for i in range(1, 13):
    print("%d x %d = %d" % (n, i, n * i))

