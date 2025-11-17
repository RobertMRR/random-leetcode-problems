# Time Based Key-Value Store
class TimeMap:

    def __init__(self):
        self.timemap = {}
    
    def set(self, key, value, timestamp):
        if self.timemap.get(key, None) is None:
            self.timemap[key] = [[value,timestamp]]
        else:
            self.timemap[key].append([value,timestamp])

    def get(self, key, timestamp=None):
        res, values = "", self.timemap.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l +r ) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res


timeMap = TimeMap()

timeMap.set("alice", "happy", 1)
timeMap.set("alice", "sad", 3)
print(timeMap.get("alice", 3))