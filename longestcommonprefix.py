from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    longestPrefixes= [len(strs) for s in range(len(strs))]
    for i in range(1, len(strs)):
        counter = 0
        for j in range(min(len(strs[i-1]), len(strs[1]))):
            if strs[i-1][j] == strs[i][j]:
                counter +=1
                print(i-1)
                longestPrefixes[i-1]= counter
            else:
                longestPrefixes.append(counter)
                break
    longestprefix = strs[0][:min(longestPrefixes)]
    return longestprefix


#print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["ab", "a"]))