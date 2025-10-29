def canMakeArithmeticProgression(arr) -> bool:
    good_result = arr[0] - arr[1]
    print(good_result)
    for i in range(len(arr)):
        tmp = arr[i] - arr[i+1]
        print(tmp)
        if abs(tmp) == abs(good_result):
            continue
        else:
            return False
    return True

print(canMakeArithmeticProgression([1,2,4]))