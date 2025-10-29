def moveZeroes(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.remove(nums[i])
            nums.append(0)

def plusOne(digits):
    tmp = ""
    for digit in digits:
        tmp += str(digit)
    tmp_int = int(tmp)
    tmp_int+=1
    return list(map(int,str(tmp_int)))

print(plusOne([1,2,3]))