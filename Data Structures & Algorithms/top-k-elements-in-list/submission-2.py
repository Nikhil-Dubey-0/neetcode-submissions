class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h_map={}
        for num in nums:
            h_map[num]=h_map.get(num,0) + 1 

        bucket = [[] for _ in range(len(nums)+1)]
        # Index = frequency, value = list of numbers with that frequency
        # Size = len(nums) + 1 because max freq is n 

        for num,freq in h_map.items():
            bucket[freq].append(num)  #nums at their freq index
        
        output=[]

        for i in range(len(nums),0,-1):  # from highest frequency(len(nums)) → lowest
            if not bucket[i]: # If bucket is empty → skip (no numbers with this frequency)
                continue
            for num in bucket[i]:   #frequency = i
                output.append(num)
                if len(output)==k:
                    return output
