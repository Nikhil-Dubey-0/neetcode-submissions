class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h_map={}
        for num in nums:
            if num in h_map:
                h_map[num]+=1
            else:
                h_map[num]=1

        h_map= dict(sorted(h_map.items(), key=lambda x: x[1], reverse=True)[:k])
        return list(h_map.keys())