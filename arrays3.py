arr = [25, 14, 56, 15, 36, 56, 77, 18, 29, 49]

min_element = min(arr)
max_element = max(arr)

s = ",".join([str(el) for el in arr])
s = "[" + s + "]"

print("The minimum of the elements of the array %s is %d" % (s, min_element))
print("The maximum of the elements of the array %s is %d" % (s, max_element))
