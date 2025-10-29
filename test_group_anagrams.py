from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    all_anagrams = []
    for word in strs:
        single_anagrams = [word]
        sorted_word = list(word)
        sorted_word.sort()
        for word2 in strs:
            if strs.index(word) == strs.index(word2):
                continue
            else:
                sorted_word2 = list(word2)
                sorted_word2.sort()
                if sorted_word2 == sorted_word:
                    single_anagrams.append(word2)
              
        all_anagrams.append(single_anagrams)
    all_anagrams2 = []
    for anagram in all_anagrams:
        anagram.sort()
        if anagram not in all_anagrams2:
            all_anagrams2.append(anagram)
    return all_anagrams2


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print("*"*80)
print(groupAnagrams([""]))
print("*"*80)
print(groupAnagrams(["a"]))
print("*"*80)