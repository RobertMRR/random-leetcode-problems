# Koko Eating Bananas
import math
def minEatingSpeed(piles, h):
    l,r = 1, max(piles)
    min_h = r
    while r >= l:
        mid = (r + l) // 2
        tmp = [math.ceil(i / mid) for i  in piles]
        if h >= sum(tmp):
            min_h = min(mid, min_h)
            r = mid - 1
        else:
            l = mid + 1
    return min_h
print(minEatingSpeed([3,6,7,11], 8))
print(minEatingSpeed([25,10,23,4],4))
print(minEatingSpeed([1,4,3,2],9))