arr = [10, 2, 3, 4, 7]


def max_of_list(arr):
    s = ",".join([str(el) for el in arr])
    s = "[" + s + "]"
    print("The maximum of the elements of the array %s is %d" % (s, max(arr)))


max_of_list(arr)
