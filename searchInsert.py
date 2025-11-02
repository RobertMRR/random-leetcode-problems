#Search insert position
def searchInsert(nums, target):
    l, r = 0, len(nums)
    tries = 0
    if target < nums[0]:
        return 0
    elif target > nums[-1]:
        return len(nums)
    while tries < len(nums):
        mid = int((l+r)/2)
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            l = mid
        elif target < nums[mid]:
            r = mid
        tries += 1
    return mid + 1

print(searchInsert([1,3,5,6],5))
print(searchInsert([1,3,5,6],2))
print(searchInsert([1,3,5,6],7))
