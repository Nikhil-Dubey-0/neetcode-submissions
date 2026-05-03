class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        numbers = set(nums)
        max_seq = 0

        while numbers:
            start = numbers.pop()  # take & remove one element


            left = start - 1
            while left in numbers:
                numbers.remove(left)
                left -= 1

        
            right = start + 1
            while right in numbers:
                numbers.remove(right)
                right += 1

            
            max_seq = max(max_seq, right - left - 1) # length = right boundary - left boundary - 1

        return max_seq