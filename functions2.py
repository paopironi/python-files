def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


n = int(input("Input a non negative integer "))
print("The factorial of %d is %d" % (n, fact(n)))
