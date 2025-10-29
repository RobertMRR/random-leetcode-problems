def removeDuplicates(nums):
    l = 0
    r = 1
    while r < len(nums):
        if nums[l] == nums[r]:
            nums.pop(r)
            continue
        l+=1
        r+=1
    return len(nums), nums

print(removeDuplicates([1,1,2]))