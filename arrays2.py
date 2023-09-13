arr = [20, 30, 25, 35, -16, 60, -100]

avg = 0

for el in arr:
    avg += el

avg = avg / len(arr)

s = ",".join([str(el) for el in arr])
s = "[" + s + "]"
print("The average of the elements of the array %s is %.2f" % (s, avg))
