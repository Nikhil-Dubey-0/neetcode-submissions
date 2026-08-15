from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        for value, times in self.time_map[key]:
            if times <= timestamp:
                res = value
            else:
                break
        return res
        