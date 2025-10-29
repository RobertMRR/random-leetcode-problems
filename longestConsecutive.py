def longestConsecutive(nums) -> int:
    nums.sort()
    print(nums)
    if not nums:
        return 0
    counter = 1
    longest_counter = 1
    for i in range(1, len(nums)):
        if nums[i-1] + 1 == nums[i]:
            counter += 1
        elif nums[i-1] == nums[i]:
            continue
        else:
            if counter > longest_counter:
                longest_counter = counter
            counter= 1
    return longest_counter

print(longestConsecutive([2,20,4,10,3,4,5]))
print(longestConsecutive([]))