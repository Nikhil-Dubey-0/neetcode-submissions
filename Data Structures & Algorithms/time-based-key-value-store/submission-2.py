from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.time_map[key]
        left = 0
        right = len(self.time_map[key]) - 1
        while left <= right:
            mid = (left + right) // 2
            if timestamp >= values[mid][1]:
                res = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return res

        