a = float(input('Enter first number '))
b = float(input('Enter second number '))
c = float(input('Enter the third number '))

if a < b:
    if b < c:
        print("Increasing order")
    else:
        print("Neither increasing or decreasing order")
else:
    if b > c:
        print("Decreasing order")
    else:
        print("Neither increasing or decreasing order")