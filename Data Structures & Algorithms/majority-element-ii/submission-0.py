from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        req_size = len(nums)/3
        out = []
        for num in count:
            if count[num] > req_size:
                out.append(num)
        return out