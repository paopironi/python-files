def is_prime(n):
    if n < 0:
        print("Negative numbers cannot be prime")
        return
    if n == 1 or n == 2:
        print("%d is a prime number" % (n))
        return
    if n % 2 == 0:
        print("%d is not a prime number" % (n))
        return
    for i in range(3, int(n / 2), 2):
        if i % 2 == 0:
            print("%d is not a prime number" % (n))
            return
    print("%d is a prime number" % (n))


n = int(input("Input an integer number "))
is_prime(n)
