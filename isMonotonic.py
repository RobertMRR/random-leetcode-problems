def isMonotonic( nums) -> bool:
    if len(nums) < 2:
        return True
    if nums[0] > nums[1]:
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                return False
    elif nums[0] < nums [1]:
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return False
    else:
        for i in range(len(nums)-1):
            print(f"nums i:{nums[i]}, nums i+1: {nums[i+1]}")
            if nums[i] == nums[i+1]:
                continue
            else:
                if nums[i] > nums[i+1]:
                    for j in range(len(nums)-1):
                        if nums[j] < nums[j+1]:
                            return False
                elif nums[i] < nums [i+1]:
                    for k in range(len(nums)-1):
                        if nums[k] > nums[k+1]:
                            return False
    return True

print(isMonotonic([2,2,2,1,4,5]))