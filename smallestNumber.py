def smallestNumber(n):
    for i in range(n):
        tmp = 2**i - 1
        if tmp > n:
            return tmp

print(smallestNumber(5))