arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum = 0
for el in arr:
    sum += el

s = ",".join([str(el) for el in arr])
s = "[" + s + "]"
print("The sum of the elements of the array %s is %d" % (s, sum))
