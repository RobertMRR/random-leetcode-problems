# Binary Search
def search(nums, target):
    l, r = 0, len(nums)-1
    while r >= l:
        middle = (l + r)//2
        if target == nums[middle]:
            return middle
        elif target > nums[middle]:
            l = middle + 1 
        else:
            r = middle - 1
    return -1

print(search([-1,0,3,5,9,12],2))
print(search([5],5))