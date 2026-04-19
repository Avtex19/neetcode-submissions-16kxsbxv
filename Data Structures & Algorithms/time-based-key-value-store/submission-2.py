#O(logn) without defaultdict

class TimeMap:
    def __init__(self):
        self.m = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.m:
            self.m[key] = []
        self.m[key].append((timestamp, value))
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.m:
            return ""
        records = self.m[key]
        l = 0
        r = len(records)-1
        res = ""

        while l <= r:
            mid = (l+r)//2
            print(records[mid])

            if records[mid][0] < timestamp:
                res = records[mid][1]
                l = mid + 1
            elif records[mid][0] > timestamp:
                r = mid - 1
            else:
                return records[mid][1]

        return res