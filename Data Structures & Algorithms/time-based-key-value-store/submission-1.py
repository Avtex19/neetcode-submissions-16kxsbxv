#bruteforce, in the dictionary values are list of tuples, for example {'alice': [(1, 'happy'), (3, 'sad')]}

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

        for i in range(len(records)-1,-1,-1):
            time = records[i][0]
            value = records[i][1]

            if time <= timestamp:
                return value
        return ""