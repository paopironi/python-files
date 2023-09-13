first = float(input('Enter first number '))
second = float(input('Enter second number '))
third = float(input('Enter the third number '))

if first == second:
    if second == third:
        print("All numbers are equal")
    else:
        print("Neither are all equal or different")
else:
    if first == third:
        print("Neither are all equal or different")
    elif second == third:
        print("Neither are all equal or different")
    else:
        print("All numbers are different")