class MyHashMap:

    def __init__(self):
        self.MyHash = {}

    def put(self, key: int, value: int) -> None:
        self.MyHash[key]=value

    def get(self, key: int) -> int:
        return self.MyHash.get(key,-1)

    def remove(self, key: int) -> None:
    # del self.MyHash[key] if key in self.MyHash, not supported for del
        # if key in self.MyHash:
        #     del self.MyHash[key]
        self.MyHash.pop(key, None)



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)