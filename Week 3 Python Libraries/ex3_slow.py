def sum_py():
    for x in range(500):
        res = 0
        for k in range(1, 10001):   #from 1 to 10,000
            res += (1/(k**2))
    print(res)

sum_py()
