def maxArea(heights):
    maxSize = 0
    l,r = 0, len(heights)-1
    while l < r:
        currSize = min(heights[l], heights[r]) * (r-l)
        if heights[r] < heights[l]:
            r -= 1
        else:
            l += 1
        maxSize = max(maxSize, currSize)

    return maxSize


assert maxArea([1,7,2,5,4,7,3,6]) == 36
assert maxArea([2,2,2]) == 4