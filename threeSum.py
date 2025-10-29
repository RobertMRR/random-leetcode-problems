def threeSum(nums):
    nums.sort()
    result = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l = i + 1
        r = len(nums) - 1
        while l < r:
            sum= nums[l] + nums[r] + nums[i]
            if sum > 0:
                r -= 1
            elif sum < 0:
                l += 1
            if sum == 0:
                result2 = [nums[l], nums[r], nums[i]]
                if result2 not in result:
                    result.append(result2)
                l += 1
    return result



print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))
