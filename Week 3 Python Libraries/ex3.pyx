def sum_py():
    cdef float res
    cdef int x, k
    for x in range(500):
        res = 0
        for k in range(1, 10001):
            res += (1/(float)(k**2))
    print(res)
