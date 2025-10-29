from collections import defaultdict
def topKFrequent(nums, k):
    distinct_items = set(nums)
    counts = {}
    for item in distinct_items:
        counter = 0
        for num in nums:
            if num == item:
                counter += 1
        counts[item] = counter
    scores = [value for key, value in counts.items()]
    scores.sort()
    scores2 = scores[-k:]
    result = []
    for key, value in counts.items():
        if value in scores2:
            result.append(key)
    return result
print(topKFrequent([1,1,1,2,2,3], 2))