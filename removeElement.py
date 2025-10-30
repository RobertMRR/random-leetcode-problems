def removeElement(nums, val):
    l = 0
    r = len(nums)
    while l<r:
        if nums[l]==val:
            nums.pop(l)
            r -= 1
            continue
        l += 1
    return r

print(removeElement([0,1,2,2,3,0,4,2], 2))