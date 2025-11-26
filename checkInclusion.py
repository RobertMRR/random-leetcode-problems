# Permutation in String
def checkInclusion(s1, s2):
    s1_list = list(s1)
    s2_list = list(s2)
    s1_list.sort()
    l, r = 0, len(s1)
    while r < len(s2)+1:
        tmp = s2_list[l:r]
        tmp.sort()
        if tmp == s1_list:
            return True
        r += 1
        l += 1
    return False


print(checkInclusion("abc", "lecabee"))
print(checkInclusion("adc", "dcda"))