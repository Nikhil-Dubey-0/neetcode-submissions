class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted((num, i) for i, num in enumerate(nums))

        i, j = 0, len(sorted_nums) - 1

        while i < j:
            curr = sorted_nums[i][0] + sorted_nums[j][0]

            if curr == target:
                return sorted([sorted_nums[i][1], sorted_nums[j][1]])
            elif curr > target:
                j -= 1
            else:
                i += 1