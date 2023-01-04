def circularArrayRotation(a, k, queries):
    temp = a[-(k%n):] 
    res =[]
    a = a[:len(a)-(k%n)]
    for ele in a:
        temp.append(ele)
    for q in queries:
        res.append(temp[q])
    return res