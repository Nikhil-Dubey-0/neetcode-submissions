class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        numbers=sorted(list(set(nums)))
    
        
        sequence=1
        max_seq=1
        for i in range(1,len(numbers)):
            if numbers[i] == numbers[i-1]+1:
                sequence +=1
            else:
                max_seq=max(max_seq, sequence)
                sequence=1
        return max(max_seq,sequence)