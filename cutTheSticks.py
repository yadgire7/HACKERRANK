def cutTheSticks(arr):
    res = [len(arr)]
    while len(arr) != 0:
        arr = sorted(arr)[::-1]
        # print(arr)
        arr = [x-arr[-1] for x in arr]
        # print(arr)
        ind = arr.index(0)
        arr = arr[:ind]
        # print(arr)
        if len(arr) == 0:
            break
        else:
            res.append(len(arr))
    return res
