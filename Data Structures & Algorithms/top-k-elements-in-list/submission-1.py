import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h_map={}
        for num in nums:
            h_map[num]=h_map.get(num,0) + 1 # h_map.get(num,0) means if num is not in h_map, num is 0 by default
        heap=[]
        for num,freq in h_map.items():
            # python create min heap by default
            heapq.heappush(heap,(freq,num))  # freq first so heap maintain by freq
            if len(heap)>k:
                heapq.heappop(heap)  # heap pop minimum value(freq) by default
        
        return [num for freq,num in heap]  #list comprehension